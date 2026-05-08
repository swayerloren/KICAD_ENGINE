# Real Project Routing Preconditions

## Purpose

Define the exact evidence that must exist before Codex/Claude may route a real KiCad PCB project.

This file is for real-project routing eligibility. It is not permission to route a blocked project.

## Mandatory Preconditions

Real routing may only start when all of these are true:

1. schematic gate is exact `PASS`
2. physical footprints are assigned
3. PCB exists and is synced to the schematic
4. placement pass 1 is exact `PASS`
5. placement orientation pass is exact `PASS`
6. board outline exists on the real PCB
7. keepouts and any required zones/ground strategy exist
8. routing plan exists
9. critical nets are explicitly identified
10. net classes are defined
11. DRC precheck passes

## Routing-Engine-Specific Preconditions

The routing engine may participate in real routing only when all of these also exist:

1. a real-board routing input export exists in the normalized routing schema
2. the routing plan has been generated from that real-board export
3. the critical-net routing plan exists
4. an unrouted-net report exists
5. a keepout-violation report exists
6. a trace-by-trace review file exists
7. a routing scorecard exists
8. the routing result is still labeled `REVIEW_ONLY`

## Hard Blockers

Do not start real routing if any of these are true:

- schematic gate not exact `PASS`
- sandbox or auto-PCB-start gates still block project progression
- footprints are missing or candidate-only where exact verification is required
- placement is not approved
- board outline is not final enough for routing
- RF or antenna keepouts are undefined
- routing plan does not exist
- critical nets are not explicitly named
- net classes are absent
- DRC precheck is not clean enough to begin routing
- the routing engine cannot ingest the board into the normalized routing schema

## Required Evidence Files

At minimum, real routing should point to:

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- `reports/AUTO_PCB_START_REPORT.md`
- `reports/PCB_SYNC_STATUS.md`
- `reports/PCB_PLACEMENT_PASS_1_REPORT.md`
- placement orientation pass report
- DRC precheck report
- routing plan report
- critical-net routing plan report
- trace-by-trace review report
- routing scorecard report

## Result Rule

If any required evidence is missing, routing must stop with exact blockers.

Do not ask for vague approval when the evidence can answer the question.
