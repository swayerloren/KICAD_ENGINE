# Placement Readiness Scorecard

## Purpose

Define the scoring and hard-fail rules that must be applied before Codex or
Claude treats a real or copied KiCad PCB placement as ready for routing.

This scorecard is placement authority, not fabrication authority.

## Required Category Scores

The placement readiness score is out of `100`:

- connector orientation proof: `0-20`
- board outline / mechanical fit: `0-15`
- antenna keepout compliance: `0-15`
- power path adjacency: `0-15`
- USB cluster compactness: `0-10`
- test pad accessibility: `0-10`
- courtyard / body clearance: `0-10`
- routing feasibility: `0-5`

## Hard-Fail Statuses

Any one of these prevents a placement from being treated as routing-ready:

- `USB_CONNECTOR_ORIENTATION_UNKNOWN`
- `POWER_CONNECTOR_ORIENTATION_UNKNOWN`
- `ESP32_ANTENNA_KEEPOUT_BLOCKED`
- `POWER_PATH_SCATTERED_BEYOND_THRESHOLD`
- `USB_CLUSTER_TOO_SPREAD`
- `TEST_PADS_INACCESSIBLE`
- `FOOTPRINT_OUTSIDE_BOARD`
- `COURTYARD_BODY_OVERLAP`
- `PLACEMENT_CREATES_IMPOSSIBLE_ROUTE`

## Output Statuses

The scorecard must end with exactly one of these:

- `PLACEMENT_READY_FOR_ROUTING`
- `PLACEMENT_REPAIR_REQUIRED`
- `PLACEMENT_BLOCKED_HUMAN_REVIEW`

## Result Rules

1. Routing may not begin from stale placement claims alone.
2. A fresh placement readiness scorecard must be generated from the current
   board state or an exact copied-board equivalent.
3. Any hard-fail status blocks routing continuation.
4. No routing workflow may treat `PLACEMENT_REPAIR_REQUIRED` as equivalent to
   placement approval.
5. `PLACEMENT_READY_FOR_ROUTING` only proves placement quality is acceptable
   enough to begin routing review. It does not override DRC, unrouted-net,
   live-state, or task-contract blockers.

## Required Findings For Every Hard Fail

Every hard-fail finding must identify:

- net, reference, or stage involved
- geometry or coordinates when applicable
- layer or board edge when applicable
- exact reason
- recommended fix

## Measurement Rules

- Edge connectors must be close enough to a board edge that their mating
  direction is mechanically obvious.
- Non-edge parts must remain inside the board outline.
- ESP32-style RF modules must expose a clear antenna keepout region with no
  body, track, or via intrusion.
- Power-path staging must follow physical current-flow order:
  connector -> fuse -> protection -> regulator -> output cluster.
- USB support parts must remain compact around the connector:
  ESD, CC, and series parts may not drift into a long scattered cluster.
- Test pads must remain edge-accessible and probeable.
- Courtyard/body overlap is a hard fail.
- If placement geometry makes clean routing unrealistic, routing feasibility
  must hard-fail.

## Expected Evidence

A real routing start should be able to point to:

- `reports/PLACEMENT_READINESS_SCORECARD.md`
- placement pass report(s)
- placement orientation review
- live project state / gate reconciliation files

## Command

Read-only copied-board or live-board scoring command:

```powershell
python 14_LAYOUT_AUTOMATION\scripts\score_placement_readiness.py `
  <board.kicad_pcb> `
  <output.json> `
  --markdown <output.md>
```
