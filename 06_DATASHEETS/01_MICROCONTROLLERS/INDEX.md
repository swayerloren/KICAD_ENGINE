# 01_MICROCONTROLLERS Index

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

This index summarizes the AI-readable microcontroller family content scaffold. Folder presence does not verify any datasheet, pinout, package, footprint, or schematic decision.

| Vendor / Group | Folders Upgraded | Generated Content Type | Verification Status |
| --- | ---: | --- | --- |
| ESPRESSIF | 10 | family overview, representative part notes, schematic notes, PCB layout notes, package/footprint notes, source-link stubs, review backlog | `UNVERIFIED` |
| STMICRO_STM32 | 19 | family overview, representative part notes, schematic notes, PCB layout notes, package/footprint notes, source-link stubs, review backlog | `PARTIALLY_RESEARCHED_WITH_STM32F1_PILOT` |
| MICROCHIP_PIC / dsPIC | 8 | family overview, representative part notes, schematic notes, PCB layout notes, package/footprint notes, source-link stubs, review backlog | `UNVERIFIED` |
| MICROCHIP_AVR | 1 | family overview, representative part notes, schematic notes, PCB layout notes, package/footprint notes, source-link stubs, review backlog | `UNVERIFIED` |
| RASPBERRY_PI_RP2040_RP2350 | 1 | family overview, representative part notes, schematic notes, PCB layout notes, package/footprint notes, source-link stubs, review backlog | `UNVERIFIED` |
| NORDIC / NXP / TI / SILABS / RENESAS / INFINEON / GIGADEVICE / WCH / ATMEL_LEGACY | 9 | family overview, representative part notes, schematic notes, PCB layout notes, package/footprint notes, source-link stubs, review backlog | `UNVERIFIED` |

## Generated File Pattern

Each upgraded family folder should contain the following generated or existing file patterns:

- `*_AI_OVERVIEW.md`
- `*_COMMON_PART_NUMBERS.md`
- `*_PART_RECORD.md`
- `*_SCHEMATIC_NOTES.md`
- `*_PCB_LAYOUT_NOTES.md`
- `*_BOOT_DEBUG_NOTES.md`
- `*_POWER_CLOCK_NOTES.md`
- `*_PACKAGE_FOOTPRINT_NOTES.md`
- `*_DEV_BOARD_NOTES.md`
- `*_COMMON_MISTAKES.md`
- `*_KICAD_SYMBOL_FOOTPRINT_NOTES.md`
- `*_SOURCE_LINKS.md`
- `*_NEEDS_REVIEW.md`

## Generation Evidence

- Generator: `03_TOOLS/scripts/datasheet_tree/create_microcontroller_family_content.py`
- Generated result JSON: `05_OUTPUTS/datasheet_tree/MCU_TREE_GENERATION_RESULTS.json`
- Rerun result JSON: `05_OUTPUTS/datasheet_tree/MCU_TREE_GENERATION_RESULTS_RERUN.json`
- Summary: `05_OUTPUTS/datasheet_tree/MCU_TREE_COMPLETION_SUMMARY.md`
- Audit: `02_HISTORY/design_reviews/MCU_DATASHEET_TREE_UPGRADE_REPORT.md`
