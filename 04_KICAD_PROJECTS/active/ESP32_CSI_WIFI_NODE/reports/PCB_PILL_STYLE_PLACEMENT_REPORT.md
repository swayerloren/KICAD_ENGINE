# PCB Pill-Style Placement Report

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Task type: `PCB_PLACEMENT_ONLY`

PCB edited: `YES`

Routing performed: `NO`

Zones created: `NO`

Fabrication outputs generated: `NO`

Production-ready claim: `NO`

## Backup

Backup path:

`C:/Users/LJ/GitHub/KICAD_ENGINE/99_BACKUPS/pre_codex_edits/20260507_110816_ESP32_CSI_WIFI_NODE_pre_pill_style_placement`

## Target PCB

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Board Outline

Final board size: `38 mm x 80 mm`

Edge.Cuts bbox: `(0.0, 0.0)` to `(38.0, 80.0)`

Board style: ESP32/STM32 pill-style dev board.

## Placement Summary

All 43 imported schematic footprints remain present.

No traces were routed.

No final copper zones were created.

Existing zone count after placement: `0`

## Primary Placement

| Group | Placement |
|---|---|
| `U2` ESP32 module | Centered at `(19.00, 28.00)`, rotation `0`. Visual review places the module at the top of the pill board with the RF/antenna/U.FL keepout facing the top edge. |
| `J2` USB-C | Centered at `(19.00, 77.00)`, rotation `90`. Visual review places USB-C at the bottom edge with intentional connector overhang. |
| `J1` barrel jack | Placed on lower-left side at `(7.00, 57.50)`, rotation `180`. This is the side-entry compromise from the selected spec. |
| Power cluster | `F1/Q1/D3/C2/C5/U1/C6/L1/C7/C8` placed in the lower/mid board region between J1 and U2. |
| USB cluster | `U3/R6/R7/R8/R9` placed above J2 in the lower board region. |
| Buttons | `SW1` at `(6.00, 63.00)`, `SW2` at `(32.00, 55.00)`. Both are side/lower-region accessible for LJ review. |
| LEDs | `D1/D2` with `R3/R4` near lower/right visible area. |
| Test pads | `TP1-TP9` in one row above USB-C, y=`70.50`, x=`5.00` through `33.00`. |

## Mounting Holes

Four mounting-hole footprints remain on the board, but the top pair was moved below the ESP32 RF/keepout region because corner placement conflicts with the current ESP32 footprint/keepout on a 38 mm board.

| Reference | Position | Status |
|---|---:|---|
| `MH1` | `(3.50, 76.50)` | Bottom-left, placed |
| `MH2` | `(34.50, 76.50)` | Bottom-right, placed |
| `MH3` | `(3.50, 45.50)` | Moved below U2 keepout; mechanical review required |
| `MH4` | `(34.50, 45.50)` | Moved below U2 keepout; mechanical review required |

## Known Placement Compromises

- Current `RF_Module:ESP32-S3-WROOM-1` footprint/keepout bbox is wider than the 38 mm board. The module body is centered, but the footprint/keepout/courtyard extends past the side edges. This is a mechanical/footprint review blocker, not silently accepted.
- Four corner M2.5 holes do not fit cleanly with the ESP32 keepout on 38 mm width. The current placement uses a bottom pair plus a moved mid-board pair for review.
- Barrel jack is retained as a side-mounted compromise. It is large for the board style and remains a mechanical review item.
- USB-C intentionally overhangs the bottom edge; DRC reports edge-clearance violations at USB pads that need footprint/board-edge review.
- Test pads fit as a bottom service row, but USB D+/D- test pads remain stub-risk review items before routing.

## Verification Outputs

- `reports/PCB_PILL_STYLE_DRC_REPORT.rpt`
- `reports/PCB_PILL_STYLE_DRC_REPORT.console.txt`
- `_verification/pcb_visual/pill_style_placement_top.svg`
- `_verification/pcb_visual/pill_style_placement_bottom.svg`
- `_verification/pcb_visual/pill_style_placement_top.png`
- `_verification/pcb_visual/pill_style_placement_bottom.png`
- `_verification/pcb_visual/pill_style_placement_3d_top.png`

## Placement Disposition

`PILL_STYLE_PLACEMENT_CREATED_NEEDS_LJ_VISUAL_REVIEW`

Routing remains blocked.
