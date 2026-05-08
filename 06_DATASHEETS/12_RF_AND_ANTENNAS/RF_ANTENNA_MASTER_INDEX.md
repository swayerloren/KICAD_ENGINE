# RF And Antenna Master Index

Date: 2026-05-02

Status: starter index. RF entries are placeholders until exact antenna, connector, cable, stackup, and matching-network evidence is recorded.

## Purpose

This folder tracks RF connector, antenna, cable, keepout, stackup, and matching-network references. It supports KiCad layout review for ESP32, Nordic, WiFi, BLE, LoRa, GNSS, cellular, and other RF designs without pretending generic RF geometry is final.

## Current Starter Records

| Topic | Component Database Record | Status | Required Verification Before Use |
| --- | --- | --- | --- |
| RF antenna pigtail generic | `08_COMPONENT_DATABASE/10_RF_AND_ANTENNAS/RF_ANTENNA_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Connector type, gender, cable length/loss, frequency range, mating connector |
| PCB antenna keepout generic | `08_COMPONENT_DATABASE/10_RF_AND_ANTENNAS/RF_ANTENNA_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Antenna vendor layout, board stackup, copper keepout, enclosure proximity |
| U.FL to SMA pigtail generic | `08_COMPONENT_DATABASE/10_RF_AND_ANTENNAS/RF_ANTENNA_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | U.FL/IPEX variant, SMA/RP-SMA gender, cable loss, strain relief, mechanical clearance |

## Agent Rules

- Do not invent controlled-impedance widths without the PCB stackup and calculator output.
- Do not place copper, ground pours, traces, mounting holes, or connectors inside antenna keepouts unless the antenna source document explicitly permits it.
- Do not equate U.FL, IPEX, MHF1, MHF3, and MHF4 mechanically.
- Do not use pigtail records as PCB footprints; the board-side connector still needs an exact part and drawing.
- Store public links and summaries first. Bundle RF vendor PDFs only if redistribution rights are clear.

## Related Rules

- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/RF_FEEDLINE_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/RF_CONNECTOR_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/ESP32_RF_ANTENNA_RULES.md`
