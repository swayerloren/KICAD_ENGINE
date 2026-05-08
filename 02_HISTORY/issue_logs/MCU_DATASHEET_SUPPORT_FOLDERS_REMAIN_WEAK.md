# Issue Log: MCU Datasheet Support Folders Remain Weak

Date: 2026-05-03
Status: `OPEN`
Severity: `LOW`

## Issue

The MCU family folders requested for the generator pass were upgraded, but several support/reference folders under `06_DATASHEETS/01_MICROCONTROLLERS` still contain weak placeholder README text with `$rel` or `$name`.

## Affected Folders

- `ESPRESSIF/ANTENNA_RF_REFERENCES`
- `ESPRESSIF/DESIGN_GUIDES`
- `ESPRESSIF/ERRATA`
- `ESPRESSIF/MODULES`
- `MICROCHIP_PIC/DESIGN_GUIDES`
- `MICROCHIP_PIC/DEVELOPMENT_BOARDS`
- `MICROCHIP_PIC/ERRATA`
- `MICROCHIP_PIC/PROGRAMMING_DEBUG_PICKIT`
- `STMICRO_STM32/DESIGN_GUIDES`
- `STMICRO_STM32/DISCOVERY_BOARDS`
- `STMICRO_STM32/ERRATA`
- `STMICRO_STM32/EVAL_BOARDS`
- `STMICRO_STM32/NUCLEO_BOARDS`
- `STMICRO_STM32/PROGRAMMING_DEBUG_STLINK`
- `OTHER`

## Why It Matters

These are not MCU family folders, so they were not rewritten by the family content generator pass. They still need a support-folder curation pass before the datasheet tree can be considered clean.

## Recommended Action

Create a separate generator or manual curation pass for module, dev-board, programming/debug, errata, design-guide, and catch-all support folders.
