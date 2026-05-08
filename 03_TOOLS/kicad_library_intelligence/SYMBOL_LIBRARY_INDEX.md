# Symbol Library Index

Date: 2026-05-02

Status: generated from read-only inspection of the installed KiCad 9 app.

## Observed Stock Symbol Root

`C:\Program Files\KiCad\9.0\share\kicad\symbols`

Generated index:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/symbol_index_summary.md`
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/symbol_index.json`

## Current Counts

| Item | Count |
| --- | ---: |
| Stock symbol library files indexed | 223 |
| Symbol records indexed | 22,582 |
| Symbol library table entries parsed from stock template plus user-global table | 450 |

## Large Symbol Libraries Observed

| Library | Notes |
| --- | --- |
| `Regulator_Linear` | Large analog/power library; verify exact regulator pinout and package. |
| `Regulator_Switching` | Switching regulators; symbol match does not verify layout or compensation. |
| `Converter_DCDC` | DCDC converters and modules; verify pin functions and thermal notes. |
| `Diode` | Diodes, TVS, ESD, Zener; package and polarity are high-risk. |
| `Device` | Generic passives and primitives; useful placeholders, not BOM selections. |
| `Connector` | USB and generic connectors; symbol pin naming must be matched to exact connector. |
| `MCU_ST_STM32F1` and other MCU libraries | Family-style symbols use package-code wildcards such as `x`; verify exact part/package. |
| `RF_Module` | Modules including ESP32 family entries; verify module variant and keepout. |

## Symbol Record Fields

The generated JSON records include:

- `library`
- `symbol`
- `library_file`
- `extends`
- `footprint_field`
- `datasheet`
- `keywords`
- `description`

## AI Usage Rules

- Use the generated index to find candidates, not to approve symbols.
- Read the actual `.kicad_sym` entry before use in a project.
- Check pin numbers, pin names, hidden power pins, multi-unit structure, footprint field, datasheet field, and aliases.
- For inherited symbols using `extends`, inspect the parent symbol too.
- For MCUs, map the exact ordering code to the KiCad wildcard symbol carefully.
- For connectors, verify pin numbering against the exact manufacturer drawing.

## Candidate Samples

Generated symbol candidate files include:

- `symbol_candidates_esp32_s3_wroom_1.md`
- `symbol_candidates_stm32f103c8t6.md`
- `symbol_candidates_usb_c_connector_generic.md`
- `symbol_candidates_mcp2562fd.md`

Important observed behavior:

- `ESP32-S3-WROOM-1` finds a direct `RF_Module:ESP32-S3-WROOM-1` candidate.
- `STM32F103C8T6` maps to wildcard-style STM32F1 symbols such as `STM32F103C8Tx`; this still requires datasheet/package verification.
- `MCP2562FD` does not appear as an exact symbol in the generated sample; MCP2562-family candidates exist and must not be assumed FD-correct.
