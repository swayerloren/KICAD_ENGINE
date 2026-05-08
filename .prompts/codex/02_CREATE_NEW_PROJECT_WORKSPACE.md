# Codex Prompt: Create New Project Workspace

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `00_CODEX_START/START_HERE.md`, `00_CODEX_START/PROJECT_INDEX.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, and `03_TOOLS/kicad_app_intelligence/KICAD_AGENT_TASK_MAP.md`.

## Goal

Create a new KiCad Engine project workspace for:

- Project ID to confirm: `[project-id]`
- Purpose: `[PROJECT_PURPOSE]`

## Restrictions

- Do not create `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, symbols, footprints, or fabrication outputs unless explicitly requested.
- Do not edit existing KiCad project files.
- Do not install tools.

## Required Workflow

1. Confirm project name and target path under `04_KICAD_PROJECTS/active`.
2. Create only safe workspace folders and planning files.
3. Record requirements as known/unknown.
4. Update indexes only if requested or established workflow requires it.
5. Write a session log in `02_HISTORY/sessions`.

## Output

Report created folders/files, remaining requirements, next design step, and verification gates required before schematic/PCB creation.

## Universal Safety Requirements

- Require backup before modifying any existing KiCad source, symbol, footprint, project, or fabrication-output file.
- Record meaningful workspace decisions and command results in `02_HISTORY`.
- Produce a verification checklist or report before any future schematic or PCB work.
- Do not fabricate datasheet claims, part limits, lifecycle status, or package data.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
