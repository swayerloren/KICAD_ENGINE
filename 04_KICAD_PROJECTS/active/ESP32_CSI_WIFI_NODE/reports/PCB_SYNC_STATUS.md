# PCB Sync Status

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Status: `PCB_SYNCED`

## Phase

Current completed phase: `PHASE_2_PCB_CREATION_UPDATE_FROM_SCHEMATIC`

Next allowed phase: `PHASE_3_PLACEMENT_PLANNING`

## Sync Evidence

| Check | Result | Evidence |
|---|---:|---|
| `.kicad_pcb` exists | `YES` | `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` |
| PCB saved after sync | `YES` | KiCad Python `pcbnew.SaveBoard` completed |
| Footprints present | `43` | PCB footprint scan |
| Missing footprints | `0` | `PCB_FOOTPRINT_IMPORT_REPORT.md` |
| Stale footprints | `0` | `PCB_FOOTPRINT_IMPORT_REPORT.md` |
| Q1 PMOS pin mapping repaired | `YES` | `Q1_PMOS_PIN_MAPPING_REPAIR_REPORT.md` |
| Schematic parity clean | `YES` | `PCB_INITIAL_DRC_REPORT.console.txt` |
| ERC | `PASS` | `Q1_PMOS_PIN_MAPPING_REPAIR_ERC.rpt` |
| Initial DRC run | `YES` | `PCB_INITIAL_DRC_REPORT.rpt` |

## Q1 Sync Repair

Q1 now uses numeric PMOS symbol `Transistor_FET:Q_PMOS_GSD`.

| Pad / pin | Function | Net |
|---|---|---|
| `1` | Gate | `GND` |
| `2` | Source | `/+5V_PROTECTED` |
| `3` | Drain | `/+5V_FUSED` |

PCB DRC schematic parity reports 0 schematic parity issues.

## DRC Status

Initial DRC result: `FAIL_EXPECTED_PHASE2_INITIAL_LAYOUT`

Known expected pre-layout issues:

- no board outline yet
- 78 unconnected items because no routing has been performed
- U2 pad 41 drill-size violations to be reviewed in later mechanical/footprint review

These are not schematic sync parity blockers.

## Gate Status

PCB creation/schematic sync blocker status: `RESOLVED`

Placement planning may begin: `YES`

Component placement may not begin until placement planning is complete and approved by the phase gate.
