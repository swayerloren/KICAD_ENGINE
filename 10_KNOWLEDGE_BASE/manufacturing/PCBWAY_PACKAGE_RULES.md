# PCBWay Package Rules

Status: generic planning guidance. Verify against current PCBWay requirements before use.

## Required Inputs

- Gerber files.
- Drill files.
- Board outline and cutouts.
- Stackup notes if controlled impedance or special materials are needed.
- BOM and pick-and-place file if assembly is requested.
- Assembly drawing or notes for non-obvious parts.

## KiCad Engine Rules

- Keep outputs labeled `NOT_FINAL`.
- Include a manifest explaining file purpose and verification status.
- Verify controlled impedance requirements with the board-house process.
- Check component rotations and side assignments manually.
- Do not assume one fab-house export format works unchanged for another.

## Common Mistakes

- Missing drill map or ambiguous slots.
- Missing assembly notes for connectors.
- Incorrect side or rotation in PNP.
- No controlled-impedance communication before ordering.

## Human Review Gate

PCBWay packages require human review of mechanical, impedance, BOM, PNP, and assembly assumptions.

