# Changelog

Price changes between daily snapshots of [`prices.json`](prices.json), newest first.
"Official list price" = the model maker's price as carried in the catalog (see [SOURCES](README.md#sources)).
"UberLLM price" = the best live offer on the UberLLM market at snapshot time; it moves during the day.
Text prices are $ per 1M input / output tokens. Every day's full table is in [`history/`](history/).

## 2026-11-03 to 2026-11-10 (UberLLM daily catalog snapshots, before this repo started)

From `GET https://api.uberllm.dev/api/v1/public/price-changes`. Text prices are $ per 1M input / output tokens.

**Official list price changes (18)**

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [NVIDIA Nemotron 3 Super 120B](https://uberllm.dev/models/nvidia/nemotron-3-super-120b) | text | $0.30 / $2.40 | $0.075 / $0.40 | in −75% / out −83% |
| [inclusionAI: Ling 3.1 Flash](https://uberllm.dev/models/inclusionai/ling-3.1-flash) | text | $0.075 / $0.225 | $0.045 / $0.135 | −40% |
| [MiniMax M2.7](https://uberllm.dev/models/minimax/minimax-m2.7) | text | $0.30 / $1.20 | $0.21 / $0.84 | −30% |
| [Qwen3 Next 80B A3B](https://uberllm.dev/models/qwen/qwen3-next-80b-a3b-instruct) | text | $0.10 / $1.10 | $0.09 / $1.10 | in −10% / out 0% |
| [NVIDIA: Nemotron 3.5 Super VL](https://uberllm.dev/models/nvidia/nemotron-3.5-super-vl) | text | $0.15 / $0.50 | $0.15 / $0.47 | in 0% / out −6% |
| [Llama 3.2 3B](https://uberllm.dev/models/meta-llama/llama-3.2-3b-instruct) | text | $0.0509 / $0.335 | $0.05 / $0.33 | in −2% / out −1% |
| [PixVerse C1 Text-to-Video (Venice)](https://uberllm.dev/models/venice/pixverse-c1-t2v) | video | $0.07 / sec | $0.07133 / sec | +2% |
| [MiniMax M2](https://uberllm.dev/models/minimax/minimax-m2) | text | $0.255 / $1.02 | $0.30 / $1.20 | +18% |
| [Qwen 3.6 27B](https://uberllm.dev/models/qwen/qwen3.6-27b) | text | $0.325 / $2.70 | $0.32 / $3.20 | in −2% / out +19% |
| [Qwen 3.5 397B](https://uberllm.dev/models/qwen/qwen3.5-397b-a17b) | text | $0.50 / $3.60 | $0.60 / $3.60 | in +20% / out 0% |
| [Reflection: Beam 1.0 501B A23B](https://uberllm.dev/models/reflection/beam-1.0-501b-a23b) | text | $0.25 / $1.00 | $0.30 / $1.00 | in +20% / out 0% |
| [Mistral Small 3.2 24B Instruct](https://uberllm.dev/models/mistralai/mistral-small-3.2-24b-instruct) | text | $0.075 / $0.20 | $0.0938 / $0.25 | +25% |
| [Mistral Small 3.2 24B Instruct (Morpheus Web)](https://uberllm.dev/models/mistralai/mistral-small-3.2-24b-instruct:web) | text | $0.075 / $0.20 | $0.0938 / $0.25 | +25% |
| [Kimi K2.5](https://uberllm.dev/models/moonshotai/kimi-k2.5) | text | $0.50 / $2.50 | $0.532 / $3.33 | in +6% / out +33% |
| [Kimi K2.5 (Morpheus Web)](https://uberllm.dev/models/moonshotai/kimi-k2.5:web) | text | $0.50 / $2.50 | $0.532 / $3.33 | in +6% / out +33% |
| [GLM 4.5 Air](https://uberllm.dev/models/z-ai/glm-4.5-air) | text | $0.13 / $0.85 | $0.20 / $1.10 | in +54% / out +29% |
| [DeepSeek: DeepSeek V4 Flash Vision Exp](https://uberllm.dev/models/deepseek/deepseek-v4-flash-vision-exp) | text | $0.2156 / $0.6468 | $0.44 / $1.32 | +104% |
| [GLM 5.3 Flash](https://uberllm.dev/models/z-ai/glm-5.3-flash) | text | $0.0285 / $0.0923 | $0.15 / $0.50 | in +426% / out +442% |

**New models (4)**: [Claude Fable 5.2](https://uberllm.dev/models/anthropic/claude-fable-5.2), [Meta: Muse Ember](https://uberllm.dev/models/meta-llama/muse-ember), [Tencent: Hy4](https://uberllm.dev/models/tencent/hy4), [Tencent: Hy4 preview](https://uberllm.dev/models/tencent/hy4-preview)

**No longer listed (2)**: `deepseek/deepseek-r1`, `x-ai/grok-imagine-quality-edit`

<details><summary>UberLLM price moves of 10% or more (164)</summary>

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
| [Mistral: Mistral Large 4](https://uberllm.dev/models/mistralai/mistral-large-4-0) | text | $0.637 / $1.91 | $0.126 / $0.378 | −80% |
| [NVIDIA Nemotron 3 Ultra 550B](https://uberllm.dev/models/nvidia/nemotron-3-ultra-550b-a55b) | text | $0.4562 / $2.28 | $0.1062 / $0.5312 | −77% |
| [Google: Gemini 4 Argon](https://uberllm.dev/models/google/gemini-4-argon) | text | $1.00 / $5.00 | $0.24 / $1.20 | −76% |
| [Gemini 3.7 Flash](https://uberllm.dev/models/google/gemini-3.7-flash) | text | $0.3375 / $1.69 | $0.09 / $0.45 | −73% |
| [Kimi K2.6](https://uberllm.dev/models/moonshotai/kimi-k2.6) | text | $0.1885 / $0.9889 | $0.052 / $0.2728 | −72% |
| [Qwen: Qwen3.7 Flash](https://uberllm.dev/models/qwen/qwen3.7-flash) | text | $0.0297 / $0.1287 | $0.0096 / $0.0416 | −68% |
| [Grok 4.7](https://uberllm.dev/models/x-ai/grok-4.7) | text | $1.58 / $4.74 | $0.64 / $1.92 | −59% |
| [MiniMax M3.1 Flash](https://uberllm.dev/models/minimax/minimax-m3-1-flash) | text | $0.069 / $0.276 | $0.0285 / $0.114 | −59% |
| [Gemini 3 Flash Preview](https://uberllm.dev/models/google/gemini-3-flash-preview) | text | $0.105 / $0.63 | $0.045 / $0.27 | −57% |
| [GPT-5.6 Terra](https://uberllm.dev/models/openai/gpt-5.6-terra) | text | $1.32 / $7.92 | $0.60 / $3.60 | −55% |
| [Mistral Large](https://uberllm.dev/models/mistralai/mistral-large) | text | $0.42 / $1.26 | $0.20 / $0.60 | −52% |
| [Qwen3.8 Flash](https://uberllm.dev/models/qwen/qwen3.8-flash) | text | $0.03 / $0.094 | $0.015 / $0.047 | −50% |
| [Z.ai: GLM 5.3 FlashX](https://uberllm.dev/models/z-ai/glm-5.3-flashx) | text | $0.37 / $1.25 | $0.185 / $0.625 | −50% |
| [Kimi K2.7 Code](https://uberllm.dev/models/moonshotai/kimi-k2.7-code) | text | $0.306 / $1.79 | $0.168 / $0.98 | −45% |
| [MiniMax M3](https://uberllm.dev/models/minimax/minimax-m3) | text | $0.09 / $0.36 | $0.051 / $0.204 | −43% |
| [GPT Image 1.5 (Venice)](https://uberllm.dev/models/venice/gpt-image-1.5) | image | $0.26 / image | $0.156 / image | −40% |
| [Gemini 3.1 Pro](https://uberllm.dev/models/google/gemini-3.1-pro) | text | $1.80 / $10.80 | $1.10 / $6.60 | −39% |
| [Qwen 3.5 35B A3B](https://uberllm.dev/models/qwen/qwen3.5-35b-a3b) | text | $0.1562 / $1.00 | $0.0975 / $0.65 | in −38% / out −35% |
| [xAI Speech to Text v1 (Venice)](https://uberllm.dev/models/venice/xai-stt-v1) | text | $0.00153 / minute | $0.000963 / minute | −37% |
| [Qwen 3.6 35B A3B](https://uberllm.dev/models/qwen/qwen3-6-35b-a3b) | text | $0.063 / $0.63 | $0.04 / $0.40 | −37% |
| [Mistral Small 4](https://uberllm.dev/models/mistralai/mistral-small-4) | text | $0.15 / $0.60 | $0.096 / $0.384 | −36% |
| [Qwen 3.6 35B A3B (E2EE)](https://uberllm.dev/models/qwen/e2ee-qwen3-6-35b-a3b) | text | $0.182 / $1.18 | $0.1165 / $0.7552 | −36% |
| [Grok 4.3](https://uberllm.dev/models/x-ai/grok-4.3) | text | $0.3625 / $0.725 | $0.2375 / $0.475 | −34% |
| [Qwen 3 Coder 480B Turbo](https://uberllm.dev/models/qwen/qwen3-coder-turbo) | text | $0.2975 / $1.27 | $0.196 / $0.84 | −34% |
| [GPT-5.6 Luna](https://uberllm.dev/models/openai/gpt-5.6-luna) | text | $0.088 / $0.528 | $0.058 / $0.348 | −34% |
| [Devstral 2 123B](https://uberllm.dev/models/mistralai/devstral-2-123b) | text | $0.012 / $0.06 | $0.008 / $0.04 | −33% |
| [Claude Sonnet 5.5](https://uberllm.dev/models/anthropic/claude-sonnet-5.5) | text | $0.86 / $4.30 | $0.58 / $2.90 | −33% |
| [Seedance 2.0 (reference-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-reference-to-video) | video | $0.0792 / sec | $0.05368 / sec | −32% |
| [Qwen 3.8 Max](https://uberllm.dev/models/qwen/qwen-3-8-max) | text | $0.65 / $1.95 | $0.45 / $1.35 | −31% |
| [Inception: Mercury 2.5](https://uberllm.dev/models/inception/mercury-2.5) | text | $0.04 / $0.15 | $0.028 / $0.105 | −30% |
| [Gemini 3.1 Pro Preview](https://uberllm.dev/models/google/gemini-3.1-pro-preview) | text | $0.90 / $5.40 | $0.64 / $3.84 | −29% |
| [Veo3.1 Fast (image-to-video)](https://uberllm.dev/models/google/veo3-1-fast-image-to-video) | video | $0.165 / sec | $0.1188 / sec | −28% |
| [Claude Opus 5.5](https://uberllm.dev/models/anthropic/claude-opus-5.5) | text | $1.56 / $7.80 | $1.16 / $5.80 | −26% |
| [Grok Imagine Pro (Venice)](https://uberllm.dev/models/venice/grok-imagine-pro) | image | $0.0525 / image | $0.0392 / image | −25% |
| [Claude Sonnet 4.6](https://uberllm.dev/models/anthropic/claude-sonnet-4.6) | text | $1.80 / $9.00 | $1.35 / $6.75 | −25% |
| [Trinity Large Thinking](https://uberllm.dev/models/arcee-ai/trinity-large-thinking) | text | $0.30 / $1.00 | $0.225 / $0.7538 | −25% |
| [Claude Opus 5](https://uberllm.dev/models/anthropic/claude-opus-5) | text | $2.70 / $13.50 | $2.05 / $10.25 | −24% |
| [GPT-6 Luna Decisions (OpenAI)](https://uberllm.dev/models/openai/gpt-6-luna-decisions) | text | $0.10 / $0 | $0.076 / $0 | in −24% / out – |
| [Aion 3.0 Mini](https://uberllm.dev/models/aion-labs/aion-3-0-mini) | text | $0.658 / $1.32 | $0.504 / $1.01 | −23% |
| [Vidu Q3 Text-to-Video](https://uberllm.dev/models/vidu/vidu-q3-text-to-video) | video | $0.1933 / sec | $0.1547 / sec | −20% |
| [Qwen3 1.7B TTS](https://uberllm.dev/models/qwen/tts-qwen3-1-7b) | audio | $0.1125 / 1K chars | $0.09 / 1K chars | −20% |
| [Chatterbox HD TTS](https://uberllm.dev/models/resemble-ai/tts-chatterbox-hd) | audio | $0.05 / 1K chars | $0.04 / 1K chars | −20% |
| [Hunyuan Image 3.0 (Venice)](https://uberllm.dev/models/venice/hunyuan-image-v3) | image | $0.09 / image | $0.072 / image | −20% |
| [Seedance 2.0 (image-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-image-to-video) | video | $0.088 / sec | $0.0704 / sec | −20% |
| [Longcat Distilled (image-to-video)](https://uberllm.dev/models/meituan/longcat-distilled-image-to-video) | video | $0.018 / sec | $0.0144 / sec | −20% |
| [LongCat Distilled Text-to-Video](https://uberllm.dev/models/meituan/longcat-distilled-text-to-video) | video | $0.018 / sec | $0.0144 / sec | −20% |
| [Ministral 3B](https://uberllm.dev/models/mistralai/ministral-3-3b-instruct) | text | $0.005 / $0.005 | $0.004 / $0.004 | −20% |
| [Flux 1.1 Pro (Venice, legacy)](https://uberllm.dev/models/venice/flux-1.1-pro) | image | $0.03 / image | $0.024 / image | −20% |
| [Stable Diffusion XL (Venice, legacy)](https://uberllm.dev/models/venice/sdxl) | image | $0.01 / image | $0.008 / image | −20% |
| [Inworld 1.5 Max TTS](https://uberllm.dev/models/inworld/tts-inworld-1-5-max) | audio | $0.0125 / 1K chars | $0.01013 / 1K chars | −19% |
| [Qwen3 0.6B TTS](https://uberllm.dev/models/qwen/tts-qwen3-0-6b) | audio | $0.0875 / 1K chars | $0.07087 / 1K chars | −19% |
| [Kling O3.4k (image-to-video)](https://uberllm.dev/models/kling/kling-o3-4k-image-to-video) | video | $0.4633 / sec | $0.3753 / sec | −19% |
| [DeepSeek V4 Flash E2EE](https://uberllm.dev/models/deepseek/e2ee-deepseek-v4-flash) | text | $0.1456 / $0.2984 | $0.1183 / $0.2424 | −19% |
| [Thinking Machines: Inkling](https://uberllm.dev/models/thinking-machines/inkling) | text | $0.49 / $1.98 | $0.40 / $1.62 | −18% |
| [Firered Image (image-to-image)](https://uberllm.dev/models/xiaohongshu/firered-image-edit) | image | $0.034 / image | $0.028 / image | −18% |
| [Wan 2.7 (image-to-video)](https://uberllm.dev/models/wan/wan-2-7-image-to-video) | video | $0.08 / sec | $0.066 / sec | −17% |
| [MiMo-V2.6-Pro](https://uberllm.dev/models/xiaomi/mimo-v2.6-pro) | text | $0.3001 / $0.6003 | $0.248 / $0.4959 | −17% |
| [Gemma 4 E2B](https://uberllm.dev/models/google/gemma-4-e2b) | text | $0.0024 / $0.0048 | $0.002 / $0.004 | −17% |
| [MiMo-V2.6-Flash](https://uberllm.dev/models/xiaomi/mimo-v2.6-flash) | text | $0.1176 / $0.2352 | $0.098 / $0.196 | −17% |
| [Aion 3.0](https://uberllm.dev/models/aion-labs/aion-3-0) | text | $2.55 / $5.10 | $2.13 / $4.26 | −16% |
| [DeepSeek V4 Flash](https://uberllm.dev/models/deepseek/deepseek-v4-flash) | text | $0.07826 / $0.1565 | $0.06643 / $0.1329 | −15% |
| [FLUX.2 Klein 4B](https://uberllm.dev/models/black-forest-labs/flux.2-klein-4b) | image | $0.015 / megapixel | $0.01275 / megapixel | −15% |
| [Meta: Muse Spark Open](https://uberllm.dev/models/meta-llama/muse-spark-open) | text | $1.09 / $3.70 | $0.925 / $3.15 | −15% |
| [GPT-5.5 Pro](https://uberllm.dev/models/openai/gpt-5.5-pro) | text | $24.90 / $149.40 | $21.60 / $129.60 | −13% |
| [FLUX.2 Flex](https://uberllm.dev/models/black-forest-labs/flux.2-flex) | image | $0.0594 / megapixel | $0.0516 / megapixel | −13% |
| [GPT-5.6 Luna Pro](https://uberllm.dev/models/openai/gpt-5.6-luna-pro) | text | $0.168 / $1.01 | $0.146 / $0.876 | −13% |
| [Kimi K3 Fast](https://uberllm.dev/models/moonshotai/kimi-k3-fast-api) | text | $3.82 / $19.12 | $3.33 / $16.65 | −13% |
| [Qwen 3 235B A22B Thinking 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-thinking-2507) | text | $0.1395 / $1.08 | $0.1215 / $0.945 | −13% |
| [Gemini 2.5 Pro](https://uberllm.dev/models/google/gemini-2.5-pro) | text | $0.40 / $3.20 | $0.35 / $2.80 | −13% |
| [Claude Fable 5.1](https://uberllm.dev/models/anthropic/claude-fable-5.1) | text | $6.50 / $32.50 | $5.70 / $28.50 | −12% |
| [Mercury 2](https://uberllm.dev/models/inception/mercury-2) | text | $0.225 / $0.675 | $0.1975 / $0.5925 | −12% |
| [Grok Imagine 1.5 Image To Video Private (image-to-video)](https://uberllm.dev/models/x-ai/grok-imagine-1-5-image-to-video-private) | video | $0.09 / sec | $0.0792 / sec | −12% |
| [GPT-5.4 Pro](https://uberllm.dev/models/openai/gpt-5.4-pro) | text | $20.10 / $120.60 | $17.70 / $106.20 | −12% |
| [Grok 4.6](https://uberllm.dev/models/x-ai/grok-4.6) | text | $1.78 / $5.34 | $1.58 / $4.74 | −11% |
| [GLM 5.2 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5-2-p) | text | $1.57 / $5.17 | $1.40 / $4.60 | −11% |
| [Qwen Image 2 Pro (image-to-image)](https://uberllm.dev/models/qwen/qwen-image-2-pro-edit) | image | $0.09 / image | $0.08 / image | −11% |
| [ElevenLabs Turbo v2.5 TTS (Venice)](https://uberllm.dev/models/venice/elevenlabs-tts-turbo-v2-5) | audio | $0.05625 / 1K chars | $0.05 / 1K chars | −11% |
| [Flux 1.1 (Venice, legacy)](https://uberllm.dev/models/venice/flux-1.1) | image | $0.009 / image | $0.008 / image | −11% |
| [MiMo-V2.6-Pro-UltraSpeed](https://uberllm.dev/models/xiaomi/mimo-v2.6-pro-ultraspeed) | text | $4.31 / $8.61 | $3.83 / $7.66 | −11% |
| [Claude Opus 4.8 Fast](https://uberllm.dev/models/anthropic/claude-opus-4.8-fast) | text | $7.50 / $37.50 | $6.70 / $33.50 | −11% |
| [GPT-5.6 Sol](https://uberllm.dev/models/openai/gpt-5.6-sol) | text | $1.92 / $9.60 | $1.72 / $8.60 | −10% |
| [GPT-6 Sol Pro](https://uberllm.dev/models/openai/gpt-6-sol-pro) | text | $1.92 / $9.60 | $1.72 / $8.60 | −10% |
| [OpenAI: GPT-6.1 Sol Pro](https://uberllm.dev/models/openai/gpt-6.1-sol-pro) | text | $1.92 / $9.60 | $1.72 / $8.60 | −10% |
| [GPT OSS 120B](https://uberllm.dev/models/openai/e2ee-gpt-oss-120b-p) | text | $0.1001 / $0.5005 | $0.0897 / $0.4485 | −10% |
| [Venice TTS 1 (legacy alias)](https://uberllm.dev/models/venice/tts-1) | audio | $0.00315 / 1K chars | $0.002835 / 1K chars | −10% |
| [Kling V3 Pro (image-to-video)](https://uberllm.dev/models/kling/kling-v3-pro-image-to-video) | video | $0.165 / sec | $0.1833 / sec | +11% |
| [Veo 3.1 Fast Text-to-Video](https://uberllm.dev/models/google/veo3-1-fast-text-to-video) | video | $0.1485 / sec | $0.165 / sec | +11% |
| [Kling V3 Standard (image-to-video)](https://uberllm.dev/models/kling/kling-v3-standard-image-to-video) | video | $0.126 / sec | $0.14 / sec | +11% |
| [Qwen3.8 2.4T A95B](https://uberllm.dev/models/qwen/qwen3.8-2.4t-a95b) | text | $0.18 / $0.54 | $0.20 / $0.60 | +11% |
| [MiniMax Music 2.6 (Venice)](https://uberllm.dev/models/venice/minimax-music-v26) | text | $0.216 / request | $0.24 / request | +11% |
| [Qwen Image (Venice)](https://uberllm.dev/models/venice/qwen-image) | image | $0.027 / image | $0.03 / image | +11% |
| [GLM-5 Turbo](https://uberllm.dev/models/z-ai/glm-5-turbo) | text | $0.588 / $1.96 | $0.66 / $2.20 | +12% |
| [Flux 2 Max — Edit (Venice)](https://uberllm.dev/models/black-forest-labs/flux-2-max-edit) | image | $0.1615 / image | $0.19 / image | +18% |
| [GPT Image 1.5 — Edit (Venice)](https://uberllm.dev/models/venice/gpt-image-1-5-edit) | image | $0.306 / image | $0.36 / image | +18% |
| [MMAudio V2 Text-to-Audio (Venice)](https://uberllm.dev/models/venice/mmaudio-v2-text-to-audio) | text | $0.0085 / request | $0.01 / request | +18% |
| [Wan 2.7 Pro (image-to-video)](https://uberllm.dev/models/wan/wan-2-7-pro-image-to-video) | video | $0.102 / sec | $0.12 / sec | +18% |
| [Recraft V4 (Venice)](https://uberllm.dev/models/venice/recraft-v4) | image | $0.04 / image | $0.0475 / image | +19% |
| [Grok 4.20 Multi-Agent Beta](https://uberllm.dev/models/x-ai/grok-4.20-multi-agent-beta) | text | $0.95 / $1.90 | $1.14 / $2.27 | +20% |
| [MoonshotAI: Kimi K3.1 Pro](https://uberllm.dev/models/moonshotai/kimi-k3.1-pro) | text | $0.40 / $2.00 | $0.48 / $2.40 | +20% |
| [Claude Haiku 5.5](https://uberllm.dev/models/anthropic/claude-haiku-5.5) | text | $0.056 / $0.28 | $0.069 / $0.345 | +23% |
| [Gemma 3 27B E2EE](https://uberllm.dev/models/google/e2ee-gemma-3-27b) | text | $0.056 / $0.20 | $0.07 / $0.25 | +25% |
| [Gemma 4 31B (E2EE)](https://uberllm.dev/models/google/e2ee-gemma-4-31b) | text | $0.10 / $0.30 | $0.125 / $0.375 | +25% |
| [ElevenLabs TTS Multilingual v2 (Venice audio)](https://uberllm.dev/models/venice/elevenlabs-tts-multilingual-v2) | text | $0.096 / request | $0.12 / request | +25% |
| [GLM 5.1 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5.1) | text | $0.44 / $1.66 | $0.55 / $2.08 | +25% |
| [OpenAI: GPT-6.1 Terra](https://uberllm.dev/models/openai/gpt-6.1-terra) | text | $0.47 / $2.35 | $0.59 / $2.95 | +26% |
| [GLM 5.1](https://uberllm.dev/models/z-ai/glm-5.1) | text | $0.154 / $0.484 | $0.196 / $0.616 | +27% |
| [GPT-5.3 Codex](https://uberllm.dev/models/openai/gpt-5.3-codex) | text | $0.63 / $5.04 | $0.805 / $6.44 | +28% |
| [Claude Opus 4.7](https://uberllm.dev/models/anthropic/claude-opus-4.7) | text | $1.95 / $9.75 | $2.55 / $12.75 | +31% |
| [Gemini 3.5 Flash Lite](https://uberllm.dev/models/google/gemini-3-5-flash-lite) | text | $0.15 / $1.25 | $0.198 / $1.65 | +32% |
| [Qwen: Qwen3.8 Omni Flash](https://uberllm.dev/models/qwen/qwen3.8-omni-flash) | text | $0.018 / $0.0564 | $0.024 / $0.0752 | +33% |
| [GLM 4.5](https://uberllm.dev/models/z-ai/glm-4.5) | text | $0.018 / $0.066 | $0.024 / $0.088 | +33% |
| [Meta: Muse Wonder](https://uberllm.dev/models/meta-llama/muse-wonder) | text | $2.04 / $10.20 | $2.80 / $14.00 | +37% |
| [Recraft V4 Pro (Venice)](https://uberllm.dev/models/venice/recraft-v4-pro) | image | $0.203 / image | $0.29 / image | +43% |
| [Qwen Image 2 Pro (Venice)](https://uberllm.dev/models/venice/qwen-image-2-pro) | image | $0.07 / image | $0.10 / image | +43% |
| [Ministral 14B 3.0](https://uberllm.dev/models/mistralai/ministral-3-14b-instruct) | text | $0.04 / $0.04 | $0.058 / $0.058 | +45% |
| [Magistral Small 2509](https://uberllm.dev/models/mistralai/magistral-small-2509) | text | $0.01 / $0.03 | $0.015 / $0.045 | +50% |
| [Gemma 4 31B](https://uberllm.dev/models/google/gemma-4-31b) | text | $0.0024 / $0.0072 | $0.0036 / $0.0108 | +50% |
| [Gemini 3.6 Flash](https://uberllm.dev/models/google/gemini-3-6-flash) | text | $0.3975 / $1.99 | $0.60 / $3.00 | +51% |
| [Claude Opus 4.6](https://uberllm.dev/models/anthropic/claude-opus-4.6) | text | $1.60 / $8.00 | $2.45 / $12.25 | +53% |
| [Orpheus TTS](https://uberllm.dev/models/canopy-labs/tts-orpheus) | audio | $0.03125 / 1K chars | $0.05 / 1K chars | +60% |
| [GPT-6.1 Sol](https://uberllm.dev/models/openai/gpt-6.1-sol) | text | $0.78 / $3.90 | $1.28 / $6.40 | +64% |
| [GPT-4o Mini](https://uberllm.dev/models/openai/gpt-4o-mini) | text | $0.0105 / $0.042 | $0.018 / $0.072 | +71% |
| [GPT-4o](https://uberllm.dev/models/openai/gpt-4o) | text | $0.35 / $1.40 | $0.60 / $2.40 | +71% |
| [Ministral 3 8B](https://uberllm.dev/models/mistralai/ministral-3-8b-instruct) | text | $0.003 / $0.003 | $0.006 / $0.006 | +100% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | text | $0.00075 / $0.003 | $0.0015 / $0.006 | +100% |
| [Qwen 3.8 27B](https://uberllm.dev/models/qwen/qwen-3-8-27b) | text | $0.009 / $0.1125 | $0.0195 / $0.2437 | +117% |
| [Meta: Muse Spark 1.2](https://uberllm.dev/models/meta-llama/muse-spark-1.2) | text | $0.275 / $0.935 | $0.6375 / $2.17 | +132% |
| [MiniMax M2.5](https://uberllm.dev/models/minimax/minimax-m2.5) | text | $0.0162 / $0.057 | $0.0378 / $0.133 | +133% |
| [GPT-OSS 120B](https://uberllm.dev/models/openai/gpt-oss-120b) | text | $0.0035 / $0.015 | $0.0084 / $0.036 | +140% |
| [Gemma 3 27B](https://uberllm.dev/models/google/gemma-3-27b-it) | text | $0.0064 / $0.016 | $0.016 / $0.04 | +150% |
| [Mistral Large 3](https://uberllm.dev/models/mistralai/mistral-large-3) | text | $0.03 / $0.09 | $0.075 / $0.225 | +150% |
| [Meta: Muse Spark 1.1](https://uberllm.dev/models/meta-llama/muse-spark-1.1) | text | $0.3625 / $1.23 | $0.9125 / $3.10 | +152% |
| [Palmyra Vision 7B](https://uberllm.dev/models/writer/palmyra-vision-7b) | text | $0.006 / $0.024 | $0.0165 / $0.066 | +175% |
| [GLM-4.7](https://uberllm.dev/models/z-ai/glm-4.7) | text | $0.0825 / $0.33 | $0.2365 / $0.946 | +187% |
| [Qwen3 Coder 30B A3B Instruct](https://uberllm.dev/models/qwen/qwen3-coder-30b-a3b-instruct) | text | $0.003 / $0.012 | $0.009 / $0.036 | +200% |
| [Qwen3 32B](https://uberllm.dev/models/qwen/qwen3-32b) | text | $0.0016 / $0.0056 | $0.0056 / $0.0196 | +250% |
| [DeepSeek V3.2](https://uberllm.dev/models/deepseek/deepseek-v3.2) | text | $0.0078 / $0.0114 | $0.0286 / $0.0418 | +267% |
| [NVIDIA Nemotron Nano 9B v2](https://uberllm.dev/models/nvidia/nemotron-nano-9b-v2) | text | $0.0018 / $0.0069 | $0.0066 / $0.0253 | +267% |
| [Qwen 3 235B A22B Instruct 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-2507) | text | $0.0056 / $0.03 | $0.02187 / $0.1172 | +291% |
| [Qwen 3 Coder 480b](https://uberllm.dev/models/qwen/qwen3-coder) | text | $0.006 / $0.02 | $0.024 / $0.08 | +300% |
| [Qwen3 VL 235B A22B](https://uberllm.dev/models/qwen/qwen3-vl-235b-a22b-instruct) | text | $0.0042 / $0.038 | $0.0189 / $0.171 | +350% |
| [Meta: Muse Spark 1.3 Contributor](https://uberllm.dev/models/meta-llama/muse-spark-1.3-contributor) | text | $0.007 / $0.014 | $0.036 / $0.072 | +414% |
| [Gemma 4 31B IT](https://uberllm.dev/models/google/gemma-4-31b-it) | text | $0.0156 / $0.0468 | $0.084 / $0.252 | +438% |
| [Qwen3 Coder Next](https://uberllm.dev/models/qwen/qwen3-coder-next) | text | $0.0024 / $0.016 | $0.0132 / $0.088 | +450% |
| [GPT OSS Safeguard 120B](https://uberllm.dev/models/openai/gpt-oss-safeguard-120b) | text | $0.0045 / $0.018 | $0.0255 / $0.102 | +467% |
| [Meta: Muse Spark 1.3](https://uberllm.dev/models/meta-llama/muse-spark-1.3) | text | $0.10 / $0.34 | $0.6125 / $2.08 | +512% |
| [GLM-4.6](https://uberllm.dev/models/z-ai/glm-4.6) | text | $0.0172 / $0.07 | $0.1591 / $0.6475 | +825% |
| [GLM 4.7 Flash](https://uberllm.dev/models/z-ai/glm-4.7-flash) | text | $0.001815 / $0.012 | $0.01694 / $0.112 | +833% |
| [DeepSeek V3.1](https://uberllm.dev/models/deepseek/deepseek-v3.1) | text | $0.0075 / $0.0285 | $0.075 / $0.285 | +900% |
| [NVIDIA Nemotron 3 Nano 30B](https://uberllm.dev/models/nvidia/nemotron-3-nano-30b-a3b) | text | $0.0015 / $0.006 | $0.01725 / $0.069 | +1050% |
| [Kimi K2 Thinking](https://uberllm.dev/models/moonshotai/kimi-k2-thinking) | text | $0.012 / $0.05 | $0.15 / $0.625 | +1150% |
| [GPT-OSS 20B](https://uberllm.dev/models/openai/gpt-oss-20b) | text | $0.0003 / $0.0013 | $0.0039 / $0.0169 | +1200% |
| [Gemma 3 12B IT](https://uberllm.dev/models/google/gemma-3-12b-it) | text | $0.001 / $0.003 | $0.0215 / $0.0645 | +2050% |
| [MiniMax M2.1](https://uberllm.dev/models/minimax/minimax-m2.1) | text | $0.003 / $0.012 | $0.315 / $1.26 | +10400% |

</details>

