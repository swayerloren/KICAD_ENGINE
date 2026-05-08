# Footprint And Package Audit - ATtiny85 Golden Path Sample

Status: `NEEDS_HUMAN_REVIEW`

Generated: `2026-05-03`

Sample: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board`

## Summary

The project-local footprint table was repaired so KiCad can resolve the upstream custom USB-A footprint nickname:

- Added `fp-lib-table`
- Library nickname: `My footprints`
- URI: `${KIPRJMOD}/custom_footprints`
- Footprint file present: `custom_footprints/MOLEX_48037-0001.kicad_mod`

This repair restores project portability for the custom footprint. It does not verify that the footprint matches the exact Molex mechanical drawing.

## Component Footprint Table

| Ref | Value | Symbol | Footprint | Package | Datasheet/source evidence | Footprint verification | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `R1` | `1K5` | `Device:R` | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | Axial THT resistor | `~` | `UNVERIFIED_GENERIC` | Low |
| `R2` | `66` | `Device:R` | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | Axial THT resistor | `~` | `UNVERIFIED_GENERIC` | Medium, USB data path |
| `R3` | `66` | `Device:R` | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | Axial THT resistor | `~` | `UNVERIFIED_GENERIC` | Medium, USB data path |
| `R4` | `470` | `Device:R` | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | Axial THT resistor | `~` | `UNVERIFIED_GENERIC` | Low |
| `R5` | `470` | `Device:R` | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` | Axial THT resistor | `~` | `UNVERIFIED_GENERIC` | Low |
| `D1` | `3.6 Zener` | `Device:D_Zener` | `Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal` | DO-34/SOD68 THT diode candidate | `~` | `UNVERIFIED_POLARITY_REVIEW_REQUIRED` | High, diode polarity and USB protection |
| `D2` | `3.6 Zener` | `Device:D_Zener` | `Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal` | DO-34/SOD68 THT diode candidate | `~` | `UNVERIFIED_POLARITY_REVIEW_REQUIRED` | High, diode polarity and USB protection |
| `D3` | `LED` | `Device:LED` | `LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder` | 1206 LED candidate | `~` | `UNVERIFIED_POLARITY_REVIEW_REQUIRED` | Medium, LED polarity |
| `D4` | `LED` | `Device:LED` | `LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder` | 1206 LED candidate | `~` | `UNVERIFIED_POLARITY_REVIEW_REQUIRED` | Medium, LED polarity |
| `U1` | `ATtiny85-20P` | `MCU_Microchip_ATtiny:ATtiny85-20P` | `Package_DIP:DIP-8_W7.62mm_Socket` | DIP-8 socket candidate | Microchip datasheet URL in schematic | `PARTIALLY_VERIFIED_SYMBOL_DATASHEET_LINK_ONLY` | Medium, pin 1/socket orientation |
| `U2` | `AMS1117-3.3` | `Regulator_Linear:AMS1117-3.3` | `Package_TO_SOT_SMD:SOT-223-3_TabPin2` | SOT-223 candidate | AMS1117 datasheet URL in schematic | `BLOCKED_UNTIL_HUMAN_REVIEW` | High, regulator pinout/thermal/package source |
| `J1` | `USB_A` | `Connector:USB_A` | `My footprints:MOLEX_48037-0001` | Molex USB-A custom footprint candidate | Footprint filename only | `BLOCKED_UNTIL_HUMAN_REVIEW` | High, connector orientation/mechanical/shield |
| `J2` | `Conn_02x05_Odd_Even` | `Connector_Generic:Conn_02x05_Odd_Even` | `Connector_PinSocket_2.54mm:PinSocket_2x05_P2.54mm_Vertical` | 2x5 2.54 mm socket candidate | `~` | `BLOCKED_UNTIL_HUMAN_REVIEW` | High, programming header pinout/orientation |

## KiCad Evidence

- Annotation check: `reports/ANNOTATION_CHECK.md` -> `PASS`
- Project validation: `reports/project_validation/project_validation_report.md` -> `WARN`
- DRC report: `_verification/kicad_cli/drc_after_repair.rpt`
- Schematic review status fields were added for `J1`, `J2`, and `U2` as `BLOCKED_UNTIL_HUMAN_REVIEW`.

## Remaining Footprint Blockers

1. `J1` custom Molex USB-A footprint must be checked against the exact Molex 48037-0001 drawing before any pass claim.
2. `J1` shield pin policy is unresolved and is an ERC error.
3. `J2` header orientation and mating/programming pinout require human review.
4. `U2` AMS1117 package and pin mapping require source verification.
5. Diode and LED polarity should be visually checked before treating the PCB as a clean demo.
6. DRC schematic parity still reports net-name conflicts inherited from the upstream board state.

## Result

`NEEDS_HUMAN_REVIEW`

The sample is useful for demonstrating KiCad Engine gate detection and controlled low-risk repair, but it is not verified for fabrication or clean benchmark scoring.
