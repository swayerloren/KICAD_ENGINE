# Microcontroller Family Content Generator Audit

Date: 2026-05-03
Scope: `03_TOOLS/scripts/datasheet_tree`
Status: `CREATED_AND_SYNTAX_VALIDATED`

## Summary

Created a repeatable microcontroller family content generator so KiCad Engine can scaffold useful AI-readable family folders instead of empty `README.md`, `INDEX.md`, `MISSING.md`, and `SOURCES.md` placeholders.

## Created Files

- `03_TOOLS/scripts/datasheet_tree/create_microcontroller_family_content.py`
- `03_TOOLS/scripts/datasheet_tree/family_content_schema.json`
- `03_TOOLS/scripts/datasheet_tree/templates/FAMILY_AI_OVERVIEW_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/COMMON_PART_NUMBERS_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/PART_RECORD_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/SCHEMATIC_NOTES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/BOOT_DEBUG_NOTES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/POWER_CLOCK_NOTES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/PACKAGE_FOOTPRINT_NOTES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/DEV_BOARD_NOTES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/COMMON_MISTAKES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/KICAD_SYMBOL_FOOTPRINT_NOTES_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/SOURCE_LINKS_TEMPLATE.md`
- `03_TOOLS/scripts/datasheet_tree/templates/NEEDS_REVIEW_TEMPLATE.md`

## Generator Behavior

- Supports `--vendor`, `--family`, and `--representative-part`.
- Supports optional `--output-folder`.
- Supports optional JSON config following `family_content_schema.json`.
- Supports optional link-only `--source-link` seed rows.
- Creates useful Markdown stubs with real sections and review gates.
- Marks unknowns as `UNKNOWN_REQUIRES_SOURCE`.
- Does not fabricate specs.
- Does not download PDFs.
- Does not scrape websites.
- Skips all existing files unless `--force` is passed.
- Supports `--dry-run` for safe preview.

## Validation Performed

| Check | Result |
| --- | --- |
| Python syntax validation | PASS |
| JSON schema parse validation | PASS |
| STM32F0 dry run | PASS |
| Existing-file protection in dry run | PASS; existing `README.md`, `INDEX.md`, `MISSING.md`, and `SOURCES.md` were reported `SKIPPED_EXISTS`. |
| Unknown-marker scan | PASS; generated templates/script use `UNKNOWN_REQUIRES_SOURCE`. |
| Targeted secret scan | PASS; no matches. |
| KiCad design file edit check | PASS; no recent KiCad design/library file edits found. |
| PDF/download behavior | PASS; generator has no download implementation. |

## Dry-Run Result

Command:

```powershell
python "03_TOOLS\scripts\datasheet_tree\create_microcontroller_family_content.py" --vendor STMICRO_STM32 --family STM32F0 --representative-part STM32F030C8T6 --dry-run --json
```

Result:

- 16 files considered.
- 0 files written.
- 4 existing base files skipped.
- 12 family/part files would be written.

## Remaining Limitations

- The generator creates safe stubs only; it does not research or verify source content.
- It does not update component database records automatically.
- It does not validate generated Markdown semantics beyond template content.
- It has not been used with `--force` or to create a real new family folder in this session.

## Final Classification

`READY_FOR_SAFE_STUB_GENERATION`

The generator is ready for future STM32F0/F2/F3/F4/G0/G4/H7-style scaffold creation and later extension to ESP32, PIC, AVR, Nordic, and other MCU families.
