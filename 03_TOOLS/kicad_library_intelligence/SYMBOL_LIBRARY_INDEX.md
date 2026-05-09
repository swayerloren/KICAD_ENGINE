# Symbol Library Index

Status: local-read-only symbol inventory guidance.

## Local Generated Outputs

When regenerated on the current machine, symbol outputs are written under:

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/symbol_index_summary.md`
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/symbol_index.json`

These outputs are local-machine inventory only. They are not portable repo truth and are not meant to stay tracked in Git.

## Regenerate

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_symbols.py
python 03_TOOLS/scripts/kicad_libraries/find_symbol_candidates.py "ESP32-S3-WROOM-1"
```

If needed, pass `--kicad-root` or `--output-dir`.

## What The Generated JSON Contains

- symbol library names
- symbol names
- source library file paths
- `extends` relationships
- footprint field values
- datasheet fields
- keywords
- descriptions

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

When generated locally, symbol candidate files typically include:

- `symbol_candidates_esp32_s3_wroom_1.md`
- `symbol_candidates_stm32f103c8t6.md`
- `symbol_candidates_usb_c_connector_generic.md`
- `symbol_candidates_mcp2562fd.md`

Typical candidate behavior:

- `ESP32-S3-WROOM-1` finds a direct `RF_Module:ESP32-S3-WROOM-1` candidate.
- `STM32F103C8T6` maps to wildcard-style STM32F1 symbols such as `STM32F103C8Tx`; this still requires datasheet/package verification.
- `MCP2562FD` does not appear as an exact symbol in the generated sample; MCP2562-family candidates exist and must not be assumed FD-correct.
