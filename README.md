# LLM API prices

An open, daily-updated dataset of AI API prices: the official list price of 527 text, image, video, music and speech models next to the lowest live price on the [UberLLM](https://uberllm.dev/models) market, how far below list that is, context length and capabilities.

**Updated:** 2026-11-10T13:21:52Z · **Models:** 260 text, 89 image, 138 video, 20 music, 11 speech, 6 transcription, 3 other · **Files:** [`prices.json`](prices.json), [`prices.csv`](prices.csv), [`CHANGELOG.md`](CHANGELOG.md), [`history/`](history/)

Disclosure: this repo is maintained by the team that runs UberLLM. The UberLLM column is our own price; the official column is the maker's price, sourced as described in [Sources](#sources). Live prices: <https://uberllm.dev/models>.

## Cheapest right now

Lowest UberLLM price per category among models that can be called now. Text: $ per 1M input / output tokens. Full list: [`prices.csv`](prices.csv).

### Text (chat) models

| Model | Context | Official price | UberLLM price | Below list |
|---|---|---|---|---|
| [GPT-OSS 20B](https://uberllm.dev/models/openai/gpt-oss-20b) | 128K | $0.03 / $0.13 | $0.000018 / $0.00009 | 99.9% |
| [GPT-OSS 120B](https://uberllm.dev/models/openai/gpt-oss-120b) | 128K | $0.07 / $0.30 | $0.000069 / $0.000297 | 99.9% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | 128K | $0.075 / $0.30 | $0.000075 / $0.0003 | 99.9% |
| [Qwen: Qwen3.8 Omni Flash](https://uberllm.dev/models/qwen/qwen3.8-omni-flash) | 1000K | $0.15 / $0.47 | $0.000146 / $0.000456 | 99.9% |
| [GLM 4.5 Air](https://uberllm.dev/models/z-ai/glm-4.5-air) | 128K | $0.20 / $1.10 | $0.000129 / $0.000842 | 99.9% |
| [Gemma 3 4B IT](https://uberllm.dev/models/google/gemma-3-4b-it) | 128K | $0.05 / $0.10 | $0.000467 / $0.000584 | 99.1–99.4% |
| [Gemma 4 E2B](https://uberllm.dev/models/google/gemma-4-e2b) | 128K | $0.04 / $0.08 | $0.0004 / $0.0008 | 99% |
| [Gemma 4 26B A4B IT](https://uberllm.dev/models/google/gemma-4-26b-a4b-it) | 262K | $0.08 / $0.10 | $0.00038 / $0.00114 | 98.9–99.5% |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | 1048K | $0.006 / $0.50 | $0.000179 / $0.001374 | 97–99.7% |
| [Gemma 3 12B IT](https://uberllm.dev/models/google/gemma-3-12b-it) | 128K | $0.05 / $0.15 | $0.000495 / $0.001485 | 99% |
| [Ministral 3B](https://uberllm.dev/models/mistralai/ministral-3-3b-instruct) | 128K | $0.10 / $0.10 | $0.001 / $0.001 | 99% |
| [GLM 4.7 Flash](https://uberllm.dev/models/z-ai/glm-4.7-flash) | 198K | $0.0605 / $0.40 | $0.000309 / $0.00204 | 99.5% |
| [Qwen 3.8 27B](https://uberllm.dev/models/qwen/qwen-3-8-27b) | 262K | $0.15 / $1.88 | $0.000195 / $0.002438 | 99.9% |
| [Gemma 3 27B](https://uberllm.dev/models/google/gemma-3-27b-it) | 40K | $0.08 / $0.20 | $0.000792 / $0.00198 | 99% |
| [NVIDIA Nemotron Nano 9B v2](https://uberllm.dev/models/nvidia/nemotron-nano-9b-v2) | 128K | $0.06 / $0.23 | $0.0006 / $0.0023 | 99% |

### Major model makers

<details><summary>OpenAI, Anthropic, Google, DeepSeek, xAI, Qwen, Moonshot, Z.ai, Mistral, Meta (164 models)</summary>

| Model | Maker | Context | Official price | UberLLM price | Below list |
|---|---|---|---|---|---|
| [GPT-5.4 Pro](https://uberllm.dev/models/openai/gpt-5.4-pro) | openai | 1000K | $30.00 / $180.00 | $4.35 / $26.07 | 85.5% |
| [GPT-5.5 Pro](https://uberllm.dev/models/openai/gpt-5.5-pro) | openai | 1000K | $30.00 / $180.00 | $7.14 / $42.82 | 76.2% |
| [GPT-6 Astra](https://uberllm.dev/models/openai/gpt-6-astra) | openai | 1050K | $10.00 / $50.00 | $0.1049 / $0.5246 | 99% |
| [GPT-5.5](https://uberllm.dev/models/openai/gpt-5.5) | openai | 1000K | $5.00 / $30.00 | $0.125 / $0.75 | 97.5% |
| [GPT-5.6 Sol](https://uberllm.dev/models/openai/gpt-5.6-sol) | openai | 1050K | $4.00 / $20.00 | $0.07598 / $0.3799 | 98.1% |
| [GPT-5.6 Sol Pro](https://uberllm.dev/models/openai/gpt-5.6-sol-pro) | openai | 1050K | $4.00 / $20.00 | $1.58 / $7.90 | 60.5% |
| [GPT-5.4](https://uberllm.dev/models/openai/gpt-5.4) | openai | 1000K | $2.50 / $15.00 | $0.0625 / $0.375 | 97.5% |
| [GPT-5.2](https://uberllm.dev/models/openai/gpt-5.2) | openai | 256K | $1.75 / $14.00 | $0.1458 / $1.17 | 91.7% |
| [GPT-5.2 Codex](https://uberllm.dev/models/openai/gpt-5.2-codex) | openai | 256K | $1.75 / $14.00 | $0.4375 / $3.50 | 75% |
| [GPT-5.3 Codex](https://uberllm.dev/models/openai/gpt-5.3-codex) | openai | 400K | $1.75 / $14.00 | $0.3907 / $3.13 | 77.7% |
| [GPT-5.6 Terra](https://uberllm.dev/models/openai/gpt-5.6-terra) | openai | 1050K | $2.00 / $12.00 | $0.04003 / $0.2402 | 98% |
| [GPT-5.6 Terra Pro](https://uberllm.dev/models/openai/gpt-5.6-terra-pro) | openai | 1050K | $2.00 / $12.00 | $1.11 / $6.68 | 44.3% |
| [GPT-4o](https://uberllm.dev/models/openai/gpt-4o) | openai | 128K | $2.50 / $10.00 | $0.374 / $1.50 | 85% |
| [GPT-6 Sol](https://uberllm.dev/models/openai/gpt-6-sol) | openai | 1050K | $2.00 / $10.00 | $0.03988 / $0.1994 | 98% |
| [GPT-6 Sol Pro](https://uberllm.dev/models/openai/gpt-6-sol-pro) | openai | 1050K | $2.00 / $10.00 | $1.70 / $8.50 | 15% |
| [GPT-6.1 Sol](https://uberllm.dev/models/openai/gpt-6.1-sol) | openai | 1050K | $2.00 / $10.00 | $0.04 / $0.20 | 98% |
| [OpenAI: GPT-6.1 Sol Pro](https://uberllm.dev/models/openai/gpt-6.1-sol-pro) | openai | 1050K | $2.00 / $10.00 | $1.70 / $8.50 | 15% |
| [OpenAI: GPT-6.1 Terra](https://uberllm.dev/models/openai/gpt-6.1-terra) | openai | 1050K | $1.00 / $5.00 | $0.02082 / $0.1041 | 97.9% |
| [OpenAI: GPT-6.1 Terra Pro](https://uberllm.dev/models/openai/gpt-6.1-terra-pro) | openai | 1050K | $1.00 / $5.00 | $0.85 / $4.25 | 15% |
| [GPT-5.4 Mini](https://uberllm.dev/models/openai/gpt-5.4-mini) | openai | 400K | $0.75 / $4.50 | $0.07499 / $0.4499 | 90% |
| [GPT 5 Mini](https://uberllm.dev/models/openai/gpt-5-mini) | openai | 400K | $0.25 / $2.00 | $0.06172 / $0.4938 | 75.3% |
| [GPT 5.4 Nano](https://uberllm.dev/models/openai/gpt-5.4-nano) | openai | 400K | $0.20 / $1.25 | $0.03951 / $0.247 | 80.2% |
| [GPT-5.6 Luna](https://uberllm.dev/models/openai/gpt-5.6-luna) | openai | 1050K | $0.20 / $1.20 | $0.005006 / $0.03003 | 97.5% |
| [GPT-5.6 Luna Pro](https://uberllm.dev/models/openai/gpt-5.6-luna-pro) | openai | 1050K | $0.20 / $1.20 | $0.1038 / $0.623 | 48.1% |
| [GPT OSS 120B](https://uberllm.dev/models/openai/e2ee-gpt-oss-120b-p) | openai | 128K | $0.13 / $0.65 | $0.06494 / $0.3247 | 50–50.1% |
| [GPT-4o Mini](https://uberllm.dev/models/openai/gpt-4o-mini) | openai | 128K | $0.15 / $0.60 | $0.009 / $0.036 | 94% |
| [GPT OSS Safeguard 120B](https://uberllm.dev/models/openai/gpt-oss-safeguard-120b) | openai | 128K | $0.15 / $0.60 | $0.015 / $0.06 | 90% |
| [GPT-6 Luna](https://uberllm.dev/models/openai/gpt-6-luna) | openai | 1050K | $0.10 / $0.50 | $0.002959 / $0.01479 | 97% |
| [GPT-6 Luna Pro](https://uberllm.dev/models/openai/gpt-6-luna-pro) | openai | 1050K | $0.10 / $0.50 | $0.08499 / $0.4249 | 15% |
| [GPT 5 Nano](https://uberllm.dev/models/openai/gpt-5-nano) | openai | 400K | $0.05 / $0.40 | $0.007322 / $0.05857 | 85.4% |
| [GPT-OSS 120B](https://uberllm.dev/models/openai/gpt-oss-120b) | openai | 128K | $0.07 / $0.30 | $0.000069 / $0.000297 | 99.9% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | openai | 128K | $0.075 / $0.30 | $0.000075 / $0.0003 | 99.9% |
| [GPT-OSS 20B](https://uberllm.dev/models/openai/gpt-oss-20b) | openai | 128K | $0.03 / $0.13 | $0.000018 / $0.00009 | 99.9% |
| [Claude Fable 5](https://uberllm.dev/models/anthropic/claude-fable-5) | anthropic | 1000K | $10.00 / $50.00 | $0.7794 / $3.90 | 92.2% |
| [Claude Fable 5.1](https://uberllm.dev/models/anthropic/claude-fable-5.1) | anthropic | 1000K | $10.00 / $50.00 | $0.5904 / $2.95 | 94.1% |
| [Claude Opus 4.8 Fast](https://uberllm.dev/models/anthropic/claude-opus-4.8-fast) | anthropic | 1000K | $10.00 / $50.00 | $5.69 / $28.47 | 43.1% |
| [Claude Opus 5 (Fast)](https://uberllm.dev/models/anthropic/claude-opus-5-fast) | anthropic | 1000K | $10.00 / $50.00 | $4.94 / $24.68 | 50.6% |
| [Claude Fable 5.2](https://uberllm.dev/models/anthropic/claude-fable-5.2) | anthropic | 1000K | $8.00 / $40.00 | $0.7154 / $3.58 | 91.1% |
| [Claude Opus 4.5](https://uberllm.dev/models/anthropic/claude-opus-4.5) | anthropic | 198K | $5.00 / $25.00 | $0.3649 / $1.82 | 92.7% |
| [Claude Opus 4.6](https://uberllm.dev/models/anthropic/claude-opus-4.6) | anthropic | 1000K | $5.00 / $25.00 | $0.0925 / $0.4625 | 98.2% |
| [Claude Opus 4.7](https://uberllm.dev/models/anthropic/claude-opus-4.7) | anthropic | 1000K | $5.00 / $25.00 | $0.035 / $0.175 | 99.3% |
| [Claude Opus 4.8](https://uberllm.dev/models/anthropic/claude-opus-4.8) | anthropic | 1000K | $5.00 / $25.00 | $0.337 / $1.69 | 93.3% |
| [Claude Opus 5](https://uberllm.dev/models/anthropic/claude-opus-5) | anthropic | 1000K | $5.00 / $25.00 | $0.17 / $0.85 | 96.6% |
| [Claude Opus 5.5](https://uberllm.dev/models/anthropic/claude-opus-5.5) | anthropic | 1000K | $4.00 / $20.00 | $0.1716 / $0.8578 | 95.7% |
| [Claude Sonnet 4.5](https://uberllm.dev/models/anthropic/claude-sonnet-4.5) | anthropic | 198K | $3.00 / $15.00 | $0.5742 / $2.87 | 80.9% |
| [Claude Sonnet 4.6](https://uberllm.dev/models/anthropic/claude-sonnet-4.6) | anthropic | 1000K | $3.00 / $15.00 | $0.051 / $0.255 | 98.3% |
| [Claude Sonnet 5](https://uberllm.dev/models/anthropic/claude-sonnet-5) | anthropic | 1000K | $2.00 / $10.00 | $0.0954 / $0.477 | 95.2% |
| [Claude Sonnet 5.5](https://uberllm.dev/models/anthropic/claude-sonnet-5.5) | anthropic | 1000K | $2.00 / $10.00 | $0.1578 / $0.7888 | 92.1% |
| [Claude Haiku 4.5](https://uberllm.dev/models/anthropic/claude-haiku-4.5) | anthropic | 200K | $1.00 / $5.00 | $0.0592 / $0.296 | 94.1% |
| [Claude Haiku 5.5](https://uberllm.dev/models/anthropic/claude-haiku-5.5) | anthropic | 100K | $0.10 / $0.50 | $0.007573 / $0.03787 | 92.4% |
| [Gemini 3.1 Pro Preview](https://uberllm.dev/models/google/gemini-3.1-pro-preview) | google | 1000K | $2.00 / $12.00 | $0.1098 / $0.6587 | 94.5% |
| [Gemini 2.5 Pro](https://uberllm.dev/models/google/gemini-2.5-pro) | google | 1048K | $1.25 / $10.00 | $0.1622 / $1.30 | 87% |
| [Google: Gemini 4 Argon](https://uberllm.dev/models/google/gemini-4-argon) | google | 1048K | $2.00 / $10.00 | $0.00998 / $0.0499 | 99.5% |
| [Gemini 3.5 Flash](https://uberllm.dev/models/google/gemini-3.5-flash) | google | 1000K | $1.50 / $9.00 | $0.007485 / $0.04491 | 99.5% |
| [Gemini 3.8 Flash](https://uberllm.dev/models/google/gemini-3.8-flash) | google | 1048K | $0.825 / $4.12 | $0.001032 / $0.00516 | 99.9% |
| [Gemini 3.6 Flash](https://uberllm.dev/models/google/gemini-3-6-flash) | google | 1000K | $0.75 / $3.75 | $0.3937 / $1.97 | 47.5% |
| [Gemini 3.7 Flash](https://uberllm.dev/models/google/gemini-3.7-flash) | google | 1048K | $0.75 / $3.75 | $0.004117 / $0.02058 | 99.5% |
| [Gemini 3 Flash Preview](https://uberllm.dev/models/google/gemini-3-flash-preview) | google | 256K | $0.50 / $3.00 | $0.0025 / $0.015 | 99.5% |
| [Gemini 2.5 Flash](https://uberllm.dev/models/google/gemini-2.5-flash) | google | 1048K | $0.30 / $2.50 | $0.00285 / $0.02375 | 99.1% |
| [Gemini 3.5 Flash Lite](https://uberllm.dev/models/google/gemini-3-5-flash-lite) | google | 1000K | $0.30 / $2.50 | $0.1677 / $1.40 | 44.1% |
| [Gemini 3.1 Flash Lite](https://uberllm.dev/models/google/gemini-3.1-flash-lite) | google | 1048K | $0.25 / $1.50 | $0.00125 / $0.0075 | 99.5% |
| [Gemma 4 31B (E2EE)](https://uberllm.dev/models/google/e2ee-gemma-4-31b) | google | 262K | $0.12 / $0.36 | $0.10 / $0.30 | 16.7% |
| [Gemma 4 31B](https://uberllm.dev/models/google/gemma-4-31b) | google | 256K | $0.12 / $0.36 | $0.024 / $0.072 | 80% |
| [Gemma 4 31B IT](https://uberllm.dev/models/google/gemma-4-31b-it) | google | 262K | $0.12 / $0.36 | $0.000912 / $0.002736 | 99.2% |
| [Gemma 3 27B](https://uberllm.dev/models/google/gemma-3-27b-it) | google | 40K | $0.08 / $0.20 | $0.000792 / $0.00198 | 99% |
| [Gemma 3 12B IT](https://uberllm.dev/models/google/gemma-3-12b-it) | google | 128K | $0.05 / $0.15 | $0.000495 / $0.001485 | 99% |
| [Gemma 3 4B IT](https://uberllm.dev/models/google/gemma-3-4b-it) | google | 128K | $0.05 / $0.10 | $0.000467 / $0.000584 | 99.1–99.4% |
| [Gemma 4 26B A4B IT](https://uberllm.dev/models/google/gemma-4-26b-a4b-it) | google | 262K | $0.08 / $0.10 | $0.00038 / $0.00114 | 98.9–99.5% |
| [Gemma 4 E2B](https://uberllm.dev/models/google/gemma-4-e2b) | google | 128K | $0.04 / $0.08 | $0.0004 / $0.0008 | 99% |
| [DeepSeek V4 Pro 0813](https://uberllm.dev/models/deepseek/deepseek-v4-pro-0813) | deepseek | 1048K | $0.111 / $4.44 | $0.002394 / $0.09576 | 97.8% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | deepseek | 1000K | $0.9553 / $1.91 | $0.002171 / $0.004342 | 99.8% |
| [DeepSeek: DeepSeek V4 Flash Vision Exp](https://uberllm.dev/models/deepseek/deepseek-v4-flash-vision-exp) | deepseek | 1048K | $0.44 / $1.32 | $0.3784 / $1.14 | 14% |
| [DeepSeek V3.1](https://uberllm.dev/models/deepseek/deepseek-v3.1) | deepseek | 128K | $0.25 / $0.95 | $0.002475 / $0.009405 | 99% |
| [DeepSeek V4 Flash 0731 Fast](https://uberllm.dev/models/deepseek/deepseek-v4-flash-0731-fast) | deepseek | 1000K | $0.35 / $0.70 | $0.21 / $0.42 | 40% |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | deepseek | 1048K | $0.006 / $0.50 | $0.000179 / $0.001374 | 97–99.7% |
| [DeepSeek V4.1 Flash 1017](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash-1017) | deepseek | 1048K | $0.006 / $0.50 | $0.000287 / $0.02392 | 95.2% |
| [DeepSeek V3.2](https://uberllm.dev/models/deepseek/deepseek-v3.2) | deepseek | 160K | $0.26 / $0.38 | $0.0026 / $0.0038 | 99% |
| [DeepSeek V4 Flash E2EE](https://uberllm.dev/models/deepseek/e2ee-deepseek-v4-flash) | deepseek | 1000K | $0.182 / $0.373 | $0.1092 / $0.2238 | 40% |
| [DeepSeek V4 Flash 0731](https://uberllm.dev/models/deepseek/deepseek-v4-flash-0731) | deepseek | 1048K | $0.0434 / $0.26 | $0.00212 / $0.0127 | 95.1% |
| [DeepSeek V4 Flash](https://uberllm.dev/models/deepseek/deepseek-v4-flash) | deepseek | 1000K | $0.091 / $0.182 | $0.004417 / $0.008833 | 95.1% |
| [Grok 4.5](https://uberllm.dev/models/x-ai/grok-4.5) | x-ai | 500K | $2.00 / $6.00 | $0.03615 / $0.1085 | 98.2% |
| [Grok 4.6](https://uberllm.dev/models/x-ai/grok-4.6) | x-ai | 500K | $2.00 / $6.00 | $0.1523 / $0.4568 | 92.4% |
| [Grok 4.7](https://uberllm.dev/models/x-ai/grok-4.7) | x-ai | 500K | $2.00 / $6.00 | $0.03351 / $0.1005 | 98.3% |
| [Grok 4.20 Beta](https://uberllm.dev/models/x-ai/grok-4.20-beta) | x-ai | 2000K | $1.25 / $2.50 | $0.175 / $0.35 | 86% |
| [Grok 4.20 Multi-Agent Beta](https://uberllm.dev/models/x-ai/grok-4.20-multi-agent-beta) | x-ai | 2000K | $1.25 / $2.50 | $0.175 / $0.35 | 86% |
| [Grok 4.3](https://uberllm.dev/models/x-ai/grok-4.3) | x-ai | 1000K | $1.25 / $2.50 | $0.01238 / $0.02475 | 99% |
| [Grok Build 0.1](https://uberllm.dev/models/x-ai/grok-build-0.1) | x-ai | 256K | $1.00 / $2.00 | $0.60 / $1.20 | 40% |
| [Qwen: Qwen3.8 Max Prime](https://uberllm.dev/models/qwen/qwen3.8-max-prime) | qwen | 1000K | $4.00 / $12.00 | $3.96 / $11.88 | 1% |
| [Qwen3.7 Max](https://uberllm.dev/models/qwen/qwen3.7-max) | qwen | 256K | $2.70 / $8.05 | $1.00 / $3.00 | 62.7–63% |
| [Qwen 3.8 Max](https://uberllm.dev/models/qwen/qwen-3-8-max) | qwen | 1000K | $2.50 / $7.50 | $0.1136 / $0.3409 | 95.5% |
| [Qwen3.8 2.4T A95B](https://uberllm.dev/models/qwen/qwen3.8-2.4t-a95b) | qwen | 1000K | $2.00 / $6.00 | $0.01394 / $0.04182 | 99.3% |
| [Qwen: Qwen3.8 Max (0902)](https://uberllm.dev/models/qwen/qwen3.8-max-0902) | qwen | 1000K | $2.00 / $6.00 | $0.002123 / $0.006369 | 99.9% |
| [Qwen 3.5 397B](https://uberllm.dev/models/qwen/qwen3.5-397b-a17b) | qwen | 128K | $0.60 / $3.60 | $0.01675 / $0.1005 | 97.2% |
| [Qwen 3 235B A22B Thinking 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-thinking-2507) | qwen | 128K | $0.45 / $3.50 | $0.075 / $0.075 | 83.3–97.9% |
| [Qwen 3.6 27B](https://uberllm.dev/models/qwen/qwen3.6-27b) | qwen | 256K | $0.32 / $3.20 | $0.01438 / $0.1438 | 95.5% |
| [Qwen 3.7 Plus](https://uberllm.dev/models/qwen/qwen3.7-plus) | qwen | 256K | $0.50 / $2.00 | $0.2493 / $0.997 | 50.1% |
| [Qwen3 VL 235B A22B](https://uberllm.dev/models/qwen/qwen3-vl-235b-a22b-instruct) | qwen | 256K | $0.21 / $1.90 | $0.0273 / $0.247 | 87% |
| [Qwen3 VL 235B](https://uberllm.dev/models/qwen/qwen3-vl-235b-a22b-thinking) | qwen | 256K | $0.21 / $1.90 | $0.1048 / $0.9481 | 50.1% |
| [Qwen 3.8 27B](https://uberllm.dev/models/qwen/qwen-3-8-27b) | qwen | 262K | $0.15 / $1.88 | $0.000195 / $0.002438 | 99.9% |
| [Qwen 3 Coder 480B Turbo](https://uberllm.dev/models/qwen/qwen3-coder-turbo) | qwen | 256K | $0.35 / $1.50 | $0.1153 / $0.4943 | 67% |
| [Qwen 3.6 35B A3B (E2EE)](https://uberllm.dev/models/qwen/e2ee-qwen3-6-35b-a3b) | qwen | 128K | $0.182 / $1.18 | $0.091 / $0.59 | 50% |
| [Qwen3 Next 80B A3B](https://uberllm.dev/models/qwen/qwen3-next-80b-a3b-instruct) | qwen | 256K | $0.09 / $1.10 | $0.000861 / $0.009473 | 99–99.1% |
| [Qwen 3.6 35B A3B](https://uberllm.dev/models/qwen/qwen3-6-35b-a3b) | qwen | 262K | $0.10 / $1.00 | $0.004235 / $0.04235 | 95.8% |
| [Qwen 3 Coder 480b](https://uberllm.dev/models/qwen/qwen3-coder) | qwen | 256K | $0.30 / $1.00 | $0.003 / $0.01 | 99% |
| [Qwen 3.5 35B A3B](https://uberllm.dev/models/qwen/qwen3.5-35b-a3b) | qwen | 256K | $0.15 / $1.00 | $0.08893 / $0.5928 | 40.7% |
| [Qwen3 VL 30B A3B](https://uberllm.dev/models/qwen/qwen3-vl-30b-a3b-thinking) | qwen | 128K | $0.25 / $0.90 | $0.10 / $0.45 | 50–60% |
| [Qwen3 Coder Next](https://uberllm.dev/models/qwen/qwen3-coder-next) | qwen | 256K | $0.12 / $0.80 | $0.001188 / $0.00792 | 99% |
| [Qwen 3 235B A22B Instruct 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-2507) | qwen | 128K | $0.14 / $0.75 | $0.02187 / $0.0875 | 84.4–88.3% |
| [Qwen3 Coder 30B A3B Instruct](https://uberllm.dev/models/qwen/qwen3-coder-30b-a3b-instruct) | qwen | 256K | $0.15 / $0.60 | $0.0015 / $0.006 | 99% |
| [Qwen3 30B A3B](https://uberllm.dev/models/qwen/qwen3-30b-a3b) | qwen | 256K | $0.12 / $0.50 | $0.084 / $0.35 | 30% |
| [Qwen3.8 Flash](https://uberllm.dev/models/qwen/qwen3.8-flash) | qwen | 1000K | $0.15 / $0.47 | $0.00147 / $0.004606 | 99% |
| [Qwen: Qwen3.8 Omni Flash](https://uberllm.dev/models/qwen/qwen3.8-omni-flash) | qwen | 1000K | $0.15 / $0.47 | $0.000146 / $0.000456 | 99.9% |
| [Qwen3 32B](https://uberllm.dev/models/qwen/qwen3-32b) | qwen | 32K | $0.08 / $0.28 | $0.0104 / $0.0364 | 87% |
| [Qwen 3.5 9B](https://uberllm.dev/models/qwen/qwen3.5-9b) | qwen | 256K | $0.17 / $0.25 | $0.03 / $0.09 | 64–82.4% |
| [Qwen 2.5 7B](https://uberllm.dev/models/qwen/e2ee-qwen-2-5-7b-p) | qwen | 32K | $0.05 / $0.13 | $0.02498 / $0.06494 | 50% |
| [Qwen: Qwen3.7 Flash](https://uberllm.dev/models/qwen/qwen3.7-flash) | qwen | 1000K | $0.03 / $0.13 | $0.001216 / $0.005268 | 95.9% |
| [Kimi K3 Fast](https://uberllm.dev/models/moonshotai/kimi-k3-fast-api) | moonshotai | 1000K | $4.50 / $22.50 | $2.70 / $13.50 | 40% |
| [Kimi K3](https://uberllm.dev/models/moonshotai/kimi-k3) | moonshotai | 1000K | $0.192 / $16.00 | $0.000946 / $0.07883 | 99.5% |
| [MoonshotAI: Kimi K3.1 Pro](https://uberllm.dev/models/moonshotai/kimi-k3.1-pro) | moonshotai | 1048K | $2.00 / $10.00 | $0.06691 / $0.3345 | 96.7% |
| [Kimi K2.7 Code](https://uberllm.dev/models/moonshotai/kimi-k2.7-code) | moonshotai | 262K | $0.60 / $3.50 | $0.01151 / $0.06712 | 98.1% |
| [Kimi K2.6](https://uberllm.dev/models/moonshotai/kimi-k2.6) | moonshotai | 256K | $0.65 / $3.41 | $0.008283 / $0.04345 | 98.7% |
| [Kimi K2.5](https://uberllm.dev/models/moonshotai/kimi-k2.5) | moonshotai | 256K | $0.532 / $3.33 | $0.003192 / $0.01995 | 99.4% |
| [Kimi K2 Thinking](https://uberllm.dev/models/moonshotai/kimi-k2-thinking) | moonshotai | 256K | $0.60 / $2.50 | $0.078 / $0.325 | 87% |
| [Kimi K2](https://uberllm.dev/models/moonshotai/kimi-k2) | moonshotai | 256K | $0.57 / $2.30 | $0.399 / $1.61 | 30% |
| [Z.ai: GLM 5.3 Prime](https://uberllm.dev/models/z-ai/glm-5.3-prime) | z-ai | 1000K | $2.80 / $8.80 | $0.02526 / $0.07938 | 99.1% |
| [GLM 5.2 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5-2-p) | z-ai | 524K | $1.75 / $5.75 | $0.8689 / $2.85 | 50.3% |
| [GLM 5.1 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5.1) | z-ai | 200K | $1.40 / $4.40 | $0.44 / $1.66 | 62.3–68.6% |
| [GLM 5.1](https://uberllm.dev/models/z-ai/glm-5.1) | z-ai | 200K | $1.40 / $4.40 | $0.00966 / $0.03036 | 99.3% |
| [GLM 5.1 Non-thinking](https://uberllm.dev/models/z-ai/glm-5.1-non-thinking) | z-ai | 200K | $1.40 / $4.40 | $1.00 / $3.35 | 23.9–28.2% |
| [GLM-5.2](https://uberllm.dev/models/z-ai/glm-5.2) | z-ai | 1048K | $0.006 / $4.40 | $0.00052 / $0.00352 | 91.3–99.9% |
| [GLM-5 Turbo](https://uberllm.dev/models/z-ai/glm-5-turbo) | z-ai | 200K | $1.20 / $4.00 | $0.06 / $0.20 | 95% |
| [GLM 5V Turbo](https://uberllm.dev/models/z-ai/glm-5v-turbo) | z-ai | 200K | $1.20 / $4.00 | $0.72 / $2.40 | 40% |
| [GLM-5](https://uberllm.dev/models/z-ai/glm-5) | z-ai | 198K | $1.00 / $3.20 | $0.00397 / $0.0127 | 99.6% |
| [GLM 4.5](https://uberllm.dev/models/z-ai/glm-4.5) | z-ai | 128K | $0.60 / $2.20 | $0.00588 / $0.02156 | 99% |
| [GLM-4.7](https://uberllm.dev/models/z-ai/glm-4.7) | z-ai | 128K | $0.55 / $2.20 | $0.00253 / $0.01012 | 99.5% |
| [GLM 4.7 Thinking](https://uberllm.dev/models/z-ai/glm-4.7-thinking) | z-ai | 128K | $0.45 / $2.00 | $0.45 / $2.00 | 0% |
| [GLM-4.6](https://uberllm.dev/models/z-ai/glm-4.6) | z-ai | 198K | $0.43 / $1.75 | $0.004172 / $0.01698 | 99% |
| [GLM 5.3](https://uberllm.dev/models/z-ai/glm-5.3) | z-ai | 1000K | $0.0699 / $1.40 | $0.000647 / $0.01295 | 99.1% |
| [Z.ai: GLM 5.3 FlashX](https://uberllm.dev/models/z-ai/glm-5.3-flashx) | z-ai | 1048K | $0.37 / $1.25 | $0.1026 / $0.3465 | 72.3% |
| [Z.ai: GLM 5.3 FlashX Legal](https://uberllm.dev/models/z-ai/glm-5.3-flashx-legal) | z-ai | 1048K | $0.37 / $1.25 | $0.2564 / $0.8662 | 30.7% |
| [GLM 4.5 Air](https://uberllm.dev/models/z-ai/glm-4.5-air) | z-ai | 128K | $0.20 / $1.10 | $0.000129 / $0.000842 | 99.9% |
| [GLM 5.3 Flash](https://uberllm.dev/models/z-ai/glm-5.3-flash) | z-ai | 1048K | $0.15 / $0.50 | $0.001283 / $0.004276 | 99.1% |
| [GLM 4.7 Flash](https://uberllm.dev/models/z-ai/glm-4.7-flash) | z-ai | 198K | $0.0605 / $0.40 | $0.000309 / $0.00204 | 99.5% |
| [Mistral Large](https://uberllm.dev/models/mistralai/mistral-large) | mistralai | 128K | $2.00 / $6.00 | $0.0928 / $0.2784 | 95.4% |
| [Mistral: Mistral Large 4](https://uberllm.dev/models/mistralai/mistral-large-4-0) | mistralai | 524K | $0.70 / $2.10 | $0.063 / $0.189 | 91% |
| [Devstral 2 123B](https://uberllm.dev/models/mistralai/devstral-2-123b) | mistralai | 256K | $0.40 / $2.00 | $0.004 / $0.02 | 99% |
| [Magistral Small 2509](https://uberllm.dev/models/mistralai/magistral-small-2509) | mistralai | 128K | $0.50 / $1.50 | $0.005 / $0.015 | 99% |
| [Mistral Large 3](https://uberllm.dev/models/mistralai/mistral-large-3) | mistralai | 256K | $0.50 / $1.50 | $0.005 / $0.015 | 99% |
| [Mistral Small 4](https://uberllm.dev/models/mistralai/mistral-small-4) | mistralai | 256K | $0.15 / $0.60 | $0.04688 / $0.1875 | 68.8% |
| [Mistral Small 3.2 24B Instruct](https://uberllm.dev/models/mistralai/mistral-small-3.2-24b-instruct) | mistralai | 256K | $0.0938 / $0.25 | $0.0135 / $0.036 | 85.6% |
| [Ministral 14B 3.0](https://uberllm.dev/models/mistralai/ministral-3-14b-instruct) | mistralai | 128K | $0.20 / $0.20 | $0.002 / $0.002 | 99% |
| [Ministral 3 8B](https://uberllm.dev/models/mistralai/ministral-3-8b-instruct) | mistralai | 128K | $0.15 / $0.15 | $0.0015 / $0.0015 | 99% |
| [Ministral 3B](https://uberllm.dev/models/mistralai/ministral-3-3b-instruct) | mistralai | 128K | $0.10 / $0.10 | $0.001 / $0.001 | 99% |
| [Meta: Muse Wonder](https://uberllm.dev/models/meta-llama/muse-wonder) | meta-llama | 1048K | $4.00 / $20.00 | $0.40 / $2.00 | 90% |
| [Meta: Muse Spark 1.1](https://uberllm.dev/models/meta-llama/muse-spark-1.1) | meta-llama | 1048K | $1.25 / $4.25 | $0.7017 / $2.39 | 43.9% |
| [Meta: Muse Spark 1.2](https://uberllm.dev/models/meta-llama/muse-spark-1.2) | meta-llama | 1048K | $1.25 / $4.25 | $0.375 / $1.27 | 70% |
| [Meta: Muse Spark 1.3](https://uberllm.dev/models/meta-llama/muse-spark-1.3) | meta-llama | 1048K | $1.25 / $4.25 | $0.125 / $0.425 | 90% |
| [Meta: Muse Spark Open](https://uberllm.dev/models/meta-llama/muse-spark-open) | meta-llama | 1048K | $1.25 / $4.25 | $0.6995 / $2.38 | 44% |
| [Meta: Muse Glimmer 30B](https://uberllm.dev/models/meta-llama/muse-glimmer-30b) | meta-llama | 131K | $0.30 / $1.20 | $0.297 / $1.19 | 1% |
| [Llama 3.3 70B Instruct](https://uberllm.dev/models/meta-llama/llama-3.3-70b-instruct) | meta-llama | 128K | $0.70 / $0.71 | $0.0147 / $0.04704 | 93.4–97.9% |
| [Meta: Muse Ember](https://uberllm.dev/models/meta-llama/muse-ember) | meta-llama | 1048K | $0.10 / $0.50 | $0.055 / $0.275 | 45% |
| [Llama 3.2 3B](https://uberllm.dev/models/meta-llama/llama-3.2-3b-instruct) | meta-llama | 128K | $0.05 / $0.33 | $0.025 / $0.165 | 50% |
| [Meta: Muse Spark 1.2 Contributor](https://uberllm.dev/models/meta-llama/muse-spark-1.2-contributor) | meta-llama | 1048K | $0.10 / $0.20 | $0.03 / $0.06 | 70% |
| [Meta: Muse Spark 1.3 Contributor](https://uberllm.dev/models/meta-llama/muse-spark-1.3-contributor) | meta-llama | 1048K | $0.10 / $0.20 | $0.03 / $0.06 | 70% |

</details>

### Image models (per image)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Seedream 4.5](https://uberllm.dev/models/bytedance/seedream-4.5) | $0.04 / image | $0.0004 / image | 99% |
| [Chroma (Venice)](https://uberllm.dev/models/venice/chroma) | $0.01 / image | $0.005 / image | 50% |
| [Z-Image Turbo (Venice)](https://uberllm.dev/models/venice/z-image-turbo) | $0.01 / image | $0.00594 / image | 40.6% |
| [Flux 1.1 (Venice, legacy)](https://uberllm.dev/models/venice/flux-1.1) | $0.01 / image | $0.006 / image | 40% |
| [Venice SD35](https://uberllm.dev/models/venice/sd35) | $0.01 / image | $0.006 / image | 40% |
| [Stable Diffusion XL (Venice, legacy)](https://uberllm.dev/models/venice/sdxl) | $0.01 / image | $0.006 / image | 40% |
| [Flux 2 Pro (Venice)](https://uberllm.dev/models/venice/flux-2-pro) | $0.03 / image | $0.0075 / image | 75% |
| [Grok Imagine — Edit (Venice)](https://uberllm.dev/models/venice/grok-imagine-edit) | $0.03 / image | $0.0147 / image | 51% |
| [Grok Imagine High Quality (Venice)](https://uberllm.dev/models/venice/grok-imagine-quality) | $0.06 / image | $0.015 / image | 75% |
| [Qwen Image (Venice)](https://uberllm.dev/models/venice/qwen-image) | $0.03 / image | $0.0165 / image | 45% |

### Image models (per megapixel)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [FLUX.2 Klein 4B](https://uberllm.dev/models/black-forest-labs/flux.2-klein-4b) | $0.015 / megapixel | $0.00375 / megapixel | 75% |
| [FLUX.2 Flex](https://uberllm.dev/models/black-forest-labs/flux.2-flex) | $0.06 / megapixel | $0.015 / megapixel | 75% |

### Video models (per second)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Longcat Distilled (image-to-video)](https://uberllm.dev/models/meituan/longcat-distilled-image-to-video) | $0.018 / sec | $0.0108 / sec | 40% |
| [LongCat Distilled Text-to-Video](https://uberllm.dev/models/meituan/longcat-distilled-text-to-video) | $0.018 / sec | $0.0108 / sec | 40% |
| [Hailuo 02 Standard Image to Video](https://uberllm.dev/models/fal-ai/minimax/hailuo-02/standard/image-to-video) | $0.017 / sec | $0.01445 / sec | 15% |
| [Pixverse C1 (reference-to-video)](https://uberllm.dev/models/pixverse/pixverse-c1-reference-to-video) | $0.0433 / sec | $0.02381 / sec | 45% |
| [Veo 3.1 Lite Text to Video](https://uberllm.dev/models/fal-ai/veo3.1/lite) | $0.03 / sec | $0.0255 / sec | 15% |
| [Pixverse C1 (image-to-video)](https://uberllm.dev/models/pixverse/pixverse-c1-image-to-video) | $0.0433 / sec | $0.02598 / sec | 40% |
| [Pixverse C1 Transition (transition)](https://uberllm.dev/models/pixverse/pixverse-c1-transition) | $0.0433 / sec | $0.02598 / sec | 40% |
| [Seedance 2.0 Mini (image-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-mini-image-to-video) | $0.044 / sec | $0.0264 / sec | 40% |
| [Seedance 2.0 Mini (reference-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-mini-reference-to-video) | $0.044 / sec | $0.0264 / sec | 40% |
| [Ovi Image-to-Video](https://uberllm.dev/models/ovi/ovi-image-to-video) | $0.044 / sec | $0.0264 / sec | 40% |

### Video models (per video)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Topaz Video Upscale](https://uberllm.dev/models/topaz-labs/topaz-video-upscale) | $0.15 / video | $0.09 / video | 40% |
| [Wan 2.2 A14B Text-to-Video](https://uberllm.dev/models/wan/wan-2-2-a14b-text-to-video) | $0.20 / video | $0.17 / video | 15% |
| [Runway Gen-4 Aleph](https://uberllm.dev/models/runway/runway-gen4-aleph) | $0.50 / video | $0.425 / video | 15% |
| [Cosmos Predict (image-to-video)](https://uberllm.dev/models/nvidia/cosmos-predict-image-to-video) | $0.801 / video | $0.5607 / video | 30% |

### Music models

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Sonilo V1.1 Sound Effects](https://uberllm.dev/models/sonilo/sonilo-sound-effects-v1-0) | – | $0.00207 / track | – |
| [Seed Audio 1.0](https://uberllm.dev/models/byteplus/seed-audio-1-0) | – | $0.002875 / track | – |
| [Sonilo V1.1 Music](https://uberllm.dev/models/sonilo/sonilo-music-v1-1) | – | $0.002875 / track | – |
| [MMAudio V2 Text-to-Audio (Venice)](https://uberllm.dev/models/venice/mmaudio-v2-text-to-audio) | $0.01 / track | $0.0045 / track | 55% |
| [ElevenLabs Sound Effects v2 (Venice)](https://uberllm.dev/models/venice/elevenlabs-sound-effects-v2) | $0.02 / track | $0.011 / track | 45% |
| [ACE-Step 1.5 (Venice)](https://uberllm.dev/models/venice/ace-step-15) | $0.03 / track | $0.0135 / track | 55% |
| [MiniMax Music 2.0 (Venice)](https://uberllm.dev/models/venice/minimax-music-v2) | $0.04 / track | $0.018 / track | 55% |
| [Venice Music Gen (legacy alias)](https://uberllm.dev/models/venice/music-gen) | $0.03 / track | $0.018 / track | 40% |
| [ElevenLabs TTS v4 Turbo](https://uberllm.dev/models/elevenlabs/elevenlabs-tts-v4-turbo) | – | $0.046 / track | – |
| [ElevenLabs TTS Multilingual v2 (Venice audio)](https://uberllm.dev/models/venice/elevenlabs-tts-multilingual-v2) | $0.12 / track | $0.054 / track | 55% |

### Speech models

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Kokoro Text to Speech (Venice)](https://uberllm.dev/models/venice/kokoro-tts) | $0.0035 / 1K chars | $0.0021 / 1K chars | 40% |
| [Venice TTS 1 (legacy alias)](https://uberllm.dev/models/venice/tts-1) | $0.0035 / 1K chars | $0.0021 / 1K chars | 40% |
| [Inworld 1.5 Max TTS](https://uberllm.dev/models/inworld/tts-inworld-1-5-max) | $0.0125 / 1K chars | $0.006875 / 1K chars | 45% |
| [xAI v1 TTS](https://uberllm.dev/models/x-ai/tts-xai-v1) | $0.01875 / 1K chars | $0.01125 / 1K chars | 40% |
| [Chatterbox HD TTS](https://uberllm.dev/models/resemble-ai/tts-chatterbox-hd) | $0.05 / 1K chars | $0.03 / 1K chars | 40% |
| [Orpheus TTS](https://uberllm.dev/models/canopy-labs/tts-orpheus) | $0.0625 / 1K chars | $0.03438 / 1K chars | 45% |
| [ElevenLabs Turbo v2.5 TTS (Venice)](https://uberllm.dev/models/venice/elevenlabs-tts-turbo-v2-5) | $0.0625 / 1K chars | $0.0375 / 1K chars | 40% |
| [Qwen3 0.6B TTS](https://uberllm.dev/models/qwen/tts-qwen3-0-6b) | $0.0875 / 1K chars | $0.03938 / 1K chars | 55% |
| [Qwen3 1.7B TTS](https://uberllm.dev/models/qwen/tts-qwen3-1-7b) | $0.1125 / 1K chars | $0.06187 / 1K chars | 45% |
| [MiniMax Speech 02 HD TTS](https://uberllm.dev/models/minimax/tts-minimax-speech-02-hd) | $0.125 / 1K chars | $0.075 / 1K chars | 40% |

## Biggest drops this week (2026-11-03 to 2026-11-10)

From UberLLM's daily catalog snapshots (`GET /api/v1/public/price-changes`). Text: $ per 1M input / output tokens, sorted by the larger of the two moves.

### Official list price cuts

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [DeepSeek V4.1 Flash 1017](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash-1017) | text | $0.30 / $1.20 | $0.006 / $0.50 | in −98% / out −58% |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | text | $0.045 / $0.50 | $0.006 / $0.50 | in −87% / out 0% |
| [NVIDIA Nemotron 3 Super 120B](https://uberllm.dev/models/nvidia/nemotron-3-super-120b) | text | $0.30 / $2.40 | $0.075 / $0.40 | in −75% / out −83% |
| [Gemma 4 26B A4B IT](https://uberllm.dev/models/google/gemma-4-26b-a4b-it) | text | $0.086 / $0.258 | $0.08 / $0.10 | in −7% / out −61% |
| [GLM 5.3](https://uberllm.dev/models/z-ai/glm-5.3) | text | $0.08 / $3.60 | $0.0699 / $1.40 | in −13% / out −61% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | text | $1.60 / $3.20 | $0.9553 / $1.91 | −40% |
| [inclusionAI: Ling 3.1 Flash](https://uberllm.dev/models/inclusionai/ling-3.1-flash) | text | $0.075 / $0.225 | $0.045 / $0.135 | −40% |
| [MiniMax M2.7](https://uberllm.dev/models/minimax/minimax-m2.7) | text | $0.30 / $1.20 | $0.21 / $0.84 | −30% |
| [DeepSeek V4 Flash 0731](https://uberllm.dev/models/deepseek/deepseek-v4-flash-0731) | text | $0.059 / $0.26 | $0.0434 / $0.26 | in −26% / out 0% |
| [Qwen3 Next 80B A3B](https://uberllm.dev/models/qwen/qwen3-next-80b-a3b-instruct) | text | $0.10 / $1.10 | $0.09 / $1.10 | in −10% / out 0% |

### UberLLM price drops

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [Gemini 3.5 Flash](https://uberllm.dev/models/google/gemini-3.5-flash) | text | $0.39 / $2.34 | $0.015 / $0.09 | −96% |
| [Nano Banana (Gemini 2.5 Flash Image)](https://uberllm.dev/models/google/gemini-2.5-flash-image) | image | $0.075 / $0.625 | $0.003 / $0.025 | −96% |
| [MiniMax M2.7 Highspeed](https://uberllm.dev/models/minimax/minimax-m2.7-highspeed) | text | $0.54 / $2.16 | $0.03 / $0.12 | −94% |
| [Gemini 3.8 Flash](https://uberllm.dev/models/google/gemini-3.8-flash) | text | $0.2805 / $1.40 | $0.02475 / $0.1237 | −91% |
| [Gemini 3.1 Flash Lite](https://uberllm.dev/models/google/gemini-3.1-flash-lite) | text | $0.08 / $0.48 | $0.0075 / $0.045 | −91% |
| [Gemini 2.5 Flash](https://uberllm.dev/models/google/gemini-2.5-flash) | text | $0.027 / $0.225 | $0.003 / $0.025 | −89% |
| [GLM-5.2](https://uberllm.dev/models/z-ai/glm-5.2) | text | $0.00084 / $0.616 | $0.00012 / $0.088 | −86% |
| [Qwen3.5 Flash](https://uberllm.dev/models/qwen/qwen3.5-flash) | text | $0.09 / $0.36 | $0.014 / $0.056 | −84% |
| [Qwen3.5 Plus](https://uberllm.dev/models/qwen/qwen3.5-plus) | text | $0.234 / $1.40 | $0.0364 / $0.2184 | −84% |
| [Qwen: Qwen3.8 Max (0902)](https://uberllm.dev/models/qwen/qwen3.8-max-0902) | text | $0.22 / $0.66 | $0.04 / $0.12 | −82% |

Every change, day by day: [`CHANGELOG.md`](CHANGELOG.md).

## Use the data

Plain HTTPS, no key. Raw file URLs:

- JSON: `https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.json`
- CSV: `https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.csv`
- A past day: `https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/history/YYYY-MM-DD.csv`

Python (stdlib):

```python
import json, urllib.request
URL = "https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.json"
data = json.load(urllib.request.urlopen(URL))
chat = [m for m in data["models"] if m["category"] == "text" and m["available"]
        and m["list_output_usd_per_mtok"] and "tools" in m["capabilities"]]
for m in sorted(chat, key=lambda m: m["list_output_usd_per_mtok"])[:10]:
    print(m["id"], m["list_input_usd_per_mtok"], m["list_output_usd_per_mtok"], m["list_price_source"])
```

JavaScript:

```js
const res = await fetch("https://raw.githubusercontent.com/PSA-Team-source/llm-api-prices/main/prices.json");
const { updated_at, models } = await res.json();
const video = models.filter(m => m.category === "video" && m.unit === "second");
console.log(updated_at, video.sort((a, b) => a.uberllm_usd_per_unit - b.uberllm_usd_per_unit).slice(0, 5));
```

jq: `jq '.models[] | select(.maker=="anthropic") | {id, list_input_usd_per_mtok, list_output_usd_per_mtok}' prices.json`

### Fields

| Field | Meaning |
|---|---|
| `id` | Model id, as used in the `model` field of an OpenAI-compatible request to UberLLM |
| `category` | text, image, video, music, speech, transcription, embedding or other (from the output modality) |
| `unit` | `1M tokens` for token-priced models; otherwise what one unit price buys: `image`, `megapixel`, `second`, `job` (one video or track), `minute`, `1K characters` |
| `list_input_usd_per_mtok`, `list_output_usd_per_mtok` | Official list price, USD per 1M tokens |
| `uberllm_input_usd_per_mtok`, `uberllm_output_usd_per_mtok` | Lowest live UberLLM price at snapshot time, USD per 1M tokens |
| `list_usd_per_unit`, `uberllm_usd_per_unit` | The same for per-unit (media) prices |
| `pct_below_list_*` | 100 × (1 − UberLLM / list), one decimal; negative = above list; empty = no list price |
| `list_price_source`, `list_price_source_url`, `list_price_checked` | Where the official price comes from (see Sources) |
| `list_price_hosts` | JSON only: the published per-token prices of named hosts (Together AI, Fireworks, Bedrock, ...) for the model |
| `video_rates` | JSON only: every per-second video price by resolution and sound, official and UberLLM |
| `vendor_pricing_page` | The maker's own pricing page, to check a list price against |
| `capabilities` | tools, reasoning, vision, structured_outputs; video: text-to-video, image-to-video, sound |
| `available` | A request can be served right now |
| `nsfw` | Made for adult or unfiltered content (text only; adult image/video/sound models are not listed) |

## Sources

Every number comes from UberLLM's public catalog, read once a day by [`update.py`](update.py):

- `GET https://api.uberllm.dev/api/v1/public/models`: model list, context length, capabilities, official list prices, UberLLM prices.
- `GET https://api.uberllm.dev/api/v1/public/market/live`: the live market board (refreshed every 30 s). Its prices win over the catalog's, as on uberllm.dev.
- `GET https://api.uberllm.dev/v1/models`: the OpenAI-compatible model list (reasoning flag).
- `GET https://api.uberllm.dev/api/v1/public/price-changes`: the weekly diff used for "Biggest drops this week" and the first CHANGELOG entry.

Official list price, per row:

- `list_price_source = "UberLLM catalog list price"`: the direct (list) price the catalog carries for the model, which is the model maker's own API price for first-party models (OpenAI, Anthropic, Google, ...) and the host's list price for open-weight models. Check it against `vendor_pricing_page` and, for open-weight models, against `list_price_hosts`.
- Any other `list_price_source` (for example `OpenRouter`, `Z.ai`, `Fal`, `Kling (Kuaishou)`, `Stability AI`): the catalog had no list of its own, so the price was read from that public page (`list_price_source_url`) on `list_price_checked`.
- No official price: the field is empty. A media model whose only known official price is not above what UberLLM charges gets no official price, so a saving is never claimed against a number we cannot show.

UberLLM price = the best offer a seller on the UberLLM market makes at snapshot time, fee included. Market prices move during the day; the snapshot is a point in time, and <https://uberllm.dev/models> always has the current one.

Found a wrong official price? Open an issue with the vendor page that shows the right one.

## How it updates

`update.py` (Python stdlib only) runs once a day. It fetches the catalog, refuses an answer that lost more than 40% of the models, diffs against the last snapshot, and commits `prices.json`, `prices.csv`, `README.md`, `CHANGELOG.md` and `history/<day>.csv` through the GitHub GraphQL API (`createCommitOnBranch`), so commits are signed by GitHub. Nothing is committed when nothing changed.

Run it yourself: `python3 update.py --out ./build` writes every file locally without touching GitHub.

To run it from GitHub Actions instead, save this as `.github/workflows/update.yml` (also in [`docs/update.yml`](docs/update.yml)):

```yaml
name: update prices
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
```

## License

- Data (`prices.json`, `prices.csv`, `history/`, `CHANGELOG.md`): [CC BY 4.0](LICENSE-DATA). Credit: "LLM API prices, PSA-Team-source/llm-api-prices (UberLLM)" with a link to this repo.
- Code (`update.py`): [MIT](LICENSE).
