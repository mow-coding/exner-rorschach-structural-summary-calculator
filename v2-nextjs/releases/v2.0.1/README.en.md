# [2026-04-27] v2.0.1 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.1 fixes usability problems found after the release of v2.0.0. The product scope of Structural Summary calculation, reference documents, and the BYOK-based coding and interpretation assistants is unchanged.

## Summary

- The interpretation assistant's input flow was reorganized from file attachment to entering Structural Summary values.
- In the coding and interpretation assistants, the AI talking too long and the screen moving in ways that were hard to control were reduced.
- The AI auto-fill flow was removed. Coding and interpretation are reviewed only through conversation with the AI.
- Fixed the API key connect/disconnect screens overlapping and required guidance not appearing.
- Fixed toasts and system notice bubbles that looked transparent or were hard to read in dark mode.
- Fixed reference document pages that did not open when a code such as `+`, `-`, or `v/+` was selected.
- The service description, terms of service, and privacy policy were revised to match the current features.

## Entering Structural Summary data in the interpretation assistant

In v2.0.0, the interpretation assistant was described as a flow in which a Structural Summary CSV file is attached. Attaching files could leave users unsure which file to use, and the AI might not read the file contents consistently in the same way.

In v2.0.1, the flow is to paste the Structural Summary values copied from the results screen into a dedicated field of the interpretation assistant. After copying the Structural Summary values on the results screen, paste them into the small Structural Summary field to the left of the interpretation assistant's input box and start asking.

Once the values are pasted, `Entered` is shown instead of the full text. While the same browser window is in use, the entry is kept until the user clears it or replaces it with new values.

To keep the interpretation assistant from accepting just any material, only input in the format of the Structural Summary values copied from the results screen is used. If a user enters unrelated text and tries to start a conversation, a notice asks them to use the results screen's copy function.

## Interpretation assistant answers

The interpretation assistant's answers were adjusted to a length and format that let the user carry on the conversation. Right after v2.0.0, answers could become too long, be cut off midway, or list too many values on one line to read comfortably.

The interpretation assistant no longer opens too many topics in a single answer and shows `supporting values` and `interpretive hypotheses` separately.

The interpretation assistant uses more intuitive terms such as `test data`, `response data`, and `Structural Summary data` instead of `protocol`.

## Coding assistant

The coding assistant helps through conversation while the user codes responses on the scoring screen. In v2.0.1, the flow in which the coding assistant filled rows automatically or applied fields with a button was removed.

The coding assistant now only explains candidates and reasoning in conversation on the basis of the selected row and the whole-sheet context. Users may refer to the AI's explanation, but must review and enter the actual coding values themselves.

Opening the coding assistant with `Ctrl/Cmd+J` on the scoring screen is retained. With no row selected, only the whole sheet is used as context without a focal row; with a row selected, that row is treated as the more important context.

## AI auto-fill removed

The `AI auto-fill` feature was removed. It attempted to fill the coding fields of the current row at once from the response note and card information.

Rorschach coding requires the clinician's review and judgment. Auto-fill was removed to prevent AI suggestions from being accepted without sufficient review; the final entry is decided by the clinician.

As a result, the AI features in v2.0.1 are simpler. The AI in the web app provides only two conversational aids: the coding assistant and the interpretation assistant.

## API key connection screen

The API key is used only while the AI connection is active and is deleted when the connection is ended.

Entering a Google API key in the OpenAI field or an OpenAI API key in the Google field points to the correct field.

The overlap between the disconnect button and the key entry dialog was fixed. Opening the interpretation assistant without an API key connected shows the required steps.

## AI model selection

Users do not choose the model themselves. The web app automatically uses the latest model chosen by the service among models released at least a month earlier whose stability has been confirmed.

Model selection guidance is shown only on the screens where it is needed, so that it does not look as though users must choose a model.

## Dark mode notices

In dark mode, system notice bubbles and the top-right toasts could look transparent or blend into the background and be hard to read. In v2.0.1, the background, border, and text colors of toasts and chat notices are shown more clearly.

Success, warning, and system notices were adjusted so they are not hidden by other screen elements or blended into the background.

## AI conversation screen

Unnecessary guidance text and duplicate messages were reduced in both the coding and interpretation assistants. Elements that interrupted the user's conversation or looked like excessive features, such as the AI model name, the list of reference documents, and field-apply buttons, were removed.

The screen being forced to keep scrolling down while the AI answered, which made scrolling hard to control, was also reduced. Automatic scrolling no longer intervenes too much when the user is reading earlier content.

The dot animation in the bubble shown while waiting for an answer was softened so it is less distracting. A conversational tool is a screen users look at for a long time, and even small movement can tire the eyes.

## Reference documents that did not open

Some reference documents have codes such as `+`, `-`, and `v/+` in their names. In v2.0.0, some links containing these codes did not open.

Items such as `[Coding/Developmental Quality] v`, `[Coding/Developmental Quality] v/+`, `[Coding/Form Quality] +`, and `[Coding/Form Quality] -` now open the correct document.

## Service information

The service description, terms of service, and privacy policy were revised to match the features actually provided. Wording that made it look as though the app offered AI credits, payments, or a store was also corrected.
