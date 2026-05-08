# Codex Prompt: Export NOT_FINAL Package

You are working in `C:\Users\LJ\GitHub\KICAD_ENGINE` from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, and relevant ERC/DRC history.

## Goal

Export review-only manufacturing-style package for:

- Project path: `[PROJECT_PATH]`
- Target output: `[GERBERS/DRILLS/BOM/PNP/STEP/ALL]`

## Restrictions

- Do not call outputs final.
- Do not overwrite prior outputs.
- Do not skip ERC/DRC status reporting.
- Do not edit project source.

## Required Workflow

1. Confirm active project, output folder, and source files.
2. Check recent ERC/DRC/project validation status.
3. Export into timestamped folder containing `NOT_FINAL`.
4. Include manifest and report paths.
5. Mark unresolved checks as `HUMAN_REVIEW_REQUIRED`.
6. Write history log.

## Output

Return output folder, generated files, verification status, missing gates, and human-review blockers.

## Universal Safety Requirements

- Do not modify KiCad source files while exporting review outputs.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source edit.
- Record exact export commands, generated paths, and limitations in `02_HISTORY`.
- Do not fabricate ERC, DRC, BOM, datasheet, footprint, or visual-review status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output folder, archive, and manifest `NOT_FINAL` until the full verification gate passes.
