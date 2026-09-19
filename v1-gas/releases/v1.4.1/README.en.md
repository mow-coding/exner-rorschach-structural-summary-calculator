# v1.4.1

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

## Metadata

| Field | Value |
| --- | --- |
| Version | `v1.4.1` |
| Release date | 2026-01-07 |
| Release type | Bug fix |
| GAS deployment | [Open GAS app](https://script.google.com/macros/s/AKfycbxMCx13pkrSzFs8f2qXfmxy2LRhkBpZTItFTIfEOoOi-zwurbysnKGfDIYtAeEdQP99/exec) |

## Patch Notes

# Main changes

## *Overview*

> **Bugs in v1.4.0 have been fixed.**

The buttons shown on the first visit to the web app and on a return visit now appear correctly.
>
- Previously, the "Start with sample data" button was shown even on a return visit.
    - First visit: "Start with sample data" button
    - Return visit (saved data present): "Load autosaved content" button
- The modal shown on a return visit was tidied.
    - The "Continue your work" title was removed; only the message "There is content from your last session." is shown

        in large bold text (so the same thing is not said twice)


> Other improvements
>
- A more noticeable effect was added when hovering over the cards on the More tab.
    - The shadow is darker
    - The background image behind the card is clearer
    - The text inside the card is blurred so the background image stands out
- Styles that belonged in `styles.html` but were still partly in `index.html` were all moved,

    making the code cleaner.


These changes are also reflected in the [Gems chatbot](https://gemini.google.com/gem/1QDCPHshPvq5J9iIKeV-1Nvy0EFzKPN6Y?usp=sharing).

---

## *Details*

### *Fix to the first-visit modal button logic*

> **What was implemented**
>
- **Problem**
    - The "Start with sample data" button was shown on both the first visit and return visits
    - On a return visit, clicking "Start with sample data" actually loaded the autosaved content
- **Solution**
    - When saved data exists: show the "Load autosaved content" button
    - When no saved data exists: show the "Start with sample data" button
    - `updateAllTexts()` no longer overwrites the text while the modal is already shown
    - Works the same in all supported languages (Korean, English, Japanese, Spanish, Portuguese)

> **Technical details**
>
- Added a guard in `updateAllTexts()` so modal text is not updated while the modal is already displayed
- `handleScoringTabFirstLoad()` checks whether saved data exists and sets the modal text
- With saved data, `modalLoadBtn.textContent` is set to `t('modal_welcome_load_saved')`
- Without saved data, `modalLoadBtn.textContent` is set to `t('modal_welcome_load')`
- `updateAllTexts()` itself also checks for saved data and sets the modal text (in case it runs before the modal is shown)

**Files**: `index.html` (lines 2387–2426: updateAllTexts; lines 3974–4060: handleScoringTabFirstLoad)

### *First-visit modal UI improvement*

> **What was implemented**
>
- **Title removed**
    - When saved data exists, the "Continue your work" title is hidden and only the message "There is content from your last session." is shown
    - Avoids saying the same thing twice
- **Message style changed**
    - When saved data exists, the message is shown in large bold black text (18px)
    - Before: small gray text
    - After: large bold black text (font-weight: bold, font-size: 18px, color: #212529)
- **First visit**
    - Without saved data, both the title and the message are shown as before
    - The message keeps its default style (small, gray)

> **Technical details**
>
- `handleScoringTabFirstLoad()` sets `modalTitle.style.display = 'none'` when saved data exists
- With saved data, inline styles (fontWeight, fontSize, color) are applied to `modalMessage`
- Without saved data, `modalTitle.style.display = 'block'` is set and the message style is reset
- The same logic is applied in `updateAllTexts()`

**Files**: `index.html` (lines 3987–3993, 4049–4054, 2403–2409, 2413–2424)

### *Static style refactoring*

> **What was implemented**
>
- **Problem**
    - Inline styles remained in `index.html`, making maintenance hard
    - CSS and HTML were not separated, so several files had to be checked to change a style
- **Solution**
    - All static styles (not controlled dynamically by JavaScript) were moved to `styles.html`
    - Styles controlled dynamically by JavaScript (`display: none`, etc.) stay in `index.html`
- **Styles moved**
    - `text-align: center` of modal titles/messages → added to `#reset-modal-title`, `#reset-modal-message`, `#ai-modal-title`, `#ai-modal-message`
    - Guide text style → added to `#Scoring_Summary > p`
    - Flex style of the info-icon wrapper → added to `.row-controls > div`
    - hr style → added to `#Notice hr`
    - Table width → added to `#list-table-body table`
    - colgroup width → added to `#list-table-body colgroup col:nth-child()`

> **Technical details**
>
- Inline style attributes removed from `index.html`
- CSS rules for those selectors added to `styles.html`
- Modal styles added to section 8.0
- More-tab styles added to sections 4.4 and 4.5
- Shared component styles added to section 2.1

**Files**:

- `index.html` (lines 212–213, 224–225, 263, 271–275, 287, 325: inline styles removed)
- `styles.html` (lines 1306–1311: modal styles; 655–666: table styles; 667–669: hr styles; 244–250: shared component styles)

### *Table of contents and comment clean-up*

> **Table of contents**
>
- **Changes**
    - Duplicate entries removed (10.31 appeared twice)
    - Order matched to the actual code order
    - New styles reflected in the `styles.html` table of contents
        - `#Scoring_Summary > p` and `.row-controls > div` added to 2.1
        - 4.4 and 4.5 added (table width/columns, divider)
        - Modal IDs added to 8.0
- **Verification**
    - Every table-of-contents comment matches the actual code position
    - The code structure can be read accurately from the table of contents

> **Unnecessary inline comments removed**
>
- **Types of comments removed**
    - Explanatory comments obvious from the code itself
        - e.g. `// 모달이 이미 표시되어 있으면 모달 텍스트는 업데이트하지 않음`
        - e.g. `// (handleScoringTabFirstLoad에서 이미 설정했을 수 있음)`
        - e.g. `// 저장된 데이터 유무에 따라 환영 모달 텍스트 설정`
        - e.g. `// '항목' 열에 내용이 있으면 새 카테고리`
        - e.g. `// "Card (카드)" -> "Card"`
        - e.g. `// Excel에서 한글이 깨지지 않도록 BOM(Byte Order Mark)을 추가합니다.`
- **Important comments kept**
    - Section divider comments (e.g. `// 10.1.5. 모든 텍스트 업데이트 함수`)
    - Comments that explain a technical reason

**Files**:

- `index.html` (lines 119–172: table of contents; 2387–2426: comments removed)
- `styles.html` (lines 47–107: table of contents)

### *More-tab card hover effect*

> **What was implemented**
>
- **Stronger shadow**
    - Before: `box-shadow: 0 4px 8px rgba(0,0,0,0.1)`
    - After: `box-shadow: 0 8px 24px rgba(0,0,0,0.25)` (darker, larger shadow)
- **Clearer background image**
    - On hover, the background image opacity rises from 0.12 to 0.35
    - `filter: saturate(1.2) contrast(1.1)` applied for stronger color
- **Text blur**
    - On hover, `filter: blur(2px)` and `opacity: 0.6` applied to the text inside the card
    - The text is blurred so the background image stands out
- **Transition**
    - `transition` applied to every effect for smooth animation

> **Technical details**
>
- Shadow, background opacity, and filter effects added to `.link-button:hover`
- Filter effect added to `.link-button:hover::before` (clearer background image)
- Filter and opacity effects added to `.link-button:hover > *` (text blur)
- `transition` (0.25s ease) added to every effect

**Files**: `styles.html` (lines 1357–1375: hover effects)

### *Changes by file*

> **index.html**
>
- **Main changes**
    - First-visit modal button logic fixed
    - Modal UI improved (title removed, message style changed)
    - Static inline styles removed
    - Table of contents and comments tidied
    - Version information unchanged (stays v1.4.0)
- **Code statistics**
    - Total lines: about 4,839
    - Main functions: 35
    - Table-of-contents sections: 35 (all match the code)

> **styles.html**
>
- **Main changes**
    - Static styles added (modal, table, hr, shared components)
    - More-tab card hover effect improved
    - Table of contents updated
    - Version information unchanged (stays v1.4.1)
- **Code statistics**
    - Total lines: about 1,561
    - CSS variables: 33 (group colors)

> **Code.gs**
>
- **Main changes**
    - No change
- **Code statistics**
    - Total lines: about 1,174

### *Testing and verification*

> **Functional tests**
>
- ✅ "Start with sample data" button shown on the first visit
- ✅ "Load autosaved content" button shown on a return visit (saved data present)
- ✅ Each button performs the correct action
- ✅ With saved data, the title is hidden and only the message is shown
- ✅ With saved data, the message is shown in large bold black text
- ✅ Behaves the same in every supported language
- ✅ More-tab card hover effect confirmed (shadow, background image, text)

> **UI/UX checks**
>
- ✅ Modal button text changes correctly with the saved state
- ✅ Modal message style changes correctly with the saved state
- ✅ More-tab card hover effect runs smoothly

> **Code quality checks**
>
- ✅ Table-of-contents comments match the code
- ✅ Unnecessary inline comments removed
- ✅ Static styles correctly moved to `styles.html`
- ✅ Inline styles minimized
- ✅ Code structure improved

---

# Roadmap

The program will be monitored continuously and further bugs fixed as they are found.

## Source files

- `source/Code.gs`
- `source/index.html`
- `source/styles.html`

## How to use

To reproduce this version, create files with the same names in a Google Apps Script project and paste in the files from `source/` as they are.
Deploying the GAS project as a web app runs that version of the calculator directly.
