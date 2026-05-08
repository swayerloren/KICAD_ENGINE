# Full Pipeline Gate Checklist

Status: `ACTIVE_CHECKLIST`

## Purpose

Use this checklist to determine whether a KiCad project may move to the next pipeline stage.

## Global Checks

- [ ] Active project confirmed.
- [ ] Target files are inside the active project.
- [ ] Required startup files read.
- [ ] Relevant project memory/history read.
- [ ] No secrets recorded.
- [ ] No KiCad design files edited without backup and explicit scope.
- [ ] Every engineering claim has evidence status.
- [ ] Unverified values, pinouts, footprints, and connector orientations are marked.

## Schematic Gate

- [ ] Native KiCad annotation evidence exists and passes.
- [ ] Annotation/completeness report exists and passes or blockers are listed.
- [ ] ERC report exists and current result is documented.
- [ ] Full-page schematic visual exists.
- [ ] Close-up crops and review exist.
- [ ] Electrical audit exists.
- [ ] BOM lock or explicit missing-BOM blocker exists.
- [ ] Footprint/package audit exists.
- [ ] All physical footprints are assigned.
- [ ] High-risk footprints are verified or explicitly marked human-review-required.
- [ ] High-risk `NEEDS_REVIEW` items are closed or explicitly blocking.
- [ ] `SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS` before PCB update.

## Sandbox / PCB Precondition Gate

- [ ] `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` exists.
- [ ] PCB Layout Sandbox report set exists.
- [ ] At least 3 layout variants were created.
- [ ] Variant scorecard exists.
- [ ] Selected layout plan exists.
- [ ] Auto approval report exists.
- [ ] Connector orientation plan exists.
- [ ] Antenna keepout plan exists.
- [ ] Board shape/dimension plan exists.
- [ ] Routing-feasibility check exists and passes.
- [ ] Selected variant has no hard fails.
- [ ] Connector orientation is known.
- [ ] No DRC/precheck blocker exists.
- [ ] Sandbox auto-approval status is `AUTO_APPROVED_FOR_PCB_WORK`.
- [ ] `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS` before PCB update or placement.

## Auto PCB Start Gate

- [ ] `AUTO_PCB_START_WORKFLOW.md` has been read.
- [ ] `AUTO_PCB_START_CHECKLIST.md` has been applied.
- [ ] Footprint/package gate is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`.
- [ ] Selected layout plan exists.
- [ ] Auto-approval report exists and says `AUTO_APPROVED_FOR_PCB_WORK`.
- [ ] Board dimensions exist.
- [ ] Connector-orientation plan exists.
- [ ] Antenna-keepout plan exists when RF is present.
- [ ] Routing-feasibility plan exists.
- [ ] Auto PCB start report exists or the task is still blocked with exact reasons.

## PCB Setup Gate

- [ ] PCB update from schematic report exists.
- [ ] `.kicad_pcb` exists.
- [ ] Board size and outline are source-backed or user-confirmed.
- [ ] Layer count, stackup, and constraints are documented.
- [ ] Mounting holes, keepouts, and mechanical areas are reviewed.
- [ ] Mechanical setup report exists.

## Placement Gate

- [ ] Placement pass 1 report exists.
- [ ] Placement pass 2 orientation report exists.
- [ ] Connectors face correct board edges/directions.
- [ ] Pin 1 and polarity orientation are reviewed.
- [ ] Courtyards and board-edge clearances are acceptable.
- [ ] Reference/value readability is acceptable.
- [ ] DRC status is documented.

## Routing Gate

- [ ] Hole/test-pad/via strategy exists and passes.
- [ ] Copper zone strategy exists and passes.
- [ ] Routing plan is `ROUTING_PLAN_READY`.
- [ ] Critical routing report passes or is accepted with documented non-blocking warnings.
- [ ] Full routing report exists.
- [ ] Trace-by-trace audit exists.
- [ ] DRC passes or review-only exception is user-approved and logged.
- [ ] Unrouted/ratsnest check is complete.

## Fabrication Export Gate

- [ ] Final PCB verification report exists.
- [ ] Final PCB verification is exactly `READY_FOR_NOT_FINAL_FAB_EXPORT`.
- [ ] Human-review list is resolved or explicitly accepted for review-only package.
- [ ] Output folder and file names include `NOT_FINAL`.
- [ ] Package manifest is created.
- [ ] Fabrication package audit is created.

## Exception Rule

Any exception must include:

- user approval
- reason
- gate skipped or softened
- risk classification
- human-review-required flag
- evidence path
