# Real Project Routing Workflow

## Purpose

Define the pass-by-pass workflow for using the routing engine on a real KiCad PCB project.

This workflow assumes all routing preconditions already pass.

## Pre-Start Checklist

Before the first trace is edited:

1. declare task type `ROUTING_EDIT_REQUIRED`
2. confirm the active project path
3. confirm target files are inside the active project
4. confirm a fresh backup exists
5. run `python 03_TOOLS/scripts/project_state/validate_live_state_before_gate.py --project <ACTIVE_PROJECT_PATH>`
6. run `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase 8`
7. run `python 14_LAYOUT_AUTOMATION/scripts/staged_routing_runner.py --project <ACTIVE_PROJECT_PATH> --stage placement_readiness`
8. confirm routing preconditions are exact `PASS` by live-state authority, not by stale markdown alone
9. confirm a fresh placement readiness scorecard exists with exact result `PLACEMENT_READY_FOR_ROUTING`
10. confirm the normalized routing input export exists for the current board state
11. generate:
   - routing plan
   - critical-net plan
   - unrouted-net report
   - keepout-violation report
   - trace-by-trace review scaffold
   - routing geometry hard-fail report
   - routing scorecard

## Execution Contract

Every real routing pass must satisfy the execution contract in
`03_TOOLS/scripts/execution_contract/`.

`ROUTING_EDIT_REQUIRED` must prove all of the following before the pass may be
treated as complete:

- backup created
- `.kicad_pcb` hash before
- `.kicad_pcb` hash after
- PCB hash changed
- DRC run
- unrouted and unconnected count before/after
- trace-change log updated
- visual export attempted

If a routing pass ends with only Markdown/report changes and no real PCB hash
change, the required final status is
`EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`.

`LIVE_PROJECT_STATE.json` is the top authority for whether routing may continue.
Reports without source hashes are weak, and stale `NO_PCB`, `0 footprints`, or
`no routing` narratives cannot override live board evidence.

Placement is not considered approved for routing unless a fresh scorecard from
`score_placement_readiness.py` returns exact status
`PLACEMENT_READY_FOR_ROUTING`.

Broad routing is not allowed when `detect_no_progress.py` reports
`BLOCKED_REPAIR_MODE`. In that case, only the recommended targeted repair stage
may proceed.

## Routing Pass Order

Routing must proceed in these stage-gated passes:

1. `placement_readiness`
2. `power_critical`
3. `ground_strategy`
4. `USB_support`
5. `boot_enable_control`
6. `USB_data`
7. `low_speed_remaining`
8. `trace_geometry_cleanup`
9. `final_connectivity`
10. `final_visual_review`

Do not skip ahead to later passes while earlier critical passes remain incomplete or low quality.

## Per-Pass Execution

For each pass:

1. identify the nets in scope
2. confirm width, clearance, layer, and via rules
3. route only the current pass nets
4. update the trace-by-trace review for every edited trace
5. run the routing geometry hard-fail checker after the pass
6. run DRC or targeted precheck after the pass when practical
7. update unrouted-net and keepout reports
8. update the routing scorecard

## Per-Pass Acceptance

A routing pass is acceptable only when:

- all nets in that pass are routed or explicitly deferred with reason
- no new RF or antenna keepout crossing exists
- no critical-net hard fail exists
- no routing geometry hard-fail status exists
- placement readiness scorecard remains `PLACEMENT_READY_FOR_ROUTING`
- every new trace appears in the trace-by-trace review
- DRC risk does not worsen without being recorded and justified

## Routing Engine Role

The routing engine is allowed to:

- sequence passes
- identify critical nets
- identify power nets
- identify USB nets
- flag keepout risks
- flag unrouted critical nets
- score routing status
- force stop conditions when hard fails appear

The routing engine is not allowed to:

- override KiCad DRC
- ignore visual routing quality
- ignore ugly geometry because the score is high
- label the board fabrication-ready

## Required Outputs

By the end of the routing workflow, the project should have:

- routing-plan report
- per-pass routing reports
- DRC evidence
- unrouted-net report
- keepout-violation report
- trace-by-trace review
- routing scorecard
- visual routing review

## Boundary

This workflow authorizes structured routing work only after all earlier project gates pass. It does not bypass sandbox, placement, DRC, or human review.
