# Barrel Jack Orientation Rules

Status: `MANDATORY_FOR_BARREL_JACK_PLACEMENT`

Generated: `2026-05-07`

These rules prevent confusion between the physical mating side of a horizontal DC barrel jack and the rear solder-leg side.

The machine-readable truth source for audits is `08_COMPONENT_DATABASE/mechanical_orientation/connector_orientation_truth.json`.

## Physical Front/Back Rule

For CUI/PJ-102AH-style and similar horizontal DC barrel jacks:

1. The barrel jack front/mating side is the female circular opening.
2. The barrel jack rear/back side is the side with solder pins, solder lugs, or 3-pin solder legs.
3. The 3-pin solder-leg side is not the connector mouth.
4. The female circular opening is the side that receives the plug.

## Edge Placement Rule

1. For edge-mounted barrel jacks, the female circular opening must face off-board.
2. For bottom-edge barrel-jack placement, the female opening faces downward/off-board.
3. For bottom-edge barrel-jack placement, the 3-pin solder side faces upward/inward toward the PCB body.
4. Do not side-mount `J1` unless LJ explicitly approves a side-entry mechanical concept.
5. If the 3-pin solder side is closest to the board edge where the plug should enter, the barrel jack is flipped wrong.

## Evidence Rule

Do not approve barrel jack orientation from pad coordinates alone.

Required evidence must include at least one physical-orientation source and footprint geometry:

- 3D model if available and verified for the exact connector
- `F.Fab`, `F.SilkS`, and `F.CrtYd` footprint geometry
- manufacturer drawing or product image showing front/mating side versus rear solder side
- pad geometry only as supporting evidence for which side is solder/back side

If no 3D model and no clear footprint geometry exist, classify:

`BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`

If 2D footprint geometry is clear but the exact 3D model is missing, classify the 2D result separately and mark:

`3D_PROOF_MISSING`

For routing-gate purposes, `3D_PROOF_MISSING` means the connector remains `NEEDS_HUMAN_REVIEW`.

## Compact Dev-Board Rule

Barrel jacks are often too bulky for pill-style dev boards. If the barrel jack forces excessive board size, service-access problems, connector conflicts, or dead area, mark:

`BARREL_JACK_NOT_PILL_BOARD_FRIENDLY`

Then recommend a smaller verified power input connector or require LJ mechanical approval.
