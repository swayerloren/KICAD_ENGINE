# Workflows Index

This file indexes the main workflows KiCad Engine provides for AI-assisted KiCad work.

These workflows are general repo capabilities, not instructions for only one board.

## ZIP / Local Startup Workflow

1. Download ZIP or clone the repo.
2. Open `KICAD_ENGINE` in VS Code.
3. Open Codex or Claude.
4. Paste the starter prompt from `README.md` or `ONE_PROMPT_START.md`.
5. Let the agent read `00_CODEX_START/START_HERE.md`.

## New Project Workflow

1. Create a folder under `04_KICAD_PROJECTS/active/<PROJECT_NAME>`.
2. Add or create KiCad project files there.
3. Ask the AI agent to read the startup stack and identify the active project.
4. Use the repo's task contracts, validation rules, and reporting structure for that project.

## Existing Project Review Workflow

1. Identify the active project path under `04_KICAD_PROJECTS/active`.
2. Read startup and safety docs first.
3. Inspect the live KiCad files and current reports.
4. Classify the task as docs-only, audit-only, or edit-required before changes.

## Project State Workflow

- build live state:
  - `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project <ACTIVE_PROJECT_PATH> --apply`
- detect stale reports:
  - `python 03_TOOLS/scripts/project_state/detect_stale_reports.py --project <ACTIVE_PROJECT_PATH> --apply`
- reconcile gates:
  - `python 03_TOOLS/scripts/project_state/reconcile_project_gates.py --project <ACTIVE_PROJECT_PATH> --apply`

## Schematic Workflow

- read startup and safety files first
- use `03_TOOLS/scripts/kicad_schematic_checks/`
- review reports under the project `reports/` folder
- run or review ERC before downstream PCB phases

## PCB Placement Workflow

- check phase eligibility:
  - `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`
- review `34_PCB_LAYOUT_SANDBOX/` first
- require planning, variant, and gate evidence before real board edits

## PCB Routing Workflow

- read `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`
- read `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`
- use copied-board rehearsal when appropriate
- apply only clean, auditable routing changes to the live board

## Validation Workflow

- ERC for schematic changes
- DRC for PCB changes
- geometry/routing audits for routing work
- visual review and blocker review before fabrication-style claims

## Manufacturing Support Workflow

- prepare Gerbers, drill files, BOM, and CPL only after the correct gates pass
- use the repo's JLCPCB and PCBWay-oriented checklists and profiles
- keep fabrication outputs `NOT_FINAL` until human review is complete

## Repo Maintenance Workflow

- maintenance cycle:
  - `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>`
- index rebuilds:
  - `python 03_TOOLS/scripts/indexing/build_repo_index.py`
  - `python 03_TOOLS/scripts/indexing/build_memory_index.py`
  - `python 03_TOOLS/scripts/indexing/build_history_index.py`

## GitHub / Docs Workflow

- stage safe docs, scripts, and config files only
- do not stage hidden envs, logs, backups, or temp payloads
- keep the repo portable for ZIP -> VS Code -> prompt use
