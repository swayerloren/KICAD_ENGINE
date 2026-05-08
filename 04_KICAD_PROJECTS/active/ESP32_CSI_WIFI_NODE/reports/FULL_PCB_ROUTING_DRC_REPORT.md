# Full PCB Routing DRC Report

Generated: 2026-05-07

Raw DRC report: `reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt`

Command:

`kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Result

- DRC command exit code: 0
- Schematic parity issues: 0
- Footprint errors: 0
- DRC violations: 12
- Unconnected items: 67

## DRC Categories

| category | count | classification |
|---|---:|---|
| `drill_out_of_range` | 12 | drill/footprint rule issue |
| `unconnected_items` | 67 | routing incomplete |
| schematic parity | 0 | PASS |
| footprint errors | 0 | PASS |
| shorts/crossings/clearance route errors | 0 | PASS in current partial route |

## Drill / Footprint Rule Issue

All 12 DRC violations are U2 pad 41 castellated/PTH drill-size checks:

- Rule: board setup min hole 0.3000 mm.
- Actual U2 pad 41 hole: 0.2000 mm.
- Classification: `DRILL_FOOTPRINT_RULE_ISSUE`.
- This is not a routing blocker, but it blocks clean DRC and any export readiness claim until LJ/fab/footprint decision.

## Routing Blockers

The board is not fully routed. The exact remaining unconnected count is 67, including:

- `+3V3` distribution.
- `/+5V_FUSED` through Q1/F1 local path.
- USB CC/D+/D-/shield cluster.
- ESP_EN and BOOT0 control networks.
- UART/debug/test pad nets.
- LED nets.
- GND connections that should primarily be handled with a later valid GND pour.

## Copper-Zone Status

No GND copper zones were created. Copper-pour DRC was not run because the routing-complete precondition was not met.

## Final DRC Classification

`ROUTING_PARTIAL_NEEDS_REPAIR`

