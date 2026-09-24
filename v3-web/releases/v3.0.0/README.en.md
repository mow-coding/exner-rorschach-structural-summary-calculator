# [2026-09-24] v3.0.0 major release — Paid web app with AI assistants

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Exner v3.0.0 lets clinicians discuss Rorschach Comprehensive System coding and Structural Summary interpretation with AI assistants in a free-form conversation. The new web app is available at [exner.app](https://exner.app). AI responses are supporting information; a clinical professional remains responsible for final coding and interpretation based on the original response and Inquiry record.

## What changed?

- Sign in with a Google account and give separate consent for sending information to the AI before using the coding and interpretation assistants. Both use GPT-6 Luna with `medium` reasoning and the standard service tier. We evaluated Jev but did not add it to the v3.0.0 response path.
- The app retrieves references relevant to the question and summarizes earlier content for follow-up questions in long conversations. Neither a summary nor an AI response changes the original protocol or a result verified by the calculator. The assistant may ask for missing information.
- The interface and reference material support Korean, English, Japanese, Spanish, and Brazilian Portuguese. We will continue improving responses in each language; we do not claim that every clinical judgment is equally complete across all five.
- Subscriptions cost **US$3.99 monthly** or **US$42.99 annually**. The amount charged in another currency and any tax depend on checkout and card terms. Usage is managed by an AI processing-cost allowance rather than a fixed number of requests. The app shows remaining usage and subscription status.

## Must I recalculate an existing protocol?

This release does not change v2 Structural Summary formulas or completed calculation results. You do not need to recalculate a v2 protocol because of this release. AI-suggested codes and explanations are not final scoring; for clinical use, compare them with the original response, Inquiry, and the full clinical record.

## Evidence and limitations

Before release, we compared GPT-5.6 Terra, GPT-6 Sol, GPT-6 Luna, and Jev on **synthetic cases**. We examined coding, interpretation, summarization, actual reference retrieval, response time, and usage by language. We also used Claude Fable 5.1 for a separate AI review. We did not treat automatic wording checks as clinical accuracy or call an AI review independent clinical review. The exact model names, figures, cost calculations, failures, and incomplete responses are in the [initial model comparison](../../benchmarks/2026-09-23/) and [follow-up release-configuration report](../../benchmarks/2026-09-24/).

![Generation costs and automatic wording checks for three GPT models with the same synthetic inputs](../../benchmarks/2026-09-23/model-comparison.svg)

The automatic checks above are **not clinical accuracy**. The next comparison used actual reference retrieval but GPT-6 Luna **Fast**, so it cannot describe the timing or costs of the released standard tier.

![Calculated retrieval and generation cost and first-token time for GPT-5.6 Terra standard and GPT-6 Luna Fast](../../benchmarks/2026-09-24/retrieval-trial.svg)

On the production site, synthetic accounts completed responses from both AI assistants and created a Live checkout. **At release, we had not yet completed a real transaction covering new-user signup, payment, entitlement, cancellation, and refund.** We will reconcile transaction and entitlement records and correct any problem found. Independent clinical review of responses and some incomplete multilingual answers also remain follow-up work.

The Terms and Privacy Policy take effect on **2026-09-24**. Consent to send information to the AI is separate from a subscription and can be withdrawn. We will publish v3 source and prompts in reviewed portions after checking secrets, clinical records, and third-party rights. These release notes and benchmark reports do not mean that all production source has already been published.
