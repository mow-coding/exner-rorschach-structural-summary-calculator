# [2026-07-17] v2.2.3 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Before you read on

v2.2.3 improves search and share previews and the AI response ratings **without changing the Structural Summary formulas or the screen layout**. Existing Structural Summary results do not need to be recalculated, and neither the calculator's input items nor the use of AI changes.

Search results and link previews now carry a title and description for each of the five languages, and the optional AI response rating is limited so that it cannot be sent too large or too often.

## Search results and link previews

The home page title used for search and sharing is `Yes, U Can!` in all five languages. The Korean description is fixed to the following sentence:

> 회원가입, 설치, 결제가 필요 없는 Exner Rorschach 종합체계(Comprehensive System) 검사 구조요약 계산기입니다. 오픈소스이며, 본 서비스는 전문가의 임상 판단을 대체하지 않습니다.

The same meaning is conveyed in English, Japanese, Spanish, and Portuguese. Each language's pages show that language's title and description in search results and link sharing.

The official address is `https://exner.yesucan.co.kr/`, and the previous address continues to work.

Ordinary search descriptions and link previews use the same title and description. This change does not alter the wording shown on the page or the screen layout.

Search engines and messengers may keep the previous information for a while, and Google may rewrite parts of the title or description depending on the search query. It therefore cannot be guaranteed that the change appears immediately in every search result and link preview.

## AI response ratings and personal data

Thumbs-up/thumbs-down ratings remain optional. Only whether the answer helped, the reason chosen, and what the service needs for aggregate counts are recorded. The question, the answer, response notes, the Structural Summary text, the API key, account identifiers, the original IP address, and browser details are not stored.

One rating accepts up to about 2 KB. Beyond 10 ratings per minute or 60 per AI connection, you are asked to wait a moment and try again. The temporary record used for this limit is kept for at most 24 hours, and rating data is retained for at most 180 days.

## Remaining limits

- The formulas, the Structural Summary output, the AI model, the reference documents, and the answering rules have not changed.
- The layout, controls, and styling of the desktop and mobile screens have not changed.
- This release does not change how AI answers are generated and does not guarantee the clinical accuracy of every future AI answer.
