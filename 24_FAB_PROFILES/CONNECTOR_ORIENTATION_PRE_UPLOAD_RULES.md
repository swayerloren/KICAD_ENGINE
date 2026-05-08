# Connector Orientation Pre-Upload Rules

Status: `ACTIVE_RULES`

Connector orientation must be proven before any upload package is approved.

## Hard Rules

- Do not approve connector orientation from coordinates or CPL rotation alone.
- Verify footprint primitives, silkscreen/fab/courtyard, pad positions, 3D model when available, and real part mating direction.
- Barrel jack female opening is the front/mating side and must face off-board for edge placement.
- Barrel jack solder-leg side is the rear/back side and must face inward on edge placement.
- USB-C receptacle mouth must face off-board and the footprint PCB-edge indicator must align to board Edge.Cuts.
- Pin headers, board-to-wire connectors, switches, sockets, and ports require mating-direction review.
- If footprint/3D evidence cannot prove mating direction, classify as blocked before export.

## Export Blockers

- Missing or ambiguous connector orientation proof.
- Missing 3D model when the project requires 3D proof and 2D geometry is insufficient.
- Connector body/courtyard collides with board edge, mounting holes, switches, test pads, or neighboring parts.
- CPL rotation conflicts with visual/3D/footprint evidence.

