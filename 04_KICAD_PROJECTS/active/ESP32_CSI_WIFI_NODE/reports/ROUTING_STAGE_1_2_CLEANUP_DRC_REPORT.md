# Routing Stage 1/2 Cleanup DRC Report

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Final classification: `STAGE_1_2_PARTIAL_NEEDS_MORE_REPAIR`

## DRC Commands

Baseline:

`kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/ROUTING_STAGE_1_2_CLEANUP_BASELINE_DRC.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Current authoritative post-reroute report:

`kicad-cli pcb drc --schematic-parity --severity-all --format report --output C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_STAGE_1_2_CLEANUP_POST_DRC_V3.rpt C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Baseline

| Metric | Result |
|---|---:|
| DRC violations | 12 |
| Unconnected items | 67 |
| Schematic parity issues | 0 |

## Current Post-Reroute Result

Authoritative raw report:

- `reports/ROUTING_STAGE_1_2_CLEANUP_POST_DRC_V3.rpt`

| Metric | Result |
|---|---:|
| DRC violations | 13 |
| Unconnected items | 65 |
| Schematic parity issues | 0 |

## Violation Breakdown

| Category | Count | Notes |
|---|---:|---|
| `tracks_crossing` | 1 | remaining `SW/BST` crossing in buck cluster |
| `drill_out_of_range` | 12 | existing `U2 pad 41` rule issue |
| schematic parity | 0 | `PASS` |

## Interpretation

What improved:

- Unconnected items improved from `67` to `65`.
- `/+5V_IN` is routed.
- `/+5V_FUSED` is routed.
- local `+3V3` output routing exists.
- No new schematic parity issues were introduced.

What still blocks completion:

- `SW/BST` crossing remains in the `U1/C6/L1` buck cluster.
- `TP1` on `/+5V_PROTECTED` remains unrouted.
- The long-standing `U2` drill-rule issue remains unchanged.

## DRC Gate Result

| Decision | Result |
|---|---|
| Stage 1/2 clean reroute complete | `NO` |
| Stage 3 USB may begin | `NO` |
| Copper pour allowed | `NO` |

## Final DRC Status

`ROUTING_PARTIAL_NEEDS_REPAIR`
