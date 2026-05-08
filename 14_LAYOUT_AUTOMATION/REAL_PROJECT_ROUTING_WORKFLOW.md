# Real Project Routing Workflow

## Purpose

Define the pass-by-pass workflow for using the routing engine on a real KiCad PCB project.

This workflow assumes all routing preconditions already pass.

## Pre-Start Checklist

Before the first trace is edited:

1. confirm the active project path
2. confirm target files are inside the active project
3. confirm a fresh backup exists
4. confirm routing preconditions are exact `PASS`
5. confirm the normalized routing input export exists for the current board state
6. generate:
   - routing plan
   - critical-net plan
   - unrouted-net report
   - keepout-violation report
   - trace-by-trace review scaffold
   - routing scorecard

## Routing Pass Order

Routing must proceed in these passes:

1. power and protection
2. regulator critical loop
3. 3V3 rail
4. USB D+/D-
5. ESD and protection connections
6. ESP32 EN/BOOT
7. decoupling
8. LEDs, buttons, and test pads
9. remaining low-risk nets

Do not skip ahead to later passes while earlier critical passes remain incomplete or low quality.

## Per-Pass Execution

For each pass:

1. identify the nets in scope
2. confirm width, clearance, layer, and via rules
3. route only the current pass nets
4. update the trace-by-trace review for every edited trace
5. run DRC or targeted precheck after the pass when practical
6. update unrouted-net and keepout reports
7. update the routing scorecard

## Per-Pass Acceptance

A routing pass is acceptable only when:

- all nets in that pass are routed or explicitly deferred with reason
- no new RF or antenna keepout crossing exists
- no critical-net hard fail exists
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
