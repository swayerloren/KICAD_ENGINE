# HOLE_PAD_VIA_STRATEGY_BLOCKED_NO_PCB

Status: `FAILED_PRECONDITION`

Date: 2026-05-03

## Attempt

Build and verify through-hole, mounting-hole, test-pad, and via strategy before routing.

## Failure Reason

The workflow is blocked because:

- no `.kicad_pcb` file exists;
- no board outline exists;
- placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`;
- no holes, test pads, vias, or zones exist to inspect;
- no selected verified fab profile provides drill/via limits;
- schematic-to-PCB gate is `FAIL`.

## Resolution Required

Resolve the schematic-to-PCB gate, create/update the PCB, define mechanical constraints, complete placement, select or confirm fab limits, then rerun this strategy review.

## Verification

No KiCad design files were modified.

