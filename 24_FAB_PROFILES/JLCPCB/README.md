# JLCPCB Fabrication Profile

Status: `ACTIVE_RULES`

Read this folder before creating or reviewing JLCPCB NOT_FINAL upload packages.

## Required Files

- `gerbers.zip`
- `BOM_JLCPCB.csv`
- `CPL_JLCPCB.csv`
- `Assembly_Notes.md`

## Required Formats

- BOM: `Comment,Designator,Footprint,LCSC Part #,Quantity,Manufacturer,Manufacturer Part Number,Notes`
- CPL: `Designator,Mid X,Mid Y,Layer,Rotation`

## Required Checks

- Run `validate_jlcpcb_bom.py`.
- Run `validate_jlcpcb_cpl.py`.
- Run `validate_pcba_package_folder.py --house jlcpcb`.
- Verify connector orientation, pin 1, polarity, and rotations visually.
- Mark package `NOT_FINAL` until LJ approves.

