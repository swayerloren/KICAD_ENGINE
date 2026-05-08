# Fabrication Profiles

Status: `ACTIVE_RULES`

Purpose: define NOT_FINAL fabrication and PCBA export requirements for KiCad Engine projects.

This folder is the required first stop before any Gerber, drill, BOM, CPL, centroid, assembly-note, or upload-package work.

## Core Rules

- Manufacturing outputs are `NOT_FINAL` until LJ explicitly approves release/upload.
- Never overwrite an older manufacturing revision folder.
- Do not export or package if DRC, no-unrouted-net proof, connector orientation, polarity, or final visual review gates fail.
- JLCPCB and PCBWay require separate upload-specific BOM and placement formats.
- Universal BOM and pick-and-place files are allowed for internal review, but upload packages must match the selected fab house.
- BOM/CPL validation is not assembly approval.
- Pick-and-place rotations must be visually checked against board screenshots, 3D evidence where available, and real connector/polarity rules.

## Required Reads

- `UNIVERSAL_PCBA_PACKAGE_RULES.md`
- `UNIVERSAL_BOM_FORMAT.md`
- `UNIVERSAL_PICK_AND_PLACE_FORMAT.md`
- `CONNECTOR_ORIENTATION_PRE_UPLOAD_RULES.md`
- `MANUFACTURING_REVISION_FOLDER_RULES.md`
- `NOT_FINAL_EXPORT_RULES.md`
- `JLCPCB\README.md`
- `PCBWAY\README.md`

## Validators

Use validators under `03_TOOLS\scripts\fabrication\` before claiming a package is structurally ready. Validators check columns, required values, quantities, coordinates, layers, and package-folder presence. They never upload anything and never edit KiCad files.

