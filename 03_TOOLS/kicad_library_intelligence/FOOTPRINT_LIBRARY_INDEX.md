# Footprint Library Index

Status: local-read-only footprint inventory guidance.

## Local Generated Outputs

When regenerated on the current machine, footprint outputs are written under:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/footprint_index_summary.md`
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/footprint_index.json`

These outputs are local-machine inventory only. They are not portable repo truth and are not meant to stay tracked in Git.

## Regenerate

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_footprints.py
python 03_TOOLS/scripts/kicad_libraries/find_footprint_candidates.py "USB-C connector generic"
```

If needed, pass `--kicad-root` or `--output-dir`.

## What The Generated JSON Contains

- footprint library names
- footprint names
- source `.kicad_mod` paths
- descriptions
- tags
- pad counts
- pad-name samples
- 3D model path references

## Footprint Record Fields

The generated JSON records include:

- `library`
- `footprint`
- `path`
- `description`
- `tags`
- `pad_count`
- `pad_names_sample`
- `model_paths`

## AI Usage Rules

- A footprint candidate is only a search hit.
- Do not assert a footprint is correct unless checked against the exact manufacturer drawing.
- Verify pad numbers, package dimensions, exposed pads, drill sizes, paste/mask, courtyard, fab layer, pin 1 mark, and 3D model.
- For modules, verify keepout and antenna geometry.
- For connectors, verify mating face, shell, shield, mounting pegs, orientation, and cable exit direction.
- For packages found only through a part-number description match, treat the result as low confidence.

## Candidate Samples

When generated locally, footprint candidate files typically include:

- `footprint_candidates_esp32_s3_wroom_1.md`
- `footprint_candidates_stm32f103c8t6.md`
- `footprint_candidates_usb_c_connector_generic.md`
- `footprint_candidates_mcp2562fd.md`

Typical candidate behavior:

- `ESP32-S3-WROOM-1` finds direct RF module footprint candidates but still needs Espressif package drawing and keepout verification.
- `USB-C connector generic` finds many `Connector_USB` candidates and marks them high-risk.
- `STM32F103C8T6` and `MCP2562FD` do not produce safe footprint candidates from the part number alone; package-specific search should be done after datasheet verification.
