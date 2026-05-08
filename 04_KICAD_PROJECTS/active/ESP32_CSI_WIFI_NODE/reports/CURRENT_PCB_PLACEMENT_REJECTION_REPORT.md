# Current PCB Placement Rejection Report

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Task type: `PLACEMENT_REJECTION_AND_REDESIGN_SPEC_ONLY`

PCB edited: `NO`

Fabrication outputs generated: `NO`

## Rejection

Current 100 mm x 65 mm placement is rejected as:

`PLACEMENT_REJECTED_NOT_PRODUCTION_SUITABLE`

## Why The Current Placement Is Rejected

The current placement is technically organized enough for a first mechanical/placement exercise, but it is not a practical ESP32/STM32-pill-style development board layout.

Specific rejection reasons:

- The 100 mm x 65 mm board creates a large unused dead area.
- The board aspect ratio is wrong for a compact dev-board format.
- The ESP32 module is placed in the upper/right area instead of being the top-end anchor of a narrow board.
- The ESP32 RF/antenna/U.FL keepout is not treated as the primary board-edge constraint.
- USB-C is on the right edge, which is acceptable for a rectangular carrier board but wrong for the requested pill-style dev-board concept.
- The barrel jack was accommodated by making the board large, which is not acceptable unless LJ explicitly chooses a wider prototype-carrier style.
- Test pads are accessible but consume a wide bottom row instead of using a side/bottom dev-board-friendly service strip.
- The placement wastes board area that should be eliminated before routing.

## Existing Evidence Used

| Evidence | Status |
|---|---:|
| PCB exists | `YES` |
| Footprint count | `43` |
| Current board outline | `100 mm x 65 mm` |
| Current DRC schematic parity | `0 schematic parity issues` |
| Current routing | `NOT_ROUTED` |
| Current zones | `NONE` |
| Current placement audit | Previously classified `PLACEMENT_READY_FOR_LJ_REVIEW`, now superseded by LJ rejection. |

## Current Placement Disposition

The current placement must not be routed.

Routing status: `BLOCKED_BY_REJECTED_PLACEMENT`

Next appropriate work: create a new compact dev-board/pill-style board outline and placement pass after LJ approves the selected redesign spec.

## Notes

This report rejects the current physical layout only. It does not reject the schematic, the imported footprint set, or the Q1 schematic-to-footprint pin-mapping repair.
