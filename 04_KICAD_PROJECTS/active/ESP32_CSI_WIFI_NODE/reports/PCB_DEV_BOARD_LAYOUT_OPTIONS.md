# PCB Dev-Board / Pill-Style Layout Options

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Task type: `LAYOUT_SPEC_ONLY`

PCB edited: `NO`

Coordinate convention: origin at lower-left, x increases right, y increases upward, all dimensions in mm.

## Design Intent

The redesigned board should behave like an ESP32/STM32 pill-style development board:

- Narrow rectangular board.
- ESP32 module at the top with RF/antenna/U.FL keepout reaching the top board edge.
- USB-C at the bottom edge, mouth facing downward.
- Power and USB support circuitry stacked vertically behind the bottom connectors.
- Buttons, LEDs, and test pads along edges instead of occupying a large center dead area.
- Barrel jack treated as a mechanical compromise, not as a reason to keep a giant board.

## Shared Placement Rules

| Area | Rule |
|---|---|
| ESP32 / RF | `U2` must be centered near the top. Antenna/U.FL end points to the top edge. No copper/components/traces under RF keepout. |
| USB | `J2` USB-C must sit on the bottom edge, connector mouth off-board downward. `U3`, `R8`, `R9`, `R6`, and `R7` go directly above/behind J2. |
| Barrel/input | `J1` is not allowed to force a giant board. If the footprint cannot fit a narrow board cleanly, flag replacement with JST/terminal/2-pin input. |
| Buck power | `J1/F1/Q1/D3/C2/C5/U1/C6/L1/C7/C8` must form one compact lower-left or mid-left power island. |
| Buttons | `SW1/SW2` must be reachable from bottom or side edge. |
| LEDs | `D1/D2` must be visible on bottom/front or side edge. |
| Test pads | `TP1-TP9` should form one service strip along a side or lower edge. USB `D+`/`D-` test pads remain optional/stub-risk flagged. |
| Mounting holes | Prefer M2.5 NPTH holes 3.5 mm from board edges if they do not collide with connector/module keepouts. |
| Ground | Bottom solid GND plane planned later. Top local GND pours only where useful. No copper under antenna keepout. |

## Option A - 38 x 80 mm Pill Board With Side Barrel Jack

Recommended first-pass compact board that keeps the existing barrel jack only as a side-mounted compromise.

### Board

- Dimensions: `38 mm wide x 80 mm tall`
- Outline: `(0,0)` to `(38,80)`
- Board style: narrow dev-board / pill board
- Thickness assumption: `1.6 mm`

### Placement

| Item | Proposed placement |
|---|---|
| `U2` ESP32-S3 module | Center at approximately `(19,64)`. Orient so antenna/U.FL/keepout points to top edge. Keepout extends from module RF end to y=`80`. |
| `J2` USB-C | Bottom edge, center at approximately `(19,1.5-3.0)` depending footprint origin. Mouth faces downward/off-board. PCB edge line aligns with y=`0`. |
| `U3` USB ESD | Directly above J2 at approximately `(19,10)`, rotated to minimize D+/D- crossover. |
| `R8/R9` USB series | Between U3 and U2, approximately `(16,14)` and `(22,14)`, close enough to keep pair short. |
| `R6/R7` CC resistors | Near J2/U3 at approximately `(12,8)` and `(26,8)`. |
| `J1` barrel jack | Left side lower edge, centered around `(2,16)` or `(3,18)`, opening off-board left. Do not use bottom edge unless footprint/courtyard proves clean. |
| `F1/Q1/D3/C2/C5` input protection | Lower-left/mid-left chain around x=`7-17`, y=`17-31`. |
| `U1/C6/L1/C7/C8` buck cluster | Mid-left/center around x=`18-28`, y=`28-42`, with L1 immediately beside U1 and capacitors tight to pins. |
| `SW1/SW2` | Right or left side edge around y=`18-30`, reachable by finger, not under J1/USB. |
| `D1/D2` LEDs | Bottom/front side around x=`28-34`, y=`8-16`, visible from top. |
| `TP1-TP9` | Right-side vertical service strip at x=`34.5`, y=`18-50`, or left-side strip if barrel placement leaves room. |
| Mounting holes | Preferred 4x M2.5 NPTH at `(3.5,3.5)`, `(34.5,3.5)`, `(3.5,76.5)`, `(34.5,76.5)`, but top holes must be checked against U2 RF keepout. Fallback 2-hole variant uses `(3.5,3.5)` and `(34.5,76.5)` or centerline holes `(19,4)` and `(19,76)`. |

### Routing Feasibility

- Good vertical flow: USB bottom to U2 top.
- Power island can stay below module keepout.
- Buck switch node can be kept short near U1/L1.
- U2 antenna area is no longer trapped in the center of the board.
- Barrel jack side entry may create local congestion and must be reviewed before committing.

### Pros

- Best match to pill-board style while preserving the existing barrel jack if it fits.
- Compact but not extreme.
- Clear USB-to-ESP32 vertical routing path.
- Good prototype ergonomics.

### Cons

- Existing barrel jack remains bulky for 38 mm width.
- Four M2.5 holes may be tight near the top RF keepout.
- Side test-pad strip must be planned carefully to avoid routing congestion.

### Production Risk

`MEDIUM`

Main risk is mechanical: barrel jack fit, mounting-hole clearance, and U2 RF keepout interaction.

### Recommendation

`RECOMMENDED_FIRST_PASS`

Use this if LJ wants a practical compact board but is not ready to remove the barrel jack from the design.

## Option B - 35 x 75 mm Compact Pill Board Without Barrel Jack

Most dev-board-like option. It assumes the barrel jack is removed, DNP, or replaced with a smaller input connector after LJ approval.

### Board

- Dimensions: `35 mm wide x 75 mm tall`
- Outline: `(0,0)` to `(35,75)`
- Board style: compact pill board

### Placement

| Item | Proposed placement |
|---|---|
| `U2` ESP32-S3 module | Center around `(17.5,60)`, antenna/U.FL/keepout points to top edge and extends to y=`75`. |
| `J2` USB-C | Bottom edge, center around `(17.5,1.5-3.0)`, mouth downward/off-board. |
| `J1` barrel jack | `NOT_RECOMMENDED`. Replace/flag as not pill-board-friendly. Suggested future input: JST-PH, JST-XH, 2-pin terminal, or solder pads after LJ approval. |
| Power section | Lower-left to center stack around x=`7-25`, y=`12-35`; no large side barrel obstruction. |
| USB section | Directly above J2: U3 at y=`9-11`, CC resistors beside/above, series resistors above U3. |
| Buttons | Side-edge tactile placement around y=`12-25`. |
| LEDs | Bottom/side visible edge around y=`8-18`. |
| Test pads | One side-edge vertical row, preferably x=`31-32`, y=`16-48`. |
| Mounting holes | Use 2x M2.5 NPTH preferred at centerline `(17.5,4)` and `(17.5,71)`, or small corner holes only if DRC/courtyard clearances prove room. |

### Routing Feasibility

- Best routing flow for USB and ESP32.
- Best RF keepout handling.
- Power routing improves because barrel jack is gone.
- Requires human-approved input connector strategy change.

### Pros

- Most like a real compact ESP32 development board.
- Lowest dead area.
- Best antenna placement.
- Cleaner routing than Option A.

### Cons

- Requires changing the power-input mechanical concept.
- Existing J1 footprint cannot be preserved without defeating compactness.
- Four M2.5 holes are unlikely to be worthwhile.

### Production Risk

`MEDIUM_HIGH_UNTIL_INPUT_DECISION`

Risk comes from requiring LJ approval to remove/replace the barrel jack.

### Recommendation

`BEST_LONG_TERM_COMPACT_OPTION_IF_LJ_APPROVES_INPUT_CHANGE`

## Option C - 45 x 80 mm Wider Prototype Board With Barrel Jack

Wider prototype option for keeping the barrel jack and four mounting holes comfortably.

### Board

- Dimensions: `45 mm wide x 80 mm tall`
- Outline: `(0,0)` to `(45,80)`
- Board style: wider prototype dev board

### Placement

| Item | Proposed placement |
|---|---|
| `U2` ESP32-S3 module | Center around `(22.5,64)`, antenna/U.FL/keepout points to top edge and extends to y=`80`. |
| `J2` USB-C | Bottom edge, center around `(22.5,1.5-3.0)`, mouth downward/off-board. |
| `J1` barrel jack | Lower-left side edge around `(3,18)` with opening off-board left, or bottom-left if a footprint-specific edge alignment proves clean. |
| Power section | Left/mid-lower block around x=`8-30`, y=`16-42`, with more room for F1/Q1/D3/U1/L1/caps. |
| USB section | Center-bottom behind J2 around x=`16-29`, y=`7-20`. |
| Buttons | Lower side edges around y=`12-28`. |
| LEDs | Lower/right visible region around y=`8-18`. |
| Test pads | Right-side vertical strip x=`41`, y=`15-52`, or bottom side row if connector clearances allow. |
| Mounting holes | 4x M2.5 NPTH at `(3.5,3.5)`, `(41.5,3.5)`, `(3.5,76.5)`, `(41.5,76.5)`, subject to U2 keepout and connector courtyard check. |

### Routing Feasibility

- Best fit if barrel jack must remain.
- More room for thermal copper around U1/L1.
- More room for clean test pad labels and four mounting holes.
- Still compact enough compared with the rejected 100 x 65 board.

### Pros

- Keeps current barrel jack with less mechanical strain.
- Four mounting holes are more realistic.
- More forgiving for hand assembly/prototype changes.

### Cons

- Less pill-like than Options A/B.
- Wider than needed if barrel jack is removed.
- Still has a larger area than a true compact dev board.

### Production Risk

`LOWER_MECHANICAL_RISK_MEDIUM_SIZE_RISK`

Best mechanical fit, but size may be larger than desired.

### Recommendation

`RECOMMENDED_IF_BARREL_JACK_AND_4_HOLES_ARE_MANDATORY`

## Option Comparison

| Option | Size | Barrel jack | Mounting holes | Fit to pill-board goal | Recommendation |
|---|---:|---|---|---|---|
| A | `38 x 80 mm` | Side lower-left compromise | 4 preferred, 2-hole fallback | Strong | Selected first-pass |
| B | `35 x 75 mm` | Remove/replace required | 2 preferred | Best | Use if LJ approves input change |
| C | `45 x 80 mm` | Comfortable side/lower-left | 4 realistic | Moderate | Use if barrel + 4 holes are mandatory |

## Selected Option

Selected layout for next placement reset: `Option A - 38 x 80 mm pill board with side barrel jack compromise`.

Reason:

- It fixes the current dead-area problem.
- It puts U2 and the RF keepout at the top edge.
- It puts USB-C at the bottom like a practical dev board.
- It preserves the existing barrel jack only if footprint/courtyard review proves it can fit.
- It provides a clear fallback path to Option C or Option B if the barrel jack blocks the compact layout.
