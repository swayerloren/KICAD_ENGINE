# Barrel Jack Orientation Rules

## Prime Rule

The barrel-jack female circular opening is the mating face.

The solder-leg or pin side is the rear/back side.

Those two sides must never be confused.

## Hard Rules

1. Do not infer barrel-jack front/back from XY position alone.
2. Do not infer barrel-jack front/back from rotation value alone.
3. The 3-pin solder-leg side is not the port opening.
4. For bottom-edge placement, the female opening must face down/off-board.
5. For bottom-edge placement, the solder-leg side must face up/inward.
6. If the 3D model is missing, classify `NEEDS_HUMAN_REVIEW`.
7. Do not proceed to routing when barrel-jack orientation is not proven.

## Evidence Requirements

- exact footprint-family match
- live component geometry
- resolved 3D-model path when available
- optional manufacturer image or drawing for manual review

## Fail Cases

- female opening points inward
- solder-leg side points outward
- body is stranded away from the serving edge
- a reviewer can only say “it is near the bottom edge” without proving which side is the port opening
