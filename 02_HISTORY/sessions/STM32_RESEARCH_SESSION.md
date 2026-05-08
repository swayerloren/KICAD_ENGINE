# STM32 Research Session

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Work Performed

Built an STM32 knowledge base for AI-assisted KiCad design using official ST product pages, family pages, application-note links, board pages, and read-only local KiCad 9 library candidate searches.

## Safety

- No datasheet PDFs were downloaded.
- No tools were installed.
- No KiCad project source files were edited.
- No files under `C:\Program Files\KiCad` were modified.
- Local KiCad library checks were read-only.

## Outputs

- STM32 datasheet/reference README and master index.
- Nucleo and Discovery board indexes.
- STM32 family overview.
- STM32 bare MCU part records in Markdown and JSON.
- STM32 dev-board records in Markdown.
- Power/decoupling, boot/debug, USB, and CAN/FDCAN design-rule snippets.
- STM32 research status file.

## Repeat-Prompt Refinement

- Added official ST schematic-pack links for MB1136 Nucleo-64, MB1367 NUCLEO-G431RB, MB1364 NUCLEO-H743ZI, and MB997 STM32F4DISCOVERY references where direct resources were observed.
- Updated part records with explicit schematic/reference-source rows.
- Updated JSON records with `schematic_source_urls` fields so AI agents can tell when a verified board schematic source is present versus still unknown.
- Updated dev-board records to separate official ST board schematics from community Blue Pill/Black Pill placeholders.

## Verification Plan

- Validate JSON syntax for `stm32_part_records.json`.
- Check required files exist.
- Check no non-link datasheet files were added under the STM32 datasheet tree.
- Check no KiCad design/manufacturing file types were edited by this task.
- Check touched files are ASCII-only.

## Verification Results

- JSON syntax validation passed for `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\stm32_part_records.json`.
- JSON record count: 9.
- All JSON records include `source_evidence_urls`.
- Repeat-pass JSON validation passed after adding `schematic_source_urls`.
- JSON records with missing `schematic_source_urls`: 0.
- All requested STM32 index, family, rule, record, and research-status files were present.
- No recent non-markdown/csv/json/txt files were found under `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32`.
- Touched STM32 research files were checked as ASCII-only.
- A broad timestamp scan still shows existing KiCad project/manufacturing files elsewhere in the workspace, but this STM32 task did not intentionally edit KiCad design files.
