# PCB Pill-Style DRC Report

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Scope: DRC after pill-style placement reset. No routing or zones were added.

## Command

```powershell
kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports/PCB_PILL_STYLE_DRC_REPORT.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

Console summary:

```text
Found 73 violations
Found 78 unconnected items
Found 0 schematic parity issues
```

## Result

DRC result: `FAIL_EXPECTED_PLACEMENT_ONLY_WITH_MECHANICAL_BLOCKERS`

Schematic parity result: `PASS`

Routing result: `NOT_ROUTED`

## DRC Category Summary

| Category | Count | Status |
|---|---:|---|
| `unconnected_items` | 78 | Expected because routing has not started. |
| `silk_overlap` | 19 | Needs silkscreen cleanup after LJ placement decision. |
| `courtyards_overlap` | 18 | Mechanical density issue on 38 mm board; needs LJ review before routing. |
| `silk_over_copper` | 17 | Needs silkscreen cleanup after LJ placement decision. |
| `drill_out_of_range` | 12 | Known U2 0.20 mm drill vs 0.30 mm rule issue. |
| `copper_edge_clearance` | 4 | USB-C edge/overhang review item. |
| `clearance` | 3 | Tight placement clearance issues needing repair if this layout is accepted. |
| `shorting_items` | 0 | No current shorting-items category in the final DRC category summary. |
| `schematic parity` | 0 | Clean. |

## Important Findings

- No schematic parity issues remain.
- No traces were routed, so unconnected items are expected.
- DRC still blocks routing because mechanical/courtyard/silkscreen/clearance issues remain.
- The 38 mm compact layout is feasible as a visual concept but not ready to route until LJ accepts or changes the barrel jack, mounting-hole, and ESP32 footprint constraints.

## Classification

`PILL_STYLE_DRC_FAIL_NEEDS_PLACEMENT_REVIEW`

Routing remains: `BLOCKED`
