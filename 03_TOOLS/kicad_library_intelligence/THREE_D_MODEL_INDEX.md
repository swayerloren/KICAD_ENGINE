# 3D Model Index

Date: 2026-05-02

Status: generated from read-only inspection of the installed KiCad 9 app.

## Observed Stock 3D Model Root

`C:\Program Files\KiCad\9.0\share\kicad\3dmodels`

Generated index:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/3d_model_summary.md`
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/3d_model_index.json`

## Current Counts

| Item | Count |
| --- | ---: |
| `.3dshapes` folders indexed | 105 |
| Model files indexed | 14,043 |
| STEP files | 7,200 |
| WRL files | 6,843 |

## AI Usage Rules

- A matching 3D model is not proof that a footprint is correct.
- Use 3D models to review height, enclosure clearance, cable direction, connector mating, and visual orientation.
- For connectors and modules, compare the 3D model to the exact manufacturer drawing.
- Missing 3D models are not necessarily design errors, but they are mechanical-review gaps.
- Do not edit stock 3D models under `C:\Program Files\KiCad`.

## Important Limits

- 3D model paths in footprints may use variables such as `${KICAD9_3DMODEL_DIR}`.
- A model can be visually similar but still wrong for a selected package.
- Some public KiCad footprints include model references without verifying the selected manufacturer ordering code.
