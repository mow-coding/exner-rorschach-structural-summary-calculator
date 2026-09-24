# Exner v3.0.0: GPT-6 Luna selection and production-path evidence — 2026-09-24

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

This report follows the [2026-09-23 comparison](../2026-09-23/) of GPT-5.6 Terra, GPT-6 Sol, GPT-6 Luna, and Jev. v3.0.0 uses **GPT-6 Luna alone, `medium` reasoning, standard (`default`) tier**. Jev and automatic fallback to another generation model are not in the product. These synthetic tests do not establish clinical accuracy or equivalence.

The initial comparison used 260 synthetic cases and 290 calls per GPT model, including 280 answer checks and summaries. Rescoring stored answers with a corrected wording checker gave GPT-5.6 Terra **257/280**, GPT-6 Sol **254/280**, and GPT-6 Luna **255/280**. These are wording-contract results, not clinical accuracy. Usage multiplied by public rates gave generation costs of **US$3.553828**, **US$2.304015**, and **US$0.130514**, respectively; the fixed three excerpts were not the product's question-specific retrieval. The Jev tests, 503 errors, and their estimated direct-provider costs remain in the [earlier report](../2026-09-23/).

When we read all 280 stored GPT-6 Luna answers and 10 summaries, we found that an early review omitted prior summary context and a Claude input path damaged UTF-8 text. We excluded those judgments and reread the corrected inputs. The resulting exploratory classifications were **217 normal, 35 safe but incomplete, 15 checker false failures, 12 indeterminate, and 1 minor source-attribution error**. Claude Fable 5.1 disagreed on some classifications and missed that error. Neither AI review is a clinician's independent review.

## Retrieval, time, and cost

| Trial | Observation | Limit |
|---|---|---|
| Seven rules with actual top-eight reference retrieval | GPT-6 Luna explained the core supplied rule in **7/7**; embedding and generation calculated at **US$0.002352** | Selected questions; not the full chat, summary, or billing path |
| Five languages × coding and interpretation, GPT-5.6 Terra/GPT-6 Luna standard | Both passed **10/10** automatic checks. Retrieval plus generation: GPT-5.6 Terra **US$0.226730**, GPT-6 Luna **US$0.011580**. Median first token **2.392s** versus **7.314s** | GPT-6 Luna missed the original first-token target in this small sample |
| GPT-6 Luna standard/Fast generation, 20 responses each | Median first token **5.582s → 2.994s**; generation cost **US$0.010000 → US$0.035559** | Fast was faster and more expensive; it was not selected |
| 30 source cases repeated three times with actual retrieval, GPT-5.6 Terra standard/GPT-6 Luna Fast | **90** answers each; retrieval plus generation **US$1.372149 → US$0.064049**, a **95.33%** reduction. Median first token **2.024s → 2.652s**; 95th percentile **5.744s → 6.846s** | The GPT-6 Luna arm used Fast, so its timing and costs are not standard-tier release measurements |

Claude Fable 5.1 reviewed the first repeat of those 30 source cases, one case at a time. Answers below the preregistered 80-point threshold were **0/30** for GPT-5.6 Terra and **4/30** for GPT-6 Luna Fast. The GPT-6 Luna cases involved low-response-count explanations in Korean and English, a general English interpretation, and a general Portuguese interpretation. The AI reviewer marked no critical error in either group, but only a development set and its first repeat were reviewed. We did not promote an instruction that helped one language but harmed another.

## Language-specific instructions and summaries

| Development set | Completed work | What remained |
|---|---|---|
| Low-response-count `v4` | GPT-6 Luna Fast **60** answers; Fable **20** review calls; generation and retrieval **US$0.062212**, Fable list-price estimate **US$10.129531** | One Spanish answer scored **76** |
| Spanish repair `v5` | GPT-6 Luna Fast **30** answers; Fable **10** reviews; generation **US$0.034716**, Fable **US$4.982458** | Spanish minimum improved **76→82**; unchanged language instructions were retained |
| Boundary set `v7` | GPT-6 Luna Fast **60** answers; Fable **20** reviews; retrieval and generation **US$0.081067**, Fable **US$9.822691** | All **30** candidate answers scored at least **80**, minimum **82**; one exposed an internal field name |
| Summaries in three source topics and five languages | GPT-5.6 Terra/GPT-6 Luna **30** summaries; Fable **15** reviews; generation **US$0.033595**, Fable **US$3.20503725** | GPT-6 Luna English and Portuguese summaries omitted an earlier retracted judgment |
| Follow-up after those summaries | **15** answers per model; Fable **15** reviews | One Korean GPT-6 Luna answer mixed another script; source attribution remained a repair target |
| Retraction-history `v9` | GPT-6 Luna standard **90** summaries; Fable **15** reviews; GPT-6 Luna **US$0.011541**, Fable **US$4.194821** | Mean AI score **86.80→88.64**; each arm had **3/45** below 80 and some open questions were still omitted |

An initial multilingual run stopped after **43/60** calls because two different prompts shared a version ID; its known retrieval and generation cost was **US$0.051947** and was retained. Six later retrieval preparations had **unknown** recorded cost, with a conservative bound of **US$0.006390**. Five translations of one source case were counted as one source case, not five independent cases. Improvements on previously seen items were not reported as a new final evaluation.

The mock-provider product path completed 13 chat requests, 13 embeddings, 2 summaries, and 13 generations. On the actual `exner.app` domain, synthetic accounts then completed **one coding and one interpretation** response, with provider model and ledger records checked; two embeddings and two generations calculated at **US$0.000892**. A synthetic web account created a Live checkout, but **no real purchase, entitlement, cancellation, or refund** was tested before release. Two production answers cannot establish a multilingual quality rate or average useful-answer cost.

The [non-identifying cost inventory](./luna-cost-inventory.json) covers **26** stored GPT-6 Luna-related run folders: **US$2.369002** calculated from OpenAI token usage and **US$117.300407** at Claude CLI displayed list price. Neither is a verified card charge; the amounts must not be combined into a total research bill. Earlier GPT/Jev trials, unknown-cost calls, infrastructure, and payment expenses are outside that inventory. The original plan for a new independent 30-source-case × five-language final set repeated twice was **not completed**, nor was independent clinician review. The Korean [technical ledger](./README.md) records the finer trial boundaries and remaining failures.
