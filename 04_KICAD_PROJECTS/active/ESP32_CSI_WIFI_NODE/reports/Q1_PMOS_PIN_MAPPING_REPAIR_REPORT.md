# Q1 PMOS Pin Mapping Repair Report

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Scope: Phase 2 PCB sync repair only. No component placement, routing, zones, or fabrication outputs were generated.

## Result

Q1 schematic-to-PCB pin mapping blocker is resolved.

## Backup

Backup created before edits:

`C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260507_102307_ESP32_CSI_WIFI_NODE_pre_q1_pmos_pinmap_repair`

## Source Evidence

Q1 intended part: AO3401A P-channel MOSFET, SOT-23.

Sources used:

- Repo source record: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/DATASHEET_CHECKLIST.md`
- Repo source record: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/COMPONENT_SELECTION_REPORT.md`
- Official AOS product page: `https://www.aosmd.com/products/mosfets/p-channel-mosfets-8v-60v/ao3401a`
- Official AOS datasheet PDF: `https://www.aosmd.com/sites/default/files/res/datasheets/AO3401A.pdf`
- KiCad standard symbol used for numeric PMOS pin mapping: `Transistor_FET:Q_PMOS_GSD`
- KiCad SOT-23 footprint used by Q1: `Package_TO_SOT_SMD:SOT-23`

Verified mapping for the repaired schematic/PCB sync:

| Pad / pin | Function | PCB net after sync |
|---|---|---|
| 1 | Gate | `GND` |
| 2 | Source | `/+5V_PROTECTED` |
| 3 | Drain | `/+5V_FUSED` |

## Before Mapping

Q1 used generic schematic symbol `Device:Q_PMOS` with non-numeric pins:

| Schematic pin | Function | Net |
|---|---|---|
| `G` | Gate | `GND` |
| `S` | Source | `/+5V_PROTECTED` |
| `D` | Drain | `/+5V_FUSED` |

The assigned footprint was `Package_TO_SOT_SMD:SOT-23`, whose pads are numbered `1`, `2`, and `3`. This caused schematic parity errors because PCB pads `1/2/3` could not match schematic pins `G/S/D`.

## After Mapping

Q1 now uses KiCad standard numeric PMOS symbol:

`Transistor_FET:Q_PMOS_GSD`

The schematic instance and generated netlist now use numeric pins:

| Schematic pin | Function | PCB pad | Net |
|---|---|---|---|
| `1` | Gate | `1` | `GND` |
| `2` | Source | `2` | `/+5V_PROTECTED` |
| `3` | Drain | `3` | `/+5V_FUSED` |

The PCB was re-synced from the schematic netlist for footprint pad nets and schematic paths only.

## Files Changed

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/Q1_PMOS_PIN_MAPPING_REPAIR_ERC.rpt`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/Q1_PMOS_PIN_MAPPING_REPAIR.net`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_INITIAL_DRC_REPORT.rpt`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_INITIAL_DRC_REPORT.console.txt`

## Verification

ERC:

`PASS`

`Q1_PMOS_PIN_MAPPING_REPAIR_ERC.rpt` reports 0 errors and 0 warnings.

DRC:

`FAIL_EXPECTED_PHASE2_INITIAL_LAYOUT`

DRC still reports expected pre-layout items:

- 13 DRC violations
- 78 unconnected items
- no board outline yet
- U2 pad 41 drill-size violations

Schematic parity:

`PASS`

`PCB_INITIAL_DRC_REPORT.console.txt` reports 0 schematic parity issues.

Footprints:

`PASS`

All 43 expected footprints are present. Missing footprints: none. Stale footprints: none.

## Status

PCB sync parity issues remain: `NO`

Placement planning may begin: `YES`

Component placement, routing, zones, and fabrication outputs remain blocked until their later phase gates are satisfied.
