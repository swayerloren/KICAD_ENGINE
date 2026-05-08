# ESP32_CSI_WIFI_NODE Selected PCB Layout Plan

Generated: `2026-05-06 22:11:31 -04:00`

Selected plan: `Plan B - Connector-Edge Optimized Board`

Status: `SELECTED_FOR_PLANNING_ONLY`

Placement may begin: `NO`

## Why Plan B Is Best

Plan B is the strongest first-layout strategy because it separates the board into predictable functional zones while preserving enclosure usability:

- Barrel jack and USB-C can share one enclosure-facing edge.
- Input power and protection stay on the left side.
- USB-C, ESD, CC resistors, and USB pair routing stay on the right side near ESP32.
- ESP32-S3-WROOM-1U can sit in the upper-right area with antenna/U.FL/pigtail clearance along the top or right edge.
- Buck regulator has enough left-center board area for compact hot-loop routing and thermal copper.
- Test pads and LEDs can be reachable and readable without interfering with RF or connector mechanics.

## Board Size Recommendation

Recommended starting board outline for planning:

`72 mm x 40 mm`

Acceptable review range:

`68 mm x 38 mm` to `78 mm x 45 mm`

This is not a locked board size. It must be confirmed against:

- exact barrel jack drawing and plug clearance;
- exact USB-C drawing, shell tabs, and cable clearance;
- enclosure wall thickness and panel openings;
- mounting screw/standoff dimensions;
- pigtail bend radius and SMA bulkhead location;
- final component height limits.

## Exact Placement Strategy

### Coordinate Convention

For planning only, use:

- Origin at lower-left board corner.
- Board width along X.
- Board height along Y.
- Bottom edge is the user connector/panel edge.
- Top edge is the RF/pigtail clearance side.

### Proposed Zones

| Zone | Approximate area on 72 mm x 40 mm board | Contents |
| --- | --- | --- |
| Left-bottom connector zone | `x=0-20 mm`, `y=0-14 mm` | Barrel jack `J1`, plug clearance, polarity marking |
| Left-center power zone | `x=8-34 mm`, `y=12-30 mm` | `F1`, `Q1`, `D1`, `C1`, `U1`, `L1`, `C2-C5` |
| Right-bottom USB zone | `x=50-72 mm`, `y=0-16 mm` | USB-C `J2`, `U3`, `R4/R5`, shield option `R3` |
| Upper-right module/RF zone | `x=36-70 mm`, `y=16-40 mm` | ESP32 module `U2`, local decoupling `C6/C7`, U.FL/pigtail clearance |
| Lower-middle user/debug zone | `x=22-50 mm`, `y=0-12 mm` | LEDs, reset/boot access, test pad row |
| Corner mechanical zones | near four corners | `MH1-MH4`, standoff keepouts |

### Connector Placement

- Place `J1` on the bottom-left edge with barrel opening facing outward.
- Place `J2` on the bottom-right edge with USB-C opening facing outward.
- Leave enough gap between connector bodies for enclosure panel strength and labeling.
- Do not finalize orientation until exact connector drawings are checked.

Required flags:

- `CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `USB_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`

### ESP32 Module Placement

- Place `U2` in the upper-right quadrant.
- Orient antenna/U.FL side toward top edge or right/top corner, depending on exact module footprint orientation.
- Keep pigtail clearance above/right of module.
- Place `C6/C7` close to module 3.3 V/GND pins.
- Keep buck switch node and inductor away from the U.FL/pigtail corridor.

Required flags:

- `RF_LAYOUT_REVIEW_REQUIRED`
- `RF_ANTENNA_KEEP_OUT_REVIEW_REQUIRED`
- `RF_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`

### Buck Regulator Placement

- Place `U1` in the left-center zone, close to protected 5 V input and before the 3.3 V distribution path.
- Place `C2` close to VIN/GND.
- Place `C5` close to BST/SW.
- Place `L1` adjacent to SW but keep SW copper compact.
- Place `C3/C4` near the regulator output and 3.3 V distribution.
- Use wide copper for power and strong ground return.

Required flags:

- `POWER_LAYOUT_REVIEW_REQUIRED`
- `THERMAL_REVIEW_REQUIRED`
- `REGULATOR_STABILITY_REVIEW_REQUIRED`

### Input Protection Placement

- Place the chain directly behind `J1`:
  - `J1`
  - `F1`
  - `Q1`
  - `D1`
  - `C1`
  - `U1` input
- TVS ground return must be short and low impedance.
- PMOS source/gate/drain mapping must not be finalized until exact pin mapping is reviewed.

Required flags:

- `INPUT_PROTECTION_REVIEW_REQUIRED`
- `POLARITY_HUMAN_REVIEW_REQUIRED`

### USB-C / ESD / CC Placement

- Place `U3` immediately behind `J2`.
- Place `R4/R5` near `J2` CC pins.
- Place `R3` shield option near connector shield/shell region, pending USB shield decision.
- Route D+/D- from `J2` through `U3` to `R6/R7` and then `U2`.
- Place `R6/R7` near ESP32 module pins unless final Espressif/reference review changes that decision.
- Avoid USB D+/D- test-pad stubs; omit `TP8/TP9` unless accepted.

Required flags:

- `USB_LAYOUT_REVIEW_REQUIRED`
- `USB_DIFF_PAIR_REVIEW_REQUIRED`
- `USB_ESD_PLACEMENT_REVIEW_REQUIRED`

### Reset/Boot Placement

- Place `SW1/SW2` in the lower-middle or right-lower user-access zone.
- Keep `R1/R2/C8` near module pins.
- Route switch lines away from USB pair and buck switch node.

### LED Placement

- Place `D2/D3` along bottom-middle user-visible area.
- Put `R8/R9` directly behind LEDs.
- Make cathode/anode polarity markers visible.

Required flag:

- `POLARITY_HUMAN_REVIEW_REQUIRED`

### Test Pad Placement

- Place `TP1/TP2/TP3` for `5V_PROTECTED`, `3V3`, and `GND` in lower-middle bring-up row.
- Place `TP4/TP5/TP6/TP7` for `EN`, `BOOT`, `U0TXD`, and `U0RXD` nearby but separated from power pads.
- Add at least one extra GND pad near UART/debug pads if board area allows.
- Treat `TP8/TP9` as optional high-risk USB pads; preferred production plan is omit or make DNI only.

### Mounting Holes

- Use four corner mounting holes, approximate center offset `5 mm` from each edge.
- Keep 5.5 mm to 6.0 mm standoff keepout around each hole as a starting point.
- Adjust top-right hole if it conflicts with U.FL/pigtail/SMA clearance.
- Do not finalize NPTH/plated status until enclosure/standoff review.

## Routing Strategy

- Route input power left-to-center with wide, short traces.
- Keep buck hot loop compact and away from USB/RF.
- Route 3.3 V from regulator to ESP32 with wide copper and local decoupling.
- Route USB pair on one layer with minimal vias and matched geometry after fab/layer stackup is known.
- Keep USB and RF/pigtail areas away from switch-node copper.
- Keep button, LED, and test pad traces slow, short, and outside sensitive USB/RF paths.

## Ground Plane Strategy

- Prefer 4-layer board:
  - L1: components and critical signals
  - L2: solid GND
  - L3: power/support routing
  - L4: secondary signals and local copper
- Maintain continuous ground under USB D+/D- and ESP32 logic routes.
- Stitch regulator ground, USB connector/ESD region, and module ground heavily, subject to final shield and RF keepout rules.
- Do not place copper in any module/pigtail/mechanical keepout that source evidence forbids.

## Open Risks

- Board size is not user-confirmed.
- No `.kicad_pcb` file exists.
- PCB update from schematic is blocked.
- No footprint is verified to an exact package drawing.
- Barrel jack exact MPN/drawing is not selected.
- USB-C exact suffix/drawing/orientation is not verified.
- ESP32 module footprint and U.FL/pigtail mechanical clearance require review.
- PMOS pin mapping remains high-risk.
- USB VBUS and shield policy remain unresolved.
- Mounting hole/standoff/enclosure details remain unresolved.

## Placement Decision

Plan B is selected for future use after gates pass.

Placement may begin now: `NO`

Required before placement:

1. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` exact `PASS`.
2. PCB update from schematic completed with backup.
3. `.kicad_pcb` exists and imports all footprints.
4. Board size and mechanical constraints confirmed by LJ.
5. Exact connector, polarity, PMOS, USB, RF, mounting, and package review items resolved or explicitly accepted for provisional layout with `HUMAN_REVIEW_REQUIRED`.
