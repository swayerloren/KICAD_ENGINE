# ESP32_CSI_WIFI_NODE PCB Layout Plan Options

Generated: `2026-05-06 22:11:31 -04:00`

Status: `PLANNING_ONLY_NO_PCB_EDIT`

## Scope And Current Gate State

This report proposes three PCB placement/layout plans only. It does not create a PCB, place parts, route traces, create zones, or generate manufacturing outputs.

Current blocking evidence:

- `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`: `BLOCKED_GATE_FAIL`
- `reports/PCB_SYNC_STATUS.md`: `NOT_SYNCED_GATE_FAIL`
- `reports/BOARD_SIZE_NEEDS_USER_REVIEW.md`: board size and mechanical constraints are not locked
- `PRE_SCHEMATIC_BOM_LOCK.md`: `0` footprints are verified to exact package drawings
- `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`: connector, polarity, RF, USB, power, and mechanical items remain open

Placement may begin now: `NO`

## Shared Planning Assumptions

- Board is a compact rectangle for a 3D printed enclosure.
- Nominal layer assumption for planning: 4-layer preferred for ground continuity, USB routing margin, and RF/noisy-power separation; 2-layer remains possible but higher risk.
- Exact board size is not defined. All dimensions below are estimates for LJ review.
- Barrel jack and USB-C both need edge access and enclosure wall clearance.
- ESP32-S3-WROOM-1U uses external antenna connector; preserve pigtail bend and SMA bulkhead clearance.
- Mounting hole planning default is four M2.5 NPTH holes with 2.7 mm drill and 5.5 mm to 6.0 mm keepout, pending confirmation.
- USB D+/D- test pads are high-risk because they can create stubs; include only if placed as very short optional bring-up pads or omit in production layout.
- All connector orientation, polarity, PMOS pin mapping, USB shield/VBUS policy, and RF pigtail/SMA details remain `HUMAN_REVIEW_REQUIRED`.

## Plan A - Compact Rectangular Board

### 1. Board Size Estimate

- Recommended estimate: `58 mm x 42 mm`.
- Alternate compact range: `55 mm x 40 mm` to `62 mm x 45 mm`.
- Use this only if enclosure size pressure is high and hand-probing access can be slightly tighter.

### 2. Connector Placement

- Put the barrel jack on the left short edge, centered vertically or slightly lower, with plug insertion clearance outside the board.
- Put USB-C on the right short edge, centered vertically or slightly upper, so both cables exit opposite sides.
- Keep connector keepouts clear of mounting holes and enclosure walls.

### 3. ESP32 Module Placement/Orientation

- Place `U2` in the upper-right or upper-center area, rotated so the module antenna/U.FL side points toward the top board edge.
- Keep the U.FL/pigtail area at the top edge with no tall parts directly above or crowding the pigtail bend.
- Keep the module away from the buck switch node and input protection path.

### 4. Buck Regulator Placement

- Place `U1`, `L1`, `C2`, `C3`, `C4`, and `C5` near the left-middle area after input protection, between the barrel input path and the ESP32 3.3 V entry.
- Keep the VIN capacitor, BST capacitor, SW node, inductor, and output capacitors tightly grouped.
- Keep SW copper small and isolated from USB/RF.

### 5. Input Protection Placement

- Place `J1 -> F1 -> Q1 -> D1 -> C1` as a short chain from the left edge inward.
- Place TVS return close to the input ground entry.
- Keep high-current 5 V traces wide and direct.

### 6. USB-C / ESD / CC Resistor Placement

- Place `J2` on the right edge.
- Put `U3` immediately behind J2, close to connector pins.
- Place `R4/R5` CC resistors adjacent to J2.
- Place `R6/R7` series resistors closer to the ESP32 module side, unless final SI review requires connector-side placement.
- Avoid vias on D+/D- if possible.

### 7. Reset/Boot Placement

- Put `SW1/SW2` on the lower-right edge or lower front edge, reachable through enclosure buttons.
- Keep `R1/R2/C8` near the ESP32 EN/GPIO0 pins while allowing switch access traces to be short and quiet.

### 8. LED Placement

- Place `D2/D3` and `R8/R9` along the lower edge or near a front-visible enclosure window.
- Keep LED polarity markings readable and not under connector overhang.

### 9. Test Pad Placement

- Put `TP1/TP2/TP3` power pads in a lower-left bring-up cluster.
- Put `TP4/TP5/TP6/TP7` near the lower-right/ESP32 side.
- Omit `TP8/TP9` USB pads unless LJ accepts the stub risk; if retained, use tiny pads in-line or extremely close to the USB path.

### 10. Mounting Hole Placement

- Four holes near corners, with estimated centers 4 mm to 5 mm from board edges.
- Keep hole keepouts clear of the barrel jack body, USB shell tabs, pigtail path, and LED/test pad access.

### 11. Routing Strategy

- Route power left-to-center, USB right-to-ESP32, and RF/pigtail top-edge only.
- Keep noisy buck loop left/center and route 3.3 V to ESP32 as a short, wide path.
- Route USB D+/D- as a matched pair from J2 through U3 and series resistors to GPIO19/GPIO20.

### 12. Ground Plane Strategy

- Prefer solid internal GND plane on layer 2 if 4-layer.
- Add local ground stitching around USB connector shield/ESD area pending shield policy.
- Stitch around module ground pads and near regulator return, but do not violate antenna/pigtail keepouts.

### 13. Pros

- Smallest practical board concept.
- Clear left-power/right-USB separation.
- Short 3.3 V path to ESP32.
- Good for a compact enclosure.

### 14. Cons

- Opposite-side cables may be awkward in a wall/enclosure.
- Less room for pigtail bend radius and SMA strain relief.
- Test pad access is tighter.
- Buck regulator and ESP32 may be closer than ideal.

### 15. Risks

- `RF_ANTENNA_KEEP_OUT_REVIEW_REQUIRED`
- `USB_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `POWER_LAYOUT_REVIEW_REQUIRED`
- Thermal and pigtail mechanical margins may be tight.
- Connector exact footprints can change board size.

### 16. Recommended Use

Use Plan A only if enclosure volume is the top priority and LJ accepts tighter debug and antenna mechanical margins.

## Plan B - Connector-Edge Optimized Board

### 1. Board Size Estimate

- Recommended estimate: `72 mm x 40 mm`.
- Alternate range: `68 mm x 38 mm` to `78 mm x 45 mm`.
- Wider horizontal shape gives both user connectors one enclosure-facing edge.

### 2. Connector Placement

- Put barrel jack `J1` on the left side of the bottom long edge.
- Put USB-C `J2` on the right side of the same bottom long edge.
- Align both connector mouths to the enclosure wall for a clean panel opening strategy.
- Leave a central bottom gap for labels or optional status LEDs.

### 3. ESP32 Module Placement/Orientation

- Place `U2` in the upper-right quadrant, with U.FL/pigtail side facing the top or right edge.
- Keep the top-right corner as antenna/pigtail clearance.
- Keep module ground and decoupling close, with no power-switching copper near the antenna/pigtail corridor.

### 4. Buck Regulator Placement

- Place the buck regulator block in the left-center area, above and inward from the barrel jack/protection chain.
- Keep it closer to input protection than to USB/RF.
- Reserve copper around the regulator for thermal spreading and via stitching if 4-layer.

### 5. Input Protection Placement

- Place `F1`, `Q1`, `D1`, and `C1` directly behind the barrel jack, progressing left-bottom edge to left-center.
- Use a compact but inspection-friendly power path: jack, fuse, PMOS, TVS/bulk, buck.

### 6. USB-C / ESD / CC Resistor Placement

- Place `U3` immediately behind USB-C on the right-bottom edge.
- Place `R4/R5` beside J2 and tied to the local connector ground return.
- Route D+/D- upward then inward to the ESP32 with minimal layer changes.
- Place `R6/R7` near the ESP32 pins or just before the module, based on final review.

### 7. Reset/Boot Placement

- Put reset and boot buttons along the right edge or bottom edge between USB-C and the ESP32 area.
- Keep them accessible from the enclosure side but away from cable strain zones.

### 8. LED Placement

- Put LEDs near the bottom-center panel area between barrel and USB-C, visible to the user.
- Place resistors immediately behind LEDs to keep polarity and assembly readable.

### 9. Test Pad Placement

- Use a top-center or lower-center test pad row with `GND`, `5V_PROTECTED`, `3V3`, `EN`, `BOOT`, `U0TXD`, and `U0RXD`.
- Keep pads accessible from the top side after enclosure opening.
- Treat USB D+/D- pads as optional and likely DNI/remove unless placed with no stub penalty.

### 10. Mounting Hole Placement

- Four corner holes with approximate centers 5 mm from edges.
- Use the elongated board to keep holes clear of connector bodies and pigtail path.
- Reserve keepouts for standoffs, USB shell tabs, and barrel jack mechanical pins.

### 11. Routing Strategy

- Partition board into left power, right USB/ESP32, and top RF/mechanical zones.
- Route 5 V from left-bottom to regulator; route 3.3 V from regulator to ESP32 with wide copper.
- Route USB D+/D- as a short right-side pair from J2 to ESP32.
- Keep debug/test traces slow and away from RF/pigtail clearance.

### 12. Ground Plane Strategy

- Prefer uninterrupted GND under USB and ESP32 logic return paths.
- Stitch around connector shield region per final shield policy.
- Add dense regulator input/output ground vias if 4-layer.
- Keep any RF/pigtail keepout clear according to Espressif/module guidance.

### 13. Pros

- Best enclosure-panel strategy for barrel and USB on one edge.
- Good separation between power input and USB/RF.
- Good test pad and LED usability.
- More room for regulator thermal copper and connector keepouts.

### 14. Cons

- Larger than Plan A.
- Same-edge cables need enclosure panel spacing and strain-relief review.
- Long horizontal shape may not suit all enclosures.

### 15. Risks

- Barrel and USB exact connector overhangs may force board width changes.
- USB shield/VBUS policy remains unresolved.
- Pigtail/SMA enclosure location still needs human mechanical review.
- Connector orientation must be verified from exact drawings.

### 16. Recommended Use

Use Plan B when the enclosure should have a single connector face and the board can be moderately wider. This is the strongest general-purpose layout plan.

## Plan C - RF/Antenna-Clearance Optimized Board

### 1. Board Size Estimate

- Recommended estimate: `70 mm x 50 mm`.
- Alternate range: `68 mm x 48 mm` to `78 mm x 55 mm`.
- Extra height is reserved for antenna pigtail bend, strain relief, and SMA bulkhead clearance.

### 2. Connector Placement

- Put barrel jack on the lower-left edge.
- Put USB-C on the lower-right edge or right edge.
- Keep all cable exits away from the top RF/pigtail area.

### 3. ESP32 Module Placement/Orientation

- Place `U2` high on the board, preferably upper-center or upper-right.
- Orient the WROOM-1U antenna connector toward the top edge.
- Reserve a top keepout/mechanical corridor for U.FL latch access, pigtail bend radius, and route to SMA bulkhead.
- Do not place the buck inductor, USB-C connector shell, mounting hardware, or tall capacitors in the pigtail corridor.

### 4. Buck Regulator Placement

- Place buck regulator in the lower-left or left-center area, far from the top RF/pigtail corridor.
- Keep power switch node copper constrained and away from the ESP32 antenna connector side.
- Use the larger board area for regulator thermal copper and ground return stitching.

### 5. Input Protection Placement

- Place input protection immediately behind the lower-left barrel jack.
- Keep the 5 V protection and buck entry compact in the lower-left zone.
- Keep high-current path away from RF/pigtail and USB D+/D-.

### 6. USB-C / ESD / CC Resistor Placement

- Place USB-C on lower-right or mid-right edge.
- Place ESD close to connector and route D+/D- inward/upward to ESP32 with controlled spacing.
- Keep the USB pair away from the top antenna pigtail path and buck switch node.

### 7. Reset/Boot Placement

- Put reset/boot on the right side below the ESP32, accessible but outside the pigtail corridor.
- Keep EN and BOOT support passives close to module pins.

### 8. LED Placement

- Put LEDs along the lower edge or right-lower user-facing area, away from RF and connector stress.
- Ensure enclosure visibility without requiring traces through the RF clearance zone.

### 9. Test Pad Placement

- Place a bring-up pad row along the lower-middle edge.
- Provide at least one ground pad near power pads and one near UART pads.
- Do not place test pads in the RF/pigtail corridor.

### 10. Mounting Hole Placement

- Four corner holes, but move top holes inward or downward if needed to preserve pigtail/SMA clearance.
- Treat the top-right mounting area as shared with antenna mechanics and require enclosure review.

### 11. Routing Strategy

- Keep RF/mechanical clearance as a top no-go corridor.
- Route power in the lower-left zone and USB in the lower-right/right zone.
- Route 3.3 V to ESP32 from below with decoupling close to module supply pins.
- Avoid traces crossing under the pigtail path unless confirmed mechanically safe.

### 12. Ground Plane Strategy

- Use solid ground under ESP32 logic and USB routes.
- Use ground stitching around module ground and board perimeter, excluding any required RF/mechanical keepout.
- Keep the top pigtail corridor mechanically clear; do not assume a 50 ohm feedline geometry unless a source-backed RF path is actually routed on-board.

### 13. Pros

- Best antenna connector access and pigtail strain relief.
- Best separation between switcher noise and RF mechanics.
- More forgiving for enclosure/SMA iteration.
- Better debug/test access than Plan A.

### 14. Cons

- Largest board.
- More enclosure volume and material.
- Longer 3.3 V and USB routes than a tightly optimized compact design.
- May be overbuilt if the pigtail/SMA path is simple.

### 15. Risks

- RF/mechanical clearance is still not source-locked.
- Exact pigtail bend radius and SMA bulkhead position are unknown.
- Larger loop areas can appear if power and USB routing are not disciplined.
- Connector and mounting-hole positions may change after enclosure design.

### 16. Recommended Use

Use Plan C if antenna reliability, pigtail access, and enclosure integration are more important than minimum size.

## Comparative Decision Matrix

| Criterion | Plan A Compact | Plan B Connector-Edge | Plan C RF Clearance |
| --- | --- | --- | --- |
| Size efficiency | `BEST` | `GOOD` | `WEAKEST` |
| Connector panel usability | `MEDIUM` | `BEST` | `GOOD` |
| RF/pigtail clearance | `MEDIUM_LOW` | `GOOD` | `BEST` |
| Buck thermal/layout room | `MEDIUM` | `GOOD` | `BEST` |
| USB route simplicity | `GOOD` | `BEST` | `GOOD` |
| Test pad access | `MEDIUM_LOW` | `BEST` | `GOOD` |
| Enclosure flexibility | `MEDIUM` | `BEST` | `GOOD_FOR_RF` |
| Risk level | `HIGHER` | `LOWEST_OVERALL` | `MEDIUM` |

## Recommended Plan

Recommended: `Plan B - Connector-Edge Optimized Board`

Reason: Plan B gives the cleanest first-revision balance. It aligns barrel jack and USB-C on one enclosure-facing edge, keeps the input power chain on the left, keeps USB on the right near the ESP32, leaves practical room for mounting holes/test pads/LEDs, and still preserves a top-right RF/pigtail clearance area. It is less cramped than Plan A and less large than Plan C.

Placement may begin now: `NO`

Reason: the PCB has not been synced from the schematic, no `.kicad_pcb` exists, board size is not user-confirmed, and the schematic-to-PCB gate is still failed.
