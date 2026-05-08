# PCB Pill-Style DRC After Placement Repair

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Scope: DRC snapshot requested after placement repair task.

PCB edited before this DRC: `NO`

Reason: Mandatory phase gate blocked placement repair before KiCad PCB edits.

## Command

```powershell
kicad-cli pcb drc --schematic-parity --severity-all --format report --output "04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PILL_STYLE_DRC_AFTER_PLACEMENT_REPAIR.rpt" "04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb"
```

## Console Summary

```text
Found 73 violations
Found 78 unconnected items
Found 0 schematic parity issues
```

## Result

DRC result: `FAIL_CURRENT_UNREPAIRED_PLACEMENT`

Schematic parity: `PASS`

Routing state: `NOT_ROUTED`

## Category Summary

| Category | Count | Disposition |
|---|---:|---|
| `unconnected_items` | 78 | Expected before routing. |
| `silk_overlap` | 19 | Needs placement/silkscreen repair. |
| `courtyards_overlap` | 18 | Placement/mechanical blocker. |
| `silk_over_copper` | 17 | Needs silkscreen repair. |
| `drill_out_of_range` | 12 | U2 footprint/rule review blocker. |
| `copper_edge_clearance` | 4 | USB-C edge/overhang review blocker. |
| `clearance` | 3 | Placement density blocker. |
| schematic parity issues | 0 | Clean. |

## Evidence Files

- `reports/PCB_PILL_STYLE_DRC_AFTER_PLACEMENT_REPAIR.rpt`
- `reports/PCB_PILL_STYLE_DRC_AFTER_PLACEMENT_REPAIR.console.txt`

## Routing Gate

Routing allowed: `NO`
