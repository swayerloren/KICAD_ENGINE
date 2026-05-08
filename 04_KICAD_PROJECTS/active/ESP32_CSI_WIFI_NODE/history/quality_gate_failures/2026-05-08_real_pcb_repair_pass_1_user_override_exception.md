# Quality Gate Exception - Real PCB Repair Pass 1

Date: `2026-05-08`

Status: `HUMAN_REVIEW_REQUIRED`

## Affected Gates

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`

## Reason

The user explicitly requested a real repair pass on the live board after the maintenance/state layer proved that the PCB exists, placement exists, and partial routing exists. Live phase checks allow phase 2 and phase 3 by file evidence even though the older formal gate markdown still records blocked states.

## Live Evidence

- `reports/LIVE_PCB_TRUTH_AUDIT.md`
- `reports/PCB_FILE_CURRENT_STATE.md`
- `reports/CURRENT_EXISTING_TRACE_AUDIT.md`
- `reports/ROUTING_CURRENT_STATE_REPORT.md`
- `reports/MAINTENANCE_LAYER_TEST_REPORT.md`
- `reports/LIVE_PROJECT_STATE.json`

## Risks

- board-level edits are proceeding before the older formal gate files are fully normalized to `PASS`
- the current board still has DRC failures, unrouted nets, and incomplete ground strategy
- any repair made in this pass remains `NOT_FAB_READY` and requires human review

## Scope

- allowed: targeted repair of the live `.kicad_pcb` and related project DRC rule if required
- not allowed: schematic edits, full routing completion, fabrication export, or fabrication-ready claims
