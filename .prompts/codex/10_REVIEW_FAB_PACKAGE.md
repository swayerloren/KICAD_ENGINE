# Codex Prompt: Review Fabrication Package

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, and relevant fabrication/verification history.

## Goal

Review fabrication package:

- Package path: `[PACKAGE_PATH]`
- Source project path: `[PROJECT_PATH_OR_UNKNOWN]`

## Restrictions

- Read-only review.
- Do not modify Gerbers, drills, BOM, PNP, or project files.
- Do not claim fab readiness unless every gate has evidence and user approval.

## Required Workflow

1. Inventory package files.
2. Check for `NOT_FINAL` labeling and manifest.
3. Compare available outputs to source project when possible.
4. Check ERC, DRC, BOM, PNP, Gerber, drill, STEP, connector, polarity, and mechanical review evidence.
5. Identify missing files and review blockers.
6. Write fabrication review report and history log.

## Output

Classify as `EXPORTED_NOT_FINAL`, `HUMAN_REVIEW_REQUIRED`, or `FAB_READY_BY_USER_APPROVAL`. Include evidence and blockers.

## Universal Safety Requirements

- Do not modify KiCad source files or generated fabrication files during review unless explicitly requested and backup gates pass.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source or output edit.
- Produce a verification report with evidence and missing gates.
- Do not fabricate ERC, DRC, BOM, datasheet, footprint, visual-review, or manufacturer-rule status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Treat all manufacturing-style outputs as `NOT_FINAL` unless the full verification gate passed and the user explicitly approved final status.
