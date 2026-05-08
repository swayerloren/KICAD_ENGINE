# PCB Intelligence-Based DRC Report

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Command output files:

- Raw report: `reports/PCB_INTELLIGENCE_BASED_DRC_REPORT.rpt`
- Console log: `reports/PCB_INTELLIGENCE_BASED_DRC_REPORT.console.txt`

## Command

```powershell
kicad-cli pcb drc --schematic-parity --severity-all --format report --output reports\PCB_INTELLIGENCE_BASED_DRC_REPORT.rpt kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

## Summary

| Check | Result |
|---|---:|
| DRC violations | `18` |
| Unconnected items | `78` |
| Schematic parity issues | `0` |
| Tracks present | `0` |
| Zones present | `0` |

## DRC Categories

| Category | Count | Disposition |
|---|---:|---|
| `drill_out_of_range` | `12` | `BLOCKING_FOOTPRINT_OR_RULE_REVIEW` |
| `silk_over_copper` | `3` | `SILKSCREEN_CLEANUP` |
| `silk_overlap` | `3` | `SILKSCREEN_CLEANUP` |
| `unconnected_items` | `78` | `EXPECTED_UNROUTED` |

## Blocking Finding

The only non-silkscreen hard DRC class after placement repair is:

`U2 pad 41 drill_out_of_range`

KiCad reports U2 pad 41 holes at `0.2000 mm` while the board setup minimum hole constraint is `0.3000 mm`. This is a footprint/rule/manufacturability review item and must not be silently accepted before routing signoff.

## Expected Findings

`unconnected_items = 78` is expected because this task explicitly prohibited routing.

## Classification

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing remains blocked pending LJ review and resolution or explicit acceptance of the U2 drill/rule issue.
