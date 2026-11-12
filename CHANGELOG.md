# Changelog

Price changes between daily snapshots of [`prices.json`](prices.json), newest first.
"Official list price" = the model maker's price as carried in the catalog (see [SOURCES](README.md#sources)).
"UberLLM price" = the best live offer on the UberLLM market at snapshot time; it moves during the day.
Text prices are $ per 1M input / output tokens. Every day's full table is in [`history/`](history/).

## 2026-11-12 (vs 2026-11-11)

**Official list price changes (26)**

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [GLM 5.1 E2EE](https://uberllm.dev/models/z-ai/e2ee-glm-5.1) | text | $1.40 / $4.40 | $1.33 / $4.18 | −5% |
| [GLM 5.1](https://uberllm.dev/models/z-ai/glm-5.1) | text | $1.40 / $4.40 | $1.33 / $4.18 | −5% |
| [DeepSeek V4 Flash](https://uberllm.dev/models/deepseek/deepseek-v4-flash) | text | $0.091 / $0.182 | $0.09 / $0.18 | −1% |
| [Flux 3 (Venice)](https://uberllm.dev/models/black-forest-labs/venice-flux-3-image) | image | – | $0.12 / image |  |
| [ElevenLabs Music v2](https://uberllm.dev/models/elevenlabs/elevenlabs-music-v2) | music | – | $0.69 / track |  |
| [ElevenLabs Music v2.5](https://uberllm.dev/models/elevenlabs/elevenlabs-music-v2-5) | music | – | $0.69 / track |  |
| [ElevenLabs Voice Changer](https://uberllm.dev/models/elevenlabs/elevenlabs-voice-changer) | music | – | $0.35 / track |  |
| [Veo3.1 Full (image-to-video)](https://uberllm.dev/models/google/veo3-1-full-image-to-video) | video | – | $0.44 / sec |  |
| [Veo 3.1 Full Text-to-Video](https://uberllm.dev/models/google/veo3-1-full-text-to-video) | video | – | $0.44 / sec |  |
| [Krea 2 Turbo (Venice)](https://uberllm.dev/models/krea/venice-krea-2-turbo) | image | – | $0.04 / image |  |
| [LongCat Text-to-Video](https://uberllm.dev/models/meituan/longcat-text-to-video) | video | – | $0.05 / sec |  |
| [Pixverse C1 (image-to-video)](https://uberllm.dev/models/pixverse/pixverse-c1-image-to-video) | video | – | $0.0433 / sec |  |
| [PixVerse V5.6 Text-to-Video](https://uberllm.dev/models/pixverse/pixverse-v5-6-text-to-video) | video | – | $0.228 / sec |  |
| [Pixverse V5.6 Transition (transition)](https://uberllm.dev/models/pixverse/pixverse-v5-6-transition) | video | – | $0.202 / sec |  |
| [Runway Gen-4.5](https://uberllm.dev/models/runway/runway-gen4-5) | video | – | $0.16 / sec |  |
| [Runway Gen-4 Turbo](https://uberllm.dev/models/runway/runway-gen4-turbo) | video | – | $0.0675 / sec |  |
| [ACE-Step 1.5 (Venice)](https://uberllm.dev/models/venice/ace-step-15) | music | – | $0.03 / track |  |
| [Venice Music Gen (legacy alias)](https://uberllm.dev/models/venice/music-gen) | music | – | $0.03 / track |  |
| [Runway Gen-4.5 Text-to-Video (Venice)](https://uberllm.dev/models/venice/runway-gen4-5-text) | video | – | $0.16 / sec |  |
| [Venice Video Gen (legacy alias)](https://uberllm.dev/models/venice/video-gen) | video | – | $0.16 / sec |  |
| [Vidu Q3 Text-to-Video](https://uberllm.dev/models/vidu/vidu-q3-text-to-video) | video | – | $0.1933 / sec |  |
| [Wan 2.5 Preview (image-to-video)](https://uberllm.dev/models/wan/wan-2-5-preview-image-to-video) | video | – | $0.056 / sec |  |
| [Grok Imagine Text-to-Video](https://uberllm.dev/models/x-ai/grok-imagine-text-to-video) | video | $0.0885 / sec | $0.089 / sec | +1% |
| [Tencent: Hy4 preview](https://uberllm.dev/models/tencent/hy4-preview) | text | $0.7506 / $2.25 | $0.834 / $2.50 | +11% |
| [Tencent HY3](https://uberllm.dev/models/tencent/hy3) | text | $0.0825 / $0.33 | $0.132 / $0.528 | +60% |
| [MiniMax M3.1 Flash](https://uberllm.dev/models/minimax/minimax-m3-1-flash) | text | $0.075 / $0.30 | $0.15 / $0.60 | +100% |

**New models (15)**

| Model | Category | Official price | UberLLM price |
|---|---|---|---|
| [Hermes 3 Llama 3.1 405b (Morpheus Web)](https://uberllm.dev/models/meta-llama/hermes-3-llama-3.1-405b:web) | text | – | $0.737 / $2.01 |
| [Llama 3.2 3B (Morpheus Web)](https://uberllm.dev/models/meta-llama/llama-3.2-3b-instruct:web) | text | – | $0.1005 / $0.402 |
| [Llama 3.3 70B (Morpheus Web)](https://uberllm.dev/models/meta-llama/llama-3.3-70b-instruct:web) | text | – | $0.469 / $1.88 |
| [MiniMax M2.5 (Morpheus Web)](https://uberllm.dev/models/minimax/minimax-m2.5:web) | text | $0.27 / $0.95 | $0.2278 / $0.7973 |
| [Mistral Small 3.2 24B Instruct (Morpheus Web)](https://uberllm.dev/models/mistralai/mistral-small-3.2-24b-instruct:web) | text | $0.0938 / $0.25 | $0.06281 / $0.1675 |
| [Kimi K2.5 (Morpheus Web)](https://uberllm.dev/models/moonshotai/kimi-k2.5:web) | text | $0.532 / $3.33 | $0.3752 / $2.35 |
| [Kimi K2.6 (Morpheus Web)](https://uberllm.dev/models/moonshotai/kimi-k2.6:web) | text | $0.65 / $3.41 | $0.5695 / $3.12 |
| [Kimi K2.7 Code (Morpheus Web)](https://uberllm.dev/models/moonshotai/kimi-k2.7-code:web) | text | $0.60 / $3.50 | $0.4556 / $2.28 |
| [OpenAI GPT OSS 120B (Morpheus Web)](https://uberllm.dev/models/openai/gpt-oss-120b:web) | text | $0.07 / $0.30 | $0.0469 / $0.201 |
| [Qwen 3 235B A22B Instruct 2507 (Morpheus Web)](https://uberllm.dev/models/qwen/qwen3-235b-a22b-2507:web) | text | $0.14 / $0.75 | $0.1005 / $0.5025 |
| [Qwen 3 Next 80b (Morpheus Web)](https://uberllm.dev/models/qwen/qwen3-next-80b-a3b-instruct:web) | text | – | $0.2345 / $1.27 |
| [GLM 5.1 Non-thinking](https://uberllm.dev/models/z-ai/glm-5.1-non-thinking) | text | $1.40 / $4.40 | $1.00 / $3.35 |
| [GLM 5.1 Non-thinking (Morpheus Web)](https://uberllm.dev/models/z-ai/glm-5.1-non-thinking:web) | text | $1.40 / $4.40 | $1.00 / $3.35 |
| [GLM 5.1 (Morpheus Web)](https://uberllm.dev/models/z-ai/glm-5.1:web) | text | $1.33 / $4.18 | $1.17 / $3.69 |
| [GLM 5 (Morpheus Web)](https://uberllm.dev/models/z-ai/glm-5:web) | text | $1.00 / $3.20 | $0.737 / $2.78 |

**No longer listed (6)**: `bytedance/seedance-2-0-mini-reference-to-video`, `google/veo3-1-fast-image-to-video`, `inception/mercury-2.5`, `pixverse/pixverse-c1-reference-to-video`, `pixverse/pixverse-c1-transition`, `vidu/vidu-q3-image-to-video`

<details><summary>UberLLM price moves of 10% or more (127)</summary>

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [Kimi K2.7 Code](https://uberllm.dev/models/moonshotai/kimi-k2.7-code) | text | $0.009788 / $0.0571 | $0.000975 / $0.005686 | −90% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | text | $0.000525 / $0.0021 | $0.000074 / $0.000297 | −86% |
| [Meta: Muse Spark 1.2](https://uberllm.dev/models/meta-llama/muse-spark-1.2) | text | $0.375 / $1.27 | $0.1125 / $0.3825 | −70% |
| [GPT-5.4 Image 2](https://uberllm.dev/models/openai/gpt-5.4-image-2) | image | $2.00 / $3.75 | $0.64 / $1.20 | −68% |
| [Flux 2 Max (Venice)](https://uberllm.dev/models/venice/flux-2-max) | image | $0.063 / image | $0.0225 / image | −64% |
| [Google: Gemini 4 Carbon](https://uberllm.dev/models/google/gemini-4-carbon) | text | $1.00 / $5.00 | $0.3792 / $1.90 | −62% |
| [Seedream 4.5](https://uberllm.dev/models/bytedance/seedream-4.5) | image | $0.024 / image | $0.01 / image | −58% |
| [MoonshotAI: Kimi K3.1 Pro](https://uberllm.dev/models/moonshotai/kimi-k3.1-pro) | text | $0.10 / $0.50 | $0.04231 / $0.2115 | −58% |
| [Tencent HY3](https://uberllm.dev/models/tencent/hy3) | text | $0.007431 / $0.02972 | $0.003275 / $0.0131 | −56% |
| [LongCat Distilled Text-to-Video](https://uberllm.dev/models/meituan/longcat-distilled-text-to-video) | video | $0.01782 / sec | $0.009 / sec | −49% |
| [GPT-6 Luna](https://uberllm.dev/models/openai/gpt-6-luna) | text | $0.008695 / $0.04348 | $0.004462 / $0.02231 | −49% |
| [Gemini 3.5 Flash Lite](https://uberllm.dev/models/google/gemini-3-5-flash-lite) | text | $0.1677 / $1.40 | $0.087 / $0.725 | −48% |
| [Grok 4.5](https://uberllm.dev/models/x-ai/grok-4.5) | text | $0.01557 / $0.04671 | $0.008322 / $0.02497 | −47% |
| [Claude Opus 5 (Fast)](https://uberllm.dev/models/anthropic/claude-opus-5-fast) | text | $4.00 / $20.00 | $2.50 / $12.49 | −38% |
| [GPT Image 1.5 (Venice)](https://uberllm.dev/models/venice/gpt-image-1.5) | image | $0.208 / image | $0.13 / image | −38% |
| [Hunyuan Image 3.0 (Venice)](https://uberllm.dev/models/venice/hunyuan-image-v3) | image | $0.072 / image | $0.045 / image | −38% |
| [Qwen Image (Venice)](https://uberllm.dev/models/venice/qwen-image) | image | $0.024 / image | $0.015 / image | −38% |
| [Cohere: Command A+](https://uberllm.dev/models/cohere/command-a-plus) | text | $0.258 / $1.29 | $0.18 / $0.90 | −30% |
| [Elorian: Glimpse](https://uberllm.dev/models/elorian/glimpse) | text | $0.516 / $2.58 | $0.36 / $1.80 | −30% |
| [Moondream: Moondream 3 Preview](https://uberllm.dev/models/moondream/moondream3-preview) | text | $0.258 / $2.15 | $0.18 / $1.50 | −30% |
| [Moondream: Moondream 3.1](https://uberllm.dev/models/moondream/moondream3.1-9b-a2b) | text | $0.258 / $2.15 | $0.18 / $1.50 | −30% |
| [Reflection: Beam 1.0 501B A23B](https://uberllm.dev/models/reflection/beam-1.0-501b-a23b) | text | $0.258 / $0.86 | $0.18 / $0.60 | −30% |
| [MiMo-V2.5-Pro](https://uberllm.dev/models/xiaomi/mimo-v2.5-pro) | text | $0.4128 / $1.55 | $0.288 / $1.08 | −30% |
| [DeepSeek: DeepSeek V4 Flash Vision Exp](https://uberllm.dev/models/deepseek/deepseek-v4-flash-vision-exp) | text | $0.3784 / $1.14 | $0.264 / $0.792 | −30% |
| [inclusionAI: Ling 3.1 Flash](https://uberllm.dev/models/inclusionai/ling-3.1-flash) | text | $0.0387 / $0.1161 | $0.027 / $0.081 | −30% |
| [LiquidAI: LFM2.5-24B-A2B](https://uberllm.dev/models/liquid/lfm-2.5-24b-a2b) | text | $0.043 / $0.602 | $0.03 / $0.42 | −30% |
| [Particle AI: Particle-1](https://uberllm.dev/models/particle-ai/particle-1) | text | $0.043 / $0.43 | $0.03 / $0.30 | −30% |
| [Qwen: Qwen3.8 Max Prime](https://uberllm.dev/models/qwen/qwen3.8-max-prime) | text | $3.44 / $10.32 | $2.40 / $7.20 | −30% |
| [Sakana: Fugu Max](https://uberllm.dev/models/sakana/fugu-max) | text | $1.72 / $5.16 | $1.20 / $3.60 | −30% |
| [Sakana: Fugu Ultra v2](https://uberllm.dev/models/sakana/fugu-ultra-v2) | text | $4.30 / $25.80 | $3.00 / $18.00 | −30% |
| [JEV 1.13 (TypeSafe)](https://uberllm.dev/models/typesafe/jev-1.13) | other | $0.03612 / $0 | $0.0252 / $0 | in −30% / out – |
| [JEV 1.14 (TypeSafe)](https://uberllm.dev/models/typesafe/jev-1.14) | other | $0.03612 / $0 | $0.0252 / $0 | in −30% / out – |
| [Pareto 26.9](https://uberllm.dev/models/unbiased/pareto-26.9) | text | $2.15 / $6.45 | $1.50 / $4.50 | −30% |
| [Claude Sonnet 5.5](https://uberllm.dev/models/anthropic/claude-sonnet-5.5) | text | $0.0995 / $0.4975 | $0.07 / $0.35 | −30% |
| [MiMo-V2.6-Pro-UltraSpeed](https://uberllm.dev/models/xiaomi/mimo-v2.6-pro-ultraspeed) | text | $3.61 / $7.22 | $2.61 / $5.22 | −28% |
| [Claude Fable 5.2](https://uberllm.dev/models/anthropic/claude-fable-5.2) | text | $2.71 / $13.55 | $1.96 / $9.82 | −28% |
| [Grok Imagine (Venice)](https://uberllm.dev/models/venice/grok-imagine) | image | $0.02 / image | $0.015 / image | −25% |
| [xAI Speech to Text v1 (Venice)](https://uberllm.dev/models/venice/xai-stt-v1) | transcription | $0.001228 / minute | $0.000944 / minute | −23% |
| [Seedream V4.5 (Venice)](https://uberllm.dev/models/venice/seedream-v4) | image | $0.0325 / image | $0.025 / image | −23% |
| [LongCat Text-to-Video](https://uberllm.dev/models/meituan/longcat-text-to-video) | video | $0.05 / sec | $0.04 / sec | −20% |
| [NVIDIA: Nemotron 3.5 Super VL](https://uberllm.dev/models/nvidia/nemotron-3.5-super-vl) | text | $0.105 / $0.35 | $0.09 / $0.282 | in −14% / out −19% |
| [LTX 2 Full Text-to-Video](https://uberllm.dev/models/lightricks/ltx-2-full-text-to-video) | video | $0.07508 / sec | $0.06183 / sec | −18% |
| [Veo 3 Fast Text-to-Video](https://uberllm.dev/models/google/veo3-fast-text-to-video) | video | $0.1403 / sec | $0.1155 / sec | −18% |
| [Veo 3 Full Text-to-Video](https://uberllm.dev/models/google/veo3-full-text-to-video) | video | $0.374 / sec | $0.308 / sec | −18% |
| [LTX 2 19B Full Text-to-Video](https://uberllm.dev/models/lightricks/ltx-2-19b-full-text-to-video) | video | $0.0748 / sec | $0.0616 / sec | −18% |
| [Runway Gen-4 Aleph](https://uberllm.dev/models/runway/runway-gen4-aleph) | video | $0.425 / video | $0.35 / video | −18% |
| [Wan 2.1 Pro Image-to-Video](https://uberllm.dev/models/wan/wan-2-1-pro-image-to-video) | video | $0.1247 / sec | $0.1027 / sec | −18% |
| [Wan 2.2 A14B Text-to-Video](https://uberllm.dev/models/wan/wan-2-2-a14b-text-to-video) | video | $0.17 / video | $0.14 / video | −18% |
| [LTX 2 Fast Text-to-Video](https://uberllm.dev/models/lightricks/ltx-2-fast-text-to-video) | video | $0.05667 / sec | $0.04667 / sec | −18% |
| [Seedance 2.0 Fast (image-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-fast-image-to-video) | video | $0.059 / sec | $0.049 / sec | −17% |
| [DeepSeek V4.1 Flash 1017](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash-1017) | text | $0.000287 / $0.02392 | $0.000239 / $0.01992 | −17% |
| [MiniMax M3](https://uberllm.dev/models/minimax/minimax-m3) | text | $0.01474 / $0.05895 | $0.01239 / $0.04958 | −16% |
| [Grok Imagine 1.5 Image To Video Private (image-to-video)](https://uberllm.dev/models/x-ai/grok-imagine-1-5-image-to-video-private) | video | $0.0792 / sec | $0.0675 / sec | −15% |
| [Kimi K2](https://uberllm.dev/models/moonshotai/kimi-k2) | text | $0.399 / $1.61 | $0.342 / $1.38 | −14% |
| [Qwen3 30B A3B](https://uberllm.dev/models/qwen/qwen3-30b-a3b) | text | $0.084 / $0.35 | $0.072 / $0.30 | −14% |
| [Z.ai: GLM 5.3 FlashX Legal](https://uberllm.dev/models/z-ai/glm-5.3-flashx-legal) | text | $0.259 / $0.875 | $0.222 / $0.75 | −14% |
| [Fireworks: Ember-1](https://uberllm.dev/models/fireworks/ember-1) | text | $2.10 / $10.49 | $1.80 / $9.00 | −14% |
| [Grok Imagine Pro (Venice)](https://uberllm.dev/models/venice/grok-imagine-pro) | image | $0.04069 / image | $0.035 / image | −14% |
| [Seedance 2.0 (reference-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-reference-to-video) | video | $0.0792 / sec | $0.06864 / sec | −13% |
| [Venice SD35](https://uberllm.dev/models/venice/sd35) | image | $0.008 / image | $0.007 / image | −12% |
| [GPT-OSS 20B](https://uberllm.dev/models/openai/gpt-oss-20b) | text | $0.000018 / $0.000089 | $0.000018 / $0.000078 | in 0% / out −12% |
| [Claude Opus 5.5](https://uberllm.dev/models/anthropic/claude-opus-5.5) | text | $0.1517 / $0.7585 | $0.136 / $0.68 | −10% |
| [fal.ai Wizper (STT)](https://uberllm.dev/models/fal-ai/fal-wizper) | transcription | $0.0048 / minute | $0.004311 / minute | −10% |
| [Qwen 2.5 7B](https://uberllm.dev/models/qwen/e2ee-qwen-2-5-7b-p) | text | $0.02248 / $0.05844 | $0.02498 / $0.06494 | +11% |
| [Mistral: Mistral Large 4](https://uberllm.dev/models/mistralai/mistral-large-4-0) | text | $0.063 / $0.189 | $0.07 / $0.21 | +11% |
| [Wan 2.6 (image-to-video)](https://uberllm.dev/models/wan/wan-2-6-image-to-video) | video | $0.0627 / sec | $0.07 / sec | +12% |
| [Wan 2.7 Pro (image-to-image)](https://uberllm.dev/models/wan/wan-2-7-pro-edit) | image | $0.05358 / image | $0.06 / image | +12% |
| [GPT-5.4 Pro](https://uberllm.dev/models/openai/gpt-5.4-pro) | text | $4.79 / $28.76 | $5.40 / $32.39 | +13% |
| [Claude Haiku 4.5](https://uberllm.dev/models/anthropic/claude-haiku-4.5) | text | $0.0653 / $0.3265 | $0.0745 / $0.3725 | +14% |
| [Meta: Muse Glimmer 30B](https://uberllm.dev/models/meta-llama/muse-glimmer-30b) | text | $0.258 / $1.03 | $0.297 / $1.19 | +15% |
| [Ministral 3 8B](https://uberllm.dev/models/mistralai/ministral-3-8b-instruct) | text | $0.001496 / $0.001496 | $0.001723 / $0.001723 | +15% |
| [Claude Haiku 5.5](https://uberllm.dev/models/anthropic/claude-haiku-5.5) | text | $0.006889 / $0.03445 | $0.008 / $0.04 | +16% |
| [Whisper 1 (Venice, legacy alias)](https://uberllm.dev/models/venice/whisper-1) | transcription | $0.0036 / minute | $0.004311 / minute | +20% |
| [Pixverse V5.6 (image-to-video)](https://uberllm.dev/models/pixverse/pixverse-v5-6-image-to-video) | video | $0.1515 / sec | $0.1818 / sec | +20% |
| [ByteDance Seed: Seed-2.0-Code](https://uberllm.dev/models/bytedance/seed-2.0-code) | text | $0.43 / $2.58 | $0.525 / $3.15 | +22% |
| [Grok Imagine — Edit (Venice)](https://uberllm.dev/models/venice/grok-imagine-edit) | image | $0.01228 / image | $0.015 / image | +22% |
| [Wan 2.7 (image-to-video)](https://uberllm.dev/models/wan/wan-2-7-image-to-video) | video | $0.0627 / sec | $0.077 / sec | +23% |
| [Seedance 2.0 (image-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-image-to-video) | video | $0.05016 / sec | $0.0616 / sec | +23% |
| [Happyhorse 1.0 (image-to-video)](https://uberllm.dev/models/happyhorse/happyhorse-1-0-image-to-video) | video | $0.08738 / sec | $0.1073 / sec | +23% |
| [Tencent: Hy4 preview](https://uberllm.dev/models/tencent/hy4-preview) | text | $0.05411 / $0.1623 | $0.06746 / $0.2023 | +25% |
| [Wan 2.7 Text-to-Video](https://uberllm.dev/models/wan/wan-2-7-text-to-video) | video | $0.0627 / sec | $0.08 / sec | +28% |
| [Happyhorse 1.1 (image-to-video)](https://uberllm.dev/models/happyhorse/happyhorse-1-1-image-to-video) | video | $0.08738 / sec | $0.1125 / sec | +29% |
| [Happyhorse 1.1 (reference-to-video)](https://uberllm.dev/models/happyhorse/happyhorse-1-1-reference-to-video) | video | $0.08738 / sec | $0.1125 / sec | +29% |
| [Chroma (Venice)](https://uberllm.dev/models/venice/chroma) | image | $0.006 / image | $0.008 / image | +33% |
| [Gemma 3 4B IT](https://uberllm.dev/models/google/gemma-3-4b-it) | text | $0.000346 / $0.000693 | $0.000463 / $0.000579 | in +34% / out −16% |
| [Kimi K3](https://uberllm.dev/models/moonshotai/kimi-k3) | text | $0.001727 / $0.07805 | $0.001286 / $0.1072 | in −26% / out +37% |
| [LTX 2 v2.3 Full Text-to-Video](https://uberllm.dev/models/lightricks/ltx-2-v2-3-full-text-to-video) | video | $0.05035 / sec | $0.07067 / sec | +40% |
| [Kling O3 4K Text-to-Video](https://uberllm.dev/models/kling/kling-o3-4k-text-to-video) | video | $0.2641 / sec | $0.3707 / sec | +40% |
| [Ltx 2 V2.3 Full (image-to-video)](https://uberllm.dev/models/lightricks/ltx-2-v2-3-full-image-to-video) | video | $0.05033 / sec | $0.07064 / sec | +40% |
| [Kling O3.4k (image-to-video)](https://uberllm.dev/models/kling/kling-o3-4k-image-to-video) | video | $0.2641 / sec | $0.3706 / sec | +40% |
| [Kling O3.4k (reference-to-video)](https://uberllm.dev/models/kling/kling-o3-4k-reference-to-video) | video | $0.2641 / sec | $0.3706 / sec | +40% |
| [Kling V3 Standard (image-to-video)](https://uberllm.dev/models/kling/kling-v3-standard-image-to-video) | video | $0.0798 / sec | $0.112 / sec | +40% |
| [LTX 2 v2.3 Fast Text-to-Video](https://uberllm.dev/models/lightricks/ltx-2-v2-3-fast-text-to-video) | video | $0.038 / sec | $0.05333 / sec | +40% |
| [Kling V3.4k (reference-to-video)](https://uberllm.dev/models/kling/kling-v3-4k-reference-to-video) | video | $0.2641 / sec | $0.3707 / sec | +40% |
| [Kling V3 Pro (image-to-video)](https://uberllm.dev/models/kling/kling-v3-pro-image-to-video) | video | $0.1045 / sec | $0.1467 / sec | +40% |
| [Kling V3 Turbo Pro (image-to-video)](https://uberllm.dev/models/kling/kling-v3-turbo-pro-image-to-video) | video | $0.08738 / sec | $0.1227 / sec | +40% |
| [Meta: Muse Ember](https://uberllm.dev/models/meta-llama/muse-ember) | text | $0.07 / $0.35 | $0.099 / $0.495 | +41% |
| [Grok 4.6](https://uberllm.dev/models/x-ai/grok-4.6) | text | $0.1217 / $0.3652 | $0.1898 / $0.5695 | +56% |
| [Seedance 2.0 Fast (reference-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-fast-reference-to-video) | video | $0.0399 / sec | $0.063 / sec | +58% |
| [Happyhorse 1.0 (reference-to-video)](https://uberllm.dev/models/happyhorse/happyhorse-1-0-reference-to-video) | video | $0.08738 / sec | $0.138 / sec | +58% |
| [Kling V3 4K Text-to-Video](https://uberllm.dev/models/kling/kling-v3-4k-text-to-video) | video | $0.2641 / sec | $0.417 / sec | +58% |
| [Ltx 2 V2.3 Fast (image-to-video)](https://uberllm.dev/models/lightricks/ltx-2-v2-3-fast-image-to-video) | video | $0.03802 / sec | $0.06003 / sec | +58% |
| [Kling V3 Pro Text-to-Video](https://uberllm.dev/models/kling/kling-v3-pro-text-to-video) | video | $0.1045 / sec | $0.165 / sec | +58% |
| [Kling V3 Standard Text-to-Video](https://uberllm.dev/models/kling/kling-v3-standard-text-to-video) | video | $0.07866 / sec | $0.1242 / sec | +58% |
| [GPT-5.2](https://uberllm.dev/models/openai/gpt-5.2) | text | $0.2151 / $1.72 | $0.3432 / $2.75 | +60% |
| [Kokoro Text to Speech (Venice)](https://uberllm.dev/models/venice/kokoro-tts) | speech | $0.00175 / 1K chars | $0.0028 / 1K chars | +60% |
| [Firered Image (image-to-image)](https://uberllm.dev/models/xiaohongshu/firered-image-edit) | image | $0.0198 / image | $0.032 / image | +62% |
| [GLM 5.3 Flash](https://uberllm.dev/models/z-ai/glm-5.3-flash) | text | $0.001525 / $0.002996 | $0.0015 / $0.005 | in −2% / out +67% |
| [DeepSeek V3.2](https://uberllm.dev/models/deepseek/deepseek-v3.2) | text | $0.0026 / $0.0038 | $0.003524 / $0.00653 | in +36% / out +72% |
| [NVIDIA Nemotron Nano 9B v2](https://uberllm.dev/models/nvidia/nemotron-nano-9b-v2) | text | $0.000599 / $0.002294 | $0.001117 / $0.004281 | in +86% / out +87% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | text | $0.000955 / $0.001911 | $0.001784 / $0.003568 | +87% |
| [Claude Sonnet 4.5](https://uberllm.dev/models/anthropic/claude-sonnet-4.5) | text | $0.5886 / $2.94 | $1.18 / $5.92 | +101% |
| [Qwen3 Coder Next](https://uberllm.dev/models/qwen/qwen3-coder-next) | text | $0.001185 / $0.0079 | $0.0024 / $0.016 | +103% |
| [NVIDIA Nemotron 3 Super 120B](https://uberllm.dev/models/nvidia/nemotron-3-super-120b) | text | $0.000748 / $0.00399 | $0.001457 / $0.008197 | in +95% / out +105% |
| [Claude Opus 4.7](https://uberllm.dev/models/anthropic/claude-opus-4.7) | text | $0.161 / $0.805 | $0.3675 / $1.84 | +128% |
| [Tencent: Hy4](https://uberllm.dev/models/tencent/hy4) | text | $0.04375 / $0.1312 | $0.1021 / $0.306 | +133% |
| [Whisper Large V3 (Venice)](https://uberllm.dev/models/venice/whisper-large-v3) | transcription | $0.0015 / minute | $0.004311 / minute | +187% |
| [GPT-5.3 Codex](https://uberllm.dev/models/openai/gpt-5.3-codex) | text | $0.1405 / $1.12 | $0.4051 / $3.24 | +188% |
| [Mistral Large 3](https://uberllm.dev/models/mistralai/mistral-large-3) | text | $0.005 / $0.015 | $0.02475 / $0.07425 | +395% |
| [GPT-5.5](https://uberllm.dev/models/openai/gpt-5.5) | text | $0.2445 / $1.47 | $1.31 / $7.84 | +435% |
| [MiMo-V2.5](https://uberllm.dev/models/xiaomi/mimo-v2-5) | text | $0.07 / $0.14 | $0.24 / $1.20 | in +243% / out +757% |
| [DeepSeek V4 Flash](https://uberllm.dev/models/deepseek/deepseek-v4-flash) | text | $0.001044 / $0.002088 | $0.0091 / $0.0182 | +772% |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | text | $0.000179 / $0.001374 | $0.002491 / $0.0277 | in +1292% / out +1916% |
| [Ministral 3B](https://uberllm.dev/models/mistralai/ministral-3-3b-instruct) | text | $0.000997 / $0.000997 | $0.025 / $0.025 | +2408% |
| [Gemma 3 27B](https://uberllm.dev/models/google/gemma-3-27b-it) | text | $0.000792 / $0.00198 | $0.02 / $0.05 | +2425% |
| [Qwen3 VL 235B A22B](https://uberllm.dev/models/qwen/qwen3-vl-235b-a22b-instruct) | text | $0.002074 / $0.01876 | $0.0525 / $0.475 | in +2431% / out +2432% |
| [GLM 4.7 Flash](https://uberllm.dev/models/z-ai/glm-4.7-flash) | text | $0.000312 / $0.002065 | $0.01815 / $0.12 | in +5717% / out +5711% |

</details>


## 2026-11-11 (vs 2026-11-10)

**Official list price changes (13)**

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [GLM 5.3 Flash](https://uberllm.dev/models/z-ai/glm-5.3-flash) | text | $0.15 / $0.50 | $0.0399 / $0.0784 | in −73% / out −84% |
| [MiniMax M3.1 Flash](https://uberllm.dev/models/minimax/minimax-m3-1-flash) | text | $0.15 / $0.60 | $0.075 / $0.30 | −50% |
| [Tencent HY3](https://uberllm.dev/models/tencent/hy3) | text | $0.132 / $0.528 | $0.0825 / $0.33 | −38% |
| [Tencent: Hy4 preview](https://uberllm.dev/models/tencent/hy4-preview) | text | $0.834 / $2.50 | $0.7506 / $2.25 | −10% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | text | – / – | $1.32 / $3.96 |  |
| [DeepSeek V4 Pro 0813](https://uberllm.dev/models/deepseek/deepseek-v4-pro-0813) | text | – / – | $1.32 / $3.96 |  |
| [DeepSeek V4 Pro (Morpheus Web)](https://uberllm.dev/models/deepseek/deepseek-v4-pro:web) | text | – / – | $1.32 / $3.96 |  |
| [DeepSeek V4.1 Flash](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash) | text | – / – | $0.30 / $1.20 |  |
| [DeepSeek V4.1 Flash 1017](https://uberllm.dev/models/deepseek/deepseek-v4.1-flash-1017) | text | – / – | $0.30 / $1.20 |  |
| [Kimi K3](https://uberllm.dev/models/moonshotai/kimi-k3) | text | – / – | $3.00 / $15.00 |  |
| [GLM-5.2](https://uberllm.dev/models/z-ai/glm-5.2) | text | – / – | $1.40 / $4.40 |  |
| [GLM 5.2 (Morpheus Web)](https://uberllm.dev/models/z-ai/glm-5.2:web) | text | – / – | $1.40 / $4.40 |  |
| [GLM 5.3](https://uberllm.dev/models/z-ai/glm-5.3) | text | – / – | $1.40 / $4.40 |  |

**New models (2)**

| Model | Category | Official price | UberLLM price |
|---|---|---|---|
| [Google: Gemini 4 Carbon](https://uberllm.dev/models/google/gemini-4-carbon) | text | $2.00 / $10.00 | $1.00 / $5.00 |
| [Inception: Mercury 2.5](https://uberllm.dev/models/inception/mercury-2.5) | text | – | $0.028 / $0.105 |

**No longer listed (15)**: `meta-llama/hermes-3-llama-3.1-405b:web`, `meta-llama/llama-3.2-3b-instruct:web`, `meta-llama/llama-3.3-70b-instruct:web`, `minimax/minimax-m2.5:web`, `mistralai/mistral-small-3.2-24b-instruct:web`, `moonshotai/kimi-k2.5:web`, `moonshotai/kimi-k2.6:web`, `moonshotai/kimi-k2.7-code:web`, `openai/gpt-oss-120b:web`, `qwen/qwen3-235b-a22b-2507:web`, `qwen/qwen3-next-80b-a3b-instruct:web`, `z-ai/glm-5.1-non-thinking`, `z-ai/glm-5.1-non-thinking:web`, `z-ai/glm-5.1:web`, `z-ai/glm-5:web`

<details><summary>UberLLM price moves of 10% or more (147)</summary>

| Model | Category | Before | After | Change |
|---|---|---|---|---|
| [Aion 2.0](https://uberllm.dev/models/aion-labs/aion-2.0) | text | $0.64 / $1.28 | $0.008 / $0.016 | −99% |
| [Aion 3.5 Mini](https://uberllm.dev/models/aion-labs/aion-3-5-mini) | text | $0.525 / $1.05 | $0.00875 / $0.0175 | −98% |
| [Aion 3.0](https://uberllm.dev/models/aion-labs/aion-3-0) | text | $1.78 / $3.56 | $0.03 / $0.06 | −98% |
| [Qwen3 32B](https://uberllm.dev/models/qwen/qwen3-32b) | text | $0.0104 / $0.0364 | $0.00079 / $0.002765 | −92% |
| [Ministral 14B 3.0](https://uberllm.dev/models/mistralai/ministral-3-14b-instruct) | text | $0.026 / $0.026 | $0.001996 / $0.001996 | −92% |
| [GPT OSS Safeguard 120B](https://uberllm.dev/models/openai/gpt-oss-safeguard-120b) | text | $0.0195 / $0.078 | $0.001497 / $0.005988 | −92% |
| [DeepSeek V4 Flash](https://uberllm.dev/models/deepseek/deepseek-v4-flash) | text | $0.009091 / $0.01818 | $0.001044 / $0.002088 | −89% |
| [DeepSeek V4 Flash 0731](https://uberllm.dev/models/deepseek/deepseek-v4-flash-0731) | text | $0.00212 / $0.0127 | $0.000901 / $0.001802 | in −57% / out −86% |
| [MiniMax M2.7 Highspeed](https://uberllm.dev/models/minimax/minimax-m2.7-highspeed) | text | $0.174 / $0.696 | $0.03 / $0.12 | −83% |
| [MiniMax M2.5](https://uberllm.dev/models/minimax/minimax-m2.5) | text | $0.0135 / $0.0475 | $0.002621 / $0.009222 | −81% |
| [Aion 3.0 Mini](https://uberllm.dev/models/aion-labs/aion-3-0-mini) | text | $0.035 / $0.07 | $0.007 / $0.014 | −80% |
| [Mistral Large 3](https://uberllm.dev/models/mistralai/mistral-large-3) | text | $0.02475 / $0.07425 | $0.005 / $0.015 | −80% |
| [GPT-5.3 Codex](https://uberllm.dev/models/openai/gpt-5.3-codex) | text | $0.3871 / $3.10 | $0.1405 / $1.12 | −64% |
| [Grok 4.7](https://uberllm.dev/models/x-ai/grok-4.7) | text | $0.03309 / $0.09928 | $0.01442 / $0.04326 | −56% |
| [Grok 4.5](https://uberllm.dev/models/x-ai/grok-4.5) | text | $0.03564 / $0.1069 | $0.01557 / $0.04671 | −56% |
| [Qwen 3 235B A22B Instruct 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-2507) | text | $0.0014 / $0.0075 | $0.000633 / $0.003389 | −55% |
| [Whisper Large V3 (Venice)](https://uberllm.dev/models/venice/whisper-large-v3) | transcription | $0.0033 / minute | $0.0015 / minute | −55% |
| [Gemini 3.1 Flash Lite](https://uberllm.dev/models/google/gemini-3.1-flash-lite) | text | $0.00242 / $0.01452 | $0.001213 / $0.007275 | −50% |
| [Meta: Muse Spark 1.1](https://uberllm.dev/models/meta-llama/muse-spark-1.1) | text | $0.7015 / $2.39 | $0.375 / $1.27 | −47% |
| [Gemini 3.6 Flash](https://uberllm.dev/models/google/gemini-3-6-flash) | text | $0.3937 / $1.97 | $0.2175 / $1.09 | −45% |
| [DeepSeek V4 Pro](https://uberllm.dev/models/deepseek/deepseek-v4-pro) | text | $0.001626 / $0.003252 | $0.000955 / $0.001911 | −41% |
| [Gemini 2.5 Flash](https://uberllm.dev/models/google/gemini-2.5-flash) | text | $0.0024 / $0.02 | $0.0015 / $0.0125 | in −37% / out −38% |
| [Claude Opus 4.7 Fast](https://uberllm.dev/models/anthropic/claude-opus-4.7-fast) | text | $27.00 / $135.00 | $18.00 / $90.00 | −33% |
| [Meta: Muse Spark 1.3 Contributor](https://uberllm.dev/models/meta-llama/muse-spark-1.3-contributor) | text | $0.03 / $0.06 | $0.02 / $0.04 | −33% |
| [Qwen 3 235B A22B Thinking 2507](https://uberllm.dev/models/qwen/qwen3-235b-a22b-thinking-2507) | text | $0.075 / $0.075 | $0.05 / $0.05 | −33% |
| [Claude Opus 4.7](https://uberllm.dev/models/anthropic/claude-opus-4.7) | text | $0.2268 / $1.13 | $0.161 / $0.805 | −29% |
| [Claude Sonnet 5.5](https://uberllm.dev/models/anthropic/claude-sonnet-5.5) | text | $0.139 / $0.6951 | $0.0995 / $0.4975 | −28% |
| [Magistral Small 2509](https://uberllm.dev/models/mistralai/magistral-small-2509) | text | $0.00693 / $0.02079 | $0.00499 / $0.01497 | −28% |
| [GLM 5.3 Flash](https://uberllm.dev/models/z-ai/glm-5.3-flash) | text | $0.001245 / $0.00415 | $0.001525 / $0.002996 | in +22% / out −28% |
| [GPT-5.6 Terra Pro](https://uberllm.dev/models/openai/gpt-5.6-terra-pro) | text | $1.11 / $6.65 | $0.80 / $4.80 | −28% |
| [Gemma 3 4B IT](https://uberllm.dev/models/google/gemma-3-4b-it) | text | $0.000463 / $0.000579 | $0.000346 / $0.000693 | in −25% / out +20% |
| [GPT-5.6 Luna Pro](https://uberllm.dev/models/openai/gpt-5.6-luna-pro) | text | $0.1034 / $0.6202 | $0.08 / $0.48 | −23% |
| [Tencent HY3](https://uberllm.dev/models/tencent/hy3) | text | $0.009441 / $0.03776 | $0.007431 / $0.02972 | −21% |
| [MiniMax M3 Preview](https://uberllm.dev/models/minimax/minimax-m3-preview) | text | $0.1499 / $0.5998 | $0.12 / $0.48 | −20% |
| [Tencent: Hy4 preview](https://uberllm.dev/models/tencent/hy4-preview) | text | $0.0676 / $0.2027 | $0.05411 / $0.1623 | −20% |
| [Grok 4.6](https://uberllm.dev/models/x-ai/grok-4.6) | text | $0.1517 / $0.455 | $0.1217 / $0.3652 | −20% |
| [Gemma 4 31B](https://uberllm.dev/models/google/gemma-4-31b) | text | $0.0009 / $0.0034 | $0.000912 / $0.002736 | in +1% / out −20% |
| [Claude Opus 5 (Fast)](https://uberllm.dev/models/anthropic/claude-opus-5-fast) | text | $4.96 / $24.80 | $4.00 / $20.00 | −19% |
| [Fireworks: Ember-1](https://uberllm.dev/models/fireworks/ember-1) | text | $2.57 / $12.86 | $2.10 / $10.49 | −18% |
| [Sakana: Fugu Max](https://uberllm.dev/models/sakana/fugu-max) | text | $2.10 / $6.30 | $1.72 / $5.16 | −18% |
| [MiniMax M3.1 Flash](https://uberllm.dev/models/minimax/minimax-m3-1-flash) | text | $0.008951 / $0.0358 | $0.007443 / $0.02977 | −17% |
| [Qwen 3.5 9B](https://uberllm.dev/models/qwen/qwen3.5-9b) | text | $0.03 / $0.09 | $0.025 / $0.075 | −17% |
| [Kokoro Text to Speech (Venice)](https://uberllm.dev/models/venice/kokoro-tts) | speech | $0.0021 / 1K chars | $0.00175 / 1K chars | −17% |
| [GPT-5.6 Luna](https://uberllm.dev/models/openai/gpt-5.6-luna) | text | $0.00497 / $0.02982 | $0.004143 / $0.02486 | −17% |
| [Grok Imagine — Edit (Venice)](https://uberllm.dev/models/venice/grok-imagine-edit) | image | $0.0147 / image | $0.01228 / image | −16% |
| [Kimi K2.7 Code](https://uberllm.dev/models/moonshotai/kimi-k2.7-code) | text | $0.01151 / $0.06713 | $0.009788 / $0.0571 | −15% |
| [Claude Opus 4.8](https://uberllm.dev/models/anthropic/claude-opus-4.8) | text | $0.337 / $1.69 | $0.29 / $1.45 | −14% |
| [ByteDance Seed: Seed-2.0-Code](https://uberllm.dev/models/bytedance/seed-2.0-code) | text | $0.495 / $2.97 | $0.43 / $2.58 | −13% |
| [Elorian: Glimpse](https://uberllm.dev/models/elorian/glimpse) | text | $0.594 / $2.97 | $0.516 / $2.58 | −13% |
| [inclusionAI: Ling 3.1 Flash](https://uberllm.dev/models/inclusionai/ling-3.1-flash) | text | $0.04455 / $0.1336 | $0.0387 / $0.1161 | −13% |
| [LiquidAI: LFM2.5-24B-A2B](https://uberllm.dev/models/liquid/lfm-2.5-24b-a2b) | text | $0.0495 / $0.693 | $0.043 / $0.602 | −13% |
| [Qwen: Qwen3.8 Max Prime](https://uberllm.dev/models/qwen/qwen3.8-max-prime) | text | $3.96 / $11.88 | $3.44 / $10.32 | −13% |
| [Sakana: Fugu Ultra v2](https://uberllm.dev/models/sakana/fugu-ultra-v2) | text | $4.95 / $29.70 | $4.30 / $25.80 | −13% |
| [Pareto 26.9](https://uberllm.dev/models/unbiased/pareto-26.9) | text | $2.48 / $7.42 | $2.15 / $6.45 | −13% |
| [Meta: Muse Glimmer 30B](https://uberllm.dev/models/meta-llama/muse-glimmer-30b) | text | $0.297 / $1.19 | $0.258 / $1.03 | −13% |
| [Reflection: Beam 1.0 501B A23B](https://uberllm.dev/models/reflection/beam-1.0-501b-a23b) | text | $0.297 / $0.99 | $0.258 / $0.86 | −13% |
| [JEV 1.14 (TypeSafe)](https://uberllm.dev/models/typesafe/jev-1.14) | other | $0.04158 / $0 | $0.03612 / $0 | in −13% / out – |
| [Qwen3.8 Flash](https://uberllm.dev/models/qwen/qwen3.8-flash) | text | $0.001692 / $0.005301 | $0.00147 / $0.004606 | −13% |
| [Meta: Muse Spark Open](https://uberllm.dev/models/meta-llama/muse-spark-open) | text | $0.6966 / $2.37 | $0.6162 / $2.10 | −12% |
| [Claude Opus 5.5](https://uberllm.dev/models/anthropic/claude-opus-5.5) | text | $0.1703 / $0.8515 | $0.1517 / $0.7585 | −11% |
| [Claude Haiku 4.5](https://uberllm.dev/models/anthropic/claude-haiku-4.5) | text | $0.0592 / $0.296 | $0.0653 / $0.3265 | +10% |
| [GPT-5.4 Pro](https://uberllm.dev/models/openai/gpt-5.4-pro) | text | $4.35 / $26.07 | $4.79 / $28.76 | +10% |
| [Grok Imagine (Venice)](https://uberllm.dev/models/venice/grok-imagine) | image | $0.018 / image | $0.02 / image | +11% |
| [Claude Opus 4.5](https://uberllm.dev/models/anthropic/claude-opus-4.5) | text | $0.3549 / $1.77 | $0.40 / $2.00 | +13% |
| [GPT-6 Luna Decisions (OpenAI)](https://uberllm.dev/models/openai/gpt-6-luna-decisions) | other | $0.06093 / $0 | $0.06878 / $0 | in +13% / out – |
| [GPT Image 1.5 — Edit (Venice)](https://uberllm.dev/models/venice/gpt-image-1-5-edit) | image | $0.216 / image | $0.248 / image | +15% |
| [Wan 2.7 (Venice)](https://uberllm.dev/models/venice/wan-2.7) | image | $0.02063 / image | $0.024 / image | +16% |
| [Grok Imagine Image To Video Private (image-to-video)](https://uberllm.dev/models/x-ai/grok-imagine-image-to-video-private) | video | $0.036 / sec | $0.042 / sec | +17% |
| [Grok Imagine Reference To Video Private (reference-to-video)](https://uberllm.dev/models/x-ai/grok-imagine-reference-to-video-private) | video | $0.036 / sec | $0.042 / sec | +17% |
| [Chroma (Venice)](https://uberllm.dev/models/venice/chroma) | image | $0.005 / image | $0.006 / image | +20% |
| [Tencent: Hy4](https://uberllm.dev/models/tencent/hy4) | text | $0.03642 / $0.1092 | $0.04375 / $0.1312 | +20% |
| [Flux 2 Max (Venice)](https://uberllm.dev/models/venice/flux-2-max) | image | $0.0522 / image | $0.063 / image | +21% |
| [Wan 2.7 (reference-to-video)](https://uberllm.dev/models/wan/wan-2-7-reference-to-video) | video | $0.066 / sec | $0.08 / sec | +21% |
| [Seedance 2.0 Mini (reference-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-mini-reference-to-video) | video | $0.0264 / sec | $0.033 / sec | +25% |
| [Kling V3 Turbo Standard (image-to-video)](https://uberllm.dev/models/kling/kling-v3-turbo-standard-image-to-video) | video | $0.07398 / sec | $0.09248 / sec | +25% |
| [Pixverse V5.6 (image-to-video)](https://uberllm.dev/models/pixverse/pixverse-v5-6-image-to-video) | video | $0.1212 / sec | $0.1515 / sec | +25% |
| [xAI v1 TTS](https://uberllm.dev/models/x-ai/tts-xai-v1) | speech | $0.01125 / 1K chars | $0.01406 / 1K chars | +25% |
| [Meta: Muse Ember](https://uberllm.dev/models/meta-llama/muse-ember) | text | $0.055 / $0.275 | $0.07 / $0.35 | +27% |
| [Grok Imagine Pro (Venice)](https://uberllm.dev/models/venice/grok-imagine-pro) | image | $0.03169 / image | $0.04069 / image | +28% |
| [PixVerse C1 Text-to-Video (Venice)](https://uberllm.dev/models/venice/pixverse-c1-t2v) | video | $0.0428 / sec | $0.05707 / sec | +33% |
| [fal.ai Wizper (STT)](https://uberllm.dev/models/fal-ai/fal-wizper) | transcription | $0.0036 / minute | $0.0048 / minute | +33% |
| [Gemini Omni Flash (reference-to-video)](https://uberllm.dev/models/google/gemini-omni-flash-reference-to-video) | video | $0.0855 / sec | $0.114 / sec | +33% |
| [Gemini 3.1 Flash TTS](https://uberllm.dev/models/google/tts-gemini-3-1-flash) | speech | $0.1125 / 1K chars | $0.15 / 1K chars | +33% |
| [Luma Uni 1 Max (image-to-image)](https://uberllm.dev/models/luma/luma-uni-1-max-edit) | image | $0.078 / image | $0.104 / image | +33% |
| [Longcat Distilled (image-to-video)](https://uberllm.dev/models/meituan/longcat-distilled-image-to-video) | video | $0.0108 / sec | $0.0144 / sec | +33% |
| [Flux 1.1 (Venice, legacy)](https://uberllm.dev/models/venice/flux-1.1) | image | $0.006 / image | $0.008 / image | +33% |
| [GPT Image 1.5 (Venice)](https://uberllm.dev/models/venice/gpt-image-1.5) | image | $0.156 / image | $0.208 / image | +33% |
| [Hunyuan Image 3.0 (Venice)](https://uberllm.dev/models/venice/hunyuan-image-v3) | image | $0.054 / image | $0.072 / image | +33% |
| [MiniMax Music 2.6 (Venice)](https://uberllm.dev/models/venice/minimax-music-v26) | music | $0.108 / track | $0.144 / track | +33% |
| [Venice SD35](https://uberllm.dev/models/venice/sd35) | image | $0.006 / image | $0.008 / image | +33% |
| [Stable Diffusion XL (Venice, legacy)](https://uberllm.dev/models/venice/sdxl) | image | $0.006 / image | $0.008 / image | +33% |
| [Luma Uni 1 (image-to-image)](https://uberllm.dev/models/luma/luma-uni-1-edit) | image | $0.036 / image | $0.048 / image | +33% |
| [Longcat (image-to-video)](https://uberllm.dev/models/meituan/longcat-image-to-video) | video | $0.03 / sec | $0.04 / sec | +33% |
| [MiniMax Speech 02 HD TTS](https://uberllm.dev/models/minimax/tts-minimax-speech-02-hd) | speech | $0.075 / 1K chars | $0.10 / 1K chars | +33% |
| [Ovi Image-to-Video](https://uberllm.dev/models/ovi/ovi-image-to-video) | video | $0.0264 / sec | $0.0352 / sec | +33% |
| [Qwen Image 2 Pro (image-to-image)](https://uberllm.dev/models/qwen/qwen-image-2-pro-edit) | image | $0.06 / image | $0.08 / image | +33% |
| [Chatterbox HD TTS](https://uberllm.dev/models/resemble-ai/tts-chatterbox-hd) | speech | $0.03 / 1K chars | $0.04 / 1K chars | +33% |
| [ElevenLabs Turbo v2.5 TTS (Venice)](https://uberllm.dev/models/venice/elevenlabs-tts-turbo-v2-5) | speech | $0.0375 / 1K chars | $0.05 / 1K chars | +33% |
| [Flux 1.1 Pro (Venice, legacy)](https://uberllm.dev/models/venice/flux-1.1-pro) | image | $0.018 / image | $0.024 / image | +33% |
| [Qwen Image 2 Pro (Venice)](https://uberllm.dev/models/venice/qwen-image-2-pro) | image | $0.06 / image | $0.08 / image | +33% |
| [Venice TTS 1 (legacy alias)](https://uberllm.dev/models/venice/tts-1) | speech | $0.0021 / 1K chars | $0.0028 / 1K chars | +33% |
| [GPT-5.2](https://uberllm.dev/models/openai/gpt-5.2) | text | $0.1593 / $1.27 | $0.2151 / $1.72 | +35% |
| [Seedance 2.0 Fast (image-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-fast-image-to-video) | video | $0.042 / sec | $0.059 / sec | +40% |
| [Stable Audio 2.5 (Venice)](https://uberllm.dev/models/venice/stable-audio-25) | music | $0.108 / track | $0.152 / track | +41% |
| [Orpheus TTS](https://uberllm.dev/models/canopy-labs/tts-orpheus) | speech | $0.03438 / 1K chars | $0.05 / 1K chars | +45% |
| [Inworld 1.5 Max TTS](https://uberllm.dev/models/inworld/tts-inworld-1-5-max) | speech | $0.006875 / 1K chars | $0.01 / 1K chars | +45% |
| [Qwen3 1.7B TTS](https://uberllm.dev/models/qwen/tts-qwen3-1-7b) | speech | $0.06187 / 1K chars | $0.09 / 1K chars | +45% |
| [ElevenLabs Sound Effects v2 (Venice)](https://uberllm.dev/models/venice/elevenlabs-sound-effects-v2) | music | $0.011 / track | $0.016 / track | +45% |
| [Qwen Image (Venice)](https://uberllm.dev/models/venice/qwen-image) | image | $0.0165 / image | $0.024 / image | +45% |
| [Grok Imagine 1.5 Image To Video Private (image-to-video)](https://uberllm.dev/models/x-ai/grok-imagine-1-5-image-to-video-private) | video | $0.054 / sec | $0.0792 / sec | +47% |
| [Seedance 2.0 (reference-to-video)](https://uberllm.dev/models/bytedance/seedance-2-0-reference-to-video) | video | $0.0528 / sec | $0.0792 / sec | +50% |
| [ElevenLabs Scribe v2 (STT)](https://uberllm.dev/models/elevenlabs/elevenlabs-scribe-v2) | transcription | $0.00501 / minute | $0.008016 / minute | +60% |
| [Veo 3.1 Fast Text-to-Video](https://uberllm.dev/models/google/veo3-1-fast-text-to-video) | video | $0.099 / sec | $0.1633 / sec | +65% |
| [LongCat Distilled Text-to-Video](https://uberllm.dev/models/meituan/longcat-distilled-text-to-video) | video | $0.0108 / sec | $0.01782 / sec | +65% |
| [Vidu Q3 Text-to-Video](https://uberllm.dev/models/vidu/vidu-q3-text-to-video) | video | $0.116 / sec | $0.1933 / sec | +67% |
| [Veo3.1 Full (image-to-video)](https://uberllm.dev/models/google/veo3-1-full-image-to-video) | video | $0.264 / sec | $0.44 / sec | +67% |
| [Veo 3.1 Full Text-to-Video](https://uberllm.dev/models/google/veo3-1-full-text-to-video) | video | $0.264 / sec | $0.44 / sec | +67% |
| [Pixverse C1 (image-to-video)](https://uberllm.dev/models/pixverse/pixverse-c1-image-to-video) | video | $0.02598 / sec | $0.0433 / sec | +67% |
| [Pixverse C1 Transition (transition)](https://uberllm.dev/models/pixverse/pixverse-c1-transition) | video | $0.02598 / sec | $0.0433 / sec | +67% |
| [Veo3.1 Fast (image-to-video)](https://uberllm.dev/models/google/veo3-1-fast-image-to-video) | video | $0.099 / sec | $0.165 / sec | +67% |
| [LongCat Text-to-Video](https://uberllm.dev/models/meituan/longcat-text-to-video) | video | $0.03 / sec | $0.05 / sec | +67% |
| [PixVerse V5.6 Text-to-Video](https://uberllm.dev/models/pixverse/pixverse-v5-6-text-to-video) | video | $0.1368 / sec | $0.228 / sec | +67% |
| [Pixverse V5.6 Transition (transition)](https://uberllm.dev/models/pixverse/pixverse-v5-6-transition) | video | $0.1212 / sec | $0.202 / sec | +67% |
| [Runway Gen-4.5](https://uberllm.dev/models/runway/runway-gen4-5) | video | $0.096 / sec | $0.16 / sec | +67% |
| [Venice Music Gen (legacy alias)](https://uberllm.dev/models/venice/music-gen) | music | $0.018 / track | $0.03 / track | +67% |
| [Venice Video Gen (legacy alias)](https://uberllm.dev/models/venice/video-gen) | video | $0.096 / sec | $0.16 / sec | +67% |
| [Wan 2.5 Preview (image-to-video)](https://uberllm.dev/models/wan/wan-2-5-preview-image-to-video) | video | $0.0336 / sec | $0.056 / sec | +67% |
| [Qwen3 0.6B TTS](https://uberllm.dev/models/qwen/tts-qwen3-0-6b) | speech | $0.03938 / 1K chars | $0.07 / 1K chars | +78% |
| [ElevenLabs TTS Multilingual v2 (Venice audio)](https://uberllm.dev/models/venice/elevenlabs-tts-multilingual-v2) | music | $0.054 / track | $0.096 / track | +78% |
| [ElevenLabs TTS v3 (Venice audio)](https://uberllm.dev/models/venice/elevenlabs-tts-v3) | music | $0.054 / track | $0.096 / track | +78% |
| [MiniMax Music 2.0 (Venice)](https://uberllm.dev/models/venice/minimax-music-v2) | music | $0.018 / track | $0.032 / track | +78% |
| [MMAudio V2 Text-to-Audio (Venice)](https://uberllm.dev/models/venice/mmaudio-v2-text-to-audio) | music | $0.0045 / track | $0.008 / track | +78% |
| [Pixverse C1 (reference-to-video)](https://uberllm.dev/models/pixverse/pixverse-c1-reference-to-video) | video | $0.02381 / sec | $0.0433 / sec | +82% |
| [Vidu Q3 (image-to-video)](https://uberllm.dev/models/vidu/vidu-q3-image-to-video) | video | $0.0495 / sec | $0.09 / sec | +82% |
| [Runway Gen-4 Turbo](https://uberllm.dev/models/runway/runway-gen4-turbo) | video | $0.03712 / sec | $0.0675 / sec | +82% |
| [Runway Gen-4.5 Text-to-Video (Venice)](https://uberllm.dev/models/venice/runway-gen4-5-text) | video | $0.088 / sec | $0.16 / sec | +82% |
| [GPT-5.5](https://uberllm.dev/models/openai/gpt-5.5) | text | $0.125 / $0.75 | $0.2445 / $1.47 | +96% |
| [Gemma 4 26B A4B IT](https://uberllm.dev/models/google/gemma-4-26b-a4b-it) | text | $0.00038 / $0.00114 | $0.0008 / $0.001 | in +111% / out −12% |
| [ACE-Step 1.5 (Venice)](https://uberllm.dev/models/venice/ace-step-15) | music | $0.0135 / track | $0.03 / track | +122% |
| [Kimi K2.6](https://uberllm.dev/models/moonshotai/kimi-k2.6) | text | $0.008257 / $0.04332 | $0.01977 / $0.1037 | +139% |
| [GPT-6 Luna](https://uberllm.dev/models/openai/gpt-6-luna) | text | $0.002956 / $0.01478 | $0.008695 / $0.04348 | +194% |
| [Claude Fable 5.2](https://uberllm.dev/models/anthropic/claude-fable-5.2) | text | $0.7152 / $3.58 | $2.71 / $13.55 | +279% |
| [ElevenLabs Music (Venice)](https://uberllm.dev/models/venice/elevenlabs-music) | music | $0.1725 / track | $0.6555 / track | +280% |
| [Gemini 3.8 Flash](https://uberllm.dev/models/google/gemini-3.8-flash) | text | $0.000799 / $0.003995 | $0.003992 / $0.01996 | +400% |
| [GPT OSS Safeguard 20B](https://uberllm.dev/models/openai/gpt-oss-safeguard-20b) | text | $0.000075 / $0.0003 | $0.000525 / $0.0021 | +600% |
| [GPT-5.4](https://uberllm.dev/models/openai/gpt-5.4) | text | $0.0625 / $0.375 | $0.4753 / $2.85 | +660% |
| [Seedream 4.5](https://uberllm.dev/models/bytedance/seedream-4.5) | image | $0.0004 / image | $0.024 / image | +5900% |

</details>


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

