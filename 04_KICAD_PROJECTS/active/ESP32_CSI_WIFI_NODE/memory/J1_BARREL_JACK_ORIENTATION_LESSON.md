# J1 Barrel Jack Orientation Lesson

Status: `ACTIVE_PROJECT_MEMORY`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Durable Lesson

For the CUI/PJ-102AH-style horizontal DC barrel jack:

- female circular barrel opening = `FRONT / MATING SIDE`
- 3-pin solder-leg side = `REAR / BACK SIDE`
- bottom-edge J1 female opening must face `DOWN / OFF-BOARD`
- bottom-edge J1 3-pin solder side must face `UP / INWARD`

J1 cannot be approved if the 3-pin solder side faces bottom/off-board.

## Evidence Requirements

Do not approve J1 orientation from coordinates alone.

Required evidence:

- 2D footprint geometry from `F.Fab`, `F.SilkS`, and `F.CrtYd`
- pad geometry only as supporting evidence for solder/back side
- exact 3D model evidence when available
- manufacturer drawing or product image showing front/opening side versus rear/solder side

If the exact STEP model is missing, mark `3D_PROOF_MISSING`.

## Current Status

Routing remains blocked until LJ confirms J1/J2 orientation and remaining placement blockers are resolved or explicitly accepted.

