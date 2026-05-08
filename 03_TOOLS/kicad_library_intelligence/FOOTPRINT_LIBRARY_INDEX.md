# Footprint Library Index

Date: 2026-05-02

Status: generated from read-only inspection of the installed KiCad 9 app.

## Observed Stock Footprint Root

`C:\Program Files\KiCad\9.0\share\kicad\footprints`

Generated index:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/footprint_index_summary.md`
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/footprint_index.json`

## Current Counts

| Item | Count |
| --- | ---: |
| Stock `.pretty` footprint libraries indexed | 155 |
| Footprints indexed | 15,415 |
| Footprints with 3D model references | 14,805 |
| Footprint table entries parsed from stock template plus user-global table | 313 |

## Large Footprint Libraries Observed

| Library | Notes |
| --- | --- |
| `Connector_Molex` | High mechanical and orientation risk. |
| `Package_DFN_QFN` | Exposed-pad, paste, pin-1, and thermal-via risk. |
| `Inductor_SMD` | Package names do not verify current rating or saturation. |
| `Connector_JST` | Series, pitch, latch direction, and mating part are high-risk. |
| `Package_SO` | Common IC packages; verify body width, pitch, pad style, and pin count. |
| `Connector_USB` | USB-C and USB variants are high-risk and manufacturer-specific. |
| `RF_Module` | Module keepouts, antenna region, and castellated pad numbering require source drawings. |
| `Crystal` | Package names do not verify crystal electrical suitability. |

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

Generated footprint candidate files include:

- `footprint_candidates_esp32_s3_wroom_1.md`
- `footprint_candidates_stm32f103c8t6.md`
- `footprint_candidates_usb_c_connector_generic.md`
- `footprint_candidates_mcp2562fd.md`

Important observed behavior:

- `ESP32-S3-WROOM-1` finds direct RF module footprint candidates but still needs Espressif package drawing and keepout verification.
- `USB-C connector generic` finds many `Connector_USB` candidates and marks them high-risk.
- `STM32F103C8T6` and `MCP2562FD` do not produce safe footprint candidates from the part number alone; package-specific search should be done after datasheet verification.
