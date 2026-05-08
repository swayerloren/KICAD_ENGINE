# Codex Prompt: Review PCB

You are working in `C:\Users\LJ\GitHub\KICAD_ENGINE` from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, `03_TOOLS/kicad_library_intelligence/HIGH_RISK_FOOTPRINTS.md`, and relevant project history.

## Goal

Review PCB for:

- Project path: `[PROJECT_PATH]`
- Review focus: `[DRC/FOOTPRINTS/CONNECTORS/RF/POWER/ALL]`

## Restrictions

- Read-only review unless user separately approves fixes.
- Do not edit `.kicad_pcb`, footprints, libraries, or outputs.
- Do not assert a footprint is correct without exact package drawing verification.
- Do not use GUI control unless explicitly approved.

## Required Workflow

1. Confirm active project and path.
2. Run read-only project validation.
3. Inspect footprint assignments, missing models, high-risk footprints, connectors, RF keepouts, polarity, and mechanical risks.
4. Run DRC if allowed.
5. Generate a review report and history log.

## Output

Provide severity-ordered findings, DRC/report paths if run, human-review items, and next steps. Do not call the PCB fabrication-ready.

## Universal Safety Requirements

- Do not modify PCB, schematic, symbol, footprint, project, or fabrication-output files during review unless explicitly requested and backup gates pass.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source edit.
- Produce a verification report or explain why DRC/checks could not run.
- Do not fabricate datasheet claims, layout constraints, package data, or verification status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
