# Codex Prompt: Research Component

You are working in `C:\Users\LJ\GitHub\KICAD_ENGINE` from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`, `.prompts/shared/DATASHEET_SUMMARY_STANDARD.md`, `06_DATASHEETS/00_INDEX/RESEARCH_PIPELINE.md`, and `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`.

## Goal

Research component:

- Part number: `[PART_NUMBER]`
- Vendor: `[VENDOR_OR_UNKNOWN]`
- Intended use: `[INTENDED_USE]`

## Restrictions

- Do not download datasheets unless the user explicitly approves.
- Do not scrape aggressively.
- Do not fabricate voltage/current/pin/package/layout claims.
- Do not assert a KiCad footprint is correct without exact package drawing verification.
- Do not edit KiCad project files.

## Required Workflow

1. Prefer official vendor sources.
2. Record source links and dates.
3. Summarize only verified facts.
4. Mark unknowns as `Unknown - requires source verification`.
5. Identify KiCad symbol and footprint candidates as candidates only.
6. Record datasheet copyright/redistribution status.

## Output

Create a research summary under `02_HISTORY/design_reviews` or the appropriate datasheet/component folder. Include history log, source links, verification flags, unknowns, and recommended next research.

## Universal Safety Requirements

- If research leads to KiCad source edits, stop and require active project confirmation, backup, rollback plan, verification plan, and history log.
- Produce a verification-status section for all major datasheet, package, pinout, and lifecycle claims.
- Do not fabricate datasheet claims, electrical limits, package data, lifecycle status, or source URLs.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL`; this research prompt should not create fabrication outputs.
