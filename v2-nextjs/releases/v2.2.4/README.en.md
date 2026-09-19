# [2026-07-18] v2.2.4 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Before you read on

v2.2.4 is a reference document, AI search, and safety release that **does not change the Structural Summary formulas or the way the scoring sheet is filled in**. The Structural Summary of a completed protocol does not need to be recalculated. Even when using only the calculator without an API key, no new examinee information has to be entered.

This release improves the reference documents and the AI search material. Clinical terms in the five languages are not matched by literal translation; the expressions actually used in each language's professional literature and academic sources come first. Document titles and order were also arranged to follow scoring and the Structural Summary rather than alphabetical order.

The optional coding and interpretation assistants answer only within the scope of the Exner Comprehensive System (CS). They do not answer questions about other test systems or requests for non-public information.

## Reference documents

### Readable titles and order on screen

The existing reference document links are unchanged, while the titles shown on screen now follow each language's clinical terms. Buttons show meaningful titles such as `Coding`, `Form Quality (FQ)`, and `Special Indices`.

The top-level documents are arranged in this flow.

1. Coding
2. Interpretation
3. Upper Section
4. Lower Section
5. Special Indices

The coding documents run in the order card, location, developmental quality (DQ), determinants, form quality (FQ), pairs, contents, popular (P), organizational activity (Z), score, GHR/PHR, and special scores. Alphabetical order is used only to find detail items within the same category.

### Clinical terms in the five languages

The Korean, English, Japanese, Spanish, and Brazilian Portuguese documents use the professional terms natural to each language. Each document explains the core definition, the conditions of application, cautions, and related items.

Notable corrections include the following.

- The English PHR document makes clear that `ALOG` is part of the early PHR conditions in the decision order.
- In the English and Spanish natural content codes, the precedence that `Bt` or `Ls` is not coded together with `Na` in the same response is made explicit.
- The Japanese document now explains `Ay` as cultural/historical content rather than anatomical content.
- The Korean document distinguishes the raw frequency `S-` from the separate ratio `S-%`.
- The Korean S-CON document states the age-15-and-over boundary and the 12 constituent criteria.

These changes do not replace the coding a clinician performs after checking the response record and the Inquiry. The reference documents are supporting material for checking the definitions and distinguishing criteria of codes; the final coding of each response remains the responsibility of the human scorer.

## AI reference document search

The AI assistant finds content related to the question in the current reference documents.

Related explanations are also found for short questions such as these.

- A short question about the relation between Cn and WSumC now retrieves both the on-screen value that includes Cn and the WSumC explanation that excludes it.
- A question about the precedence of `Na`, `Bt`, and `Ls` no longer retrieves only the general descriptions of the three content codes while missing the exact precedence sentence.

## Scope of the coding and interpretation assistants

Both assistants follow these principles.

- They answer only coding and Structural Summary questions of the Exner Comprehensive System (CS).
- They do not widen their answers to separate test systems such as R-PAS or MMPI, or to general counseling or diagnostic questions.
- They refuse requests to disclose the service's non-public information or the user's API key or connection details.
- When age is actually needed for an interpretation, they may explain why and ask within the AI conversation, but the calculator itself never requires an age.
- They do not settle a diagnosis or risk from the Structural Summary alone and give priority to the interview, behavioral observation, raw data, and the clinician's judgment.

Requests outside the Exner CS scope or for non-public information are not answered; instead, the assistants point to coding or Structural Summary questions they can answer.

## Preventing excessive repetition of AI requests

Beyond 12 AI conversation requests per minute or 120 per hour, you are asked to wait a moment. This limit reduces accidental repetition of the same request and unexpectedly high costs. To enforce it, the API key, questions, answers, Structural Summary text, and clinical content are not stored separately.

Thumbs-up/thumbs-down ratings store no conversation text and are kept for at most 180 days.

## Changes to screens and the service description

- The left sidebar has an opaque background so the content behind it does not show through.
- Fixed the language menu being clipped or misaligned over the content when opened with the sidebar collapsed.
- The reference document buttons use the five-language titles and the order that follows scoring and interpretation.
- The dialog that asks how to start (new data, sample data, or saved data) opens again every time the scoring screen is entered.
- Code-like key phrases in the reference documents are shown in a red that is easy to distinguish in both light and dark mode.
- In the coding assistant, the down arrow that appears when scrolling up to read earlier messages sits right above the input area. It no longer covers the middle of the conversation during long answers.
- The version 2 and version 1 records are collapsed when first opened.
- The service name is unified as `Exner Rorschach Comprehensive System Structural Summary Calculator`.
- The service description credits MOW for production and the Seoul Institute of Clinical Psychology (SICP) for verifying early calculation results and reviewing from the standpoint of real clinical use.

The scoring sheet's columns, dropdowns, calculate button, zoom controls, and the Structural Summary results screen are unchanged. The mobile screens are unchanged as well.

AI responses may differ each time and are not guaranteed to be clinically accurate for every real question. Nor is the correctness of the Structural Summary calculation judged by AI answers.

## Public sources for the terms in the five languages

Each language's professional usage comes first, and the codes and identifiers of the Comprehensive System are kept as they are. No single source is treated as the correct answer for every language.

- Korean: [KCI - Construction of the Korean Rorschach Comprehensive System for Children based on Exner's Comprehensive System](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001392063), [KCI - Coping and defense of North Korean defectors on the Rorschach](https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001391524)
- English: [International Rorschach Institute manuals](https://www.rorschach-institute.org/manuals.html), [Meyer and Viglione, An Introduction to Rorschach Assessment](https://www.utoledo.edu/al/psychology/pdfs/meyer/MeyerViglione2008IntroRorschach.pdf)
- Japanese: [誠信書房 - 包括システムによるロールシャッハ臨床](https://www.seishinshobo.co.jp/book/b88274.html)
- Spanish: [Sociedad Española de Rorschach y Métodos Proyectivos](https://www.rorschach.es/index.php/programas-de-los-cursos), [CHESSSS](https://rorschachspain.org/chessss/), [Manual de codificación del Rorschach para el Sistema Comprehensivo](https://www.psimatica.com/tienda/psicodiagnostico/23-manual-de-codificacion-del-rorschach-autor-john-exner.html)
- Brazilian Portuguese: [SciELO - Localização e qualidade formal do Rorschach-SC no Brasil](https://www.scielo.br/j/pusf/a/kFHxFGKH3qx9gdVtyC6nqWS/), [SciELO - Indícios de validade do déficit relacional no Método de Rorschach](https://www.scielo.br/j/pusf/a/6Xy8zSJGCNq49BWjXRpYNhx/)
- Common translation and adaptation principles: [International Test Commission Guidelines](https://www.intestcom.org/page/14)
