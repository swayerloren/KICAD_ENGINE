# PCBWay Fabrication Profile

Status: `ACTIVE_RULES`

Read this folder before creating or reviewing PCBWay NOT_FINAL upload packages.

## Required Files

- `gerbers.zip`
- `BOM_PCBWay.csv`
- `Centroid_PCBWay.csv`
- `Assembly_Notes.md`

## Required Formats

- BOM: `Line #,Quantity Per Part Number,Reference Designator,Part Number,Part Description,Package,Type,Manufacturer Name,Manufacturer Part Number,Distributor Part Number,Notes`
- Centroid: `Designator,Mid X,Mid Y,Rotation,Layer`

## Required Checks

- Run `validate_pcbway_bom.py`.
- Run `validate_pcbway_centroid.py`.
- Run `validate_pcba_package_folder.py --house pcbway`.
- Verify connector orientation, pin 1, polarity, and rotations visually.
- Mark package `NOT_FINAL` until LJ approves.

