# ESP32_CSI_WIFI_NODE PCB Placement Pass 1 Report

Date: `2026-05-07`

Status: `PLACEMENT_EXISTS_NEEDS_REVIEW`

## Scope

This report is a live-board placement truth audit.

No new KiCad PCB edits were made in this session.

## Live Placement Result

| Item | Result |
| --- | --- |
| PCB file exists | `YES` |
| Board outline exists | `YES - 60.0 mm x 95.0 mm` |
| Footprints present on PCB | `43` |
| Mounting holes present | `4` |
| Placement visible on live board | `YES` |
| Anchor positions inside board outline bbox | `43 / 43` |

## Current Placement Facts

- `U2` is placed near the top of the board.
- `J1` is placed on the bottom-left edge.
- `J2` is placed on the bottom edge.
- `TP1..TP9` are arranged in a right-side vertical service row.
- `SW1` and `SW2` are placed on the left side.
- Partial routing already exists around the lower power/regulator cluster.

## DRC Context

| Item | Result |
| --- | --- |
| DRC violations | `12` |
| Unconnected items | `65` |
| Zones | `0` |

The live board is not a `NO_PCB` state.

## Readiness

Ready for LJ placement review: `NO`

Routing allowed: `NO`

Reason:

- live placement exists, but refreshed placement/orientation approval is still required
- the formal schematic-to-PCB gate is still `FAIL`
- the live board still has active DRC and unrouted-net blockers
