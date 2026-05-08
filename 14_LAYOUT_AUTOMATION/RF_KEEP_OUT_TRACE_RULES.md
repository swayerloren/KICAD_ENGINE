# RF Keepout Trace Rules

## Purpose

Define routing rules around RF modules, onboard antennas, and keepout regions.

## Rules

- Do not route through the antenna keepout.
- Do not let unrelated traces clip the keepout boundary.
- RF-adjacent routing must be intentional and explicitly reviewed.
- If routing pressure pushes traces toward the keepout, treat that as a placement or board-shape warning.

## Failure Conditions

- any trace crosses the antenna keepout
- routing pressure forces USB or switching copper into the keepout area
