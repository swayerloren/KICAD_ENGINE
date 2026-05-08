# Power Tree And Return Paths

## Actual Power Nets

- `/+5V_IN`: raw input from `J1` to `F1`.
- `/+5V_FUSED`: fused input from `F1` to `Q1`.
- `/+5V_PROTECTED`: protected input from `Q1` to `D3/C2/C5/U1/TP1`.
- `/BUCK_BST`: bootstrap local net for `U1/C6`.
- `/BUCK_SW`: switch node between `U1`, `C6`, and `L1`.
- `+3V3`: regulator output rail feeding `U2`, decoupling, LEDs/control pullups, and `TP3`.
- `GND`: common return path.

## Power Cluster Components

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `C2` | `10uF_IN` | `Capacitor_SMD:C_0805_2012Metric` | `POWER_INPUT_BUCK` | `/+5V_PROTECTED`, `GND` | `U1`, `Q1`, `D3` | `FALSE` |
| `C5` | `47uF_16V` | `Capacitor_SMD:C_1206_3216Metric` | `POWER_INPUT_BUCK` | `/+5V_PROTECTED`, `GND` | `U1`, `Q1`, `D3` | `FALSE` |
| `C6` | `100nF_CBST` | `Capacitor_SMD:C_0603_1608Metric` | `POWER_INPUT_BUCK` | `/BUCK_BST`, `/BUCK_SW` | `U1` | `FALSE` |
| `C7` | `22uF_OUT` | `Capacitor_SMD:C_1206_3216Metric` | `POWER_INPUT_BUCK` | `+3V3`, `GND` | `L1`, `U1` | `FALSE` |
| `C8` | `22uF_OUT` | `Capacitor_SMD:C_1206_3216Metric` | `POWER_INPUT_BUCK` | `+3V3`, `GND` | `L1`, `U1` | `FALSE` |
| `D3` | `TVS_NEEDS_REVIEW` | `Diode_SMD:D_SMA` | `POWER_INPUT_BUCK` | `/+5V_PROTECTED`, `GND` | `Q1`, `C2`, `C5` | `TRUE` |
| `F1` | `PTC_1206` | `Fuse:Fuse_1206_3216Metric` | `POWER_INPUT_BUCK` | `/+5V_FUSED`, `/+5V_IN` | `J1`, `Q1` | `FALSE` |
| `J1` | `JACK_5V` | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` | `POWER_INPUT_BUCK` | `/+5V_IN`, `GND` | `F1`, `Q1` | `TRUE` |
| `L1` | `3.9uH_REV` | `Inductor_SMD:L_Vishay_IFSC-1515AH_4x4x1.8mm` | `POWER_INPUT_BUCK` | `+3V3`, `/BUCK_SW` | `U1`, `C7`, `C8` | `TRUE` |
| `Q1` | `AO3401A_REV` | `Package_TO_SOT_SMD:SOT-23` | `POWER_INPUT_BUCK` | `/+5V_FUSED`, `/+5V_PROTECTED`, `GND` | `F1`, `D3`, `C2`, `C5`, `U1` | `TRUE` |
| `U1` | `AP63203_NEEDS_REVIEW` | `Package_TO_SOT_SMD:TSOT-23-6` | `POWER_INPUT_BUCK` | `+3V3`, `/+5V_PROTECTED`, `/BUCK_BST`, `/BUCK_SW`, `GND` | `C2`, `C5`, `C6`, `L1`, `C7`, `C8` | `TRUE` |

## Return Path Rules

- `J1/F1/Q1/D3/C2/C5` must stay close.
- `U1/C6/L1/C7/C8` must be compact; `/BUCK_SW` must be short.
- `GND` must provide low-impedance return for input protection, buck regulator, ESD, and ESP32 decoupling.
- Do not run buck switching copper near USB D+/D- or ESP32 RF keepout.
