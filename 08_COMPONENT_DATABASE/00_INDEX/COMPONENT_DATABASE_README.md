# Component Database README

Date: 2026-05-02

Status: structured part-intelligence scaffold. Not a verified component library.

## Purpose

`08_COMPONENT_DATABASE` stores structured component intelligence that helps Codex, Claude, and similar agents reason beyond raw PDFs. It links parts to datasheets, KiCad symbol candidates, footprint candidates, 3D model candidates, layout warnings, common mistakes, use cases, and verification state.

This database does not replace datasheets, KiCad libraries, ERC, DRC, footprint review, BOM review, or human engineering judgment.

## Folder Map

| Folder | Purpose |
| --- | --- |
| `00_INDEX` | Master index, schemas, rules, and example records. |
| `01_MICROCONTROLLERS` | MCU and processor part records. |
| `02_POWER` | Regulators, converters, power switches, fuses, and power-management parts. |
| `03_COMMUNICATION` | CAN, USB, Ethernet, RS-485, radio PHYs, transceivers, and interface parts. |
| `04_CONNECTORS` | Board connectors, RF connectors, USB connectors, headers, terminals, and cable interfaces. |
| `05_PROTECTION` | TVS, ESD arrays, surge protection, reverse-polarity protection, and overcurrent parts. |
| `06_SENSORS` | Sensor part records. |
| `07_ANALOG` | Op amps, comparators, references, ADC/DAC support, and analog front-end parts. |
| `08_DRIVERS` | Motor drivers, LED drivers, gate drivers, load drivers, and actuator drivers. |
| `09_PASSIVES` | Crystals, inductors, capacitors, resistors, ferrites, and other passive records. |
| `10_RF_AND_ANTENNAS` | Antennas, RF paths, RF connectors, matching networks, and RF layout snippets. |
| `11_DEV_BOARDS_AND_MODULES` | Dev boards, modules, carrier boards, and vendor eval boards. |
| `12_KICAD_SYMBOL_FOOTPRINT_MATCHES` | Verified or candidate KiCad symbol-to-footprint mappings. |
| `13_DESIGN_RULE_SNIPPETS` | Reusable design warnings and layout snippets tied to part families. |
| `14_PART_SELECTION_GUIDES` | Decision guides for choosing components. |
| `15_PACKAGE_FOOTPRINT_DATABASE` | Exact package drawing and footprint-verification records. |
| `16_VERIFICATION_RECORDS` | Evidence records for source, symbol, footprint, package, and human review status. |
| `99_UNVERIFIED_INBOX` | Temporary records and imported notes that are not curated. |

## Rules

- Use this database as a navigation and reasoning layer, not as a source of truth.
- Use `UNVERIFIED_PLACEHOLDER` until a specific verification step has been completed.
- Do not invent electrical limits, pin counts, package names, footprint names, or lifecycle status.
- Do not mark a KiCad symbol or footprint as verified unless it was checked against the datasheet/package drawing.
- Keep local datasheet paths pointed at `06_DATASHEETS`; do not store PDFs here.
- Keep records small, auditable, and easy to diff.

## Example Records

Initial placeholder examples are in:

- `08_COMPONENT_DATABASE/00_INDEX/EXAMPLE_COMPONENT_RECORDS.md`
- `08_COMPONENT_DATABASE/00_INDEX/example_component_records.json`

These examples are intentionally unverified. Later prompts can promote individual records after source review.

## Core Starter Placeholder Records

Strict starter placeholders are stored in:

- `08_COMPONENT_DATABASE/99_UNVERIFIED_INBOX/core_starter_records/CORE_STARTER_RECORDS.md`
- `08_COMPONENT_DATABASE/99_UNVERIFIED_INBOX/core_starter_records/core_starter_records.json`

They are marked `UNVERIFIED_PLACEHOLDER` and exist only to give agents a safe place to start research. They do not approve a schematic symbol, footprint, package drawing, 3D model, or pinout.

## No-Guess Rules

Read `DO_NOT_GUESS_RULES.md` before using any record for schematic, PCB, BOM, or manufacturing-related work.
