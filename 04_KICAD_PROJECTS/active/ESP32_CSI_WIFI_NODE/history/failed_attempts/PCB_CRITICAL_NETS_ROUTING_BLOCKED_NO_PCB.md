# PCB_CRITICAL_NETS_ROUTING_BLOCKED_NO_PCB

Status: `FAILED_BLOCKED`

Date: 2026-05-03

## Attempt

Route only critical nets, refill zones, run DRC, export PCB visuals, and create close-up verification.

## Failure/Blocker

The workflow failed at precondition checks before any routing:

- routing plan is `ROUTING_PLAN_BLOCKED`;
- schematic-to-PCB gate is `FAIL`;
- no `.kicad_pcb` exists;
- placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`;
- zone setup is `ZONE_SETUP_FAIL`;
- via strategy is `HOLE_PAD_VIA_FAIL`.

## Correct Behavior

Do not route critical nets until upstream PCB gates pass.

## Evidence

- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
- `reports/PCB_ROUTING_PLAN.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`

