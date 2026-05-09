# 3D Model Index

Status: local-read-only 3D model inventory guidance.

## Local Generated Outputs

When regenerated on the current machine, 3D model outputs are written under:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/3d_model_summary.md`
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/3d_model_index.json`

These outputs are local-machine inventory only. They are not portable repo truth and are not meant to stay tracked in Git.

## Regenerate

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_3d_models.py
```

If needed, pass `--kicad-root` or `--output-dir`.

## AI Usage Rules

- A matching 3D model is not proof that a footprint is correct.
- Use 3D models to review height, enclosure clearance, cable direction, connector mating, and visual orientation.
- For connectors and modules, compare the 3D model to the exact manufacturer drawing.
- Missing 3D models are not necessarily design errors, but they are mechanical-review gaps.
- Do not edit stock 3D models in the detected KiCad install.

## Important Limits

- 3D model paths in footprints may use variables such as `${KICAD9_3DMODEL_DIR}`.
- A model can be visually similar but still wrong for a selected package.
- Some public KiCad footprints include model references without verifying the selected manufacturer ordering code.
