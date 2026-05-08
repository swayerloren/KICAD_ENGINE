# Placement Dependency Map

Current placement is not ready for routing. Future movement must preserve these electrical dependencies.

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `C1` | `1uF_EN` | `Capacitor_SMD:C_0603_1608Metric` | `RESET_BOOT` | `/ESP_EN`, `GND` | `U2`, `SW2` | `FALSE` |
| `C2` | `10uF_IN` | `Capacitor_SMD:C_0805_2012Metric` | `POWER_INPUT_BUCK` | `/+5V_PROTECTED`, `GND` | `U1`, `Q1`, `D3` | `FALSE` |
| `C3` | `10uF_MOD` | `Capacitor_SMD:C_0805_2012Metric` | `ESP32_MODULE_RF` | `+3V3`, `GND` | `U2` | `FALSE` |
| `C4` | `100nF_MOD` | `Capacitor_SMD:C_0603_1608Metric` | `ESP32_MODULE_RF` | `+3V3`, `GND` | `U2` | `FALSE` |
| `C5` | `47uF_16V` | `Capacitor_SMD:C_1206_3216Metric` | `POWER_INPUT_BUCK` | `/+5V_PROTECTED`, `GND` | `U1`, `Q1`, `D3` | `FALSE` |
| `C6` | `100nF_CBST` | `Capacitor_SMD:C_0603_1608Metric` | `POWER_INPUT_BUCK` | `/BUCK_BST`, `/BUCK_SW` | `U1` | `FALSE` |
| `C7` | `22uF_OUT` | `Capacitor_SMD:C_1206_3216Metric` | `POWER_INPUT_BUCK` | `+3V3`, `GND` | `L1`, `U1` | `FALSE` |
| `C8` | `22uF_OUT` | `Capacitor_SMD:C_1206_3216Metric` | `POWER_INPUT_BUCK` | `+3V3`, `GND` | `L1`, `U1` | `FALSE` |
| `D1` | `PWR_LED` | `LED_SMD:LED_0603_1608Metric` | `LED` | `/PLED`, `GND` | `R3` | `FALSE` |
| `D2` | `STATUS_LED` | `LED_SMD:LED_0603_1608Metric` | `LED` | `/SLED`, `GND` | `R4` | `FALSE` |
| `D3` | `TVS_NEEDS_REVIEW` | `Diode_SMD:D_SMA` | `POWER_INPUT_BUCK` | `/+5V_PROTECTED`, `GND` | `Q1`, `C2`, `C5` | `TRUE` |
| `F1` | `PTC_1206` | `Fuse:Fuse_1206_3216Metric` | `POWER_INPUT_BUCK` | `/+5V_FUSED`, `/+5V_IN` | `J1`, `Q1` | `FALSE` |
| `J1` | `JACK_5V` | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` | `POWER_INPUT_BUCK` | `/+5V_IN`, `GND` | `F1`, `Q1` | `TRUE` |
| `J2` | `USB-C_NEEDS_REVIEW` | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `USB` | `/CC1`, `/CC2`, `/DM_C`, `/DP_C`, `/SHIELD`, `GND`, `unconnected-(J2-VBUS-PadA4)` | `U3`, `R6`, `R7` | `TRUE` |
| `L1` | `3.9uH_REV` | `Inductor_SMD:L_Vishay_IFSC-1515AH_4x4x1.8mm` | `POWER_INPUT_BUCK` | `+3V3`, `/BUCK_SW` | `U1`, `C7`, `C8` | `TRUE` |
| `MH1` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `MH2` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `MH3` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `MH4` | `M2.5_NPTH` | `MountingHole:MountingHole_2.7mm_M2.5` | `MECHANICAL` |  |  | `TRUE` |
| `Q1` | `AO3401A_REV` | `Package_TO_SOT_SMD:SOT-23` | `POWER_INPUT_BUCK` | `/+5V_FUSED`, `/+5V_PROTECTED`, `GND` | `F1`, `D3`, `C2`, `C5`, `U1` | `TRUE` |
| `R1` | `10k_EN` | `Resistor_SMD:R_0603_1608Metric` | `RESET_BOOT` | `+3V3`, `/ESP_EN` | `U2`, `SW2` | `FALSE` |
| `R2` | `10k_BOOT` | `Resistor_SMD:R_0603_1608Metric` | `RESET_BOOT` | `+3V3`, `/BOOT0` | `U2`, `SW1` | `FALSE` |
| `R3` | `2.2k` | `Resistor_SMD:R_0603_1608Metric` | `LED` | `+3V3`, `/PLED` | `D1` | `FALSE` |
| `R4` | `2.2k` | `Resistor_SMD:R_0603_1608Metric` | `LED` | `/SLED`, `/STATUS_LED` | `D2` | `FALSE` |
| `R5` | `0R_DNI` | `Resistor_SMD:R_0603_1608Metric` | `USB_SHIELD_POLICY` | `/SHIELD`, `GND` | `J2`, `GND` | `FALSE` |
| `R6` | `5.1k_CC1` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/CC1`, `GND` | `J2` | `FALSE` |
| `R7` | `5.1k_CC2` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/CC2`, `GND` | `J2` | `FALSE` |
| `R8` | `22R_D-` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/DM_C`, `/DM_E` | `U3`, `U2` | `FALSE` |
| `R9` | `22R_D+` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/DP_C`, `/DP_E` | `U3`, `U2` | `FALSE` |
| `SW1` | `BOOT_GPIO0_REVIEW` | `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` | `RESET_BOOT` | `/BOOT0`, `GND` | `U2`, `R2` | `FALSE` |
| `SW2` | `RESET_EN_REVIEW` | `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` | `RESET_BOOT` | `/ESP_EN`, `GND` | `U2`, `R1`, `C1` | `FALSE` |
| `TP1` | `TP_5V` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/+5V_PROTECTED` |  | `FALSE` |
| `TP2` | `TP_EN` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/ESP_EN` |  | `FALSE` |
| `TP3` | `TP_3V3` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `+3V3` |  | `FALSE` |
| `TP4` | `TP_BOOT` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/BOOT0` |  | `FALSE` |
| `TP5` | `TP_GND` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `GND` |  | `FALSE` |
| `TP6` | `TP_U0TXD` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/U0TXD` |  | `FALSE` |
| `TP7` | `TP_U0RXD` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/U0RXD` |  | `FALSE` |
| `TP8` | `TP_D+_REV` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/DP_E` |  | `FALSE` |
| `TP9` | `TP_D-_REV` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/DM_E` |  | `FALSE` |
| `U1` | `AP63203_NEEDS_REVIEW` | `Package_TO_SOT_SMD:TSOT-23-6` | `POWER_INPUT_BUCK` | `+3V3`, `/+5V_PROTECTED`, `/BUCK_BST`, `/BUCK_SW`, `GND` | `C2`, `C5`, `C6`, `L1`, `C7`, `C8` | `TRUE` |
| `U2` | `ESP32-S3-WROOM-1U` | `RF_Module:ESP32-S3-WROOM-1` | `ESP32_MODULE_RF` | `+3V3`, `/BOOT0`, `/DM_E`, `/DP_E`, `/ESP_EN`, `/STATUS_LED`, `/U0RXD`, `/U0TXD`, `GND`, `unconnected-(U2-IO1-Pad39)`, `unconnected-(U2-IO10-Pad18)`, `unconnected-(U2-IO11-Pad19)`, `unconnected-(U2-IO12-Pad20)`, `unconnected-(U2-IO13-Pad21)`, `unconnected-(U2-IO14-Pad22)`, `unconnected-(U2-IO15-Pad8)`, `unconnected-(U2-IO16-Pad9)`, `unconnected-(U2-IO17-Pad10)`, `unconnected-(U2-IO18-Pad11)`, `unconnected-(U2-IO21-Pad23)`, `unconnected-(U2-IO3-Pad15)`, `unconnected-(U2-IO35-Pad28)`, `unconnected-(U2-IO36-Pad29)`, `unconnected-(U2-IO37-Pad30)`, `unconnected-(U2-IO38-Pad31)`, `unconnected-(U2-IO39-Pad32)`, `unconnected-(U2-IO4-Pad4)`, `unconnected-(U2-IO40-Pad33)`, `unconnected-(U2-IO41-Pad34)`, `unconnected-(U2-IO42-Pad35)`, `unconnected-(U2-IO45-Pad26)`, `unconnected-(U2-IO46-Pad16)`, `unconnected-(U2-IO47-Pad24)`, `unconnected-(U2-IO48-Pad25)`, `unconnected-(U2-IO5-Pad5)`, `unconnected-(U2-IO6-Pad6)`, `unconnected-(U2-IO7-Pad7)`, `unconnected-(U2-IO8-Pad12)`, `unconnected-(U2-IO9-Pad17)` | `C3`, `C4`, `R8`, `R9`, `SW1`, `SW2` | `TRUE` |
| `U3` | `USB_ESD_REV` | `Package_TO_SOT_SMD:SOT-23-6` | `USB` | `/DM_C`, `/DP_C`, `GND` | `J2`, `R8`, `R9` | `TRUE` |

## Hard Placement Blocks

- Current placement audit is BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK.
- J1 barrel jack strategy unresolved.
- U2 footprint/keepout width risk unresolved.
- Four-hole compact mounting unresolved.
- Test pads crowded near USB/support parts.
- DRC has courtyard/clearance/silkscreen blockers.
