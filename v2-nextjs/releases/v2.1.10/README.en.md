# [2026-07-13] v2.1.10 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Before you read on

v2.1.10 fixes reference document search problems that remained after v2.1.9.

The app screens and the formulas have not changed. Rorschach codes attached to Japanese sentences are preserved, and broad interpretation questions now use interpretation documents only. The AI does not settle the final code or replace the clinician's judgment.

## Summary

- A Rorschach code followed by Japanese, as in `FQ+の...`, `v/+の...`, or `3r+(2)/Rの...`, is recognized as the whole code.
- Natural, broad interpretation questions also receive related interpretation documents, and broad questions receive interpretation documents only.
- The same reference document no longer appears more than once in search results.

The AI does not automatically settle codes or make a diagnosis; the final judgment rests with the clinician.

## Remaining limits

- Depending on how a question is phrased, a related interpretation document may be missed.
- Better search and answering do not prove clinical accuracy.
- Actual clinical usefulness, the quality of the multilingual sentences, and safety must be judged by qualified professionals.
