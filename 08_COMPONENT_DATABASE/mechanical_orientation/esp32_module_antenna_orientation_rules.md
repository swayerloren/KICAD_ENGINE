# ESP32 Module Antenna Orientation Rules

## Prime Rule

The ESP32 antenna keepout side must face outward toward the board edge.

## Hard Rules

1. The keepout must not point inward into the board body.
2. The keepout must not be trapped in the board middle.
3. Antenna orientation is not proven by module XY position or rotation alone.
4. If the keepout cannot be inferred from the live footprint geometry, classify `NEEDS_HUMAN_REVIEW`.
5. Do not proceed to routing when the antenna-facing side is not proven.

## Evidence Requirements

- exact module-family match when available
- live inferred keepout geometry
- board-edge relationship for the inferred keepout
- optional resolved 3D-model path

## Fail Cases

- inferred keepout side does not face the nearest board edge
- keepout side is too far from the board edge to act as an outward-facing antenna zone
- traces, vias, or components are later routed into the keepout
