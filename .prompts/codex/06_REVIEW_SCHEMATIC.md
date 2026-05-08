# Codex Prompt: Review Schematic

You are working in `C:\Users\LJ\GitHub\KICAD_ENGINE` from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, and relevant project memory/history.

## Goal

Review schematic for:

- Project path: `[PROJECT_PATH]`
- Review focus: `[POWER/MCU/USB/CAN/CONNECTORS/ALL]`

## Restrictions

- Read-only review unless user separately approves fixes.
- Do not edit schematic, project, libraries, or PCB.
- Do not assert datasheet compliance without source evidence.
- Do not assert footprints are correct from schematic fields alone.

## Required Workflow

1. Confirm active project and project path.
2. Parse schematic and library references read-only.
3. Run project validation and ERC availability checks where safe.
4. Check power, connectors, polarity, datasheet coverage, and symbol candidates.
5. Run ERC if the project gate allows read-only verification.
6. Write a review report and history log.

## Output

Provide findings ordered by severity with file references, ERC/report paths if run, unresolved risks, and recommended next steps.

## Universal Safety Requirements

- Do not modify schematic, PCB, symbol, footprint, project, or fabrication-output files during review unless explicitly requested and backup gates pass.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source edit.
- Produce a verification report or explain why ERC/checks could not run.
- Do not fabricate datasheet claims, pinouts, electrical limits, package data, or verification status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
