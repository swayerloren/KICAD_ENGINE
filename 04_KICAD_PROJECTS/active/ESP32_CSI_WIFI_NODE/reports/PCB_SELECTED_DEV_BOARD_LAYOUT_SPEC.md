# Selected Dev-Board Layout Specification

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Status: `SELECTED_FOR_NEXT_PLACEMENT_RESET`

PCB edited: `NO`

Selected option: `Option A - 38 mm x 80 mm pill board`

## Board

- Board dimensions: `38 mm wide x 80 mm tall`
- Origin: lower-left
- Board outline: `(0,0)` to `(38,80)`
- Layer count: `2`
- Board thickness assumption: `1.6 mm`
- Board style: ESP32/STM32 pill-style development board

## Orientation Strategy

| Item | Required orientation |
|---|---|
| `U2` ESP32-S3 module | Top of board, centered horizontally. Rotate so antenna/U.FL/keepout points toward top edge. |
| `J2` USB-C | Bottom edge. Mouth faces off-board downward. PCB-edge line aligns with y=`0`. |
| `J1` barrel jack | Lower-left side edge if retained. Opening faces off-board left. Do not enlarge board solely for J1 without LJ approval. |
| `U1/L1` buck cluster | Lower-left to mid-left. Keep switch loop compact and away from USB/RF. |
| `SW1/SW2` | Side or lower edge, finger-accessible. |
| `D1/D2` | Visible lower/front or side edge. |
| `TP1-TP9` | One side-edge service row, not center-board clutter. |

## Exact First-Pass Coordinate Targets

These are placement targets for the next PCB reset pass. They must be adjusted if actual footprint courtyard checks show collisions.

| Reference(s) | Target coordinate / region | Rotation intent |
|---|---|---|
| Board outline | `(0,0)`, `(38,0)`, `(38,80)`, `(0,80)` | n/a |
| `U2` | Center near `(19,64)` | Antenna/U.FL end toward y=`80` |
| U2 RF keepout | From U2 RF end to top board edge y=`80`; full keepout width per footprint/module guide | No copper/components/traces |
| `J2` | Bottom center near x=`19`; footprint edge aligned to y=`0` | Mouth downward/off-board |
| `U3` | Around `(19,10)` | Match USB D+/D- flow |
| `R8/R9` | Around `(16,14)` and `(22,14)` | Between U3 and U2 |
| `R6/R7` | Around `(12,8)` and `(26,8)` | Close to J2 CC pins |
| `J1` | Lower-left side, center around `(2-3,16-18)` | Opening left/off-board |
| `F1` | Around `(8,18)` | In line after J1 |
| `Q1` | Around `(13,20)` | After F1, confirm PMOS orientation |
| `D3` | Around `(10,27)` | Near protected input |
| `C2/C5` | Around `(15-19,27)` | Tight to U1 input/protected input |
| `U1` | Around `(20,32)` | Orient for shortest IN/SW/GND loop |
| `C6` | Around `(20,36)` | Tight to U1 BST/SW |
| `L1` | Around `(26,32)` | Immediately at U1 SW side |
| `C7/C8` | Around `(26-31,38)` | Tight output caps near L1/+3V3 |
| `C3/C4` | Near U2 power pins, below module body but outside RF keepout | Tight ESP32 decoupling |
| `SW1/SW2` | Side-accessible around y=`20-30`; one left, one right if ergonomic | Button actuator to edge |
| `D1/D2` | Lower/right visible edge around y=`10-16` | Polarity marks visible |
| `TP1-TP9` | Right-side vertical row around x=`34.5`, y=`18-50` | Labels readable; USB pads optional/stub-risk flagged |

## Mounting-Hole Strategy

Primary mounting strategy:

- Try four M2.5 NPTH holes, 2.7 mm drill.
- Nominal coordinates:
  - `MH1`: `(3.5,3.5)`
  - `MH2`: `(34.5,3.5)`
  - `MH3`: `(3.5,76.5)`
  - `MH4`: `(34.5,76.5)`
- Keep at least 3 mm copper/component courtyard clearance where physically possible.
- Top mounting holes must not violate U2 antenna/U.FL keepout or module courtyard.

Fallback mounting strategy:

- If four M2.5 holes collide with U2 RF keepout or connector courtyards, use two M2.5 NPTH holes instead:
  - Preferred diagonal: `(3.5,3.5)` and `(34.5,76.5)`
  - Alternate centerline: `(19,4)` and `(19,76)`
- Do not reduce board usability or RF clearance just to force four holes.

## Ground And Zone Strategy

For later zone phase only:

- Bottom layer planned as solid GND plane.
- Top local GND pours around USB ESD, regulator, and ESP32 decoupling only where useful.
- No copper pour under U2 antenna/U.FL keepout.
- Stitching vias planned near USB shield/ESD and perimeter, outside RF keepout.
- Regulator thermal copper planned near U1/L1, not under antenna keepout.

## Routing Strategy

Routing is not allowed yet. For the future routing phase:

- Route USB D+/D- vertically from J2 to U3/R8/R9, then to U2 with minimum stubs.
- Keep CC resistors close to J2.
- Keep buck input and switching loop compact around U1/L1/C2/C5/C6/C7/C8.
- Keep BUCK_SW short and away from USB and RF keepout.
- Route power vertically upward after regulation to U2 and local decoupling.
- Keep test pads off critical USB lines unless LJ accepts the stub risk.

## Required Human Decisions Before Placement Reset

| Decision | Required action |
|---|---|
| Barrel jack retention | LJ must accept side-mounted J1 on a 38 mm board, choose Option C, or approve replacing/removing J1. |
| Mounting-hole count | LJ must accept four-hole attempt with fallback to two holes if courtyard/RF keepout conflicts occur. |
| U2 footprint/package | Confirm `ESP32-S3-WROOM-1U` intent against current `RF_Module:ESP32-S3-WROOM-1` footprint/keepout behavior. |
| U2 drill rule issue | Decide whether 0.20 mm module pad holes are acceptable for the intended fab or require footprint/rule change. |
| USB test pads | Decide whether USB D+/D- test pads stay, move, or become DNP/no-fit due stub risk. |

## Placement Reset Authorization Status

PCB reset/replacement placement may begin: `YES_AFTER_LJ_APPROVES_THIS_SELECTED_SPEC`

Routing remains: `BLOCKED`
