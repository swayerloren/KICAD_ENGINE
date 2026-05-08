# Schematic Annotation Check

Status: `PASS`

Generated: `2026-05-03T14:56:57`
Schematic: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`

## Summary

- Pass: 43
- Warn: 0
- Fail: 0

## Findings

| Status | Code | Reference | Message | Evidence |
| --- | --- | --- | --- | --- |
| `PASS` | `REFERENCE_PRESENT` | `R2` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R2` | Value field is present. | `66` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `R2` | Footprint field is populated. | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `D1` | Reference is present and annotated. | `Device:D_Zener` |
| `PASS` | `VALUE_PRESENT` | `D1` | Value field is present. | `3.6 Zener` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `D1` | Footprint field is populated. | `Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `U1` | Reference is present and annotated. | `MCU_Microchip_ATtiny:ATtiny85-20P` |
| `PASS` | `VALUE_PRESENT` | `U1` | Value field is present. | `ATtiny85-20P` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `U1` | Footprint field is populated. | `Package_DIP:DIP-8_W7.62mm_Socket` |
| `PASS` | `REFERENCE_PRESENT` | `J2` | Reference is present and annotated. | `Connector_Generic:Conn_02x05_Odd_Even` |
| `PASS` | `VALUE_PRESENT` | `J2` | Value field is present. | `Conn_02x05_Odd_Even` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `J2` | Footprint field is populated. | `Connector_PinSocket_2.54mm:PinSocket_2x05_P2.54mm_Vertical` |
| `PASS` | `REFERENCE_PRESENT` | `R4` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R4` | Value field is present. | `470` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `R4` | Footprint field is populated. | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `#FLG0101` | Reference is present and annotated. | `power:PWR_FLAG` |
| `PASS` | `VALUE_PRESENT` | `#FLG0101` | Value field is present. | `PWR_FLAG` |
| `PASS` | `REFERENCE_PRESENT` | `D2` | Reference is present and annotated. | `Device:D_Zener` |
| `PASS` | `VALUE_PRESENT` | `D2` | Value field is present. | `3.6 Zener` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `D2` | Footprint field is populated. | `Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `D4` | Reference is present and annotated. | `Device:LED` |
| `PASS` | `VALUE_PRESENT` | `D4` | Value field is present. | `LED` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `D4` | Footprint field is populated. | `LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder` |
| `PASS` | `REFERENCE_PRESENT` | `R3` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R3` | Value field is present. | `66` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `R3` | Footprint field is populated. | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `U2` | Reference is present and annotated. | `Regulator_Linear:AMS1117-3.3` |
| `PASS` | `VALUE_PRESENT` | `U2` | Value field is present. | `AMS1117-3.3` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `U2` | Footprint field is populated. | `Package_TO_SOT_SMD:SOT-223-3_TabPin2` |
| `PASS` | `REFERENCE_PRESENT` | `R5` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R5` | Value field is present. | `470` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `R5` | Footprint field is populated. | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `#FLG0102` | Reference is present and annotated. | `power:PWR_FLAG` |
| `PASS` | `VALUE_PRESENT` | `#FLG0102` | Value field is present. | `PWR_FLAG` |
| `PASS` | `REFERENCE_PRESENT` | `J1` | Reference is present and annotated. | `Connector:USB_A` |
| `PASS` | `VALUE_PRESENT` | `J1` | Value field is present. | `USB_A` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `J1` | Footprint field is populated. | `My footprints:MOLEX_48037-0001` |
| `PASS` | `REFERENCE_PRESENT` | `R1` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R1` | Value field is present. | `1K5` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `R1` | Footprint field is populated. | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| `PASS` | `REFERENCE_PRESENT` | `D3` | Reference is present and annotated. | `Device:LED` |
| `PASS` | `VALUE_PRESENT` | `D3` | Value field is present. | `LED` |
| `PASS` | `FOOTPRINT_ASSIGNED` | `D3` | Footprint field is populated. | `LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder` |

## Safe Use

- This is an automated screening report, not final engineering approval.
- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.
- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.
