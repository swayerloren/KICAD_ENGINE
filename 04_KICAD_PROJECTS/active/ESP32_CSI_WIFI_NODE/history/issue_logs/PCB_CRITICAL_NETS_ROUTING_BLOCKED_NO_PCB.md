# PCB_CRITICAL_NETS_ROUTING_BLOCKED_NO_PCB

Status: `OPEN`

Severity: `HIGH`

Date opened: 2026-05-03

## Issue

Critical-net routing cannot begin for `ESP32_CSI_WIFI_NODE`.

## Evidence

- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
- `reports/PCB_ROUTING_PLAN.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- `reports/COPPER_ZONE_STRATEGY_REPORT.md`

## Blocking Conditions

- No `.kicad_pcb` exists.
- Schematic-to-PCB gate is not `PASS`.
- Placement pass 2 is not `PASS`.
- Copper-zone strategy is not `PASS`.
- Routing plan is not `READY`.

## Required Resolution

Complete schematic-to-PCB gate closure, PCB update, mechanical setup, placement, via strategy, and zone strategy before routing critical nets.

