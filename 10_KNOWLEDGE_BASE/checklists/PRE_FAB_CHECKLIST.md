# Pre-Fabrication Checklist

Use before exporting or reviewing manufacturing-style outputs.

## Required Status

- Outputs are labeled `NOT_FINAL`.
- ERC passed or all violations are documented and approved.
- DRC passed or all violations are documented and approved.
- BOM reviewed.
- Footprints verified against exact packages.
- Connector orientation reviewed by a human.
- Polarity orientation reviewed by a human.
- Mechanical fit reviewed.

## Package Contents

- Gerber files.
- Drill files.
- Board stackup/fab notes if needed.
- BOM.
- Pick-and-place file if assembly is requested.
- Assembly drawing or notes if needed.
- Readme or manifest with `NOT_FINAL` status.

## Stop Conditions

Do not call outputs final if any connector, polarity, footprint, 3D/mechanical, BOM, ERC, DRC, or fab-house requirement is unresolved.

