# LLM API prices

An open, daily-updated dataset of AI API prices: the official list price of 518 text, image, video, music and speech models next to the lowest live price on the [UberLLM](https://uberllm.dev/models) market, how far below list that is, context length and capabilities.

**Updated:** 2026-11-11T03:17:10Z · **Models:** 247 text, 89 image, 142 video, 20 music, 11 speech, 6 transcription, 3 other · **Files:** [`prices.json`](prices.json), [`prices.csv`](prices.csv), [`CHANGELOG.md`](CHANGELOG.md), [`history/`](history/)

Disclosure: this repo is maintained by the team that runs UberLLM. The UberLLM column is our own price; the official column is the maker's price, sourced as described in [Sources](#sources). Live prices: <https://uberllm.dev/models>.

## Cheapest right now

Lowest UberLLM price per category among models that can be called now. Text: $ per 1M input / output tokens. Full list: [`prices.csv`](prices.csv).

### Text (chat) models

| Model | Context | Official price | UberLLM price | Below list |
|---|---|---|---|---|
| [GPT-OSS 20B](https://uberllm.dev/models/openai/gpt-oss-20b) | 128K | $0.03 / $0.13 | $0.000018 / $0.000089 | 99.9% |
| [GPT-OSS 120B](https://uberllm.dev/models/openai/gpt-oss-120b) | 128K | $0.07 / $0.30 | $0.000069 / $0.000297 | 99.9% |
| [Qwen: Qwen3.8 Omni Flash](https://uberllm.dev/models/qwen/qwen3.8-omni-flash) | 1000K | $0.15 / $0.47 | $0.000146 / $0.000456 | 99.9% |
| [GLM 4.5 Air](https://uberllm.dev/models/z-ai/glm-4.5-air) | 128K | $0.20 / $1.10 | $0.000129 / $0.000842 | 99.9% |
| [Gemma 3 4B IT](https://uberllm.dev/models/google/gemma-3-4b-it) | 128K | $0.05 / $0.10 | $0.000346 / $0.000693 | 99.3% |
| [Gemma 4 E2B](https://uberllm.dev/models/google/gemma-4-e2b) | 128K | $0.04 / $0.08 | $0.000399 / $0.000798 | 99% |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | 1048K | $0.30 / $1.20 | $0.000179 / $0.001374 | 99.9% |
| [Gemma 3 12B IT](https://uberllm.dev/models/google/gemma-3-12b-it) | 128K | $0.05 / $0.15 | $0.000494 / $0.001481 | 99% |
| [Ministral 3B](https://uberllm.dev/models/mistralai/ministral-3-3b-instruct) | 128K | $0.10 / $0.10 | $0.000997 / $0.000997 | 99% |
| [GLM 4.7 Flash](https://uberllm.dev/models/z-ai/glm-4.7-flash) | 198K | $0.0605 / $0.40 | $0.000312 / $0.002065 | 99.5% |
| [Gemma 4 31B IT](https://uberllm.dev/models/google/gemma-4-31b-it) | 262K | $0.12 / $0.36 | $0.0006 / $0.0018 | 99.5% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | 128K | $0.075 / $0.30 | $0.000525 / $0.0021 | 99.3% |
| [Qwen 3.8 27B](https://uberllm.dev/models/qwen/qwen-3-8-27b) | 262K | $0.15 / $1.88 | $0.000195 / $0.002438 | 99.9% |
| [Gemma 3 27B](https://uberllm.dev/models/google/gemma-3-27b-it) | 40K | $0.08 / $0.20 | $0.000792 / $0.00198 | 99% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | 1000K | $1.32 / $3.96 | $0.000955 / $0.001911 | 99.9–100% |

### Major model makers

<details><summary>OpenAI, Anthropic, Google, DeepSeek, xAI, Qwen, Moonshot, Z.ai, Mistral, Meta (161 models)</summary>

| Model | Maker | Context | Official price | UberLLM price | Below list |
|---|---|---|---|---|---|
| [GPT-5.4 Pro](https://uberllm.dev/models/openai/gpt-5.4-pro) | openai | 1000K | $30.00 / $180.00 | $4.79 / $28.76 | 84% |
| [GPT-5.5 Pro](https://uberllm.dev/models/openai/gpt-5.5-pro) | openai | 1000K | $30.00 / $180.00 | $7.28 / $43.70 | 75.7% |
| [GPT-6 Astra](https://uberllm.dev/models/openai/gpt-6-astra) | openai | 1050K | $10.00 / $50.00 | $0.10 / $0.50 | 99% |
| [GPT-5.5](https://uberllm.dev/models/openai/gpt-5.5) | openai | 1000K | $5.00 / $30.00 | $0.2445 / $1.47 | 95.1% |
| [GPT-5.6 Sol](https://uberllm.dev/models/openai/gpt-5.6-sol) | openai | 1050K | $4.00 / $20.00 | $0.0804 / $0.402 | 98% |
| [GPT-5.6 Sol Pro](https://uberllm.dev/models/openai/gpt-5.6-sol-pro) | openai | 1050K | $4.00 / $20.00 | $1.56 / $7.80 | 61% |
| [GPT-5.4](https://uberllm.dev/models/openai/gpt-5.4) | openai | 1000K | $2.50 / $15.00 | $0.4753 / $2.85 | 81% |
| [GPT-5.2](https://uberllm.dev/models/openai/gpt-5.2) | openai | 256K | $1.75 / $14.00 | $0.2151 / $1.72 | 87.7% |
| [GPT-5.2 Codex](https://uberllm.dev/models/openai/gpt-5.2-codex) | openai | 256K | $1.75 / $14.00 | $0.4375 / $3.50 | 75% |
| [GPT-5.3 Codex](https://uberllm.dev/models/openai/gpt-5.3-codex) | openai | 400K | $1.75 / $14.00 | $0.1405 / $1.12 | 92% |
| [GPT-5.6 Terra](https://uberllm.dev/models/openai/gpt-5.6-terra) | openai | 1050K | $2.00 / $12.00 | $0.04127 / $0.2476 | 97.9% |
| [GPT-5.6 Terra Pro](https://uberllm.dev/models/openai/gpt-5.6-terra-pro) | openai | 1050K | $2.00 / $12.00 | $0.80 / $4.80 | 60% |
| [GPT-4o](https://uberllm.dev/models/openai/gpt-4o) | openai | 128K | $2.50 / $10.00 | $0.374 / $1.50 | 85% |
| [GPT-6 Sol](https://uberllm.dev/models/openai/gpt-6-sol) | openai | 1050K | $2.00 / $10.00 | $0.04 / $0.20 | 98% |
| [GPT-6 Sol Pro](https://uberllm.dev/models/openai/gpt-6-sol-pro) | openai | 1050K | $2.00 / $10.00 | $1.70 / $8.50 | 15% |
| [GPT-6.1 Sol](https://uberllm.dev/models/openai/gpt-6.1-sol) | openai | 1050K | $2.00 / $10.00 | $0.03998 / $0.1999 | 98% |
| [OpenAI: GPT-6.1 Sol Pro](https://uberllm.dev/models/openai/gpt-6.1-sol-pro) | openai | 1050K | $2.00 / $10.00 | $1.70 / $8.50 | 15% |
| [OpenAI: GPT-6.1 Terra](https://uberllm.dev/models/openai/gpt-6.1-terra) | openai | 1050K | $1.00 / $5.00 | $0.0191 / $0.0955 | 98.1% |
| [OpenAI: GPT-6.1 Terra Pro](https://uberllm.dev/models/openai/gpt-6.1-terra-pro) | openai | 1050K | $1.00 / $5.00 | $0.85 / $4.25 | 15% |
| [GPT-5.4 Mini](https://uberllm.dev/models/openai/gpt-5.4-mini) | openai | 400K | $0.75 / $4.50 | $0.07499 / $0.4499 | 90% |
| [GPT 5 Mini](https://uberllm.dev/models/openai/gpt-5-mini) | openai | 400K | $0.25 / $2.00 | $0.0612 / $0.4896 | 75.5% |
| [GPT 5.4 Nano](https://uberllm.dev/models/openai/gpt-5.4-nano) | openai | 400K | $0.20 / $1.25 | $0.03836 / $0.2398 | 80.8% |
| [GPT-5.6 Luna](https://uberllm.dev/models/openai/gpt-5.6-luna) | openai | 1050K | $0.20 / $1.20 | $0.004143 / $0.02486 | 97.9% |
| [GPT-5.6 Luna Pro](https://uberllm.dev/models/openai/gpt-5.6-luna-pro) | openai | 1050K | $0.20 / $1.20 | $0.08 / $0.48 | 60% |
| [GPT OSS 120B](https://uberllm.dev/models/openai/e2ee-gpt-oss-120b-p) | openai | 128K | $0.13 / $0.65 | $0.06494 / $0.3247 | 50–50.1% |
| [GPT-4o Mini](https://uberllm.dev/models/openai/gpt-4o-mini) | openai | 128K | $0.15 / $0.60 | $0.009 / $0.036 | 94% |
| [GPT OSS Safeguard 120B](https://uberllm.dev/models/openai/gpt-oss-safeguard-120b) | openai | 128K | $0.15 / $0.60 | $0.001497 / $0.005988 | 99% |
| [GPT-6 Luna](https://uberllm.dev/models/openai/gpt-6-luna) | openai | 1050K | $0.10 / $0.50 | $0.008695 / $0.04348 | 91.3% |
| [GPT-6 Luna Pro](https://uberllm.dev/models/openai/gpt-6-luna-pro) | openai | 1050K | $0.10 / $0.50 | $0.08499 / $0.4249 | 15% |
| [GPT 5 Nano](https://uberllm.dev/models/openai/gpt-5-nano) | openai | 400K | $0.05 / $0.40 | $0.007498 / $0.05998 | 85% |
| [GPT-OSS 120B](https://uberllm.dev/models/openai/gpt-oss-120b) | openai | 128K | $0.07 / $0.30 | $0.000069 / $0.000297 | 99.9% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | openai | 128K | $0.075 / $0.30 | $0.000525 / $0.0021 | 99.3% |
| [GPT-OSS 20B](https://uberllm.dev/models/openai/gpt-oss-20b) | openai | 128K | $0.03 / $0.13 | $0.000018 / $0.000089 | 99.9% |
| [Claude Fable 5](https://uberllm.dev/models/anthropic/claude-fable-5) | anthropic | 1000K | $10.00 / $50.00 | $0.7437 / $3.72 | 92.6% |
| [Claude Fable 5.1](https://uberllm.dev/models/anthropic/claude-fable-5.1) | anthropic | 1000K | $10.00 / $50.00 | $0.6122 / $3.06 | 93.9% |
| [Claude Opus 4.8 Fast](https://uberllm.dev/models/anthropic/claude-opus-4.8-fast) | anthropic | 1000K | $10.00 / $50.00 | $5.69 / $28.47 | 43.1% |
| [Claude Opus 5 (Fast)](https://uberllm.dev/models/anthropic/claude-opus-5-fast) | anthropic | 1000K | $10.00 / $50.00 | $4.00 / $20.00 | 60% |
| [Claude Fable 5.2](https://uberllm.dev/models/anthropic/claude-fable-5.2) | anthropic | 1000K | $8.00 / $40.00 | $2.71 / $13.55 | 66.1% |
| [Claude Opus 4.5](https://uberllm.dev/models/anthropic/claude-opus-4.5) | anthropic | 198K | $5.00 / $25.00 | $0.40 / $2.00 | 92% |
| [Claude Opus 4.6](https://uberllm.dev/models/anthropic/claude-opus-4.6) | anthropic | 1000K | $5.00 / $25.00 | $0.0845 / $0.4225 | 98.3% |
| [Claude Opus 4.7](https://uberllm.dev/models/anthropic/claude-opus-4.7) | anthropic | 1000K | $5.00 / $25.00 | $0.161 / $0.805 | 96.8% |
| [Claude Opus 4.8](https://uberllm.dev/models/anthropic/claude-opus-4.8) | anthropic | 1000K | $5.00 / $25.00 | $0.29 / $1.45 | 94.2% |
| [Claude Opus 5](https://uberllm.dev/models/anthropic/claude-opus-5) | anthropic | 1000K | $5.00 / $25.00 | $0.165 / $0.825 | 96.7% |
| [Claude Opus 5.5](https://uberllm.dev/models/anthropic/claude-opus-5.5) | anthropic | 1000K | $4.00 / $20.00 | $0.1517 / $0.7585 | 96.2% |
| [Claude Sonnet 4.5](https://uberllm.dev/models/anthropic/claude-sonnet-4.5) | anthropic | 198K | $3.00 / $15.00 | $0.5886 / $2.94 | 80.4% |
| [Claude Sonnet 4.6](https://uberllm.dev/models/anthropic/claude-sonnet-4.6) | anthropic | 1000K | $3.00 / $15.00 | $0.0534 / $0.267 | 98.2% |
| [Claude Sonnet 5](https://uberllm.dev/models/anthropic/claude-sonnet-5) | anthropic | 1000K | $2.00 / $10.00 | $0.0936 / $0.468 | 95.3% |
| [Claude Sonnet 5.5](https://uberllm.dev/models/anthropic/claude-sonnet-5.5) | anthropic | 1000K | $2.00 / $10.00 | $0.0995 / $0.4975 | 95% |
| [Claude Haiku 4.5](https://uberllm.dev/models/anthropic/claude-haiku-4.5) | anthropic | 200K | $1.00 / $5.00 | $0.0653 / $0.3265 | 93.5% |
| [Claude Haiku 5.5](https://uberllm.dev/models/anthropic/claude-haiku-5.5) | anthropic | 100K | $0.10 / $0.50 | $0.006889 / $0.03445 | 93.1% |
| [Gemini 3.1 Pro Preview](https://uberllm.dev/models/google/gemini-3.1-pro-preview) | google | 1000K | $2.00 / $12.00 | $0.1032 / $0.6192 | 94.8% |
| [Gemini 2.5 Pro](https://uberllm.dev/models/google/gemini-2.5-pro) | google | 1048K | $1.25 / $10.00 | $0.1576 / $1.26 | 87.4% |
| [Google: Gemini 4 Argon](https://uberllm.dev/models/google/gemini-4-argon) | google | 1048K | $2.00 / $10.00 | $0.0097 / $0.0485 | 99.5% |
| [Google: Gemini 4 Carbon](https://uberllm.dev/models/google/gemini-4-carbon) | google | 1048K | $2.00 / $10.00 | $1.00 / $5.00 | 50% |
| [Gemini 3.5 Flash](https://uberllm.dev/models/google/gemini-3.5-flash) | google | 1000K | $1.50 / $9.00 | $0.0075 / $0.045 | 99.5% |
| [Gemini 3.8 Flash](https://uberllm.dev/models/google/gemini-3.8-flash) | google | 1048K | $0.825 / $4.12 | $0.003992 / $0.01996 | 99.5% |
| [Gemini 3.6 Flash](https://uberllm.dev/models/google/gemini-3-6-flash) | google | 1000K | $0.75 / $3.75 | $0.2175 / $1.09 | 71% |
| [Gemini 3.7 Flash](https://uberllm.dev/models/google/gemini-3.7-flash) | google | 1048K | $0.75 / $3.75 | $0.004001 / $0.02001 | 99.5% |
| [Gemini 3 Flash Preview](https://uberllm.dev/models/google/gemini-3-flash-preview) | google | 256K | $0.50 / $3.00 | $0.002425 / $0.01455 | 99.5% |
| [Gemini 2.5 Flash](https://uberllm.dev/models/google/gemini-2.5-flash) | google | 1048K | $0.30 / $2.50 | $0.0015 / $0.0125 | 99.5% |
| [Gemini 3.5 Flash Lite](https://uberllm.dev/models/google/gemini-3-5-flash-lite) | google | 1000K | $0.30 / $2.50 | $0.1677 / $1.40 | 44.1% |
| [Gemini 3.1 Flash Lite](https://uberllm.dev/models/google/gemini-3.1-flash-lite) | google | 1048K | $0.25 / $1.50 | $0.001213 / $0.007275 | 99.5% |
| [Gemma 4 31B (E2EE)](https://uberllm.dev/models/google/e2ee-gemma-4-31b) | google | 262K | $0.12 / $0.36 | $0.10 / $0.30 | 16.7% |
| [Gemma 4 31B](https://uberllm.dev/models/google/gemma-4-31b) | google | 256K | $0.12 / $0.36 | $0.000912 / $0.002736 | 99.2% |
| [Gemma 4 31B IT](https://uberllm.dev/models/google/gemma-4-31b-it) | google | 262K | $0.12 / $0.36 | $0.0006 / $0.0018 | 99.5% |
| [Gemma 3 27B](https://uberllm.dev/models/google/gemma-3-27b-it) | google | 40K | $0.08 / $0.20 | $0.000792 / $0.00198 | 99% |
| [Gemma 3 12B IT](https://uberllm.dev/models/google/gemma-3-12b-it) | google | 128K | $0.05 / $0.15 | $0.000494 / $0.001481 | 99% |
| [Gemma 3 4B IT](https://uberllm.dev/models/google/gemma-3-4b-it) | google | 128K | $0.05 / $0.10 | $0.000346 / $0.000693 | 99.3% |
| [Gemma 4 E2B](https://uberllm.dev/models/google/gemma-4-e2b) | google | 128K | $0.04 / $0.08 | $0.000399 / $0.000798 | 99% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | deepseek | 1000K | $1.32 / $3.96 | $0.000955 / $0.001911 | 99.9–100% |
| [DeepSeek V4 Pro 0813](https://uberllm.dev/models/deepseek/deepseek-v4-pro-0813) | deepseek | 1048K | $1.32 / $3.96 | $0.002331 / $0.09324 | 97.6–99.8% |
| [DeepSeek: DeepSeek V4 Flash Vision Exp](https://uberllm.dev/models/deepseek/deepseek-v4-flash-vision-exp) | deepseek | 1048K | $0.44 / $1.32 | $0.3784 / $1.14 | 14% |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | deepseek | 1048K | $0.30 / $1.20 | $0.000179 / $0.001374 | 99.9% |
| [DeepSeek V4.1 Flash 1017](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash-1017) | deepseek | 1048K | $0.30 / $1.20 | $0.000287 / $0.02392 | 98–99.9% |
| [DeepSeek V3.1](https://uberllm.dev/models/deepseek/deepseek-v3.1) | deepseek | 128K | $0.25 / $0.95 | $0.002469 / $0.009381 | 99% |
| [DeepSeek V4 Flash 0731 Fast](https://uberllm.dev/models/deepseek/deepseek-v4-flash-0731-fast) | deepseek | 1000K | $0.35 / $0.70 | $0.2065 / $0.413 | 41% |
| [DeepSeek V3.2](https://uberllm.dev/models/deepseek/deepseek-v3.2) | deepseek | 160K | $0.26 / $0.38 | $0.0026 / $0.0038 | 99% |
| [DeepSeek V4 Flash E2EE](https://uberllm.dev/models/deepseek/e2ee-deepseek-v4-flash) | deepseek | 1000K | $0.182 / $0.373 | $0.1092 / $0.2238 | 40% |
| [DeepSeek V4 Flash](https://uberllm.dev/models/deepseek/deepseek-v4-flash) | deepseek | 1000K | $0.091 / $0.182 | $0.001044 / $0.002088 | 98.9% |
| [Grok 4.5](https://uberllm.dev/models/x-ai/grok-4.5) | x-ai | 500K | $2.00 / $6.00 | $0.01557 / $0.04671 | 99.2% |
| [Grok 4.6](https://uberllm.dev/models/x-ai/grok-4.6) | x-ai | 500K | $2.00 / $6.00 | $0.1217 / $0.3652 | 93.9% |
| [Grok 4.7](https://uberllm.dev/models/x-ai/grok-4.7) | x-ai | 500K | $2.00 / $6.00 | $0.01442 / $0.04326 | 99.3% |
| [Grok 4.20 Beta](https://uberllm.dev/models/x-ai/grok-4.20-beta) | x-ai | 2000K | $1.25 / $2.50 | $0.175 / $0.35 | 86% |
| [Grok 4.20 Multi-Agent Beta](https://uberllm.dev/models/x-ai/grok-4.20-multi-agent-beta) | x-ai | 2000K | $1.25 / $2.50 | $0.175 / $0.35 | 86% |
| [Grok 4.3](https://uberllm.dev/models/x-ai/grok-4.3) | x-ai | 1000K | $1.25 / $2.50 | $0.01238 / $0.02475 | 99% |
| [Grok Build 0.1](https://uberllm.dev/models/x-ai/grok-build-0.1) | x-ai | 256K | $1.00 / $2.00 | $0.60 / $1.20 | 40% |
| [Qwen: Qwen3.8 Max Prime](https://uberllm.dev/models/qwen/qwen3.8-max-prime) | qwen | 1000K | $4.00 / $12.00 | $3.44 / $10.32 | 14% |
| [Qwen3.7 Max](https://uberllm.dev/models/qwen/qwen3.7-max) | qwen | 256K | $2.70 / $8.05 | $1.00 / $3.00 | 62.7–63% |
| [Qwen 3.8 Max](https://uberllm.dev/models/qwen/qwen-3-8-max) | qwen | 1000K | $2.50 / $7.50 | $0.114 / $0.342 | 95.4% |
| [Qwen3.8 2.4T A95B](https://uberllm.dev/models/qwen/qwen3.8-2.4t-a95b) | qwen | 1000K | $2.00 / $6.00 | $0.01394 / $0.04182 | 99.3% |
| [Qwen: Qwen3.8 Max (0902)](https://uberllm.dev/models/qwen/qwen3.8-max-0902) | qwen | 1000K | $2.00 / $6.00 | $0.0021 / $0.0063 | 99.9% |
| [Qwen 3.5 397B](https://uberllm.dev/models/qwen/qwen3.5-397b-a17b) | qwen | 128K | $0.60 / $3.60 | $0.01675 / $0.1005 | 97.2% |
| [Qwen 3 235B A22B Thinking 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-thinking-2507) | qwen | 128K | $0.45 / $3.50 | $0.05 / $0.05 | 88.9–98.6% |
| [Qwen 3.6 27B](https://uberllm.dev/models/qwen/qwen3.6-27b) | qwen | 256K | $0.32 / $3.20 | $0.01438 / $0.1438 | 95.5% |
| [Qwen 3.7 Plus](https://uberllm.dev/models/qwen/qwen3.7-plus) | qwen | 256K | $0.50 / $2.00 | $0.2497 / $0.999 | 50% |
| [Qwen3 VL 235B A22B](https://uberllm.dev/models/qwen/qwen3-vl-235b-a22b-instruct) | qwen | 256K | $0.21 / $1.90 | $0.002074 / $0.01876 | 99% |
| [Qwen3 VL 235B](https://uberllm.dev/models/qwen/qwen3-vl-235b-a22b-thinking) | qwen | 256K | $0.21 / $1.90 | $0.1049 / $0.949 | 50% |
| [Qwen 3.8 27B](https://uberllm.dev/models/qwen/qwen-3-8-27b) | qwen | 262K | $0.15 / $1.88 | $0.000195 / $0.002438 | 99.9% |
| [Qwen 3 Coder 480B Turbo](https://uberllm.dev/models/qwen/qwen3-coder-turbo) | qwen | 256K | $0.35 / $1.50 | $0.1153 / $0.4943 | 67% |
| [Qwen 3.6 35B A3B (E2EE)](https://uberllm.dev/models/qwen/e2ee-qwen3-6-35b-a3b) | qwen | 128K | $0.182 / $1.18 | $0.091 / $0.59 | 50% |
| [Qwen3 Next 80B A3B](https://uberllm.dev/models/qwen/qwen3-next-80b-a3b-instruct) | qwen | 256K | $0.09 / $1.10 | $0.00078 / $0.009533 | 99.1% |
| [Qwen 3.6 35B A3B](https://uberllm.dev/models/qwen/qwen3-6-35b-a3b) | qwen | 262K | $0.10 / $1.00 | $0.004235 / $0.04235 | 95.8% |
| [Qwen 3 Coder 480b](https://uberllm.dev/models/qwen/qwen3-coder) | qwen | 256K | $0.30 / $1.00 | $0.002964 / $0.00988 | 99% |
| [Qwen 3.5 35B A3B](https://uberllm.dev/models/qwen/qwen3.5-35b-a3b) | qwen | 256K | $0.15 / $1.00 | $0.08991 / $0.5994 | 40.1% |
| [Qwen3 VL 30B A3B](https://uberllm.dev/models/qwen/qwen3-vl-30b-a3b-thinking) | qwen | 128K | $0.25 / $0.90 | $0.10 / $0.45 | 50–60% |
| [Qwen3 Coder Next](https://uberllm.dev/models/qwen/qwen3-coder-next) | qwen | 256K | $0.12 / $0.80 | $0.001185 / $0.0079 | 99% |
| [Qwen 3 235B A22B Instruct 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-2507) | qwen | 128K | $0.14 / $0.75 | $0.000633 / $0.003389 | 99.5% |
| [Qwen3 Coder 30B A3B Instruct](https://uberllm.dev/models/qwen/qwen3-coder-30b-a3b-instruct) | qwen | 256K | $0.15 / $0.60 | $0.000691 / $0.002765 | 99.5% |
| [Qwen3 30B A3B](https://uberllm.dev/models/qwen/qwen3-30b-a3b) | qwen | 256K | $0.12 / $0.50 | $0.084 / $0.35 | 30% |
| [Qwen3.8 Flash](https://uberllm.dev/models/qwen/qwen3.8-flash) | qwen | 1000K | $0.15 / $0.47 | $0.00147 / $0.004606 | 99% |
| [Qwen: Qwen3.8 Omni Flash](https://uberllm.dev/models/qwen/qwen3.8-omni-flash) | qwen | 1000K | $0.15 / $0.47 | $0.000146 / $0.000456 | 99.9% |
| [Qwen3 32B](https://uberllm.dev/models/qwen/qwen3-32b) | qwen | 32K | $0.08 / $0.28 | $0.00079 / $0.002765 | 99% |
| [Qwen 3.5 9B](https://uberllm.dev/models/qwen/qwen3.5-9b) | qwen | 256K | $0.17 / $0.25 | $0.025 / $0.075 | 70–85.3% |
| [Qwen 2.5 7B](https://uberllm.dev/models/qwen/e2ee-qwen-2-5-7b-p) | qwen | 32K | $0.05 / $0.13 | $0.02248 / $0.05844 | 55% |
| [Qwen: Qwen3.7 Flash](https://uberllm.dev/models/qwen/qwen3.7-flash) | qwen | 1000K | $0.03 / $0.13 | $0.001216 / $0.005268 | 95.9% |
| [Kimi K3 Fast](https://uberllm.dev/models/moonshotai/kimi-k3-fast-api) | moonshotai | 1000K | $4.50 / $22.50 | $2.70 / $13.50 | 40% |
| [Kimi K3](https://uberllm.dev/models/moonshotai/kimi-k3) | moonshotai | 1000K | $3.00 / $15.00 | $0.001727 / $0.07805 | 99.5–99.9% |
| [MoonshotAI: Kimi K3.1 Pro](https://uberllm.dev/models/moonshotai/kimi-k3.1-pro) | moonshotai | 1048K | $2.00 / $10.00 | $0.10 / $0.50 | 95% |
| [Kimi K2.7 Code](https://uberllm.dev/models/moonshotai/kimi-k2.7-code) | moonshotai | 262K | $0.60 / $3.50 | $0.009788 / $0.0571 | 98.4% |
| [Kimi K2.6](https://uberllm.dev/models/moonshotai/kimi-k2.6) | moonshotai | 256K | $0.65 / $3.41 | $0.01977 / $0.1037 | 97% |
| [Kimi K2.5](https://uberllm.dev/models/moonshotai/kimi-k2.5) | moonshotai | 256K | $0.532 / $3.33 | $0.003192 / $0.01995 | 99.4% |
| [Kimi K2 Thinking](https://uberllm.dev/models/moonshotai/kimi-k2-thinking) | moonshotai | 256K | $0.60 / $2.50 | $0.005925 / $0.02469 | 99% |
| [Kimi K2](https://uberllm.dev/models/moonshotai/kimi-k2) | moonshotai | 256K | $0.57 / $2.30 | $0.399 / $1.61 | 30% |
| [Z.ai: GLM 5.3 Prime](https://uberllm.dev/models/z-ai/glm-5.3-prime) | z-ai | 1000K | $2.80 / $8.80 | $0.02526 / $0.07938 | 99.1% |
| [GLM 5.2 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5-2-p) | z-ai | 524K | $1.75 / $5.75 | $0.8741 / $2.87 | 50% |
| [GLM 5.1 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5.1) | z-ai | 200K | $1.40 / $4.40 | $0.44 / $1.66 | 62.3–68.6% |
| [GLM 5.1](https://uberllm.dev/models/z-ai/glm-5.1) | z-ai | 200K | $1.40 / $4.40 | $0.01123 / $0.03529 | 99.2% |
| [GLM-5.2](https://uberllm.dev/models/z-ai/glm-5.2) | z-ai | 1048K | $1.40 / $4.40 | $0.00052 / $0.00352 | 99.9–100% |
| [GLM 5.3](https://uberllm.dev/models/z-ai/glm-5.3) | z-ai | 1000K | $1.40 / $4.40 | $0.000647 / $0.01295 | 99.7–100% |
| [GLM-5 Turbo](https://uberllm.dev/models/z-ai/glm-5-turbo) | z-ai | 200K | $1.20 / $4.00 | $0.06 / $0.20 | 95% |
| [GLM 5V Turbo](https://uberllm.dev/models/z-ai/glm-5v-turbo) | z-ai | 200K | $1.20 / $4.00 | $0.7193 / $2.40 | 40.1% |
| [GLM-5](https://uberllm.dev/models/z-ai/glm-5) | z-ai | 198K | $1.00 / $3.20 | $0.00393 / $0.01258 | 99.6% |
| [GLM 4.5](https://uberllm.dev/models/z-ai/glm-4.5) | z-ai | 128K | $0.60 / $2.20 | $0.00588 / $0.02156 | 99% |
| [GLM-4.7](https://uberllm.dev/models/z-ai/glm-4.7) | z-ai | 128K | $0.55 / $2.20 | $0.00154 / $0.00616 | 99.7% |
| [GLM 4.7 Thinking](https://uberllm.dev/models/z-ai/glm-4.7-thinking) | z-ai | 128K | $0.45 / $2.00 | $0.45 / $2.00 | 0% |
| [GLM-4.6](https://uberllm.dev/models/z-ai/glm-4.6) | z-ai | 198K | $0.43 / $1.75 | $0.004162 / $0.01694 | 99% |
| [Z.ai: GLM 5.3 FlashX](https://uberllm.dev/models/z-ai/glm-5.3-flashx) | z-ai | 1048K | $0.37 / $1.25 | $0.1036 / $0.35 | 72% |
| [Z.ai: GLM 5.3 FlashX Legal](https://uberllm.dev/models/z-ai/glm-5.3-flashx-legal) | z-ai | 1048K | $0.37 / $1.25 | $0.259 / $0.875 | 30% |
| [GLM 4.5 Air](https://uberllm.dev/models/z-ai/glm-4.5-air) | z-ai | 128K | $0.20 / $1.10 | $0.000129 / $0.000842 | 99.9% |
| [GLM 4.7 Flash](https://uberllm.dev/models/z-ai/glm-4.7-flash) | z-ai | 198K | $0.0605 / $0.40 | $0.000312 / $0.002065 | 99.5% |
| [GLM 5.3 Flash](https://uberllm.dev/models/z-ai/glm-5.3-flash) | z-ai | 1048K | $0.0399 / $0.0784 | $0.001525 / $0.002996 | 96.2% |
| [Mistral Large](https://uberllm.dev/models/mistralai/mistral-large) | mistralai | 128K | $2.00 / $6.00 | $0.0928 / $0.2784 | 95.4% |
| [Mistral: Mistral Large 4](https://uberllm.dev/models/mistralai/mistral-large-4-0) | mistralai | 524K | $0.70 / $2.10 | $0.063 / $0.189 | 91% |
| [Devstral 2 123B](https://uberllm.dev/models/mistralai/devstral-2-123b) | mistralai | 256K | $0.40 / $2.00 | $0.003985 / $0.01992 | 99% |
| [Magistral Small 2509](https://uberllm.dev/models/mistralai/magistral-small-2509) | mistralai | 128K | $0.50 / $1.50 | $0.00499 / $0.01497 | 99% |
| [Mistral Large 3](https://uberllm.dev/models/mistralai/mistral-large-3) | mistralai | 256K | $0.50 / $1.50 | $0.005 / $0.015 | 99% |
| [Mistral Small 4](https://uberllm.dev/models/mistralai/mistral-small-4) | mistralai | 256K | $0.15 / $0.60 | $0.04688 / $0.1875 | 68.8% |
| [Mistral Small 3.2 24B Instruct](https://uberllm.dev/models/mistralai/mistral-small-3.2-24b-instruct) | mistralai | 256K | $0.0938 / $0.25 | $0.0135 / $0.036 | 85.6% |
| [Ministral 14B 3.0](https://uberllm.dev/models/mistralai/ministral-3-14b-instruct) | mistralai | 128K | $0.20 / $0.20 | $0.001996 / $0.001996 | 99% |
| [Ministral 3 8B](https://uberllm.dev/models/mistralai/ministral-3-8b-instruct) | mistralai | 128K | $0.15 / $0.15 | $0.001496 / $0.001496 | 99% |
| [Ministral 3B](https://uberllm.dev/models/mistralai/ministral-3-3b-instruct) | mistralai | 128K | $0.10 / $0.10 | $0.000997 / $0.000997 | 99% |
| [Meta: Muse Wonder](https://uberllm.dev/models/meta-llama/muse-wonder) | meta-llama | 1048K | $4.00 / $20.00 | $0.40 / $2.00 | 90% |
| [Meta: Muse Spark 1.1](https://uberllm.dev/models/meta-llama/muse-spark-1.1) | meta-llama | 1048K | $1.25 / $4.25 | $0.375 / $1.27 | 70% |
| [Meta: Muse Spark 1.2](https://uberllm.dev/models/meta-llama/muse-spark-1.2) | meta-llama | 1048K | $1.25 / $4.25 | $0.375 / $1.27 | 70% |
| [Meta: Muse Spark 1.3](https://uberllm.dev/models/meta-llama/muse-spark-1.3) | meta-llama | 1048K | $1.25 / $4.25 | $0.125 / $0.425 | 90% |
| [Meta: Muse Spark Open](https://uberllm.dev/models/meta-llama/muse-spark-open) | meta-llama | 1048K | $1.25 / $4.25 | $0.6162 / $2.10 | 50.7% |
| [Meta: Muse Glimmer 30B](https://uberllm.dev/models/meta-llama/muse-glimmer-30b) | meta-llama | 131K | $0.30 / $1.20 | $0.258 / $1.03 | 14% |
| [Meta: Muse Ember](https://uberllm.dev/models/meta-llama/muse-ember) | meta-llama | 1048K | $0.10 / $0.50 | $0.07 / $0.35 | 30% |
| [Llama 3.2 3B](https://uberllm.dev/models/meta-llama/llama-3.2-3b-instruct) | meta-llama | 128K | $0.05 / $0.33 | $0.025 / $0.165 | 50% |
| [Meta: Muse Spark 1.2 Contributor](https://uberllm.dev/models/meta-llama/muse-spark-1.2-contributor) | meta-llama | 1048K | $0.10 / $0.20 | $0.03 / $0.06 | 70% |
| [Meta: Muse Spark 1.3 Contributor](https://uberllm.dev/models/meta-llama/muse-spark-1.3-contributor) | meta-llama | 1048K | $0.10 / $0.20 | $0.02 / $0.04 | 80% |

</details>

### Image models (per image)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Z-Image Turbo (Venice)](https://uberllm.dev/models/venice/z-image-turbo) | $0.01 / image | $0.004 / image | 60% |
| [Chroma (Venice)](https://uberllm.dev/models/venice/chroma) | $0.01 / image | $0.006 / image | 40% |
| [Flux 2 Pro (Venice)](https://uberllm.dev/models/venice/flux-2-pro) | $0.03 / image | $0.0075 / image | 75% |
| [Flux 3 Klein](https://uberllm.dev/models/black-forest-labs/flux-3-klein) | $0.009 / image | $0.008 / image | 11.1% |
| [Flux 1.1 (Venice, legacy)](https://uberllm.dev/models/venice/flux-1.1) | $0.01 / image | $0.008 / image | 20% |
| [Venice SD35](https://uberllm.dev/models/venice/sd35) | $0.01 / image | $0.008 / image | 20% |
| [Stable Diffusion XL (Venice, legacy)](https://uberllm.dev/models/venice/sdxl) | $0.01 / image | $0.008 / image | 20% |
| [Grok Imagine — Edit (Venice)](https://uberllm.dev/models/venice/grok-imagine-edit) | $0.03 / image | $0.01228 / image | 59.1% |
| [Grok Imagine High Quality (Venice)](https://uberllm.dev/models/venice/grok-imagine-quality) | $0.06 / image | $0.015 / image | 75% |
| [Seedream 5.0 Flash](https://uberllm.dev/models/bytedance/seedream-5-0-flash) | $0.018 / image | $0.0162 / image | 10% |

### Image models (per megapixel)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [FLUX.2 Klein 4B](https://uberllm.dev/models/black-forest-labs/flux.2-klein-4b) | $0.015 / megapixel | $0.00375 / megapixel | 75% |
| [FLUX.2 Flex](https://uberllm.dev/models/black-forest-labs/flux.2-flex) | $0.06 / megapixel | $0.015 / megapixel | 75% |

### Video models (per second)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Grok Imagine Video 1.5](https://uberllm.dev/models/x-ai/grok-imagine-1-5-image-to-video) | $0.08 / sec | $0.012 / sec | 85% |
| [Grok Imagine](https://uberllm.dev/models/x-ai/grok-imagine-image-to-video) | $0.05 / sec | $0.012 / sec | 76% |
| [Grok Imagine Text-to-Video](https://uberllm.dev/models/x-ai/grok-imagine-text-to-video) | $0.0885 / sec | $0.012 / sec | 86.4% |
| [Seedance 1.0 Pro](https://uberllm.dev/models/bytedance/seedance-1-0-pro) | – | $0.014 / sec | – |
| [Longcat Distilled (image-to-video)](https://uberllm.dev/models/meituan/longcat-distilled-image-to-video) | $0.018 / sec | $0.0144 / sec | 20% |
| [Hailuo 02 Standard Image to Video](https://uberllm.dev/models/fal-ai/minimax/hailuo-02/standard/image-to-video) | $0.017 / sec | $0.01445 / sec | 15% |
| [LongCat Distilled Text-to-Video](https://uberllm.dev/models/meituan/longcat-distilled-text-to-video) | $0.018 / sec | $0.01782 / sec | 1% |
| [Seedance 1.0 Pro Fast](https://uberllm.dev/models/bytedance/seedance-1-0-pro-fast-image-to-video) | – | $0.018 / sec | – |
| [Seedance 2.0 Mini (image-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-mini-image-to-video) | $0.044 / sec | $0.019 / sec | 56.8% |
| [PixVerse V6](https://uberllm.dev/models/pixverse/pixverse-v6) | $0.02222 / sec | $0.02 / sec | 10% |

### Video models (per video)

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Topaz Video Upscale](https://uberllm.dev/models/topaz-labs/topaz-video-upscale) | $0.15 / video | $0.0855 / video | 43% |
| [Wan 2.2 A14B Text-to-Video](https://uberllm.dev/models/wan/wan-2-2-a14b-text-to-video) | $0.20 / video | $0.17 / video | 15% |
| [Runway Gen-4 Aleph](https://uberllm.dev/models/runway/runway-gen4-aleph) | $0.50 / video | $0.425 / video | 15% |
| [Cosmos Predict (image-to-video)](https://uberllm.dev/models/nvidia/cosmos-predict-image-to-video) | $0.801 / video | $0.5607 / video | 30% |

### Music models

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Sonilo V1.1 Sound Effects](https://uberllm.dev/models/sonilo/sonilo-sound-effects-v1-0) | – | $0.00207 / track | – |
| [Seed Audio 1.0](https://uberllm.dev/models/byteplus/seed-audio-1-0) | – | $0.002875 / track | – |
| [Sonilo V1.1 Music](https://uberllm.dev/models/sonilo/sonilo-music-v1-1) | – | $0.002875 / track | – |
| [MMAudio V2 Text-to-Audio (Venice)](https://uberllm.dev/models/venice/mmaudio-v2-text-to-audio) | – | $0.008 / track | – |
| [ElevenLabs Sound Effects v2 (Venice)](https://uberllm.dev/models/venice/elevenlabs-sound-effects-v2) | $0.02 / track | $0.016 / track | 20% |
| [Venice Music Gen (legacy alias)](https://uberllm.dev/models/venice/music-gen) | – | $0.03 / track | – |
| [MiniMax Music 2.0 (Venice)](https://uberllm.dev/models/venice/minimax-music-v2) | $0.04 / track | $0.032 / track | 20% |
| [ElevenLabs TTS v4 Turbo](https://uberllm.dev/models/elevenlabs/elevenlabs-tts-v4-turbo) | – | $0.046 / track | – |
| [ElevenLabs TTS v4](https://uberllm.dev/models/elevenlabs/elevenlabs-tts-v4) | – | $0.092 / track | – |
| [ElevenLabs TTS Multilingual v2 (Venice audio)](https://uberllm.dev/models/venice/elevenlabs-tts-multilingual-v2) | $0.12 / track | $0.096 / track | 20% |

### Speech models

| Model | Official price | UberLLM price | Below list |
|---|---|---|---|
| [Kokoro Text to Speech (Venice)](https://uberllm.dev/models/venice/kokoro-tts) | $0.0035 / 1K chars | $0.00175 / 1K chars | 50% |
| [Venice TTS 1 (legacy alias)](https://uberllm.dev/models/venice/tts-1) | – | $0.0028 / 1K chars | – |
| [Inworld 1.5 Max TTS](https://uberllm.dev/models/inworld/tts-inworld-1-5-max) | $0.0125 / 1K chars | $0.01 / 1K chars | 20% |
| [xAI v1 TTS](https://uberllm.dev/models/x-ai/tts-xai-v1) | $0.01875 / 1K chars | $0.01406 / 1K chars | 25% |
| [Chatterbox HD TTS](https://uberllm.dev/models/resemble-ai/tts-chatterbox-hd) | $0.05 / 1K chars | $0.04 / 1K chars | 20% |
| [Orpheus TTS](https://uberllm.dev/models/canopy-labs/tts-orpheus) | $0.0625 / 1K chars | $0.05 / 1K chars | 20% |
| [ElevenLabs Turbo v2.5 TTS (Venice)](https://uberllm.dev/models/venice/elevenlabs-tts-turbo-v2-5) | $0.0625 / 1K chars | $0.05 / 1K chars | 20% |
| [Qwen3 0.6B TTS](https://uberllm.dev/models/qwen/tts-qwen3-0-6b) | $0.0875 / 1K chars | $0.07 / 1K chars | 20% |
| [Qwen3 1.7B TTS](https://uberllm.dev/models/qwen/tts-qwen3-1-7b) | $0.1125 / 1K chars | $0.09 / 1K chars | 20% |
| [MiniMax Speech 02 HD TTS](https://uberllm.dev/models/minimax/tts-minimax-speech-02-hd) | $0.125 / 1K chars | $0.10 / 1K chars | 20% |

## Prices under review

The catalog's official price for these 5 models failed a sanity check (see `list_price_review_reason`), so it is left out, with no % below list, until it is checked against the maker's own page. The UberLLM price is still listed.

| Model | Category | Why |
|---|---|---|
| [DeepSeek V4 Flash 0731](https://uberllm.dev/models/deepseek/deepseek-v4-flash-0731) | text | input list price more than 3x off other listings of the same model |
| [Gemma 4 26B A4B IT](https://uberllm.dev/models/google/gemma-4-26b-a4b-it) | text | output:input ratio 1.2 vs 5.0 for the maker's other models |
| [Llama 3.3 70B Instruct](https://uberllm.dev/models/meta-llama/llama-3.3-70b-instruct) | text | output:input ratio 1.0 vs 3.4 for the maker's other models |
| [MMAudio V2 Text-to-Audio (Venice)](https://uberllm.dev/models/venice/mmaudio-v2-text-to-audio) | music | more than 10x off the median music price per job |
| [Venice TTS 1 (legacy alias)](https://uberllm.dev/models/venice/tts-1) | speech | more than 10x off the median speech price per 1K characters |

## Biggest drops this week (2026-11-04 to 2026-11-11)

From UberLLM's daily catalog snapshots (`GET /api/v1/public/price-changes`). Text: $ per 1M input / output tokens, sorted by the larger of the two moves.

### Official list price cuts

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [NVIDIA Nemotron 3 Super 120B](https://uberllm.dev/models/nvidia/nemotron-3-super-120b) | text | $0.30 / $2.40 | $0.075 / $0.40 | in −75% / out −83% |
| [MiniMax M3.1 Flash](https://uberllm.dev/models/minimax/minimax-m3-1-flash) | text | $0.15 / $0.60 | $0.075 / $0.30 | −50% |
| [inclusionAI: Ling 3.1 Flash](https://uberllm.dev/models/inclusionai/ling-3.1-flash) | text | $0.075 / $0.225 | $0.045 / $0.135 | −40% |
| [Tencent HY3](https://uberllm.dev/models/tencent/hy3) | text | $0.132 / $0.528 | $0.0825 / $0.33 | −38% |
| [MiniMax M2.7](https://uberllm.dev/models/minimax/minimax-m2.7) | text | $0.30 / $1.20 | $0.21 / $0.84 | −30% |
| [Qwen3 Next 80B A3B](https://uberllm.dev/models/qwen/qwen3-next-80b-a3b-instruct) | text | $0.10 / $1.10 | $0.09 / $1.10 | in −10% / out 0% |
| [NVIDIA: Nemotron 3.5 Super VL](https://uberllm.dev/models/nvidia/nemotron-3.5-super-vl) | text | $0.15 / $0.50 | $0.15 / $0.47 | in 0% / out −6% |
| [Llama 3.2 3B](https://uberllm.dev/models/meta-llama/llama-3.2-3b-instruct) | text | $0.0509 / $0.335 | $0.05 / $0.33 | in −2% / out −1% |

### UberLLM price drops

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [Gemini 3.5 Flash](https://uberllm.dev/models/google/gemini-3.5-flash) | text | $0.405 / $2.43 | $0.015 / $0.09 | −96% |
| [Nano Banana (Gemini 2.5 Flash Image)](https://uberllm.dev/models/google/gemini-2.5-flash-image) | image | $0.075 / $0.625 | $0.003 / $0.025 | −96% |
| [Gemini 3.7 Flash](https://uberllm.dev/models/google/gemini-3.7-flash) | text | $0.3375 / $1.69 | $0.015 / $0.075 | −96% |
| [Gemini 2.5 Flash](https://uberllm.dev/models/google/gemini-2.5-flash) | text | $0.057 / $0.475 | $0.003 / $0.025 | −95% |
| [Gemini 3.1 Flash Lite](https://uberllm.dev/models/google/gemini-3.1-flash-lite) | text | $0.0725 / $0.435 | $0.0075 / $0.045 | −90% |
| [MiniMax M2.7 Highspeed](https://uberllm.dev/models/minimax/minimax-m2.7-highspeed) | text | $0.54 / $2.16 | $0.09 / $0.36 | −83% |
| [Gemini 3.8 Flash](https://uberllm.dev/models/google/gemini-3.8-flash) | text | $0.2475 / $1.24 | $0.05775 / $0.2888 | −77% |
| [Google: Gemini 4 Argon](https://uberllm.dev/models/google/gemini-4-argon) | text | $1.00 / $5.00 | $0.24 / $1.20 | −76% |
| [Kimi K2.6](https://uberllm.dev/models/moonshotai/kimi-k2.6) | text | $0.1885 / $0.9889 | $0.052 / $0.2728 | −72% |
| [Qwen3.5 Flash](https://uberllm.dev/models/qwen/qwen3.5-flash) | text | $0.09 / $0.36 | $0.025 / $0.10 | −72% |

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

- `list_price_source` starting "UberLLM catalog list price": the direct (list) price the catalog carries for the model, meant to be the maker's own API price for first-party models (OpenAI, Anthropic, Google, ...) and the host's list price for open-weight models. The public catalog does not record which vendor page that number was read from, so `list_price_source_url` is empty and the source says so. `vendor_pricing_page` is the maker's pricing page to check it against (it is not where the number was read); for open-weight models, `list_price_hosts` has the named hosts' own prices.
- Any other `list_price_source` (for example `OpenRouter`, `Z.ai`, `Fal`, `Kling (Kuaishou)`, `Stability AI`): the catalog had no list of its own, so the price was read from that public page (`list_price_source_url`) on `list_price_checked`.
- `list_price_status`: `ok` = the official price passed the sanity check; `unverified` = it failed it (input under 1/40 of output, an output:input ratio more than 3x off the maker's other models, an input more than 3x off other listings of the same model, or a media price more than 10x off its category median), so the official price and every % below list are left empty until it is checked; `none` = no official price.
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
