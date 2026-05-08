# Codex Prompt: Plan Schematic

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`, `03_TOOLS/kicad_app_intelligence/KICAD_AGENT_TASK_MAP.md`, and relevant `01_MEMORY`/`02_HISTORY`.

## Goal

Plan schematic for:

- Project ID: `[project-id]`
- Feature/block: `[SCHEMATIC_BLOCK]`

## Restrictions

- Planning only unless user explicitly approves source edits.
- Do not edit `.kicad_sch`, `.kicad_pro`, libraries, or PCB files.
- Do not choose final footprints without package drawing verification.
- Do not invent datasheet facts.

## Required Workflow

1. Confirm active project and requirements.
2. Identify parts, datasheets, power rails, connectors, interfaces, protection, and programming/debug needs.
3. Identify symbol and footprint candidates as candidates only.
4. List ERC/DRC/BOM checks needed after future edits.
5. Identify backup requirements before any future schematic edit.

## Output

Create a schematic plan/review note in `02_HISTORY/design_reviews` or project history. Include risks, unknowns, verification plan, and next steps.

## Universal Safety Requirements

- Do not modify schematic, PCB, symbol, footprint, project, or fabrication-output files during planning.
- Require active project confirmation, backup, rollback plan, verification plan, and history log before future KiCad source edits.
- Do not fabricate datasheet claims, part limits, pinouts, package data, or lifecycle status.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
