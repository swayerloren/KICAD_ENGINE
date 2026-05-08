# Barrel Jack Orientation Guide

Status: `ACTIVE_KNOWLEDGE_BASE`

Generated: `2026-05-07`

## Key Lesson

For horizontal DC barrel jacks, the female circular barrel opening is the front/mating side. The solder-leg side is the rear/back side.

Do not confuse the 3-pin solder-leg side with the plug opening.

## Bottom-Edge Placement

When a horizontal barrel jack is used on the bottom edge of a PCB:

- female circular opening faces down/off-board
- 3-pin solder-leg side faces up/inward toward the PCB body
- pads remain on the PCB
- connector body may overhang only when the exact footprint and mechanical drawing support that placement

## Evidence Needed

Orientation proof requires more than coordinates. Use:

- exact 3D model when available
- `F.Fab`, `F.SilkS`, and `F.CrtYd` footprint geometry
- manufacturer drawing or product image
- pad positions as support for the solder/back side only

If the exact 3D model is missing, do not claim 3D proof. If the footprint geometry also does not clearly identify the front/mouth side, classify:

`BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`

## Pill-Board Warning

Barrel jacks are mechanically awkward on narrow pill-style dev boards. If they crowd USB, mounting holes, switches, test pads, or create dead area, classify:

`BARREL_JACK_NOT_PILL_BOARD_FRIENDLY`

Recommend a smaller verified power input connector unless LJ explicitly accepts the barrel jack.

