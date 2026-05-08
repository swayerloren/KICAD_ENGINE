# Codex Prompt: Add Component To Database

You are working in `C:\Users\LJ\GitHub\KICAD_ENGINE` from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`, `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`, `08_COMPONENT_DATABASE/00_INDEX/VERIFICATION_LEVELS.md`, and `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`.

## Goal

Add or update component database record for:

- Part number: `[PART_NUMBER]`
- Category: `[CATEGORY]`

## Restrictions

- Do not invent exact specifications.
- Do not promote `UNVERIFIED_PLACEHOLDER` records without evidence.
- Do not mark footprints verified without exact package drawing comparison.
- Do not edit KiCad project files.

## Required Workflow

1. Load existing component records and indexes.
2. Use verified source evidence or mark unknowns.
3. Include KiCad symbol, footprint, and 3D model candidates as candidates only.
4. Add warnings, common mistakes, layout notes, required external parts, and verification flags.
5. Update the master component index if appropriate.
6. Write session/history notes.

## Output

Return changed files, verification status, unresolved unknowns, and next verification steps.

## Universal Safety Requirements

- Back up existing database records before replacing or substantially rewriting them.
- If scope changes to KiCad source edits, stop and require active project confirmation, backup, rollback plan, verification plan, and history log.
- Record component database changes in `02_HISTORY`.
- Do not fabricate datasheet claims, electrical limits, package data, source URLs, or lifecycle status.
- Do not mark a footprint verified unless the exact part package and manufacturer drawing have been checked.
- Label every generated manufacturing-style output `NOT_FINAL`; this database prompt should not create fabrication outputs.
