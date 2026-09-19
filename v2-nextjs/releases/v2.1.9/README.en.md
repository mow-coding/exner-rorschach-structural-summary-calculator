# [2026-07-12] v2.1.9 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Before you read on

v2.1.9 improves the search method so that the coding assistant and the interpretation assistant find the reference documents that fit a question more reliably before answering.

The app screens have not changed. Reference documents related to a question are found more accurately in the five languages, and the coding assistant now refers only to the rows the user has selected.

## Summary

- Single-character natural-language words are less often mistaken for Rorschach codes, while codes made explicit by context, such as `Card I`, `Content A`, and the lowercase determinant `m`, are preserved.
- Questions containing Korean particles and endings or Japanese, and compound indices such as `3r+(2)/R`, are recognized more accurately.
- Documents related to the question are found more accurately.
- Results with too little meaning are excluded, and the same reference document no longer appears several times.
- The coding assistant refers only to the currently selected row and the rows the user selected together with it.

This release improves reference document search, but the AI does not automatically settle the final code or make a diagnosis. The final judgment rests with the clinician.

## Remaining limits

- Better search does not prove clinical accuracy.
- GPT-5.5 responses are probabilistic, so future responses are not guaranteed.
- Actual clinical usefulness, the quality of the multilingual sentences, and safety must be judged by qualified professionals.
