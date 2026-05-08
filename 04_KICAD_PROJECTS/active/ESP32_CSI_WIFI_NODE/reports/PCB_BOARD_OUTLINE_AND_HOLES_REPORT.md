# ESP32_CSI_WIFI_NODE PCB Board Outline And Holes Report

Generated: `2026-05-06 22:15:29 -04:00`

Status: `NOT_CREATED_NO_PCB`

## Summary

The selected layout plan exists and recommends a `72 mm x 40 mm` board, but no `.kicad_pcb` file exists and the schematic-to-PCB gate is still failed. Therefore, board outline and mounting holes were not created.

## Selected Plan Evidence

- Selected plan: `Plan B - Connector-Edge Optimized Board`
- Evidence: `reports/PCB_SELECTED_LAYOUT_PLAN.md`
- Planning outline: `72 mm x 40 mm`
- Coordinate convention: origin at lower-left board corner; bottom edge is connector/panel edge; top edge is RF/pigtail clearance side.

## Board Outline

| Item | Value |
| --- | --- |
| Board dimensions intended for future review | `72 mm x 40 mm` |
| Lower-left corner | `(0 mm, 0 mm)` |
| Lower-right corner | `(72 mm, 0 mm)` |
| Upper-right corner | `(72 mm, 40 mm)` |
| Upper-left corner | `(0 mm, 40 mm)` |
| Applied to PCB | `NO` |

## Mounting Hole Planning Coordinates

| Ref | Planning coordinate | Planning drill/keepout | Applied |
| --- | --- | --- | --- |
| `MH1` | `(5 mm, 5 mm)` | M2.5 planning default, 2.7 mm NPTH drill, 5.5 mm to 6.0 mm keepout | `NO` |
| `MH2` | `(67 mm, 5 mm)` | M2.5 planning default, 2.7 mm NPTH drill, 5.5 mm to 6.0 mm keepout | `NO` |
| `MH3` | `(5 mm, 35 mm)` | M2.5 planning default, 2.7 mm NPTH drill, 5.5 mm to 6.0 mm keepout | `NO` |
| `MH4` | `(67 mm, 35 mm)` | M2.5 planning default, 2.7 mm NPTH drill, 5.5 mm to 6.0 mm keepout | `NO` |

## Required Before Applying

1. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` must be exact `PASS`.
2. PCB update from schematic must create/import the board file after backup.
3. Exact enclosure/standoff dimensions must confirm the board outline and hole positions.
4. Connector drawings must verify barrel jack and USB-C edge overhangs.
5. ESP32/U.FL/pigtail/SMA clearance must be reviewed.

## Result

Board outline created: `NO`

Mounting holes placed: `NO`
