# PCB_FULL_ROUTING_BLOCKED_CRITICAL_ROUTING_FAIL

Status: `OPEN`

Severity: `HIGH`

Date opened: 2026-05-03

## Issue

Full routing cannot begin because the required critical-routing precondition failed.

## Evidence

- `reports/PCB_FULL_ROUTING_REPORT.md`
- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
- `reports/PCB_ROUTING_PLAN.md`

## Blocking Conditions

- Critical routing result is `CRITICAL_ROUTING_FAIL`.
- Routing plan result is `ROUTING_PLAN_BLOCKED`.
- No `.kicad_pcb` exists.
- No routed critical nets exist for acceptance.

## Required Resolution

Resolve upstream PCB gates, complete critical routing, and produce acceptable critical-routing verification before full routing.

