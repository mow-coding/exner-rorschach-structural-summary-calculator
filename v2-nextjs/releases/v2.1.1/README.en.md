# [2026-06-27] v2.1.1 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.1.1 fixes problems in the scoring input screen and in the AI connection flow. The Gemini/Google AI connection was removed, and the flow was simplified to OpenAI with your own API key.

## Summary

- Fixed: dragging text with the mouse inside the response memo popup was mistaken for a click on the backdrop and closed the popup.
- Selecting another row during a coding assistant conversation no longer discards the existing conversation or the answer in progress.
- The AI features accept only an OpenAI API key; the Google Gemini connection is no longer offered.
- In the API key dialog, the model name and the key guidance are shown on one easy-to-read line.

## AI connection and the scoring screen

The AI features now accept only an OpenAI API key. Entering a former Google/Gemini key shows a notice that an OpenAI key is required. The API key is used for the AI connection in encrypted form; the connection lasts at most 24 hours, and ending it also deletes the key.

The coding assistant refers to the selected row, but moving to another row does not discard the existing messages. You can keep the conversation and continue asking with another row as reference.

The response memo popup fix does not affect calculated scoring results; only the condition for closing the popup during input was made more precise.
