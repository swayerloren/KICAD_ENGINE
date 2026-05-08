# Mounting And Connector Mechanical Plan

## Connector Components

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `J1` | `JACK_5V` | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` | `POWER_INPUT_BUCK` | `/+5V_IN`, `GND` | `F1`, `Q1` | `TRUE` |
| `J2` | `USB-C_NEEDS_REVIEW` | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `USB` | `/CC1`, `/CC2`, `/DM_C`, `/DP_C`, `/SHIELD`, `GND`, `unconnected-(J2-VBUS-PadA4)` | `U3`, `R6`, `R7` | `TRUE` |

## Mounting Holes

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `MH1` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `MH2` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `MH3` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `MH4` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |

## Rules

- `J2` USB-C should be bottom-edge, mouth downward/off-board, edge-line aligned.
- `J1` barrel jack is not pill-board-friendly and requires LJ mechanical decision.
- Connector plug/cable envelopes must not block test pads, buttons, LEDs, or mounting holes.
- Four M2.5 holes are not proven practical on the 38 mm board.
- Top holes must not violate ESP32 RF keepout.
- Current status: `MOUNTING_HOLE_STRATEGY_REQUIRES_LJ_DECISION`.
