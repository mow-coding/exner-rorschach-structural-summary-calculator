# [2026-02-15] v2.0.0 Major Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.0 is the first version 2 release, moving v1.4.1 to a new web app. It keeps the core of v1, the Rorschach Exner (CS) Structural Summary calculation flow, and adds multilingual screens, reference document search, and BYOK-based AI assistance.

The biggest change in this version is BYOK (Bring Your Own Key): users connect their own OpenAI or Google API key to use the AI features. AI usage costs are incurred on the connected account, and the API key is used only while the AI connection is active.

## What is kept from v1.4.1

The core purpose of v1.4.1 is unchanged. Users enter Rorschach responses row by row, organize the values needed for the Structural Summary, such as card, location, developmental quality, determinants, form quality, contents, and special scores, and then calculate the results.

The Structural Summary calculation flow, results review, CSV export, and multilingual support provided in v1 are carried over into v2. The input and results screens were rebuilt as web app screens that are easy to use on both mobile and desktop.

## How it is used

The main screens are the scoring screen, the interpretation assistant, reference documents, account management, and the version archive. The basic calculation features and reference document search are available without signing in; to use the AI features, sign in and connect an API key.

## BYOK AI connection

The AI features in v2 work only with BYOK. The app does not sell AI credits or subscriptions; users connect an API key from either OpenAI or Google.

The API key is used only while the AI connection is active and is deleted on sign-out or when the connection expires. Entering an OpenAI key or a Google key in the wrong field is pointed out immediately.

Users do not choose the model themselves. The web app automatically uses the latest model chosen by the service among models whose stability has been confirmed some time after release. As of v2.0.0, the default models are GPT-5.4 for OpenAI and Gemini 2.5 Pro for Google.

When an AI provider rejects a request, the errors are not collapsed into one. The app distinguishes an invalid API key, a billing or usage limit problem, and a model that cannot be used with that API key, and tells the user which it is.

## Coding assistant

The AI on the scoring screen is organized as the coding assistant. "Coding" here does not mean programming; it means encoding Rorschach responses into the symbols and categories of the Exner (CS) system.

The coding assistant opens with the Ctrl/Cmd+J shortcut. The whole sheet entered on the current scoring screen is passed as the default context, and when a specific row is selected, that row is emphasized as the more important context. When no row is selected, only the whole-sheet context is used, without a focal row.

The coding assistant does not settle the answer automatically. When reviewing a response's location, determinants, form quality, and content categories, it explains the possible candidates and the reasoning on the basis of the reference documents and the entered data.

v2.0.0 provides no auto-fill button. The AI only explains candidates and reasoning; the final coding is decided by the clinician after reviewing the response context.

## Interpretation assistant

The interpretation assistant is an AI screen for carrying on an interpretation conversation on the basis of a Structural Summary CSV. Users attach a CSV file containing the Structural Summary values, add age, sex, the observation context, and the hypotheses or questions the clinician already has in mind, and ask the AI to review them.

The interpretation assistant plays a supporting role: it explains patterns in the Structural Summary results and checks the hypotheses the user has formed. It does not replace an official diagnosis or the final interpretation; the final judgment rests with the clinician.

## Reference documents

v2 also provides a collection of short explanatory documents that the web app and the AI assistants consult. These documents explain the main concepts of Structural Summary calculation, coding, and interpretation, and can be searched directly on the reference document screen.

The reference documents are built on material produced and organized jointly by the Seoul Institute of Clinical Psychology and MOW. The goal of publishing them is to let users see what knowledge the AI bases its answers on. This ties in with the design principle of not leaving the AI features as a black box, so that users can check the evidence and judge for themselves.

Reference documents whose names contain codes such as `+`, `-`, and `v/+` open correctly.

## The AI does not replace the clinician's judgment

v2 is not meant to be a system in which the AI judges in place of the professional; it aims to help clinical psychologists and trainees review and judge on clearer evidence. That is why only two AI features remain: the coding assistant on the scoring screen and the interpretation assistant on a separate chat screen.

AI answers are for reference and support; the final coding and interpretation are judged by the clinician.

## Security and privacy

API keys and the text of AI conversations are not kept as long-term account data. The API key is used only while the AI is connected and is deleted on sign-out or when the connection expires.

AI usage costs are incurred on the API provider account the user connected; the app itself has no payment or subscription feature.

## Screens and usability

The top menu, language selection, light/dark mode, account management, version archive, and reference document search screens were newly organized.

On the scoring screen, row selection, adding/deleting rows, shortcuts, and the undo/redo flow were tidied. Selected rows stay highlighted, and the context the coding assistant receives changes with the selection.

A CSV attach button and drag-and-drop attachment were added to the interpretation assistant screen. Besides pasting text, users can attach a Structural Summary CSV and use its contents as the context of the AI conversation. Only one attachment is accepted at a time, which reduces the chance of the AI reading the wrong context from mixed material.

## Multilingual support

v2 supports Korean, English, Japanese, Spanish, and Portuguese screens. The language is chosen from a dropdown, and the layout stays stable across screen sizes and differing string lengths per language.

## Product scope

The core scope of v2.0.0 is Structural Summary calculation, reference documents, and the BYOK-based coding and interpretation assistants. It does not include service-provided AI credits, payments, or subscriptions.
