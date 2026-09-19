# [2026-07-14] v2.2.0 Minor Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

> **Current formulas:** the D/AdjD extremes, the EBPer display condition, the GHR/PHR decision order, the missing Cn in the Lower Section `FC:CF+C`, and the zero-denominator handling of WDA% and Afr were corrected in v2.2.1. v2.2.2 separated the calculations that include Cn from those that do not and completed the GHR/PHR classification of incomplete rows with an empty Form Quality (FQ). The calculator does not take an age; only when an age-restricted interpretation is requested does the AI interpretation conversation ask for the information it needs. **For the current calculation basis, see the [v2.2.2 note](../v2.2.2/).**

## Before you read on

v2.2.0 is the first v2.2.x release: it keeps the calculator at the center, gathers the desktop's main menus into a left sidebar, and rebuilds the interpretation assistant to resemble a typical AI chat screen. AI answer ratings store no conversation text; the user only picks a predefined reason.

Calculation items handled in this release that needed further correction were fixed in v2.2.1 and v2.2.2. The AI assistant does not answer questions outside the Exner Comprehensive System or requests for non-public information.

## Summary

### Shared screens and the sidebar

- The former top and bottom menus were merged into a fixed icon bar on desktop, a sidebar that opens over the content, and a mobile menu.
- The sidebar does not push the content, stays open when navigating to another page, and gathers language, theme, and AI session controls in one place.
- Before sign-in only "start AI session" is shown; after sign-in only "end AI session", with a confirmation dialog before ending.
- A multilingual shortcut guide was added that collects the existing calculator shortcuts, the sidebar shortcuts, and how to zoom and pan the scoring screen.
- The background and the light/dark colors of the calculator, interpretation assistant, reference documents, service description, terms, privacy policy, and version archive were unified.
- The unnecessary outer border and the whole-page copy button were removed from the service, terms, and privacy pages.

### BYOK and the interpretation assistant

- BYOK (Bring Your Own Key) means the user connects their own OpenAI API key to use the optional AI features.
- The OpenAI API key and the `OpenAI GPT-5.5` label sit on the same line, and the duplicate title and the automatic-model notice were removed, so the AI connection dialog is compact.
- The notice that the API key is kept encrypted for at most 24 hours for the AI connection and deleted when the connection ends is shown more clearly. The dialog no longer changes size when an invalid-key notice appears.
- The interpretation assistant became a full workspace without an outer card, and long conversations scroll inside the conversation area rather than the whole page.
- Auto-scroll that follows the AI answer stops when the person scrolls up, and the latest answer can be reached again when needed.
- Stop answer, copy message, jump to the previous question, a translucent input box, and a Structural Summary paste status were added.
- User and AI messages have a copy button, and AI messages gained thumbs-up/down with a predefined-reason picker.
- AI answer ratings keep no question or answer text and no free text. Only whether it helped, the chosen reason, the language, the model, whether the answer completed, and its rough length are kept for at most 180 days.

### Scoring screen

- The row drag handle is no longer clipped at the table edge.
- Multi-row selection with a plain click, `Shift + click`, and `Ctrl/Command + click`, and the row-move preview, work reliably.
- Select boxes with a value, empty ones, and disabled ones keep the same size and alignment and differ only in shade.
- Column widths were adjusted so the table fits one screen on a typical desktop and scrolls horizontally only inside the scoring area on narrow screens.
- `Alt + mouse wheel` zooms the whole scoring screen between 40% and 125% around the pointer, and `Ctrl + drag` pans the zoomed screen.
- Row order guidance is shown in the blue strip right below the table.
- The bottom buttons were arranged as add/delete/help on the left and calculate/reset inputs in the center.

### Reference documents and the version archive

- The reference document search box stays visible on results and document pages, and the query carries over to the next screen.
- The no-results notice, the document category buttons, and the copy-complete notice were aligned in the five languages.
- The reference document body became a reading view without an outer card, with the search box, categories, and body sharing one center line.
- The version 2 and GAS version 1 records collapse and expand by their headings, and the screen no longer shifts sideways when a vertical scrollbar appears on expansion.
- The GAS run guidance moved into an information tooltip beside the heading that can also be opened from the keyboard.

## Calculation changes in v2.2.0

v2.2.0 corrected the following seven items. The current formulas also reflect the later corrections in v2.2.1 and v2.2.2.

| Item | Correction |
| --- | --- |
| EBPer | Shown only when `EA >= 4`, both M and WSumC are positive, and the ratio is `>= 2.5` |
| Active/passive movement | `Ma-p`, `FMa-p`, `ma-p` are added to both the active and the passive side |
| `3r+(2)/R` | The weight of reflections `Fr+rF` corrected from 2 to the standard formula's 3 |
| HVI | The Zd auxiliary boundary corrected from `> 3.0` to `> 3.5` |
| ZEst | The last valid boundary `Zf=50` now returns `173` |
| D/AdjD | `0` instead of `-0` in the negative range |
| Lambda | `∞` instead of 0 when every response is pure F |

Four kinds of material were used to compare calculation results.

- [Sample computerized score reports in Essentials of Rorschach Assessment](https://elmirmohammedmemorypsy.com/wp-content/uploads/2021/04/essentials-of-rorschach-assessment.pdf)
- [Engelman et al., "Why am I so stuck?"](https://www.therapeuticassessment.com/docs/Engelman_et_al_2016_copy.pdf)
- [Tibon Czopp et al., amnestic syndrome case](https://pubmed.ncbi.nlm.nih.gov/23985019/) and its [erratum](https://www.tandfonline.com/doi/pdf/10.1080/13554794.2014.910345)
- The actual formulas of the [publicly distributed 2019 Excel workbook](https://blog.naver.com/jin_k84/221539279596) consulted during early v1 development. The workbook's internal credit reads `[Scoring Program] _by. Ju-Ri`; no real name is inferred and the original file is not redistributed.

For the two items where the published tables and the public score columns disagreed, neither side was taken as the sole correct answer.

National group means are not answer keys for the same score column. Cultural differences mainly affect coding, norms, and interpretation rather than the formulas, so Korean, Japanese, and English-language materials were used separately to check the range of answers by culture and age.

## Scope of the AI assistant

- It does not answer general R-PAS interpretation, general MMPI interpretation, unrelated questions, or requests for non-public information.
- Valid Exner comparison or differentiation questions are allowed only to the extent of explaining the boundary, without extending into general interpretation of other systems.
- S-CON interpretation applies to people aged 15 and over. The calculator does not take an age; only when asked for S-CON interpretation does the AI assistant confirm the age in the conversation if needed.
- A direct question about Popular (`P`) receives the Popular reference document first.

Using GPT-5.5 with your own API key is retained. AI conversations last only while the current browser window is in use and are not kept as long-term account records. The AI does not replace the clinician's final judgment or guarantee the accuracy of every answer.

## Remaining limits

- This calculation scope does not mathematically prove every possible response combination.
- Because the calculator does not take an age, withholding S-CON interpretation for people aged 14 and under must be checked by the clinician using it.
- Actual clinical usefulness, the quality of the multilingual sentences, and safety must be judged by qualified professionals.
