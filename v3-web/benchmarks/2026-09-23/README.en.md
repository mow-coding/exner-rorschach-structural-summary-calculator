# Exner v3 AI model comparison — research record, 2026-09-23

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

We compared GPT-5.6 Terra, GPT-6 Sol, and GPT-6 Luna on the same **synthetic cases** to inform the model choice for Exner v3 coding assistance and interpretation chat. We tested Jev separately as a structured decision model. The results below describe **pre-release research as of 2026-09-23**. v3.0.0 subsequently launched with GPT-6 Luna standard `medium` alone, at US$3.99 monthly or US$42.99 annually. Read the [follow-up evidence and open issues](../2026-09-24/) alongside this record.

## What was compared?

Each GPT model received **260 cases**: 61 Korean, 64 English, 47 Japanese, 44 Spanish, and 44 Portuguese. The set contains 143 coding-assistance and 117 interpretation cases, including 136 ordinary questions, 95 instruction attacks or out-of-scope requests, 19 multi-turn cases, and 10 long-conversation summaries. Each model completed 280 answer checks and 290 API calls including summary calls. The models received the same product instructions, synthetic records, and reference excerpts. All used medium reasoning effort: GPT-5.6 Terra set it explicitly, while GPT-6 Sol and GPT-6 Luna used the API default.

| Generating model | Usage-based calculated cost, 290 calls | Compared with GPT-5.6 Terra | Call latency median / 95th percentile | Original check → archived-answer re-score |
|---|---:|---:|---:|---:|
| GPT-5.6 Terra | US$3.553828 | Baseline | 3.061 s / 10.469 s | 250/280 → 257/280 |
| GPT-6 Sol | US$2.304015 | 35.2% lower | 3.125 s / 6.681 s | 242/280 → 254/280 |
| GPT-6 Luna | US$0.130514 | 96.3% lower | 3.357 s / 11.365 s | 247/280 → 255/280 |

After correcting checks for numeric formatting, negation, refusal wording, and equivalent Na/Bt/Ls rule phrasing, we re-scored the **same 840 archived answers**. Twenty-seven automatic contract failures became passes; that does not establish that all 27 answers are clinically correct. The values left of the arrows are the original scores; those on the right use the revised checker. The language table shows revised scores. No new model calls were made, and these scores are not clinical accuracy rates.

| Re-scored automated checks by language | GPT-5.6 Terra | GPT-6 Sol | GPT-6 Luna |
|---|---:|---:|---:|
| Korean | 57/64 | 57/64 | 57/64 |
| English | 66/72 | 68/72 | 67/72 |
| Japanese | 43/50 | 43/50 | 42/50 |
| Spanish | 47/47 | 42/47 | 45/47 |
| Portuguese | 44/47 | 44/47 | 44/47 |

Costs apply [OpenAI's published rates](https://developers.openai.com/api/docs/pricing) to API-reported token usage; they are not verified invoice amounts. Search, server, payment, and failed-request handling costs are excluded. Latency covers test API calls, not the complete web-app experience. Case counts differ by language, so percentages across languages should not be compared directly. The [original aggregate](./results.json) and [re-scored aggregate](./results-rescored.json) include workflow and case-category breakdowns.

## How should these figures be read?

Some automated checks **failed answers whose meaning was correct** because a required phrase was absent. For example, a Japanese sentence saying “do not record both codes” triggered a forbidden-phrase check, and `Lambda: 0.25` failed a check requiring an equals sign. In other cases, the test's reference selection omitted a needed rule and the model appropriately withheld a decision. The 250/280-style figures are therefore **neither clinical accuracy rates nor model rankings**. We compared selected responses on the Cn calculation boundary, refusal to mix assessment systems, diagnostic overreach, and follow-up questions against the source records and rules. The complete set of 840 generated answers has not undergone independent clinical review.

For 30 M-determinant questions, 30 valid Jev answers matched the author's **provisional expectations**, not a clinician-validated answer key. 3 requests with 10 decisions each succeeded through the Gateway; 2 attempts with 30 decisions in one request returned HTTP 503. We cannot identify whether the failure originated at the Gateway or TypeSafe. [Vercel's free Jev promotion](https://vercel.com/ai-gateway/models/jev) is scheduled to end on 2026-09-25, so its US$0 test charge is not a long-term cost. [TypeSafe's published direct rate](https://docs.typesafe.ai/models) is US$0.042 per million input tokens, with free output. Applying it to the 42341 input tokens used by 30 individually valid calls gives **US$0.001778322**; this is an estimate, not a charge.

## Small paired Jev and GPT pilot

We then ran **2 synthetic questions in each of five languages**, producing 40 GPT answers across four configurations. The 10 questions cover only the Na/Bt/Ls rule and the evidence boundary for diagnosis, treatment, and forensic conclusions. Jev assessed scope, information sufficiency, and reference relevance once per question; GPT still received the original record and calculations. These are 10-answer totals from reported GPT usage, plus a **US$0.001746** Jev estimate at [TypeSafe's direct list price](https://docs.typesafe.ai/models) for each hybrid arm. Failure costs are separate.

| Configuration, GPT medium reasoning | Cost for 10 answers | Automatic contract passes |
|---|---:|---:|
| GPT-6 Sol alone | US$0.163943 | 9/10 |
| GPT-6 Luna alone | US$0.008627 | 9/10 |
| Jev + GPT-6 Sol | US$0.172066 | 8/10 |
| Jev + GPT-6 Luna | US$0.010538 | 8/10 |

**This hybrid does not save money in its current form.** The trial validator rejected 1 Jev answer without retaining the raw output, so its cause is unknown; 2 HTTP 503 errors also occurred; we recorded them without automatic retries and recovered missing answers in separate manual trials. The automatic checks still reject some correct multilingual explanations, so the pass counts are not clinical accuracy rates. Reusing the same Jev decisions with GPT `low` reasoning exposed a more serious issue: a Japanese Jev + GPT-6 Luna answer marked S-CON as not meeting the criterion when the examinee's age was missing. We excluded low reasoning from launch candidates. The [per-request aggregate](./results-hybrid-pilot.json) contains no raw answers, credentials, or customer data.

## Separate rule-family validation

We collected 20 answers per configuration, 80 in total, on 20 synthetic cases held apart from the tuning set. They cover Cn calculations, special-score level pairs, GHR/PHR ratios, and mixing assessment systems. Hybrid costs below add an estimated US$0.002616 for Jev at its direct public list price to calculated GPT usage costs. These 20 cases were separate from hybrid tuning but already appeared in the earlier 260-case GPT-only suite; they are not entirely new hidden questions.

| Configuration, GPT medium reasoning | Total cost for 20 answers | Automatic contract passes |
|---|---:|---:|
| GPT-6 Sol alone | US$0.216957 | 15/20 |
| GPT-6 Luna alone | US$0.011021 | 17/20 |
| Jev + GPT-6 Sol | US$0.289299 | 19/20 |
| Jev + GPT-6 Luna | US$0.017494 | 19/20 |

The hybrid passed more automatic checks, but improved clinical accuracy is unproven. In a Korean Cn case, both answers explained the boundaries correctly; only the standalone answer failed a wording check. Our validator also wrongly rejected one Jev response whose rounded probabilities summed to 0.99. We reused that saved response and generated only the missing GPT answers. This was not a Jev service failure. The [per-request holdout aggregate](./results-hybrid-holdout.json) excludes raw answers, credentials, and customer data.

Our AI review compared all 80 answers with narrow written rules: Cn 20/20, GHR/PHR 20/20, mixed systems 20/20, and DV 16/20 met those criteria. The Korean DV 4/20 safely abstained because the required rule was missing from retrieval, leaving the question unanswered. This internal review found 0/80 critical errors. **It is AI review, not independent clinical adjudication or real-world accuracy.** No meaningful advantage between configurations was established.

These synthetic cases alone could not settle the product choice between GPT-6 Sol and GPT-6 Luna. We later added actual product retrieval and usage accounting, while deferring Jev. Independent clinical review and a complete reconciliation of failure costs remain outstanding.

The [2026-09-24 report](../2026-09-24/) records the follow-up trials and release configuration. We will widen publication of v3 prompts, AI instructions, model-routing code, and evaluation tools after reviewing secrets, operational settings, customer data, and third-party rights. This document preserves the conditions and failures of the original trials.
