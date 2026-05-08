# Knowledge Base Reference Design Setup Session

Date: 2026-05-02
Scope: Prompt 4 reusable knowledge base and reference design library setup.

## Startup Reads

- Read `AGENTS.md`.
- Read `09_ACCURACY_ENGINE/README.md`.
- Inspected `10_KNOWLEDGE_BASE`.
- Inspected `12_REFERENCE_DESIGN_LIBRARY`.

## Work Completed

- Confirmed the requested `10_KNOWLEDGE_BASE` folder structure already existed.
- Confirmed the requested circuit files already existed.
- Added missing `10_KNOWLEDGE_BASE/common_mistakes/PIC_COMMON_MISTAKES.md`.
- Updated knowledge-base README and index with the Prompt 4 core circuit and common-mistake file set.
- Confirmed the requested `12_REFERENCE_DESIGN_LIBRARY` folder structure existed.
- Updated the reference-design index, schema, template, public-source rules, and verification levels to use `VERIFIED`, `PARTIALLY_VERIFIED`, `LINK_ONLY`, and `UNVERIFIED`.
- Added official/vendor source portal entries as `LINK_ONLY` records.
- Updated `README_GPT.md` and `FOR CHAT GPT.MD`.

## Safety Results

- No KiCad design files were edited.
- No datasheets or proprietary reference files were downloaded.
- No installers or package managers were run.
- No secrets were added.
- Health check passed with `PASS=131 WARN=0 FAIL=0`.

## Remaining Follow-Up

- Create individual reference records when a specific source is used for a design decision.
- Promote source records beyond `LINK_ONLY` only after source, revision, license, and engineering evidence review.
- Keep exact values out of reusable guidance unless source citations are recorded.

