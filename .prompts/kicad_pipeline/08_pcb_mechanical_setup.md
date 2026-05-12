# 08 PCB Mechanical Setup

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: set up PCB mechanical constraints before placement and routing. Do not route traces.

## Mandatory Phase Gate

This is Phase 4. Before doing anything, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project "[ACTIVE_PROJECT_PATH]" --phase 4`

If the result is `BLOCKED`, stop and report the missing earlier phase. A missing `.kicad_pcb` or missing `reports/PCB_SYNC_STATUS.md` blocks this task.

## Read First

1. `AGENTS.md`
2. `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
3. Active project mechanical notes
4. `09_ACCURACY_ENGINE/pcb_rules/PCB_CREATION_STANDARD.md`
5. `34_PCB_LAYOUT_SANDBOX/PCB_WORK_AUTO_START_RULES.md`
6. `layout_sandbox/SELECTED_LAYOUT_PLAN.md`
7. `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md`
8. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
9. `08_COMPONENT_DATABASE/mechanical_orientation/README.md`
10. `08_COMPONENT_DATABASE/mechanical_orientation/connector_orientation_truth.json`

## Preconditions

- PCB exists and is synced.
- Auto PCB start status is not blocked.
- Board size, layer count, stackup, mounting holes, connector edge constraints, and antenna/mechanical constraints are source-backed or user-confirmed.
- Connector and antenna orientation truth are source-backed or blocked.

If board size is unknown, stop with `AUTO_PCB_START_BLOCKED` and create `reports/BOARD_SIZE_NEEDS_USER_REVIEW.md`.

## Do

1. Create backup.
2. Set board outline, layer/constraint setup, mounting holes, keepouts, antenna keepout, connector/mechanical areas, and board notes according to the auto-approved selected layout plan.
3. Run connector-orientation and ESP32-antenna orientation audits in dry-run mode and attach the results to the mechanical setup report.
4. Run DRC.
5. Export board visual evidence.
6. Create `reports/PCB_MECHANICAL_SETUP_REPORT.md`.

## Required Result

Return one result:

- `MECHANICAL_SETUP_PASS`
- `MECHANICAL_SETUP_FAIL`
- `AUTO_PCB_START_BLOCKED`

AI quality closeout is required.
