# PCB Work Auto Start Rules

## Purpose

Define when Codex/Claude may automatically begin real PCB work after the layout sandbox proves the selected plan is ready.

## Allowed Start Condition

Real `.kicad_pcb` update, creation, board-outline application, fixed-mechanical placement, main-group placement, first-pass DRC, and placement-visual export may begin only when all of these are true:

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`
- the footprint/package gate result is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
- `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`
- the selected sandbox status is exactly `AUTO_APPROVED_FOR_PCB_WORK`
- `layout_sandbox/SELECTED_LAYOUT_PLAN.md` exists
- the auto-approval report exists
- board dimensions are defined
- connector-orientation planning exists
- antenna-keepout planning exists when the design includes RF
- routing-feasibility planning exists
- active project, backup plan, verification plan, and rollback plan are confirmed

## Auto-Continue Scope

When the allowed-start condition is satisfied, Codex/Claude may automatically continue to:

1. update PCB from schematic
2. create or update the real `.kicad_pcb`
3. apply the approved board outline
4. place fixed mechanical components
5. place main component groups according to the selected layout plan
6. run DRC
7. export placement and mechanical visual review evidence

This is the only automatic handoff from sandbox planning into real PCB work.

## Block Rule

If any auto-start precondition fails, stop with `AUTO_PCB_START_BLOCKED`.

The blocked report must list the exact missing or failing items, not a vague approval request.

Examples:

- `SCHEMATIC_TO_PCB_GATE_STATUS.md` is not `PASS`
- footprint/package evidence is below `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
- no selected layout plan exists
- no auto-approval report exists
- board dimensions remain assumed
- connector orientation is still unknown
- antenna keepout evidence is missing
- routing-feasibility evidence is missing

If the sandbox auto status is any `AUTO_BLOCKED_*` value:

- do not ask LJ for generic approval
- do not start real PCB work
- create or update the blocked report with exact missing evidence and next actions

## Human Review Rule

Human review may still be requested for a specific unresolved risk, but only after the blocked report identifies that exact risk.

Examples:

- unresolved barrel jack geometry
- unresolved RF pigtail clearance
- unresolved connector mating direction from incomplete manufacturer evidence
- unresolved footprint package evidence for a high-risk connector

## Scope Boundary

This rule allows automatic PCB start only through:

- PCB update from schematic
- board outline / mechanical setup
- fixed and grouped placement
- DRC
- placement visual review evidence

It does not auto-approve:

- final trace routing
- USB routing quality
- RF routing quality
- switching-regulator routing quality
- fabrication readiness
- ignoring DRC
- ignoring connector, antenna, or power-path risks
