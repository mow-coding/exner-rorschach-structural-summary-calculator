# Exner Rorschach Structural Summary Calculator

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

Exner is a web app for reviewing Rorschach Comprehensive System coding and Structural Summaries. The current **v3.0.0** combines the calculator with AI assistants that can answer follow-up questions. Suggested codes and explanations are supporting information; the clinician makes the final judgment from the original response and record from the inquiry phase.

## Use the app

- [Paid v3 web app](https://exner.app): Available in Korean, English, Japanese, Spanish, and Brazilian Portuguese. Subscriptions cost **US$3.99 per month** or **US$42.99 per year**.
- [Free v2 web app](https://exner.yesucan.co.kr): The existing Structural Summary calculator remains available, with optional AI assistance using your own API key.

## What changed in v3.0.0

A Google account and subscription give access to coding and interpretation assistants. Both use **GPT-6 Luna**. In longer conversations, the app summarizes earlier context for follow-up questions. The Structural Summary formulas have not changed from v2, so this release alone does not require recalculating existing records.

The [v3.0.0 release notes](./v3-web/releases/v3.0.0/README.en.md) explain the features and clinical limits. The [model comparison](./v3-web/benchmarks/2026-09-23/) and [follow-up evaluation](./v3-web/benchmarks/2026-09-24/) describe the methods, results, and costs. Automated checks on synthetic cases are not clinical accuracy rates.

## Source and earlier versions

This repository contains the [published v2 source](./v2-nextjs/source/), [published v1 source](./v1-gas/current/), and [full release history](./CHANGELOG.en.md). The full v3 production source has not yet been published. We plan to publish reviewed source and AI instructions after checking secrets, clinical records, and third-party rights, while retaining existing copyright notices.

MOW plans and operates the service. The Seoul Institute of Clinical Psychology (SICP) contributed to checking early calculation results and reviewing clinical use. See also the [acknowledgements and early learning references](./ACKNOWLEDGEMENTS.en.md).

The [v3 notice](./v3-web/NOTICE.md) explains attribution and publication scope for the new v3 records. Earlier v1 and v2 copyright notices remain in place.
