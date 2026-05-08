# LJ Bottom Edge Connector Review Checklist

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07T13:03:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

## Review Required

Routing remains blocked until LJ reviews and accepts or redirects the connector/mechanical decisions below.

## Checklist

| Item | Status | LJ Review |
|---|---|---|
| J2 USB-C is on bottom edge | `PASS` | Confirm visually in KiCad/3D. |
| J2 mouth faces down/off-board | `PASS` | Confirm using 3D render. |
| J2 PCB-edge alignment | `PASS_WITH_REVIEW_NOTE` | Confirm footprint PCB-edge line against Edge.Cuts in KiCad. |
| J1 is not side-mounted | `PASS` | J1 is bottom-left in 2D. |
| J1 mouth faces down/off-board | `BLOCKED` | Cannot prove without the missing barrel jack 3D model or LJ acceptance of 2D footprint evidence. |
| J1 should remain barrel jack on pill board | `NEEDS_LJ_DECISION` | Decide whether to keep J1 or replace with smaller power input in a later schematic/PCB revision. |
| Test pads clear of USB-C shell | `PASS` | TP row is on right side, not behind J2. |
| USB passives separate from test pads | `PASS` | R6/R7/R8/R9 are not mixed into service row. |
| U3 close to J2 | `PASS` | U3 directly behind J2. |
| U2 RF keepout clear before routing/zones | `PASS_FOR_CURRENT_PHASE` | No traces/zones/vias exist yet. |
| Mounting holes clear of RF and connector areas | `PASS` | Four holes are placed outside obvious connector/RF areas. |
| Silkscreen over pads/holes | `PASS` | Latest DRC shows no silkscreen warnings. |
| U2 pad 41 drill-size violations | `BLOCKER` | Needs footprint/rule/manufacturing decision before routing signoff. |

## LJ Decisions Needed

1. Accept J1 bottom-left placement based on 2D footprint/courtyard evidence, or require a valid 3D model before accepting.
2. Decide whether the barrel jack should remain on this pill-style board or be replaced in a later revision.
3. Resolve U2 pad 41 drill-size DRC issue: footprint correction, board rule exception, or manufacturer capability decision.

## Routing Status

`ROUTING_BLOCKED`
