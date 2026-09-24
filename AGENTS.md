# Public Archive Working Rules

These instructions apply to the public showcase repository.

## Repository Boundary

- This repository is a curated public archive, not the private production source.
- Never add private paths, local file names, secrets, API keys, raw prompts, unpublished source materials, private payloads, or internal work notes.
- Do not change application UI, calculation logic, corpus content, embeddings, or deployment state while performing a documentation-only task.

## Public Writing

- Read `v2-nextjs/source/docs/ops/PUBLIC_RELEASE_DOCUMENTATION.md` before editing reader-facing documents.
- The repository-root README in all five languages is a short introduction to the **latest released version only**. At every release, replace its version, app link, current offer, and release-note/evidence links; do not append older versions, release lists, or historical feature summaries. Keep history in `CHANGELOG*` and the version directories. Review all five README files together before publishing.
- Read the complete v1 GAS release-note series before a repository-wide voice rewrite. For routine work, also read the latest two v2 notes, the root README, and the root CHANGELOG.
- Treat the owner-authored v1 GAS patch notes as protected historical originals. Do not rewrite, modernize, or shorten them. Revert a later non-owner insertion only when an exact preserved original proves the difference; otherwise obtain the owner's explicit approval before any v1 edit.
- Write the released product story, not the draft history. Do not narrate agent conversations, internal approval, rejected drafts, or audience strategy.
- Explain the visible or clinical effect first, followed by the affected condition, recalculation guidance, evidence, and limitations. Keep internal verification procedures and technical operations out of reader-facing release notes.
- Correct archive metadata, ordering, formatting, and inaccurate public prose quietly. Never add dated correction banners or narrate documentation cleanup, test reruns, database or credential handling, build gates, deployment preparation, or mirror synchronization in reader-facing prose.

## Five-Language Contract

- Korean is the factual canonical locale. Managed companions are English, Japanese, neutral Spanish, and Brazilian Portuguese.
- Follow `docs/localization/PUBLIC_DOCUMENT_LOCALIZATION.md` and `docs/localization/RELEASE_DOCUMENT_WORKFLOW.md`.
- Use `docs/localization/clinical-terminology.json` and verify uncertain wording against `docs/localization/TERMINOLOGY_SOURCES.md` plus independent authoritative research.
- Add every managed group to `docs/localization/manifest.json`. Keep new or changed groups in `draft` until factual parity and independent target-language review are complete.
- Run `scripts/verify-public-document-locales.ps1 -AllowDraft` while editing. Publication requires the strict command without `-AllowDraft` to pass.
- A request-level technical evidence ledger may remain in one language when its findings are summarized and linked from the five reader-facing release notes; do not disguise such a ledger as a translated reader-facing report.
- Do not commit, push, open a pull request, publish a release, or deploy unless the user explicitly requests it.

## Versioned Rights

- Read `LICENSES.md` before changing license, attribution, or publication scope. Keep a license and copyright notice in each published version directory; do not use the repository-root license alone to imply that one party owns every version.
- Preserve existing MIT grants and original notices for previously published work. Attribute SICP and MOW only for their respective contributions. A different license for a future, newly published work requires an explicit rights decision and cannot retroactively withdraw the MIT permission already granted for earlier copies.
- Publishing new v3 operating source requires a separate secret, patient-data, third-party-rights, and ownership review. Documentation under `v3-web/` does not imply that the private operating source has been published or licensed.

## AI Model Provenance

- Before each AI experiment or AI-assisted document review, record the provider, exact public model name and API/CLI model ID, version, reasoning/thinking setting, processing tier, assigned role, and how the setting was verified. Preserve the observed usage and cost basis afterward.
- Spell out model generations in comparisons (for example, `GPT-5.6 Terra` and `GPT-6 Luna`). Do not label a result only `Terra`, `Sol`, or `Luna` when multiple generations could be confused.
- Separate model defaults from explicitly supplied settings. If the model ID, thinking level, tier, or actual charge cannot be verified, write `not captured` or `unknown`; never infer it from a product name or current defaults.
- Keep the run-by-run technical ledger in public benchmark evidence or a private source record as appropriate. Reader-facing release notes must link to that ledger and accurately distinguish model-generated draft, AI review, and human clinical review.
