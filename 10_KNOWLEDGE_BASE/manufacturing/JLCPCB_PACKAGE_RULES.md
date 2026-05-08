# JLCPCB Package Rules

Status: generic planning guidance. Verify against current JLCPCB requirements before use.

## Required Inputs

- Board dimensions and layer count.
- Stackup and copper weight if non-default.
- Gerber files.
- Drill files.
- BOM if assembly is requested.
- Pick-and-place file if assembly is requested.
- Assembly notes for DNP, orientation, substitutions, and special handling.

## KiCad Engine Rules

- Export packages as `NOT_FINAL` until full review passes.
- Do not claim JLCPCB compatibility without checking the current JLCPCB file requirements.
- Verify BOM MPNs, quantities, designators, and DNP status.
- Verify pick-and-place rotations and side values.
- Review polarized parts and connectors manually.

## Common Mistakes

- Treating KiCad default PNP rotation as fabrication-approved.
- Missing LCSC/JLC part information when assembly requires it.
- Omitting DNP notes.
- Submitting unreviewed connector orientation.

## Human Review Gate

JLCPCB packages require human review of Gerbers, drill files, BOM, PNP, polarity, connectors, substitutions, and assembly notes.

