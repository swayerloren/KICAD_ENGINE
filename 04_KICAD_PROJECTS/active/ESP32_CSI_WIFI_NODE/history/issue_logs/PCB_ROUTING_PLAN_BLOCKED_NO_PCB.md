# PCB_ROUTING_PLAN_BLOCKED_NO_PCB

Status: `OPEN`

Severity: `HIGH`

Date opened: 2026-05-03

## Issue

Routing cannot begin for `ESP32_CSI_WIFI_NODE`.

## Evidence

- `reports/PCB_ROUTING_PLAN.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
- `reports/COPPER_ZONE_STRATEGY_REPORT.md`

## Blocking Conditions

- Schematic-to-PCB gate is not `PASS`.
- No `.kicad_pcb` exists.
- No board outline exists.
- Placement has not passed.
- Hole/test-pad/via strategy has not passed.
- Copper-zone strategy has not passed.
- Footprints are not assigned and verified to exact package drawings.

## Required Resolution

Complete the schematic-to-PCB gate, PCB update, mechanical setup, placement, hole/test-pad/via strategy, and copper-zone strategy before routing.

