# ESP32 RF Keepout Plan

## ESP32 Cluster

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `C3` | `10uF_MOD` | `Capacitor_SMD:C_0805_2012Metric` | `ESP32_MODULE_RF` | `+3V3`, `GND` | `U2` | `FALSE` |
| `C4` | `100nF_MOD` | `Capacitor_SMD:C_0603_1608Metric` | `ESP32_MODULE_RF` | `+3V3`, `GND` | `U2` | `FALSE` |
| `U2` | `ESP32-S3-WROOM-1U` | `RF_Module:ESP32-S3-WROOM-1` | `ESP32_MODULE_RF` | `+3V3`, `/BOOT0`, `/DM_E`, `/DP_E`, `/ESP_EN`, `/STATUS_LED`, `/U0RXD`, `/U0TXD`, `GND`, `unconnected-(U2-IO1-Pad39)`, `unconnected-(U2-IO10-Pad18)`, `unconnected-(U2-IO11-Pad19)`, `unconnected-(U2-IO12-Pad20)`, `unconnected-(U2-IO13-Pad21)`, `unconnected-(U2-IO14-Pad22)`, `unconnected-(U2-IO15-Pad8)`, `unconnected-(U2-IO16-Pad9)`, `unconnected-(U2-IO17-Pad10)`, `unconnected-(U2-IO18-Pad11)`, `unconnected-(U2-IO21-Pad23)`, `unconnected-(U2-IO3-Pad15)`, `unconnected-(U2-IO35-Pad28)`, `unconnected-(U2-IO36-Pad29)`, `unconnected-(U2-IO37-Pad30)`, `unconnected-(U2-IO38-Pad31)`, `unconnected-(U2-IO39-Pad32)`, `unconnected-(U2-IO4-Pad4)`, `unconnected-(U2-IO40-Pad33)`, `unconnected-(U2-IO41-Pad34)`, `unconnected-(U2-IO42-Pad35)`, `unconnected-(U2-IO45-Pad26)`, `unconnected-(U2-IO46-Pad16)`, `unconnected-(U2-IO47-Pad24)`, `unconnected-(U2-IO48-Pad25)`, `unconnected-(U2-IO5-Pad5)`, `unconnected-(U2-IO6-Pad6)`, `unconnected-(U2-IO7-Pad7)`, `unconnected-(U2-IO8-Pad12)`, `unconnected-(U2-IO9-Pad17)` | `C3`, `C4`, `R8`, `R9`, `SW1`, `SW2` | `TRUE` |

## Rules

- `U2` must remain near the top edge with antenna/U.FL/RF keepout facing the top edge.
- No copper, traces, vias, test pads, mounting holes, or components are allowed in the RF keepout.
- Reports state `RF_Module:ESP32-S3-WROOM-1` footprint/keepout bbox is approximately 48 mm wide, wider than the 38 mm board.
- This is `REQUIRES_LJ_EXPLICIT_ACCEPTANCE` or board/footprint repair before routing.
- Keep buck regulator switching copper away from `U2` RF area.
