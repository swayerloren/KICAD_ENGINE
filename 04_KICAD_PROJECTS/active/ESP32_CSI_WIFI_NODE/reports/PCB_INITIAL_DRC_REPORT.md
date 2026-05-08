# PCB Initial DRC Report

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Scope: Phase 2 initial DRC after Q1 PMOS pin mapping repair and PCB schematic sync.

## Result

DRC result: `FAIL_EXPECTED_PHASE2_INITIAL_LAYOUT`

Schematic parity result: `PASS`

## Command Evidence

Command:

`kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/PCB_INITIAL_DRC_REPORT.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Console summary:

```text
Found 13 violations
Found 78 unconnected items
Found 0 schematic parity issues
Saved DRC Report to 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_INITIAL_DRC_REPORT.rpt
```

## DRC Violations

The DRC violations are expected at this phase because mechanical setup and routing have not started.

| Category | Count | Status |
|---|---:|---|
| Drill size out of range | 12 | Open for later footprint/mechanical review |
| Invalid outline | 1 | Expected before mechanical setup |
| Unconnected items | 78 | Expected before routing |
| Schematic parity issues | 0 | Resolved |
| Footprint errors | 0 | Resolved |

## Q1 Check

Q1 parity blocker is gone.

| Pad | Net |
|---|---|
| `1` | `GND` |
| `2` | `/+5V_PROTECTED` |
| `3` | `/+5V_FUSED` |

## Classification

`DRC_FAIL_EXPECTED_PRE_LAYOUT_NO_SYNC_BLOCKER`

This DRC result does not block Phase 3 placement planning. It does block later fabrication, production review, and signoff phases until mechanical setup, placement, routing, and final audit are complete.
