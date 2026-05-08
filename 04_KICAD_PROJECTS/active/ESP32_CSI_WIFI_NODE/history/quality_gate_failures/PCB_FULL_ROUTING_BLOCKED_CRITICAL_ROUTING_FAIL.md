# PCB_FULL_ROUTING_BLOCKED_CRITICAL_ROUTING_FAIL

Status: `QUALITY_GATE_BLOCKED`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

Date: 2026-05-03

## Gate

Full PCB routing gate.

## Failure

Full routing is blocked because critical routing is not pass/acceptable.

## Blocking Evidence

- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`: `CRITICAL_ROUTING_FAIL`
- `reports/PCB_ROUTING_PLAN.md`: `ROUTING_PLAN_BLOCKED`
- Active project `kicad/` folder: no `.kicad_pcb`

## Required Human Review

Human review remains required for all upstream schematic-to-PCB, footprint, placement, via, zone, critical-routing, and PCB verification gates before full routing.

