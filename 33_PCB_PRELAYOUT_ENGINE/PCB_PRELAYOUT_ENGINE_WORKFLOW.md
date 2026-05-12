# PCB Prelayout Engine Workflow

## Purpose

Define the exact sequence that must happen before real PCB placement or routing begins.

## Workflow

1. Confirm active project and read-only scope.
2. Extract a board digital twin from the current project board or approved copied board.
3. Build connector mechanical truth records for every edge-facing or access-critical connector.
4. Generate at least three placement variants.
5. For each variant:
   - place fixed mechanical items first
   - preserve RF keepout space
   - project 45-degree route channels
   - count projected open nets
   - score the variant
6. Compare all variants and select the highest-ranked non-failed candidate.
7. Run the prelayout gate.
8. Permit real PCB placement only if:
   - at least three variants were generated
   - at least one variant scored `PASS`
   - the latest gate result records `placement_gate_status: PASS`
   - the selected variant has no connector-direction hard fail
   - the selected variant has no projected open-net blocker
9. Permit real PCB routing only if:
   - the placement conditions above remain true
   - the latest gate result records `routing_gate_status: PASS`
   - live-board open-net evidence does not already prove the board is still incomplete

## Required Outputs

- digital twin JSON
- three or more placement variant JSON files
- projected-route JSON for each variant
- one score JSON for each variant
- one comparison JSON
- one gate-result JSON
- optional preview SVG/Markdown artifacts

## Read-Only Rule

The engine may inspect KiCad files and run `kicad-cli` DRC in read-only mode.

It must not:

- move footprints on the real board
- route tracks
- delete tracks
- create zones
- save KiCad files
