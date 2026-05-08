# Codex Prompt: Run ERC/DRC

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, and `03_TOOLS/scripts/project_validation/README.md`.

## Goal

Run verification for:

- Project path: `[PROJECT_PATH]`
- Checks: `[ERC/DRC/BOTH/PROJECT_VALIDATION]`

## Restrictions

- Do not edit project source.
- Do not export manufacturing outputs unless explicitly requested.
- Do not mark results final.

## Required Workflow

1. Confirm active project and path.
2. Use read-only validation first when appropriate.
3. Run `run_erc.ps1` and/or `run_drc.ps1` with quoted paths.
4. Save reports under `02_HISTORY/erc_drc_reports` or approved output folder.
5. Record command outcomes in history.

## Output

Summarize pass/warn/fail status, report paths, key violations, and remaining non-ERC/DRC review risks.

## Universal Safety Requirements

- Do not modify schematic, PCB, symbol, footprint, project, or fabrication-output files while running ERC/DRC.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source edit.
- Record exact commands, exit codes, report paths, and limitations in `02_HISTORY`.
- Do not fabricate datasheet, ERC, DRC, BOM, footprint, or visual-review status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL`; ERC/DRC reports are review artifacts, not fab approval.
