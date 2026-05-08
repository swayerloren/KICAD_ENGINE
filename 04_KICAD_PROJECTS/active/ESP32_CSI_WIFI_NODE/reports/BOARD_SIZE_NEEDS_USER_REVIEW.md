# BOARD_SIZE_NEEDS_USER_REVIEW

Status: `BLOCKED_NEEDS_USER_REVIEW`

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-03

## Why This File Exists

PCB mechanical setup was requested, but the required board size and mechanical constraints are not known.

The workflow explicitly requires stopping instead of guessing when board size is unknown.

## Blocking Facts

- PCB file exists: `NO`
- PCB synced from schematic: `NO`
- Schematic-to-PCB gate: `FAIL`
- PCB update report: `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
- Mechanical note files matching `notes/mechanical*.md`: `NOT_FOUND`
- `REQUIREMENTS.md` lists exact board outline dimensions as an open question.
- `REQUIREMENTS.md` also lists mounting hole diameter, screw size, keepout/standoff geometry, enclosure internal dimensions, maximum board height, antenna/SMA location, and pigtail length as open mechanical items.

## User Decisions Required

Provide or confirm:

1. Board outline dimensions in mm.
2. Board shape if not rectangular.
3. Layer count.
4. Board thickness.
5. Fabrication house or generic design-rule target.
6. Enclosure internal dimensions.
7. Maximum component height.
8. Mounting hole count, diameter, plating, screw size, standoff diameter, and keepout radius.
9. Barrel jack exact part number, wall-facing edge, overhang, and plug clearance.
10. USB-C exact connector part number, board-edge relation, shell tab clearance, and cable clearance.
11. ESP32-S3-WROOM-1U antenna/U.FL pigtail path, SMA bulkhead location, bend radius, strain relief, and enclosure clearance.
12. Test pad access side, pad size, probe clearance, and any no-component zones.

## Required Next Step

Do not create or edit the PCB yet.

First resolve the schematic-to-PCB gate and provide mechanical constraints. Then create or update the PCB using a backed-up, KiCad-safe workflow.

