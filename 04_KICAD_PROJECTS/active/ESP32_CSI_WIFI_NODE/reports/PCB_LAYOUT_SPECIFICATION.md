# PCB Layout Specification

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Phase: `PHASE_3_PLACEMENT_PLANNING`  
Status: `PLACEMENT_SPECIFICATION_CREATED`  
Scope: planning only. No PCB edits, placement, routing, zones, or fabrication outputs.

## Phase Gate

Phase gate result for Phase 3: `ALLOWED`

Evidence:

- `reports/PCB_SYNC_STATUS.md` says Phase 2 is synced and placement planning may begin.
- `reports/Q1_PMOS_PIN_MAPPING_REPAIR_REPORT.md` resolves Q1 schematic/PCB parity.
- `reports/PCB_INITIAL_DRC_REPORT.md` shows initial DRC was run and schematic parity is clean.

## Board Definition

First-pass prototype board:

- Width: `100 mm`
- Height: `65 mm`
- Origin: lower-left corner
- Board outline rectangle: `(0,0)` to `(100,65)`
- Layer count: 2
- Thickness: `1.6 mm`
- Units: mm

Coordinate convention:

- `x=0` is left edge.
- `x=100` is right edge.
- `y=0` is bottom edge.
- `y=65` is top edge.
- Coordinates are footprint nominal centers unless an edge alignment is stated.

## Mounting Holes

Use four M2.5 NPTH holes:

| Ref | Center | Drill | Copper | Clearance requirement |
|---|---:|---:|---|---|
| `MH1` | `(5,5)` | `2.7 mm` | none | 3 mm copper/component clearance |
| `MH2` | `(95,5)` | `2.7 mm` | none | 3 mm copper/component clearance |
| `MH3` | `(5,60)` | `2.7 mm` | none | 3 mm copper/component clearance |
| `MH4` | `(95,60)` | `2.7 mm` | none | 3 mm copper/component clearance |

Mounting-hole exclusion circles should be treated as at least `r=4.35 mm` from hole center for component/copper planning: `1.35 mm drill radius + 3.0 mm clearance`.

## Connector Placement

### J1 Barrel Jack

- Target center: `(4.0,17.0)`
- Edge: left board edge
- Orientation: jack opening faces off-board to the left
- Placement note: horizontal barrel jack footprint may require body or courtyard overhang past `x=0`; final mechanical setup must align the jack mouth/body with the board edge using the actual footprint outline.
- Keepout: reserve `x=0..18`, `y=8..28` for J1 body/courtyard, plug insertion, and power-entry clearance.
- Power-flow direction: left-to-right from J1 to F1, Q1, D3/C2/C5, then U1.

### J2 USB-C

- Target center: `(96.5,18.0)`
- Edge: right board edge
- Orientation: USB-C mouth faces off-board to the right
- Edge alignment: connector front/mouth edge aligns to `x=100`
- Placement note: actual footprint anchor may not equal connector mouth. During mechanical setup, align the footprint’s PCB-edge/mouth geometry to the right board edge, not merely its center.
- Keepout: reserve `x=84..100`, `y=8..29` for connector body, cable clearance, and USB support passives.

## ESP32 Module Placement

U2: `ESP32-S3-WROOM-1U` value with footprint `RF_Module:ESP32-S3-WROOM-1`.

- Target center: `(69.0,43.0)`
- Orientation assumption: module long axis left-right; antenna/U.FL/pigtail side points toward the top edge.
- Human-review flag: value is `ESP32-S3-WROOM-1U` while footprint is `ESP32-S3-WROOM-1`. This must be reviewed before final placement approval because the `1U` external-antenna module has different antenna/U.FL/pigtail mechanical concerns than onboard-antenna variants.
- Keepout: reserve a no-component/no-copper RF clearance band from approximately `x=52..86`, `y=52..65`, adjusted to the actual footprint’s antenna/U.FL/pigtail keepout once placed.
- USB pins should face or be routed toward the USB support area at right/lower-right as directly as the footprint pinout allows.
- Keep the buck switch node and inductor away from the U2 RF/top keepout.

## Power Placement Strategy

Power path is a tight left-to-center chain:

`J1 -> F1 -> Q1 -> D3/C2/C5 -> U1/L1/C6/C7/C8 -> +3V3 rail -> U2`

Recommended area:

- Power entry: `x=3..30`, `y=13..23`
- Protection/input bulk: `x=25..45`, `y=13..27`
- Buck regulator: `x=42..58`, `y=23..35`
- Output capacitors / +3V3 handoff: `x=55..67`, `y=28..38`

Placement requirements:

- F1 immediately after J1 center pin path.
- Q1 after F1, with short drain/source path and gate pull/reference routed cleanly.
- D3 and C2/C5 near protected input and GND return.
- U1 close to protection but physically separated from USB D+/D- and U2 RF keepout.
- L1 adjacent to U1 SW pin.
- C6 close to U1 BST/SW pins.
- C2/C5 close to U1 IN/GND.
- C7/C8 close to U1 output/+3V3/GND.
- BUCK_SW copper short, compact, and isolated from USB/RF.

## USB Placement Strategy

USB path:

`J2 -> U3 ESD -> R8/R9 series -> U2 USB pins`

Recommended area:

- Connector: right edge around `(96.5,18.0)`
- ESD: `(85.0,18.0)`, within 5-10 mm of connector signal pins if the actual footprint allows
- CC resistors: `(86.5,13.0)` and `(86.5,15.0)`, close behind J2
- Series resistors: `(80.5,19.0)` and `(80.5,21.0)`, between ESD and U2 USB pins
- USB test pads TP8/TP9: bottom test row only if accepted despite stub risk; otherwise move/remove from high-speed path during later review

Routing assumptions:

- Route DP/DM as short, parallel, same-layer traces where practical.
- Avoid vias unless needed for escape.
- Avoid running USB under or near the buck switch node.
- Place U3 with the protected side toward U2 and connector side toward J2, subject to verified pinout/orientation.

## Reset, Boot, LEDs, and Test Pads

Switches:

- `SW1 BOOT`: accessible bottom edge near `(40,8)`
- `SW2 RESET/EN`: accessible bottom edge near `(50,8)`

LEDs:

- `D1 PWR_LED`: visible bottom/front edge near `(58,8)`
- `D2 STATUS_LED`: visible bottom/front edge near `(64,8)`
- LED resistors close to their LEDs and source nets.

Test pads:

- Place in a clean row along bottom edge at `y=6.5`, between `x=25` and `x=75`.
- Keep away from mounting holes at `(5,5)` and `(95,5)`.
- Maintain readable labels above or below pads, outside copper/pad areas.

## Ground and Zone Strategy

Planned later phase, not created in this task:

- B.Cu solid GND plane.
- F.Cu local GND pours where helpful.
- No copper in ESP32 antenna/U.FL/pigtail keepout.
- Via stitching near USB shield/ESD return and board perimeter.
- Normal thermal relief for passives.
- Direct/solid GND for ESD and high-current return where appropriate.
- Keep USB shield policy human-reviewed before final zone/return implementation.

## Trace Width Starting Points

Initial net-class targets:

| Class | Width | Clearance | Notes |
|---|---:|---:|---|
| Signal | `0.20 mm` | `0.20 mm` | low-speed GPIO, boot/reset, LEDs |
| USB FS D+/D- | `0.25 mm` | `0.20 mm` | matched/parallel as practical |
| +3V3 power | `0.50 mm min` | `0.20 mm` | wider near regulator/output caps if possible |
| +5V/protected input | `0.75 mm min` | `0.20 mm` | where space allows |
| Buck switch node | compact | `0.20 mm+` | short, controlled copper, no long run |
| Vias | `0.60 mm dia / 0.30 mm drill` | per rules | unless footprint constraints require otherwise |

## Blockers Before Placement

The following must be handled or explicitly accepted before Phase 5 component placement is considered review-ready:

1. Confirm actual J1 barrel jack footprint edge/mouth anchor and overhang.
2. Confirm actual J2 USB-C footprint edge alignment and connector orientation.
3. Review `ESP32-S3-WROOM-1U` value versus `RF_Module:ESP32-S3-WROOM-1` footprint.
4. Review U2 pad 41 drill-size DRC issue.
5. Confirm U3 USB ESD pinout/orientation.
6. Confirm D3 TVS package/polarity/orientation.
7. Confirm Q1 AO3401A package/orientation on SOT-23 despite resolved pin mapping.
8. Decide whether TP8/TP9 are allowed on USB D+/D- given stub risk.
9. Confirm USB shield/GND policy.

## Placement May Begin

Placement planning is complete enough to proceed to Phase 4 mechanical setup, not direct component placement.

Next allowed phase after this planning package: `PHASE_4_MECHANICAL_SETUP`.
