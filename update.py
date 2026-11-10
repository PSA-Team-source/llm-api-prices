#!/usr/bin/env python3
"""llm-api-prices updater: fetch the public UberLLM catalog, build prices.json /
prices.csv / README.md / CHANGELOG.md / history/<day>.csv, diff against the last
snapshot and commit the result to GitHub through the GraphQL API
(createCommitOnBranch, so commits are signed by GitHub). Python 3.9+, stdlib only.

  python3 update.py --out DIR          build into DIR (no GitHub; DIR's own files are "previous")
  python3 update.py --commit           build and commit to REPO (default PSA-Team-source/llm-api-prices)
  python3 update.py --commit --force   commit even if today's snapshot is already there
  python3 update.py --selftest         offline checks of the pricing and diff logic

Token for --commit: $GITHUB_TOKEN, else GITHUB_TOKEN=... in ./.env (next to this
file) or ~/llm-api-prices/.env. Needs contents:write on the repo. Never logged.

Self-healing: every HTTP call retries with backoff; a commit that loses a race
(branch moved) re-reads the head and tries again; a catalog that shrank by more
than 40% against the last snapshot is refused (a partial API answer must never
wipe the dataset); nothing is committed when no price changed; a run that finds
today's snapshot already committed exits 0, so a second daily cron run only
does work when the first one failed.
"""
import argparse
import base64
import csv
import datetime as dt
import fcntl
import io
import json
import logging
import math
import os
import sys
import time
import urllib.error
import urllib.request

API = os.environ.get("ULL_API", "https://api.uberllm.dev")
SITE = "https://uberllm.dev"
REPO = os.environ.get("REPO", "PSA-Team-source/llm-api-prices")
BRANCH = os.environ.get("BRANCH", "main")
UA = "llm-api-prices-updater/1.0 (+https://github.com/PSA-Team-source/llm-api-prices)"
HERE = os.path.dirname(os.path.abspath(__file__))
MOVE = 0.10  # an UberLLM price move this large (either way) goes in the changelog

# Where a model maker publishes its own API prices, to check a list price against.
# Only pages that answered HTTP 200 when this list was written (2026-11-10).
VENDOR_PAGES = {
    "openai": "https://platform.openai.com/docs/pricing",
    "anthropic": "https://docs.claude.com/en/docs/about-claude/pricing",
    "google": "https://ai.google.dev/gemini-api/docs/pricing",
    "deepseek": "https://api-docs.deepseek.com/quick_start/pricing",
    "x-ai": "https://docs.x.ai/docs/models",
    "mistralai": "https://mistral.ai/pricing",
    "moonshotai": "https://platform.moonshot.ai/docs/pricing/chat",
    "z-ai": "https://docs.z.ai/guides/overview/pricing",
    "qwen": "https://www.alibabacloud.com/help/en/model-studio/models",
    "black-forest-labs": "https://bfl.ai/pricing",
    "kling": "https://klingai.com/global/dev/pricing",
    "fal-ai": "https://fal.ai/pricing",
    "elevenlabs": "https://elevenlabs.io/pricing/api",
}

CATEGORIES = ["text", "image", "video", "music", "speech", "transcription", "embedding", "other"]

FIELDS = [
    "id", "name", "maker", "category", "unit", "context_length", "max_output_tokens",
    "capabilities", "input_modalities", "open_weights", "nsfw", "available",
    "list_input_usd_per_mtok", "list_output_usd_per_mtok", "list_cache_read_usd_per_mtok",
    "uberllm_input_usd_per_mtok", "uberllm_output_usd_per_mtok", "uberllm_cache_read_usd_per_mtok",
    "pct_below_list_input", "pct_below_list_output",
    "list_usd_per_unit", "uberllm_usd_per_unit", "pct_below_list_unit",
    "list_price_source", "list_price_source_url", "list_price_checked",
    "vendor_pricing_page", "uberllm_page",
]

log = logging.getLogger("llm-api-prices")


# ---------------------------------------------------------------- HTTP

def http(url, method="GET", body=None, headers=None, tries=4, timeout=60):
    """JSON in, JSON out, retried with backoff on network errors, 429 and 5xx."""
    data = json.dumps(body).encode() if body is not None else None
    h = {"User-Agent": UA, "Accept": "application/json"}
    if data is not None:
        h["Content-Type"] = "application/json"
    h.update(headers or {})
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, method=method, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
            return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 404:
                return None
            if e.code not in (429, 500, 502, 503, 504):
                detail = e.read()[:300].decode("utf-8", "replace")
                raise RuntimeError(f"{method} {url.split('?')[0]} -> HTTP {e.code}: {detail}") from None
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:
            last = e
        wait = 5 * 3 ** i
        log.warning("%s %s failed (%s), retry %d/%d in %ds", method, url.split("?")[0], last, i + 1, tries - 1, wait)
        if i < tries - 1:
            time.sleep(wait)
    raise RuntimeError(f"{method} {url.split('?')[0]} failed after {tries} tries: {last}")


# ---------------------------------------------------------------- data

def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def clean(v):
    """Round away float noise (0.30000000000000004) but keep tiny prices."""
    return float(f"{v:.6g}") if num(v) else None


def pct_below(now, lst):
    if not num(now) or not num(lst) or lst <= 0:
        return None
    return round(100 * (1 - now / lst), 1)


def category(m):
    out = m.get("output_modalities") or []
    inp = m.get("input_modalities") or []
    for mod, cat in (("video", "video"), ("image", "image"), ("music", "music"), ("audio", "speech")):
        if mod in out:
            return cat
    if "embedding" in out:
        return "embedding"
    if out == ["text"]:
        return "transcription" if inp == ["audio"] else "text"
    return "other"


def capabilities(m, v1):
    caps = set(m.get("capabilities") or [])
    out = []
    if m.get("supports_tools") or "tools" in caps:
        out.append("tools")
    if v1.get("supports_reasoning") or "reasoning" in caps:
        out.append("reasoning")
    if "image" in (m.get("input_modalities") or []):
        out.append("vision")
    if "structured_outputs" in caps or "response_format" in caps:
        out.append("structured_outputs")
    for c in ("text-to-video", "image-to-video", "audio"):
        if c in caps:
            out.append(c if c != "audio" else "sound")
    return out


def media_official(m, ours):
    """The site's one official price for a media unit (web lib/market.ts
    mediaOfficialUsd): the catalog list when above ours, else media_ref (maker,
    then OpenRouter, then Fal) when at least 1% above ours. None = no official
    price above what UberLLM charges (then none is claimed)."""
    lst, ref = m.get("media_list_usd"), m.get("media_ref") or {}
    if not num(ours) or ours <= 0:
        return (lst, None) if num(lst) else (None, None)
    if num(lst) and lst > ours:
        return lst, None
    if num(ref.get("usd")) and ref["usd"] >= ours * 1.01:
        return ref["usd"], ref
    return None, None


def build_rows(models, v1):
    rows = []
    for m in models:
        cat = category(m)
        if m.get("nsfw") and cat not in ("text", "transcription", "embedding", "other"):
            continue  # adult picture/video/sound models stay off public lists (as on uberllm.dev)
        mid = m["id"]
        v = v1.get(mid, {})
        r = dict.fromkeys(FIELDS)
        r.update(
            id=mid, name=m.get("display_name") or mid, maker=mid.split("/")[0], category=cat,
            context_length=m.get("context_length") or None, max_output_tokens=m.get("max_output_tokens") or None,
            capabilities=capabilities(m, v), input_modalities=m.get("input_modalities") or [],
            open_weights=bool(m.get("open_weights")), nsfw=bool(m.get("nsfw")), available=bool(m.get("available")),
            vendor_pricing_page=VENDOR_PAGES.get(mid.split("/")[0]), uberllm_page=f"{SITE}/models/{mid}",
        )
        unit = m.get("media_unit")
        if unit and unit != "1M tokens" and cat != "text":
            ours = m.get("media_price_now_usd")
            if not num(ours) and m.get("available"):
                ours = m.get("media_list_usd")  # served at its listed price
            lst, ref = media_official(m, ours)
            if not num(ours) and not num(lst):
                continue
            r.update(unit=unit, uberllm_usd_per_unit=clean(ours), list_usd_per_unit=clean(lst),
                     pct_below_list_unit=pct_below(ours, lst))
            if num(lst):
                if ref:
                    r.update(list_price_source=ref.get("source"), list_price_source_url=ref.get("url"),
                             list_price_checked=ref.get("checked"))
                else:
                    r.update(list_price_source="UberLLM catalog list price")
            rates = [
                {"resolution": x.get("resolution") or "", "sound": bool(x.get("audio")),
                 "list_usd_per_second": clean(x.get("list_usd_per_second")),
                 "uberllm_usd_per_second": clean(x.get("usd_per_second"))}
                for x in m.get("media_rates") or []
            ]
            if rates:
                r["video_rates"] = rates
        else:
            now = m.get("price_now") or {}
            li, lo = m.get("list_input_usd_per_mtok"), m.get("list_output_usd_per_mtok")
            if not now and not num(li):
                continue
            r.update(
                unit="1M tokens",
                list_input_usd_per_mtok=clean(li), list_output_usd_per_mtok=clean(lo),
                list_cache_read_usd_per_mtok=clean(m.get("list_cache_read_usd_per_mtok")),
                uberllm_input_usd_per_mtok=clean(now.get("input_usd_per_mtok")),
                uberllm_output_usd_per_mtok=clean(now.get("output_usd_per_mtok")),
                uberllm_cache_read_usd_per_mtok=clean(now.get("cache_read_usd_per_mtok")),
                pct_below_list_input=pct_below(now.get("input_usd_per_mtok"), li),
                pct_below_list_output=pct_below(now.get("output_usd_per_mtok"), lo),
            )
            if num(li) or num(lo):
                r["list_price_source"] = m.get("list_source") or "UberLLM catalog list price"
            hosts = [
                {"name": p["name"], "input_usd_per_mtok": clean(p.get("input_usd_per_mtok")),
                 "output_usd_per_mtok": clean(p.get("output_usd_per_mtok"))}
                for p in m.get("providers") or [] if p.get("name")
            ]
            if hosts:
                r["list_price_hosts"] = hosts
        rows.append(r)
    rows.sort(key=lambda r: (CATEGORIES.index(r["category"]), r["id"]))
    return rows


def fetch():
    models = http(f"{API}/api/v1/public/models")
    if not models or not models.get("models"):
        raise RuntimeError("catalog came back empty")
    live = http(f"{API}/api/v1/public/market/live") or {}
    v1 = {m["id"]: m for m in (http(f"{API}/v1/models") or {}).get("data", [])}
    changes = http(f"{API}/api/v1/public/price-changes") or {}
    lm = live.get("models") or {}
    # The live board's fields win, exactly as uberllm.dev merges them (lib/market.ts mergeLive).
    merged = [{**m, **lm.get(m["id"], {})} for m in models["models"]]
    return merged, v1, changes


def to_csv(rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({k: (";".join(r[k]) if isinstance(r[k], list) else ("" if r[k] is None else r[k])) for k in FIELDS})
    return buf.getvalue()


# ---------------------------------------------------------------- formatting

def usd(v):
    if not num(v):
        return ""
    if v == 0:
        return "$0"
    if v >= 1:
        return f"${v:,.2f}"
    s = f"{v:.{max(2, 3 - math.floor(math.log10(v)))}f}".rstrip("0")  # 4 significant digits, never 1e-05
    return "$" + (s + "0" if len(s.split(".")[1]) < 2 else s)


def unit_word(u, cat=""):
    if u == "job":
        return {"video": "video", "music": "track"}.get(cat, "request")
    return {"second": "sec", "1K characters": "1K chars"}.get(u, u)


def price_cell(r, side):
    """side = 'list' | 'uberllm'."""
    if r["unit"] == "1M tokens":
        i, o = r[f"{side}_input_usd_per_mtok"], r[f"{side}_output_usd_per_mtok"]
        return f"{usd(i)} / {usd(o)}" if num(i) and num(o) else ""
    v = r[f"{side}_usd_per_unit"]
    return f"{usd(v)} / {unit_word(r['unit'], r['category'])}" if num(v) else ""


def pct_cell(r):
    if r["unit"] == "1M tokens":
        p = [x for x in (r["pct_below_list_input"], r["pct_below_list_output"]) if num(x)]
        if not p:
            return ""
        a, b = min(p), max(p)
        return f"{a:g}%" if a == b else f"{a:g}–{b:g}%"
    p = r["pct_below_list_unit"]
    return f"{p:g}%" if num(p) else ""


def md_link(r):
    return f"[{r['name'].replace('|', '/')}]({r['uberllm_page']})"


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(out)


# ---------------------------------------------------------------- diffs

def side(r):
    """The values a diff compares, per row."""
    if r["unit"] == "1M tokens":
        return {"list": (r["list_input_usd_per_mtok"], r["list_output_usd_per_mtok"]),
                "now": (r["uberllm_input_usd_per_mtok"], r["uberllm_output_usd_per_mtok"])}
    return {"list": (r["list_usd_per_unit"],), "now": (r["uberllm_usd_per_unit"],)}


def rel(a, b):
    """Relative change per priced component (input, output for tokens), None
    where a side is missing; None when nothing compares."""
    c = tuple(y / x - 1 if num(x) and num(y) and x > 0 else None for x, y in zip(a, b))
    return c if any(v is not None for v in c) else None


def mag(c):
    """The largest move of a change (signed), for sorting and thresholds."""
    return max((v for v in c or () if v is not None), key=abs, default=0.0)


def fmt_side(r, vals):
    if r["unit"] == "1M tokens":
        return " / ".join(usd(v) if num(v) else "–" for v in vals)
    return f"{usd(vals[0])} / {unit_word(r['unit'], r['category'])}" if num(vals[0]) else "–"


def diff(prev, rows):
    p = {r["id"]: r for r in prev}
    n = {r["id"]: r for r in rows}
    d = {"new": [n[k] for k in sorted(n.keys() - p.keys())],
         "removed": [p[k] for k in sorted(p.keys() - n.keys())], "list": [], "moves": []}
    for k in sorted(n.keys() & p.keys()):
        a, b = side(p[k]), side(n[k])
        if a["list"] != b["list"] and any(num(x) for x in b["list"]):
            d["list"].append((n[k], a["list"], b["list"], rel(a["list"], b["list"])))
        c = rel(a["now"], b["now"])
        if c is not None and abs(mag(c)) >= MOVE:
            d["moves"].append((n[k], a["now"], b["now"], c))
    d["list"].sort(key=lambda x: mag(x[3]))
    d["moves"].sort(key=lambda x: mag(x[3]))
    return d


def signed(c):
    """"−40%", or "in −87% / out 0%" when input and output moved differently."""
    one = lambda v: "–" if v is None else ("0%" if round(v * 100) == 0 else f"{'+' if v > 0 else '−'}{abs(v) * 100:.0f}%")  # noqa: E731
    if not c:
        return ""
    if len(c) == 2 and one(c[0]) != one(c[1]):
        return f"in {one(c[0])} / out {one(c[1])}"
    return one(c[-1] if c[-1] is not None else c[0])


def changelog_entry(title, d, note=""):
    if not (d["new"] or d["removed"] or d["list"] or d["moves"]):
        return ""
    out = [f"## {title}", ""]
    if note:
        out += [note, ""]
    pub = lambda r: not r["nsfw"]  # noqa: E731  (keep adult models out of the human-readable log)
    lst = [x for x in d["list"] if pub(x[0])]
    if lst:
        out += [f"**Official list price changes ({len(lst)})**", "",
                table(["Model", "Category", "Before", "After", "Change"],
                      [[md_link(r), r["category"], fmt_side(r, a), fmt_side(r, b), signed(c)] for r, a, b, c in lst]), ""]
    new = [r for r in d["new"] if pub(r)]
    if new:
        out += [f"**New models ({len(new)})**", "",
                table(["Model", "Category", "Official price", "UberLLM price"],
                      [[md_link(r), r["category"], price_cell(r, "list") or "–", price_cell(r, "uberllm") or "–"] for r in new]), ""]
    gone = [r for r in d["removed"] if pub(r)]
    if gone:
        out += [f"**No longer listed ({len(gone)})**: " + ", ".join(f"`{r['id']}`" for r in gone), ""]
    mv = [x for x in d["moves"] if pub(x[0])]
    if mv:
        out += [f"<details><summary>UberLLM price moves of {MOVE * 100:.0f}% or more ({len(mv)})</summary>", "",
                table(["Model", "Category", "Before", "After", "Change"],
                      [[md_link(r), r["category"], fmt_side(r, a), fmt_side(r, b), signed(c)] for r, a, b, c in mv]),
                "", "</details>", ""]
    return "\n".join(out) + "\n"


def week_rows(changes):
    """The public weekly diff (GET /api/v1/public/price-changes) as rows for the
    'this week' tables: (name, id, kind, what, before, after, change)."""
    out = []
    for c in changes.get("changes") or []:
        if c.get("nsfw") or c.get("change") not in ("list", "price"):
            continue
        b, a = c.get("before") or {}, c.get("after") or {}
        lst = c["change"] == "list"
        if "media_unit" in a or "media_price_usd" in a:
            k = "media_list_usd" if lst else "media_price_usd"
            x, y = b.get(k), a.get(k)
            ch = rel((x,), (y,))
            u = unit_word(a.get("media_unit") or "", c.get("kind") or "")
            fb, fa = (f"{usd(x)} / {u}" if num(x) else "–"), (f"{usd(y)} / {u}" if num(y) else "–")
        else:
            ki, ko = ("list_input_usd_per_mtok", "list_output_usd_per_mtok") if lst else ("input_usd_per_mtok", "output_usd_per_mtok")
            x, y = b.get(ko), a.get(ko)
            ch = rel((b.get(ki), x), (a.get(ki), y))
            fb = f"{usd(b.get(ki))} / {usd(x)}" if num(x) else "–"
            fa = f"{usd(a.get(ki))} / {usd(y)}" if num(y) else "–"
        if ch is None:
            continue
        out.append((c.get("name") or c["model"], c["model"], c.get("kind") or "", c["change"], fb, fa, ch))
    return out


def seed_entry(changes):
    """First CHANGELOG entry, from UberLLM's own daily snapshots before this repo existed."""
    if not changes.get("from"):
        return ""
    lines = [f"## {changes['from']} to {changes['to']} (UberLLM daily catalog snapshots, before this repo started)", "",
             "From `GET https://api.uberllm.dev/api/v1/public/price-changes`. Text prices are $ per 1M input / output tokens.", ""]
    wr = week_rows(changes)
    lst = sorted([w for w in wr if w[3] == "list"], key=lambda w: mag(w[6]))
    mv = sorted([w for w in wr if w[3] == "price" and abs(mag(w[6])) >= MOVE], key=lambda w: mag(w[6]))
    link = lambda w: f"[{w[0].replace('|', '/')}]({SITE}/models/{w[1]})"  # noqa: E731
    if lst:
        lines += [f"**Official list price changes ({len(lst)})**", "",
                  table(["Model", "Category", "Before", "After", "Change"], [[link(w), w[2], w[4], w[5], signed(w[6])] for w in lst]), ""]
    new = [c for c in changes.get("changes") or [] if c.get("change") == "new" and not c.get("nsfw")]
    if new:
        lines += [f"**New models ({len(new)})**: " + ", ".join(f"[{c['name']}]({SITE}/models/{c['model']})" for c in new), ""]
    gone = [c for c in changes.get("changes") or [] if c.get("change") == "removed" and not c.get("nsfw")]
    if gone:
        lines += [f"**No longer listed ({len(gone)})**: " + ", ".join(f"`{c['model']}`" for c in gone), ""]
    if mv:
        lines += [f"<details><summary>UberLLM price moves of {MOVE * 100:.0f}% or more ({len(mv)})</summary>", "",
                  table(["Model", "Category", "Before", "After", "Change"], [[link(w), w[2], w[4], w[5], signed(w[6])] for w in mv]),
                  "", "</details>", ""]
    return "\n".join(lines) + "\n"


CHANGELOG_HEAD = """# Changelog

Price changes between daily snapshots of [`prices.json`](prices.json), newest first.
"Official list price" = the model maker's price as carried in the catalog (see [SOURCES](README.md#sources)).
"UberLLM price" = the best live offer on the UberLLM market at snapshot time; it moves during the day.
Text prices are $ per 1M input / output tokens. Every day's full table is in [`history/`](history/).

"""


def merge_changelog(old, entry):
    body = old[len(CHANGELOG_HEAD):] if old and old.startswith(CHANGELOG_HEAD) else (old or "")
    return CHANGELOG_HEAD + entry + ("\n" if entry and body else "") + body


# ---------------------------------------------------------------- README

WORKFLOW_YML = """name: update prices
on:
  schedule:
    - cron: "17 3 * * *"
  workflow_dispatch:
permissions:
  contents: write
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python3 update.py --commit
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""


def readme(rows, meta, changes):
    pub = [r for r in rows if r["available"] and not r["nsfw"]]
    counts = {c: sum(1 for r in rows if r["category"] == c) for c in CATEGORIES}
    parts = [
        "# LLM API prices",
        "",
        "An open, daily-updated dataset of AI API prices: the official list price of "
        f"{len(rows)} text, image, video, music and speech models next to the lowest live price on the "
        "[UberLLM](https://uberllm.dev/models) market, how far below list that is, context length and capabilities.",
        "",
        f"**Updated:** {meta['updated_at']} · **Models:** "
        + ", ".join(f"{counts[c]} {c}" for c in CATEGORIES if counts[c])
        + " · **Files:** [`prices.json`](prices.json), [`prices.csv`](prices.csv), [`CHANGELOG.md`](CHANGELOG.md), [`history/`](history/)",
        "",
        "Disclosure: this repo is maintained by the team that runs UberLLM. The UberLLM column is our own "
        "price; the official column is the maker's price, sourced as described in [Sources](#sources). "
        "Live prices: <https://uberllm.dev/models>.",
        "",
    ]

    def cheapest(cat, unit=None, n=12):
        rs = [r for r in pub if r["category"] == cat and (unit is None or r["unit"] == unit)]
        if unit == "1M tokens" or (unit is None and cat == "text"):
            rs = [r for r in rs if num(r["uberllm_output_usd_per_mtok"]) and num(r["list_output_usd_per_mtok"])]
            rs.sort(key=lambda r: (r["uberllm_input_usd_per_mtok"] or 0) + r["uberllm_output_usd_per_mtok"])
        else:
            rs = [r for r in rs if num(r["uberllm_usd_per_unit"])]
            rs.sort(key=lambda r: r["uberllm_usd_per_unit"])
        return rs[:n]

    parts += ["## Cheapest right now", "",
              "Lowest UberLLM price per category among models that can be called now. Text: $ per 1M input / output tokens. "
              "Full list: [`prices.csv`](prices.csv).", ""]
    t = cheapest("text", "1M tokens", 15)
    if t:
        parts += ["### Text (chat) models", "",
                  table(["Model", "Context", "Official price", "UberLLM price", "Below list"],
                        [[md_link(r), f"{r['context_length'] // 1000}K" if r["context_length"] else "", price_cell(r, "list"),
                          price_cell(r, "uberllm"), pct_cell(r)] for r in t]), ""]

    big = ("openai", "anthropic", "google", "deepseek", "x-ai", "qwen", "moonshotai", "z-ai", "mistralai", "meta-llama")
    flag = [r for r in pub if r["category"] == "text" and r["maker"] in big and num(r["list_output_usd_per_mtok"])
            and num(r["uberllm_output_usd_per_mtok"]) and ":" not in r["id"]]
    flag.sort(key=lambda r: (big.index(r["maker"]), -(r["list_output_usd_per_mtok"] or 0), r["id"]))
    if flag:
        parts += ["### Major model makers", "",
                  "<details><summary>OpenAI, Anthropic, Google, DeepSeek, xAI, Qwen, Moonshot, Z.ai, Mistral, Meta "
                  f"({len(flag)} models)</summary>", "",
                  table(["Model", "Maker", "Context", "Official price", "UberLLM price", "Below list"],
                        [[md_link(r), r["maker"], f"{r['context_length'] // 1000}K" if r["context_length"] else "",
                          price_cell(r, "list"), price_cell(r, "uberllm"), pct_cell(r)] for r in flag]),
                  "", "</details>", ""]

    for cat, unit, title in (("image", "image", "Image models (per image)"), ("image", "megapixel", "Image models (per megapixel)"),
                             ("video", "second", "Video models (per second)"), ("video", "job", "Video models (per video)"),
                             ("music", None, "Music models"), ("speech", None, "Speech models")):
        t = cheapest(cat, unit, 10)
        if t:
            parts += [f"### {title}", "",
                      table(["Model", "Official price", "UberLLM price", "Below list"],
                            [[md_link(r), price_cell(r, "list") or "–", price_cell(r, "uberllm"), pct_cell(r) or "–"] for r in t]), ""]

    wr = week_rows(changes)
    if changes.get("from") and wr:
        span = f"{changes['from']} to {changes['to']}"
        lst = sorted([w for w in wr if w[3] == "list" and mag(w[6]) < 0], key=lambda w: mag(w[6]))[:10]
        mv = sorted([w for w in wr if w[3] == "price" and mag(w[6]) < 0], key=lambda w: mag(w[6]))[:10]
        link = lambda w: f"[{w[0].replace('|', '/')}]({SITE}/models/{w[1]})"  # noqa: E731
        parts += [f"## Biggest drops this week ({span})", "",
                  "From UberLLM's daily catalog snapshots (`GET /api/v1/public/price-changes`). Text: $ per 1M input / output tokens, sorted by the larger of the two moves.", ""]
        if lst:
            parts += ["### Official list price cuts", "",
                      table(["Model", "Category", "Before", "After", "Change"], [[link(w), w[2], w[4], w[5], signed(w[6])] for w in lst]), ""]
        if mv:
            parts += ["### UberLLM price drops", "",
                      table(["Model", "Category", "Before", "After", "Change"], [[link(w), w[2], w[4], w[5], signed(w[6])] for w in mv]), ""]
        parts += ["Every change, day by day: [`CHANGELOG.md`](CHANGELOG.md).", ""]

    parts += [
        "## Use the data", "",
        "Plain HTTPS, no key. Raw file URLs:", "",
        "- JSON: `https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.json`",
        "- CSV: `https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.csv`",
        "- A past day: `https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/history/YYYY-MM-DD.csv`", "",
        "Python (stdlib):", "",
        "```python",
        "import json, urllib.request",
        "URL = \"https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.json\"",
        "data = json.load(urllib.request.urlopen(URL))",
        "chat = [m for m in data[\"models\"] if m[\"category\"] == \"text\" and m[\"available\"]",
        "        and m[\"list_output_usd_per_mtok\"] and \"tools\" in m[\"capabilities\"]]",
        "for m in sorted(chat, key=lambda m: m[\"list_output_usd_per_mtok\"])[:10]:",
        "    print(m[\"id\"], m[\"list_input_usd_per_mtok\"], m[\"list_output_usd_per_mtok\"], m[\"list_price_source\"])",
        "```", "",
        "JavaScript:", "",
        "```js",
        "const res = await fetch(\"https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.json\");",
        "const { updated_at, models } = await res.json();",
        "const video = models.filter(m => m.category === \"video\" && m.unit === \"second\");",
        "console.log(updated_at, video.sort((a, b) => a.uberllm_usd_per_unit - b.uberllm_usd_per_unit).slice(0, 5));",
        "```", "",
        "jq: `jq '.models[] | select(.maker==\"anthropic\") | {id, list_input_usd_per_mtok, list_output_usd_per_mtok}' prices.json`", "",
        "### Fields", "",
        table(["Field", "Meaning"], [
            ["`id`", "Model id, as used in the `model` field of an OpenAI-compatible request to UberLLM"],
            ["`category`", "text, image, video, music, speech, transcription, embedding or other (from the output modality)"],
            ["`unit`", "`1M tokens` for token-priced models; otherwise what one unit price buys: `image`, `megapixel`, `second`, `job` (one video or track), `minute`, `1K characters`"],
            ["`list_input_usd_per_mtok`, `list_output_usd_per_mtok`", "Official list price, USD per 1M tokens"],
            ["`uberllm_input_usd_per_mtok`, `uberllm_output_usd_per_mtok`", "Lowest live UberLLM price at snapshot time, USD per 1M tokens"],
            ["`list_usd_per_unit`, `uberllm_usd_per_unit`", "The same for per-unit (media) prices"],
            ["`pct_below_list_*`", "100 × (1 − UberLLM / list), one decimal; negative = above list; empty = no list price"],
            ["`list_price_source`, `list_price_source_url`, `list_price_checked`", "Where the official price comes from (see Sources)"],
            ["`list_price_hosts`", "JSON only: the published per-token prices of named hosts (Together AI, Fireworks, Bedrock, ...) for the model"],
            ["`video_rates`", "JSON only: every per-second video price by resolution and sound, official and UberLLM"],
            ["`vendor_pricing_page`", "The maker's own pricing page, to check a list price against"],
            ["`capabilities`", "tools, reasoning, vision, structured_outputs; video: text-to-video, image-to-video, sound"],
            ["`available`", "A request can be served right now"],
            ["`nsfw`", "Made for adult or unfiltered content (text only; adult image/video/sound models are not listed)"],
        ]), "",
        "## Sources", "",
        "Every number comes from UberLLM's public catalog, read once a day by [`update.py`](update.py):", "",
        "- `GET https://api.uberllm.dev/api/v1/public/models`: model list, context length, capabilities, official list prices, UberLLM prices.",
        "- `GET https://api.uberllm.dev/api/v1/public/market/live`: the live market board (refreshed every 30 s). Its prices win over the catalog's, as on uberllm.dev.",
        "- `GET https://api.uberllm.dev/v1/models`: the OpenAI-compatible model list (reasoning flag).",
        "- `GET https://api.uberllm.dev/api/v1/public/price-changes`: the weekly diff used for \"Biggest drops this week\" and the first CHANGELOG entry.",
        "",
        "Official list price, per row:", "",
        "- `list_price_source = \"UberLLM catalog list price\"`: the direct (list) price the catalog carries for the model, which is the model maker's "
        "own API price for first-party models (OpenAI, Anthropic, Google, ...) and the host's list price for open-weight models. "
        "Check it against `vendor_pricing_page` and, for open-weight models, against `list_price_hosts`.",
        "- Any other `list_price_source` (for example `OpenRouter`, `Z.ai`, `Fal`, `Kling (Kuaishou)`, `Stability AI`): the catalog had no list of its own, so the "
        "price was read from that public page (`list_price_source_url`) on `list_price_checked`.",
        "- No official price: the field is empty. A media model whose only known official price is not above what UberLLM charges gets no official price, "
        "so a saving is never claimed against a number we cannot show.", "",
        "UberLLM price = the best offer a seller on the UberLLM market makes at snapshot time, fee included. Market prices move during the day; "
        "the snapshot is a point in time, and <https://uberllm.dev/models> always has the current one.", "",
        "Found a wrong official price? Open an issue with the vendor page that shows the right one.", "",
        "## How it updates", "",
        "`update.py` (Python stdlib only) runs once a day. It fetches the catalog, refuses an answer that lost more than 40% of the models, "
        "diffs against the last snapshot, and commits `prices.json`, `prices.csv`, `README.md`, `CHANGELOG.md` and `history/<day>.csv` "
        "through the GitHub GraphQL API (`createCommitOnBranch`), so commits are signed by GitHub. Nothing is committed when nothing changed.", "",
        "Run it yourself: `python3 update.py --out ./build` writes every file locally without touching GitHub.", "",
        "To run it from GitHub Actions instead, save this as `.github/workflows/update.yml` (also in [`docs/update.yml`](docs/update.yml)):", "",
        "```yaml", WORKFLOW_YML.rstrip(), "```", "",
        "## License", "",
        "- Data (`prices.json`, `prices.csv`, `history/`, `CHANGELOG.md`): [CC BY 4.0](LICENSE-DATA). Credit: \"LLM API prices, PSA-Team-source/llm-api-prices (UberLLM)\" with a link to this repo.",
        "- Code (`update.py`): [MIT](LICENSE).", "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- GitHub

def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t.strip()
    for p in (os.path.join(HERE, ".env"), os.path.expanduser("~/llm-api-prices/.env")):
        try:
            for line in open(p):
                k, _, v = line.strip().partition("=")
                if k in ("GITHUB_TOKEN", "GH_TOKEN") and v:
                    return v.strip().strip("'\"")
        except OSError:
            pass
    raise RuntimeError("no GitHub token: set GITHUB_TOKEN or put GITHUB_TOKEN=... in ~/llm-api-prices/.env")


def gh(path, tok, **kw):
    return http(f"https://api.github.com{path}", headers={"Authorization": f"Bearer {tok}",
                                                          "Accept": "application/vnd.github+json"}, **kw)


def gh_file(path, tok, ref):
    r = gh(f"/repos/{REPO}/contents/{path}?ref={ref}", tok)
    if not r:
        return None
    if r.get("content") and r.get("encoding") == "base64":
        return base64.b64decode(r["content"]).decode()
    blob = gh(f"/repos/{REPO}/git/blobs/{r['sha']}", tok)  # files over 1 MB come back without content
    return base64.b64decode(blob["content"]).decode()


def gh_head(tok):
    return gh(f"/repos/{REPO}/git/ref/heads/{BRANCH}", tok)["object"]["sha"]


def gh_commit(files, message, tok):
    q = """mutation($input: CreateCommitOnBranchInput!) {
      createCommitOnBranch(input: $input) { commit { oid url } } }"""
    adds = [{"path": p, "contents": base64.b64encode(c.encode()).decode()} for p, c in files.items()]
    for i in range(4):
        head = gh_head(tok)
        body = {"query": q, "variables": {"input": {
            "branch": {"repositoryNameWithOwner": REPO, "branchName": BRANCH},
            "message": {"headline": message[0], "body": message[1]},
            "expectedHeadOid": head, "fileChanges": {"additions": adds}}}}
        r = http("https://api.github.com/graphql", "POST", body, {"Authorization": f"Bearer {tok}"}, timeout=120)
        if r and not r.get("errors"):
            return r["data"]["createCommitOnBranch"]["commit"]
        err = json.dumps((r or {}).get("errors"))[:400]
        log.warning("commit attempt %d failed: %s", i + 1, err)
        if "expectedHeadOid" not in err and "head" not in err.lower():
            raise RuntimeError(f"commit refused: {err}")
        time.sleep(5)
    raise RuntimeError("commit failed: branch kept moving")


# ---------------------------------------------------------------- main

def build(prev_json, prev_changelog, today):
    models, v1, changes = fetch()
    rows = build_rows(models, v1)
    prev_rows = (prev_json or {}).get("models") or []
    if prev_rows and len(rows) < 0.6 * len(prev_rows):
        raise RuntimeError(f"catalog shrank from {len(prev_rows)} to {len(rows)} models; refusing to publish a partial answer")
    if len(rows) < 50:
        raise RuntimeError(f"only {len(rows)} priced models; refusing to publish")
    changed = prev_rows != rows
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    meta = {"updated_at": now, "snapshot_date": today, "count": len(rows),
            "source": f"{API}/api/v1/public/models", "license": "CC-BY-4.0",
            "homepage": "https://github.com/PSA-Team-source/llm-api-prices"}
    out = {**meta, "models": rows}
    if prev_rows:
        d = diff(prev_rows, rows)
        entry = changelog_entry(f"{today} (vs {(prev_json or {}).get('snapshot_date', 'previous snapshot')})", d)
        log.info("diff: %d new, %d removed, %d list changes, %d UberLLM moves >= %d%%",
                 len(d["new"]), len(d["removed"]), len(d["list"]), len(d["moves"]), MOVE * 100)
    else:
        entry = seed_entry(changes)
    files = {
        "prices.json": json.dumps(out, indent=1, ensure_ascii=False) + "\n",
        "prices.csv": to_csv(rows),
        f"history/{today}.csv": to_csv(rows),
        "README.md": readme(rows, meta, changes),
        "CHANGELOG.md": merge_changelog(prev_changelog, entry),
    }
    return files, changed, len(rows)


def selftest():
    """python3 update.py --selftest: the pricing math and diff logic, offline."""
    assert usd(0.000018) == "$0.000018" and usd(0.2) == "$0.20" and usd(1234.5) == "$1,234.50" and usd(0) == "$0"
    assert pct_below(0.25, 1.0) == 75.0 and pct_below(1, None) is None and pct_below(2, 1) == -100.0
    assert signed(rel((0.045, 0.5), (0.006, 0.5))) == "in −87% / out 0%"
    assert signed(rel((1.0, 2.0), (0.6, 1.2))) == "−40%" and mag(rel((1.0, 2.0), (0.5, 2.2))) == -0.5
    base = {"display_name": "M", "context_length": 1000, "output_modalities": ["text"], "input_modalities": ["text"],
            "available": True, "list_input_usd_per_mtok": 1.0, "list_output_usd_per_mtok": 4.0,
            "price_now": {"input_usd_per_mtok": 0.5, "output_usd_per_mtok": 2.0}}
    vid = {"display_name": "V", "output_modalities": ["video"], "media_unit": "second", "available": True,
           "media_price_now_usd": 0.1, "media_list_usd": 0.1,
           "media_ref": {"usd": 0.2, "source": "Fal", "url": "https://fal.ai/x", "checked": "2026-11-10T00:00:00Z"}}
    adult = {**vid, "nsfw": True}
    rows = build_rows([{"id": "a/m", **base}, {"id": "b/v", **vid}, {"id": "c/x", **adult}], {})
    assert [r["id"] for r in rows] == ["a/m", "b/v"], rows  # adult video is never listed
    t, v = rows
    assert t["pct_below_list_input"] == 50.0 and t["list_price_source"] == "UberLLM catalog list price"
    assert v["list_usd_per_unit"] == 0.2 and v["list_price_source"] == "Fal" and v["pct_below_list_unit"] == 50.0
    # a media list price not above ours is not claimed as official
    v2 = build_rows([{"id": "b/v", **{**vid, "media_ref": None}}], {})[0]
    assert v2["list_usd_per_unit"] is None and v2["pct_below_list_unit"] is None
    later = build_rows([{"id": "a/m", **{**base, "list_output_usd_per_mtok": 3.0, "price_now": {"input_usd_per_mtok": 0.1, "output_usd_per_mtok": 0.4}}},
                        {"id": "d/n", **base}], {})
    d = diff(rows, later)
    assert [r["id"] for r in d["new"]] == ["d/n"] and [r["id"] for r in d["removed"]] == ["b/v"]
    assert len(d["list"]) == 1 and len(d["moves"]) == 1 and "−80%" in signed(d["moves"][0][3])
    assert "Official list price changes (1)" in changelog_entry("x", d)
    assert changelog_entry("x", diff(rows, rows)) == ""
    assert merge_changelog(merge_changelog("", "A\n"), "B\n").startswith(CHANGELOG_HEAD + "B\n\nA\n")
    print("selftest ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", help="write files into this directory (no GitHub)")
    ap.add_argument("--commit", action="store_true", help=f"commit to {REPO}@{BRANCH}")
    ap.add_argument("--force", action="store_true", help="run even if today's snapshot exists")
    ap.add_argument("--selftest", action="store_true", help="run the offline checks and exit")
    ap.add_argument("--log", default=os.environ.get("LOG_FILE"), help="also log to this file")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    handlers = [logging.StreamHandler(sys.stderr)]
    if a.log:
        if os.path.exists(a.log) and os.path.getsize(a.log) > 5 << 20:
            os.replace(a.log, a.log + ".1")
        handlers.append(logging.FileHandler(a.log))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", handlers=handlers)
    if not (a.out or a.commit):
        ap.error("pass --out DIR or --commit")

    if a.out:
        os.makedirs(os.path.join(a.out, "history"), exist_ok=True)
    lock = open(os.path.join(a.out or HERE, ".update.lock"), "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log.info("another run holds the lock; exiting")
        return 0

    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    try:
        if a.out:
            rd = lambda p: open(os.path.join(a.out, p)).read() if os.path.exists(os.path.join(a.out, p)) else None  # noqa: E731
            pj = rd("prices.json")
            files, changed, n = build(json.loads(pj) if pj else None, rd("CHANGELOG.md"), today)
            for p, c in files.items():
                with open(os.path.join(a.out, p), "w") as f:
                    f.write(c)
            log.info("wrote %d files for %d models into %s (changed=%s)", len(files), n, a.out, changed)
            return 0

        tok = token()
        pj = gh_file("prices.json", tok, BRANCH)
        prev = json.loads(pj) if pj else None
        if prev and prev.get("snapshot_date") == today and not a.force:
            log.info("snapshot for %s already committed; nothing to do", today)
            return 0
        files, changed, n = build(prev, gh_file("CHANGELOG.md", tok, BRANCH), today)
        if prev and not changed:
            log.info("no price changed since %s; no commit", prev.get("snapshot_date"))
            return 0
        c = gh_commit(files, (f"data: prices {today} ({n} models)",
                              "Daily snapshot from https://api.uberllm.dev/api/v1/public/models by update.py."), tok)
        log.info("committed %s %s", c["oid"][:10], c["url"])
        return 0
    except Exception as e:  # noqa: BLE001 - logged, non-zero exit so cron mail / the next run notices
        log.error("update failed: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
