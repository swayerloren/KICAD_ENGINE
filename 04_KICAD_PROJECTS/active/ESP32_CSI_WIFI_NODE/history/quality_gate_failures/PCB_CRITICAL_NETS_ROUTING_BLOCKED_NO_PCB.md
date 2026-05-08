# PCB_CRITICAL_NETS_ROUTING_BLOCKED_NO_PCB

Status: `QUALITY_GATE_BLOCKED`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

Date: 2026-05-03

## Gate

Critical-net PCB routing gate.

## Failure

Critical-net routing is blocked because the required PCB and routing preconditions are not met.

## Blocking Evidence

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`: gate result `FAIL`.
- `reports/PCB_ROUTING_PLAN.md`: final result `ROUTING_PLAN_BLOCKED`.
- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`: final result `PLACEMENT_ORIENTATION_FAIL`.
- `reports/COPPER_ZONE_STRATEGY_REPORT.md`: final result `ZONE_SETUP_FAIL`.
- Active project `kicad/` folder: no `.kicad_pcb`.

## Required Human Review

Human review remains required for footprints, connector orientation, polarity, USB policy, RF/antenna keepout, regulator layout, mechanical constraints, and all high-risk `NEEDS_REVIEW` items before routing can start.

