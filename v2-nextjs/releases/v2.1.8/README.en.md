# [2026-07-11] v2.1.8 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Before you read on

v2.1.8 improves the content and the search of the 1,015 reference documents in five languages used by the AI assistants.

The app screens have not changed. The improvement is not to the calculator's formulas but to how the optional AI assistant finds the documents relevant to a question.

## Main changes

- The 1,015 reference documents in five languages now state the strength of evidence and the limits of each explanation.
- The PTI, S-CON, DEPI, CDI, HVI, and OBS explanations state the strength of evidence and the limits that the clinician must check.
- A positive S-CON alone is not treated as a conclusion of risk; the assistant answers that a direct risk assessment and clinician confirmation are needed.
- Multilingual search finds related documents regardless of accents.
- The AI assistant answers questions on the basis of these reference documents.
- The AI assistant understands natural synonyms but avoids diagnostic conclusions, unsupported certainty, and automatic application.

## Remaining limits

- The reference documents and the AI assistant do not replace clinical judgment.
- Model responses are probabilistic, so future responses are not guaranteed.
- The sentences in the five languages are for reference and do not replace the official clinical translations of each language.
