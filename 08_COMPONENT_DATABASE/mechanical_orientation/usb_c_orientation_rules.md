# USB-C Orientation Rules

## Prime Rule

The USB-C receptacle mouth/opening must face off-board through the serving board edge.

## Hard Rules

1. USB-C orientation is not proven by XY position or rotation alone.
2. The mouth/opening must face off-board.
3. The footprint `PCB Edge` direction must align with `Edge.Cuts` when the footprint provides it.
4. Pads must remain on-board; expected shell/body overhang may extend off-board only when mechanically intended.
5. If the required 3D model is missing, classify `NEEDS_HUMAN_REVIEW`.
6. Do not proceed to routing when USB-C orientation is not proven.

## Evidence Requirements

- exact footprint-family match
- live component geometry
- resolved 3D-model path
- edge-alignment check against the board outline

## Fail Cases

- mouth/opening points inward
- PCB-edge marker points away from the serving edge
- connector body is too far from the board edge to act as an edge connector
- review claims rely only on bottom-edge XY position or numeric rotation
