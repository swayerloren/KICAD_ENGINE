# Component Database Scaffold Session

Date: 2026-05-02

## Purpose

Create `08_COMPONENT_DATABASE` as a structured part-intelligence layer for Codex, Claude, and similar agents. The database is intended to supplement datasheets with source-linked, verification-aware component records.

## Context Read

- `AGENTS.md`
- `06_DATASHEETS/00_INDEX/METADATA_SCHEMA.md`
- `06_DATASHEETS/00_INDEX/NAMING_CONVENTIONS.md`

## Folders Created

- `08_COMPONENT_DATABASE/00_INDEX`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS`
- `08_COMPONENT_DATABASE/02_POWER`
- `08_COMPONENT_DATABASE/03_COMMUNICATION`
- `08_COMPONENT_DATABASE/04_CONNECTORS`
- `08_COMPONENT_DATABASE/05_PROTECTION`
- `08_COMPONENT_DATABASE/06_SENSORS`
- `08_COMPONENT_DATABASE/07_ANALOG`
- `08_COMPONENT_DATABASE/08_DRIVERS`
- `08_COMPONENT_DATABASE/09_PASSIVES`
- `08_COMPONENT_DATABASE/10_RF_AND_ANTENNAS`
- `08_COMPONENT_DATABASE/11_DEV_BOARDS_AND_MODULES`
- `08_COMPONENT_DATABASE/12_KICAD_SYMBOL_FOOTPRINT_MATCHES`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS`
- `08_COMPONENT_DATABASE/14_PART_SELECTION_GUIDES`
- `08_COMPONENT_DATABASE/99_UNVERIFIED_INBOX`

## Files Created

- `08_COMPONENT_DATABASE/00_INDEX/COMPONENT_DATABASE_README.md`
- `08_COMPONENT_DATABASE/00_INDEX/MASTER_COMPONENT_INDEX.md`
- `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`
- `08_COMPONENT_DATABASE/00_INDEX/VERIFICATION_LEVELS.md`
- `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`
- `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`
- `08_COMPONENT_DATABASE/00_INDEX/EXAMPLE_COMPONENT_RECORDS.md`
- `08_COMPONENT_DATABASE/00_INDEX/example_component_records.json`

## Example Records

Created placeholder Markdown and JSON records for 19 requested parts and generic components:

- ESP32-S3-WROOM-1
- ESP32-S3-WROOM-1U
- STM32F103C8T6
- STM32F411CEU6
- PIC16F877A
- PIC18F4550
- RP2040
- MCP2562FD
- SN65HVD230
- LM2596
- AMS1117-3.3
- USB-C 16-pin receptacle generic
- U.FL connector generic
- SMA edge connector generic
- polyfuse generic
- TVS diode generic
- ESD diode array generic
- 8 MHz crystal generic
- 40 MHz crystal generic

## Handoff Updates

- `README_GPT.md`
- `FOR CHAT GPT.MD`

Backup:

- `99_BACKUPS/pre_codex_edits/component_database_handoff_20260502_163242`

## Verification

- All requested `08_COMPONENT_DATABASE` folders exist.
- All requested master files exist.
- JSON example catalog parses successfully and contains 19 records.
- All initial records use `UNVERIFIED_PLACEHOLDER`.

## Safety Notes

- No datasheets were downloaded.
- No exact unverified electrical specs were added.
- No KiCad project source files were modified.
- The component database is a scaffold and must not be treated as approved design data.
