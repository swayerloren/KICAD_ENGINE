# PCB File Current State

Date: `2026-05-07`

PCB file: `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## File Identity

| Field | Value |
| --- | --- |
| SHA256 | `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844` |
| Last modified | `2026-05-07 16:28:37 -04:00` |
| Size | `170233 bytes` |

## Geometry

| Field | Value |
| --- | --- |
| Edge.Cuts segments | `4` |
| Outline result | `PASS - closed rectangular outline present` |
| Outline extents | `xmin 0.0 / xmax 60.0 / ymin 0.0 / ymax 95.0` |
| Board dimensions | `60.0 mm x 95.0 mm` |

## Inventory

| Field | Value |
| --- | --- |
| Nets | `52` |
| Pads | `167` |
| Footprints | `43` |
| Mounting-hole footprints | `4` |
| Track segments | `24` |
| Grouped traces | `6` |
| Vias | `2` |
| Zones | `0` |
| Keepouts extracted | `0` |

## Anchor Placement Check

Live footprint-anchor bounding check against the board outline:

- anchors inside board bbox: `43 / 43`
- anchors outside board bbox: `0`

This is an anchor-position check only. It does not prove full body, courtyard, or enclosure fit clearance.

## Key Live Placements

| Ref | Footprint | Position |
| --- | --- | --- |
| `J1` | `BarrelJack_CUI_PJ-102AH_Horizontal` | `(14.0, 80.8)` |
| `J2` | `USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `(39.0, 91.325)` |
| `U1` | `TSOT-23-6` | `(29.0, 69.5)` |
| `U2` | `ESP32-S3-WROOM-1` | `(30.0, 28.0)` |
| `U3` | `SOT-23-6` | `(39.0, 78.0)` |
| `Q1` | `SOT-23` | `(23.0, 78.0)` |
| `L1` | `L_Vishay_IFSC-1515AH_4x4x1.8mm` | `(37.0, 69.5)` |

## Visual Evidence

- `_verification/pcb_visual/live_pcb_truth_audit/top.png`
- `_verification/pcb_visual/live_pcb_truth_audit/bottom.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_power_input_area.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_regulator_power_path.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_esp32_module_antenna_keepout.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_usb_c_connector.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_test_pad_row.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_mounting_holes_montage.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_existing_routed_traces_top.png`
- `_verification/pcb_visual/live_pcb_truth_audit/crop_existing_routed_traces_bottom.png`

## Current State Classification

`PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
