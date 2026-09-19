# [2026-05-21] v2.0.2 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.2 fixes problems with the Structural Summary CSV found after v2.0.1. The overall product direction and the way the AI features are used have not changed; the data copied or downloaded from the results screen now reflects the Structural Summary shown on screen more accurately.

**The Structural Summary values themselves have not changed, so there is no need to recalculate.** However, if you ran an AI interpretation with a Structural Summary CSV copied in v2.0.1, some items may have been missing or the same name may have appeared twice, so please check that interpretation with values copied again in v2.0.2 or later. For the same reason, it is safer to regenerate any downloaded CSV files you keep.

## Summary

- In the data download dialog, the Korean item name `입력값 원자료 CSV` was corrected to `점수계열 원자료 CSV`.
- Fixed duplicate headers and missing items that could appear in the CSV string produced by the `Copy Structural Summary values` button.
- Copy and download now provide the same Structural Summary items.
- Fixed the session-start popup reappearing repeatedly after an AI provider key error in an AI session signed in with an API key.
- The default OpenAI chat model was updated from GPT-5.4 to GPT-5.5.
- The interpretation assistant's confirmation that Structural Summary values were pasted is now shown as `Entered ✅`.

## What to check in the interpretation assistant

In v2.0.1, the interpretation assistant is used by copying values from the results screen with the `Copy Structural Summary values` button, pasting them into the Structural Summary field of the interpretation AI screen, and starting the conversation.

In v2.0.1, names used in several sections, such as `D`, `Zf`, `Zd`, `GHR`, and `PHR`, could be duplicated in the copied data. Some items shown on screen, such as `Single`, `Contents`, `Form Quality`, `Special Scores`, `Approach`, and `Blends`, could also be missing.

This was not a problem with the API key connection or the AI conversation itself, but the Structural Summary data passed to the interpretation assistant could be incomplete or ambiguous.

## What changed

Copy and download now provide the same complete set of items, and items with the same name are shown so that they can be told apart.

The score-series raw data CSV includes only the scoring rows actually used in the calculation. Temporary rows with an empty card and incomplete rows are excluded.

The interpretation assistant accepts the Structural Summary data copied from the results screen and does not treat unrelated ordinary sentences as Structural Summary data.
