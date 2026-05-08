# Claude Prompt: Research Component

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before researching:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `06_DATASHEETS/00_INDEX/RESEARCH_PIPELINE.md`
4. `06_DATASHEETS/00_INDEX/PUBLIC_RELEASE_DATASHEET_POLICY.md`
5. `06_DATASHEETS/00_INDEX/SOURCE_PRIORITY_RULES.md`
6. `06_DATASHEETS/00_INDEX/NAMING_CONVENTIONS.md`
7. `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`
8. `08_COMPONENT_DATABASE/00_INDEX/VERIFICATION_LEVELS.md`
9. `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`
10. `.prompts/shared/DATASHEET_SUMMARY_STANDARD.md`
11. `.prompts/shared/SAFETY_GATES.md`

## Goal

Research a component and create AI-readable notes that distinguish verified facts from placeholders.

## Universal Requirements

- Do not modify KiCad project files.
- If research leads to project edits, stop and require active project confirmation, backup, verification plan, rollback plan, and history log.
- Record research sources and findings in `02_HISTORY/` or the appropriate database path.
- Produce a verification-status section for every researched claim.
- Do not fabricate datasheet values, pinouts, electrical limits, lifecycle status, package dimensions, or application constraints.
- Do not approve footprints without exact manufacturer package drawings.
- Label any generated manufacturing-style output `NOT_FINAL`; this prompt should not create fab outputs.

## Source Rules

Prefer:

1. Official manufacturer product pages.
2. Official datasheets, reference manuals, errata, app notes, package drawings, and reference designs.
3. Official GitHub or vendor CAD/reference repositories.
4. Distributor pages only for availability/lifecycle hints, clearly marked.
5. Community sources only as unverified context.

Do not download or bundle PDFs unless redistribution permission is clear.

## Output

Create or update research notes with:

- Part number, vendor, family, package, category.
- Source links and source confidence.
- Verified and unverified fields.
- Datasheet/source document list.
- KiCad symbol and footprint candidates marked as candidates only.
- Common mistakes and AI warnings.
- Missing information and next verification steps.
