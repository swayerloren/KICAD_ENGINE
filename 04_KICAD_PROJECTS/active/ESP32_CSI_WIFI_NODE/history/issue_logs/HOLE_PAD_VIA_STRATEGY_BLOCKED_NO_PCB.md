# HOLE_PAD_VIA_STRATEGY_BLOCKED_NO_PCB

Status: `OPEN`

Severity: `HIGH`

Date opened: 2026-05-03

## Issue

Hole, test-pad, and via strategy is blocked because no PCB exists and the upstream schematic-to-PCB, mechanical, and placement gates are not passing.

## Evidence

- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
- `_verification/pcb_visual/HOLE_PAD_VIA_CLOSEUP_REVIEW.md`

## Blocking Effect

Do not define final via sizes, place vias, add ground stitching, add thermal vias, place/modify mounting holes, place/modify test pads, route traces, create zones, or generate PCB manufacturing outputs.

## Required Closure Evidence

- Schematic-to-PCB gate is `PASS`.
- `.kicad_pcb` exists.
- Board outline and mechanical constraints exist.
- Placement pass 1 and pass 2 complete.
- Selected fab profile or user-confirmed fab rules provide drill/via limits.
- Mounting-hole hardware and GND/isolation policy are confirmed.
- Test-pad list and access strategy are confirmed.
- DRC and PCB visual close-up review complete.

