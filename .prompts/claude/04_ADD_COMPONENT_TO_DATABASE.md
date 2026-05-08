# Claude Prompt: Add Component To Database

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before editing the component database:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `08_COMPONENT_DATABASE/00_INDEX/COMPONENT_DATABASE_README.md`
4. `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`
5. `08_COMPONENT_DATABASE/00_INDEX/VERIFICATION_LEVELS.md`
6. `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`
7. `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`
8. `06_DATASHEETS/00_INDEX/NAMING_CONVENTIONS.md`
9. `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`
10. `.prompts/shared/SAFETY_GATES.md`

## Goal

Add or update structured component records without overstating verification.

## Universal Requirements

- Do not modify KiCad project files.
- Back up any existing database record before replacing or substantially rewriting it.
- If scope changes to KiCad source edits, stop and require active project confirmation, backup, rollback plan, verification plan, and history log.
- Record database changes in `02_HISTORY/`.
- Produce a verification report listing verified, unverified, and missing fields.
- Do not fabricate datasheet claims.
- Do not mark a footprint verified unless exact manufacturer package drawing and KiCad footprint geometry have been checked.
- Label any manufacturing-style output `NOT_FINAL`; this prompt should not create fab outputs.

## Workflow

1. Locate the correct category under `08_COMPONENT_DATABASE/`.
2. Check for an existing record and preserve it with a backup if replacing content.
3. Use the canonical schema and verification flags.
4. Add both markdown and JSON records when the category uses both.
5. Link local datasheet paths only when files actually exist.
6. Use source URL placeholders when the source has not been verified.
7. Mark unknown exact values as `Unknown - requires source verification`.

## Output

Report:

- Files created or updated.
- Verification flags used.
- Datasheet/source status.
- KiCad symbol/footprint candidate status.
- Remaining missing information.
- History log path.
