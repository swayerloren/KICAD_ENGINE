# Net Topology Map

Source: parsed PCB pad-net assignments from `ESP32_CSI_WIFI_NODE.kicad_pcb`.

Documented nets: `52`

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

## Detailed Connected Pads

### `/BUCK_BST`

Purpose: Bootstrap node for U1, local to U1/C6/SW.

- `C6` pad `2` (100nF_CBST)
- `U1` pad `6` (AP63203_NEEDS_REVIEW)

### `/BUCK_SW`

Purpose: Switching node between U1 SW pin and L1.

- `C6` pad `1` (100nF_CBST)
- `L1` pad `1` (3.9uH_REV)
- `U1` pad `5` (AP63203_NEEDS_REVIEW)

### `+3V3`

Purpose: Buck-regulated 3.3 V rail feeding ESP32 and low-voltage peripherals.

- `C3` pad `2` (10uF_MOD)
- `C4` pad `2` (100nF_MOD)
- `C7` pad `2` (22uF_OUT)
- `C8` pad `2` (22uF_OUT)
- `L1` pad `2` (3.9uH_REV)
- `R1` pad `2` (10k_EN)
- `R2` pad `2` (10k_BOOT)
- `R3` pad `2` (2.2k)
- `TP3` pad `1` (TP_3V3)
- `U1` pad `1` (AP63203_NEEDS_REVIEW)
- `U2` pad `2` (ESP32-S3-WROOM-1U)

### `/+5V_FUSED`

Purpose: Input after PTC fuse and before PMOS reverse-polarity stage.

- `F1` pad `2` (PTC_1206)
- `Q1` pad `3` (AO3401A_REV)

### `/+5V_IN`

Purpose: Raw external 5 V input from barrel jack.

- `F1` pad `1` (PTC_1206)
- `J1` pad `2` (JACK_5V)

### `/+5V_PROTECTED`

Purpose: Protected 5 V after Q1; feeds TVS/input caps/buck and test point.

- `C2` pad `2` (10uF_IN)
- `C5` pad `2` (47uF_16V)
- `D3` pad `2` (TVS_NEEDS_REVIEW)
- `Q1` pad `2` (AO3401A_REV)
- `TP1` pad `1` (TP_5V)
- `U1` pad `2` (AP63203_NEEDS_REVIEW)
- `U1` pad `3` (AP63203_NEEDS_REVIEW)

### `GND`

Purpose: Common return path, ESD return, regulator return, and module ground.

- `C1` pad `1` (1uF_EN)
- `C2` pad `1` (10uF_IN)
- `C3` pad `1` (10uF_MOD)
- `C4` pad `1` (100nF_MOD)
- `C5` pad `1` (47uF_16V)
- `C7` pad `1` (22uF_OUT)
- `C8` pad `1` (22uF_OUT)
- `D1` pad `1` (PWR_LED)
- `D2` pad `1` (STATUS_LED)
- `D3` pad `1` (TVS_NEEDS_REVIEW)
- `J1` pad `1` (JACK_5V)
- `J2` pad `A1` (USB-C_NEEDS_REVIEW)
- `J2` pad `A12` (USB-C_NEEDS_REVIEW)
- `J2` pad `B1` (USB-C_NEEDS_REVIEW)
- `J2` pad `B12` (USB-C_NEEDS_REVIEW)
- `Q1` pad `1` (AO3401A_REV)
- `R5` pad `1` (0R_DNI)
- `R6` pad `1` (5.1k_CC1)
- `R7` pad `1` (5.1k_CC2)
- `SW1` pad `2` (BOOT_GPIO0_REVIEW)
- `SW1` pad `2` (BOOT_GPIO0_REVIEW)
- `SW2` pad `2` (RESET_EN_REVIEW)
- `SW2` pad `2` (RESET_EN_REVIEW)
- `TP5` pad `1` (TP_GND)
- `U1` pad `4` (AP63203_NEEDS_REVIEW)
- `U2` pad `1` (ESP32-S3-WROOM-1U)
- `U2` pad `40` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U2` pad `41` (ESP32-S3-WROOM-1U)
- `U3` pad `3` (USB_ESD_REV)

### `/DM_C`

Purpose: USB D- at connector/ESD side.

- `J2` pad `A7` (USB-C_NEEDS_REVIEW)
- `J2` pad `B7` (USB-C_NEEDS_REVIEW)
- `R8` pad `1` (22R_D-)
- `U3` pad `2` (USB_ESD_REV)

### `/DM_E`

Purpose: USB D- at ESP32 side after series resistor.

- `R8` pad `2` (22R_D-)
- `TP9` pad `1` (TP_D-_REV)
- `U2` pad `13` (ESP32-S3-WROOM-1U)

### `/DP_C`

Purpose: USB D+ at connector/ESD side.

- `J2` pad `A6` (USB-C_NEEDS_REVIEW)
- `J2` pad `B6` (USB-C_NEEDS_REVIEW)
- `R9` pad `1` (22R_D+)
- `U3` pad `1` (USB_ESD_REV)

### `/DP_E`

Purpose: USB D+ at ESP32 side after series resistor.

- `R9` pad `2` (22R_D+)
- `TP8` pad `1` (TP_D+_REV)
- `U2` pad `14` (ESP32-S3-WROOM-1U)

### `/CC1`

Purpose: USB-C CC1 pull-down path.

- `J2` pad `A5` (USB-C_NEEDS_REVIEW)
- `R6` pad `2` (5.1k_CC1)

### `/CC2`

Purpose: USB-C CC2 pull-down path.

- `J2` pad `B5` (USB-C_NEEDS_REVIEW)
- `R7` pad `2` (5.1k_CC2)

### `/SHIELD`

Purpose: USB connector shield policy net.

- `J2` pad `S1` (USB-C_NEEDS_REVIEW)
- `J2` pad `S1` (USB-C_NEEDS_REVIEW)
- `J2` pad `S1` (USB-C_NEEDS_REVIEW)
- `J2` pad `S1` (USB-C_NEEDS_REVIEW)
- `R5` pad `2` (0R_DNI)

### `/BOOT0`

Purpose: ESP32 boot-mode net.

- `R2` pad `1` (10k_BOOT)
- `SW1` pad `1` (BOOT_GPIO0_REVIEW)
- `SW1` pad `1` (BOOT_GPIO0_REVIEW)
- `TP4` pad `1` (TP_BOOT)
- `U2` pad `27` (ESP32-S3-WROOM-1U)

### `/ESP_EN`

Purpose: ESP32 enable/reset net.

- `C1` pad `2` (1uF_EN)
- `R1` pad `1` (10k_EN)
- `SW2` pad `1` (RESET_EN_REVIEW)
- `SW2` pad `1` (RESET_EN_REVIEW)
- `TP2` pad `1` (TP_EN)
- `U2` pad `3` (ESP32-S3-WROOM-1U)

### `/PLED`

Purpose: Power LED resistor/LED net.

- `D1` pad `2` (PWR_LED)
- `R3` pad `1` (2.2k)

### `/SLED`

Purpose: Status LED resistor/LED net.

- `D2` pad `2` (STATUS_LED)
- `R4` pad `1` (2.2k)

### `/STATUS_LED`

Purpose: ESP32 status LED drive net.

- `R4` pad `2` (2.2k)
- `U2` pad `38` (ESP32-S3-WROOM-1U)

### `/U0RXD`

Purpose: ESP32 UART receive/debug test net.

- `TP7` pad `1` (TP_U0RXD)
- `U2` pad `36` (ESP32-S3-WROOM-1U)

### `/U0TXD`

Purpose: ESP32 UART transmit/debug test net.

- `TP6` pad `1` (TP_U0TXD)
- `U2` pad `37` (ESP32-S3-WROOM-1U)

### `unconnected-(J2-VBUS-PadA4)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `J2` pad `A4` (USB-C_NEEDS_REVIEW)
- `J2` pad `A9` (USB-C_NEEDS_REVIEW)
- `J2` pad `B4` (USB-C_NEEDS_REVIEW)
- `J2` pad `B9` (USB-C_NEEDS_REVIEW)

### `unconnected-(U2-IO1-Pad39)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `39` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO10-Pad18)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `18` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO11-Pad19)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `19` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO12-Pad20)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `20` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO13-Pad21)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `21` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO14-Pad22)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `22` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO15-Pad8)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `8` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO16-Pad9)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `9` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO17-Pad10)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `10` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO18-Pad11)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `11` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO21-Pad23)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `23` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO3-Pad15)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `15` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO35-Pad28)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `28` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO36-Pad29)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `29` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO37-Pad30)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `30` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO38-Pad31)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `31` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO39-Pad32)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `32` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO4-Pad4)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `4` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO40-Pad33)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `33` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO41-Pad34)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `34` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO42-Pad35)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `35` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO45-Pad26)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `26` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO46-Pad16)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `16` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO47-Pad24)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `24` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO48-Pad25)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `25` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO5-Pad5)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `5` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO6-Pad6)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `6` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO7-Pad7)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `7` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO8-Pad12)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `12` (ESP32-S3-WROOM-1U)

### `unconnected-(U2-IO9-Pad17)`

Purpose: Explicit no-connect imported from schematic/PCB for unused module or connector pad.

- `U2` pad `17` (ESP32-S3-WROOM-1U)
