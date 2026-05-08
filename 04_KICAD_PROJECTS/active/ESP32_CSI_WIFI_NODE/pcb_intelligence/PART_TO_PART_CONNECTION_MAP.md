# Part-To-Part Connection Map

| Net | Criticality | Pads | Priority | Width mm | Via policy | Risk |
|---|---|---:|---:|---:|---|---|
| `/BUCK_BST` | `CRITICAL_POWER` | 2 | 1 | `0.2` | Avoid vias; keep local to U1/L1/C6. | Switching noise and loop-area risk; keep away from USB/RF. |
| `/BUCK_SW` | `CRITICAL_POWER` | 3 | 1 | `0.5` | Avoid vias; keep local to U1/L1/C6. | Switching noise and loop-area risk; keep away from USB/RF. |
| `+3V3` | `CRITICAL_POWER` | 11 | 2 | `0.5` | Vias acceptable only when current path and return path remain low impedance. | Brownout/voltage-drop risk if distribution or return is poor. |
| `/+5V_FUSED` | `CRITICAL_POWER` | 2 | 2 | `0.75` | Vias acceptable only when current path and return path remain low impedance. | Power input/protection path and barrel jack mechanical decision affect route. |
| `/+5V_IN` | `CRITICAL_POWER` | 2 | 2 | `0.75` | Vias acceptable only when current path and return path remain low impedance. | Power input/protection path and barrel jack mechanical decision affect route. |
| `/+5V_PROTECTED` | `CRITICAL_POWER` | 7 | 2 | `0.75` | Vias acceptable only when current path and return path remain low impedance. | Power input/protection path and barrel jack mechanical decision affect route. |
| `GND` | `GROUND` | 41 | 2 | `None` | Use ground vias for low-impedance returns/stitching; avoid ESP32 RF keepout. | Low to medium; route after critical nets. |
| `/DM_C` | `CRITICAL_USB` | 4 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DM_E` | `CRITICAL_USB` | 3 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DP_C` | `CRITICAL_USB` | 4 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DP_E` | `CRITICAL_USB` | 3 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/CC1` | `CRITICAL_USB` | 2 | 4 | `0.25` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/CC2` | `CRITICAL_USB` | 2 | 4 | `0.25` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/SHIELD` | `CRITICAL_USB` | 5 | 4 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | USB shield policy remains human-review required. |
| `/BOOT0` | `CONTROL_SIGNAL` | 5 | 5 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/ESP_EN` | `CONTROL_SIGNAL` | 6 | 5 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/PLED` | `CONTROL_SIGNAL` | 2 | 5 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/SLED` | `CONTROL_SIGNAL` | 2 | 5 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/STATUS_LED` | `CONTROL_SIGNAL` | 2 | 5 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/U0RXD` | `DEBUG_TEST` | 2 | 6 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/U0TXD` | `DEBUG_TEST` | 2 | 6 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `unconnected-(J2-VBUS-PadA4)` | `LOW_SPEED` | 4 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO1-Pad39)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO10-Pad18)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO11-Pad19)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO12-Pad20)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO13-Pad21)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO14-Pad22)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO15-Pad8)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO16-Pad9)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO17-Pad10)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO18-Pad11)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO21-Pad23)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO3-Pad15)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO35-Pad28)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO36-Pad29)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO37-Pad30)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO38-Pad31)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO39-Pad32)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO4-Pad4)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO40-Pad33)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO41-Pad34)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO42-Pad35)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO45-Pad26)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO46-Pad16)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO47-Pad24)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO48-Pad25)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO5-Pad5)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO6-Pad6)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO7-Pad7)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO8-Pad12)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |
| `unconnected-(U2-IO9-Pad17)` | `LOW_SPEED` | 1 | 9 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | No route expected; verify no unintended connection. |

## Net-Based Part Groups

### `/BUCK_BST`

Connected references: `C6`, `U1`

Placement dependency: U1/C6/L1 must be adjacent with compact loop.

### `/BUCK_SW`

Connected references: `C6`, `L1`, `U1`

Placement dependency: U1/C6/L1 must be adjacent with compact loop.

### `+3V3`

Connected references: `C3`, `C4`, `C7`, `C8`, `L1`, `R1`, `R2`, `R3`, `TP3`, `U1`, `U2`

Placement dependency: U1/L1/C7/C8 near regulator output; C3/C4 close to U2 3V3/GND pins.

### `/+5V_FUSED`

Connected references: `F1`, `Q1`

Placement dependency: J1/F1/Q1/D3/C2/C5/U1 must remain close in source-to-load order.

### `/+5V_IN`

Connected references: `F1`, `J1`

Placement dependency: J1/F1/Q1/D3/C2/C5/U1 must remain close in source-to-load order.

### `/+5V_PROTECTED`

Connected references: `C2`, `C5`, `D3`, `Q1`, `TP1`, `U1`, `U1`

Placement dependency: J1/F1/Q1/D3/C2/C5/U1 must remain close in source-to-load order.

### `GND`

Connected references: `C1`, `C2`, `C3`, `C4`, `C5`, `C7`, `C8`, `D1`, `D2`, `D3`, `J1`, `J2`, `J2`, `J2`, `J2`, `Q1`, `R5`, `R6`, `R7`, `SW1`, `SW1`, `SW2`, `SW2`, `TP5`, `U1`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U2`, `U3`

Placement dependency: Continuous return plane required; avoid splitting USB/power returns; no copper in RF keepout.

### `/DM_C`

Connected references: `J2`, `J2`, `R8`, `U3`

Placement dependency: J2/U3/R8/R9/U2 must form short direct USB path; test pads are stub-risk.

### `/DM_E`

Connected references: `R8`, `TP9`, `U2`

Placement dependency: J2/U3/R8/R9/U2 must form short direct USB path; test pads are stub-risk.

### `/DP_C`

Connected references: `J2`, `J2`, `R9`, `U3`

Placement dependency: J2/U3/R8/R9/U2 must form short direct USB path; test pads are stub-risk.

### `/DP_E`

Connected references: `R9`, `TP8`, `U2`

Placement dependency: J2/U3/R8/R9/U2 must form short direct USB path; test pads are stub-risk.

### `/CC1`

Connected references: `J2`, `R6`

Placement dependency: R6/R7 close to J2 CC pins.

### `/CC2`

Connected references: `J2`, `R7`

Placement dependency: R6/R7 close to J2 CC pins.

### `/SHIELD`

Connected references: `J2`, `J2`, `J2`, `J2`, `R5`

Placement dependency: No special placement beyond clean routing and service access.

### `/BOOT0`

Connected references: `R2`, `SW1`, `SW1`, `TP4`, `U2`

Placement dependency: SW1/SW2 and R1/R2/C1/C3 close enough for clean routing while edge-accessible.

### `/ESP_EN`

Connected references: `C1`, `R1`, `SW2`, `SW2`, `TP2`, `U2`

Placement dependency: SW1/SW2 and R1/R2/C1/C3 close enough for clean routing while edge-accessible.

### `/PLED`

Connected references: `D1`, `R3`

Placement dependency: LEDs at visible edge; resistors near LEDs.

### `/SLED`

Connected references: `D2`, `R4`

Placement dependency: LEDs at visible edge; resistors near LEDs.

### `/STATUS_LED`

Connected references: `R4`, `U2`

Placement dependency: LEDs at visible edge; resistors near LEDs.

### `/U0RXD`

Connected references: `TP7`, `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `/U0TXD`

Connected references: `TP6`, `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(J2-VBUS-PadA4)`

Connected references: `J2`, `J2`, `J2`, `J2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO1-Pad39)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO10-Pad18)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO11-Pad19)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO12-Pad20)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO13-Pad21)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO14-Pad22)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO15-Pad8)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO16-Pad9)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO17-Pad10)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO18-Pad11)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO21-Pad23)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO3-Pad15)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO35-Pad28)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO36-Pad29)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO37-Pad30)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO38-Pad31)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO39-Pad32)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO4-Pad4)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO40-Pad33)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO41-Pad34)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO42-Pad35)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO45-Pad26)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO46-Pad16)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO47-Pad24)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO48-Pad25)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO5-Pad5)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO6-Pad6)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO7-Pad7)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO8-Pad12)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.

### `unconnected-(U2-IO9-Pad17)`

Connected references: `U2`

Placement dependency: No special placement beyond clean routing and service access.
