# Pre-Schematic BOM And Footprint Assignment Lock

Project: `ESP32_CSI_WIFI_NODE`  
Date: `2026-05-06`  
Status: `DRAFT_LOCK_BLOCKED_NEEDS_HUMAN_REVIEW`  
Scope: physical schematic symbols parsed from `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

This file is a planning lock for BOM values and footprint assignment. It does not edit the schematic and does not approve PCB update.

## Lock Rules

- No footprint in this file is `VERIFIED_EXACT_PACKAGE_DRAWING`.
- Installed KiCad footprints are candidates only.
- High-risk parts remain `NEEDS_HUMAN_REVIEW` until exact manufacturer part number, package drawing, pin numbering, and orientation evidence are reviewed.
- Do not use this lock to update PCB.
- Do not treat package names from supplier pages, project notes, or generic KiCad names as final footprint proof.

## Source Key

- `SRC_ESP32_DATASHEET`: Espressif ESP32-S3-WROOM-1 / WROOM-1U datasheet link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_ESP32_HW_GUIDE`: Espressif ESP32-S3 hardware design guidance links recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_AP63203`: Diodes AP63200/AP63201/AP63203/AP63205 datasheet link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_TPD2EUSB30`: TI TPD2EUSB30 product page/datasheet link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_USB4105`: GCT USB4105 specification link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_PJ102A_REFERENCE`: Same Sky / CUI PJ-102A reference datasheet link recorded in `COMPONENT_SELECTION_REPORT.md`; not a final selected barrel jack.
- `SRC_1206L110THYR`: Littelfuse 1206L110THYR source link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_SMAJ5_0A`: Littelfuse SMAJ5.0A source link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_AO3401A`: AOS AO3401A source link recorded in `COMPONENT_SELECTION_REPORT.md`.
- `SRC_PROJECT_REQUIREMENTS`: `REQUIREMENTS.md`, `COMPONENT_SELECTION_PLAN.md`, `DATASHEET_CHECKLIST.md`, and current schematic parse evidence.
- `SRC_INSTALLED_KICAD`: candidate footprint exists in installed KiCad 9.0 footprint libraries, checked read-only.

## Status Vocabulary

- `VERIFIED_EXACT_PACKAGE_DRAWING`: exact part and exact package drawing were checked against the candidate footprint.
- `CANDIDATE_NEEDS_HUMAN_REVIEW`: plausible candidate exists, but exact package/pin/orientation review is not complete.
- `BLOCKED_NO_EXACT_PART`: function/value is known, but exact manufacturer part number is not selected.
- `BLOCKED_NO_PACKAGE`: exact package/size is not selected, so no safe footprint can be locked.

## Summary

- Total physical schematic parts parsed: `43`
- Exact drawing verified footprints: `0`
- Candidate footprints requiring human review: `30`
- Blocked by missing exact part: `7`
- Blocked by missing package: `6`
- Schematic footprint assignment can safely proceed now: `NO`

## BOM And Footprint Lock Table

| Ref | Current Value | Function | MPN/Value Lock | Package Lock | Candidate KiCad Footprint | Source/Evidence | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J1 | `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW` | 5 V barrel input | Exact MPN not selected; requirement is 5.5 mm OD / 2.1 mm ID center-positive right-angle jack | Right-angle through-hole barrel jack, exact drawing required | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` as reference candidate only | `SRC_PJ102A_REFERENCE`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH connector/mechanical/orientation | `BLOCKED_NO_EXACT_PART` |
| F1 | `PTC_HOLD_CURRENT_NEEDS_REVIEW` | Input resettable fuse | Littelfuse `1206L110THYR` or equivalent 1.1 A hold class candidate | 1206 resettable PTC | `Fuse:Fuse_1206_3216Metric` | `SRC_1206L110THYR`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH power/current derating | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| Q1 | `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW` | Reverse-polarity P-channel MOSFET | AOS `AO3401A` class candidate | SOT-23, exact pin mapping required | `Package_TO_SOT_SMD:SOT-23` | `SRC_AO3401A`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH PMOS pin mapping/orientation | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| D1 | `5V_TVS_NEEDS_REVIEW` | 5 V input TVS | Littelfuse `SMAJ5.0A` class candidate | SMA / DO-214AC class, exact polarity/package drawing required | `Diode_SMD:D_SMA` | `SRC_SMAJ5_0A`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH polarity/protection | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| C1 | `47uF_>=16V_BULK_NEEDS_REVIEW` | Input bulk capacitor | 47 uF, >=16 V required by current schematic value; exact MPN not selected | Package not selected | No safe locked footprint | `SRC_PROJECT_REQUIREMENTS` | MEDIUM power/inrush/package | `BLOCKED_NO_PACKAGE` |
| U1 | `AP63203WU-7_3V3_2A_NEEDS_REVIEW` | 3.3 V buck regulator | Diodes `AP63203WU-7` | TSOT26 / WU package, drawing check required | `Package_TO_SOT_SMD:TSOT-23-6` | `SRC_AP63203`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH regulator thermal/pinout/layout | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| L1 | `3.9uH_NEEDS_REVIEW_MPN` | Buck inductor | 3.9 uH value; exact shielded inductor MPN not selected | Package not selected | No safe locked footprint | `SRC_AP63203`, `SRC_PROJECT_REQUIREMENTS` | HIGH switcher current/saturation/height | `BLOCKED_NO_EXACT_PART` |
| C2 | `10uF_CIN` | Buck VIN capacitor | 10 uF MLCC; exact MPN not selected | 0805 or 1206 candidate package requires derating review | `Capacitor_SMD:C_0805_2012Metric` or `Capacitor_SMD:C_1206_3216Metric` | `SRC_AP63203`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM switcher input loop | `BLOCKED_NO_PACKAGE` |
| C3 | `22uF_COUT` | Buck VOUT capacitor 1 | 22 uF MLCC; exact MPN not selected | 0805 or 1206 candidate package requires derating review | `Capacitor_SMD:C_0805_2012Metric` or `Capacitor_SMD:C_1206_3216Metric` | `SRC_AP63203`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM switcher output stability | `BLOCKED_NO_PACKAGE` |
| C4 | `22uF_COUT` | Buck VOUT capacitor 2 | 22 uF MLCC; exact MPN not selected | 0805 or 1206 candidate package requires derating review | `Capacitor_SMD:C_0805_2012Metric` or `Capacitor_SMD:C_1206_3216Metric` | `SRC_AP63203`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM switcher output stability | `BLOCKED_NO_PACKAGE` |
| C5 | `100nF_CBST` | AP63203 bootstrap capacitor | 100 nF | 0603 planning candidate | `Capacitor_SMD:C_0603_1608Metric` | `SRC_AP63203`, `SRC_INSTALLED_KICAD` | MEDIUM switcher support part | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| U2 | `ESP32-S3-WROOM-1U-N16R8` | ESP32-S3 module | Espressif `ESP32-S3-WROOM-1U-N16R8` primary | ESP32-S3-WROOM-1U module; -1U land-pattern equivalence requires review | `RF_Module:ESP32-S3-WROOM-1` | `SRC_ESP32_DATASHEET`, `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | HIGH module/RF/mechanical | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| C6 | `10uF_MODULE_DECOUPLING` | ESP32 module bulk decoupling | 10 uF MLCC; exact MPN not selected | 0805 candidate package requires derating review | `Capacitor_SMD:C_0805_2012Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM module power | `BLOCKED_NO_PACKAGE` |
| C7 | `100nF_MODULE_DECOUPLING` | ESP32 module local decoupling | 100 nF | 0603 planning candidate | `Capacitor_SMD:C_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | LOW/MEDIUM module power | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| R1 | `10k_EN_PULLUP` | ESP32 EN pull-up | 10 k | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM boot/reset | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| C8 | `1uF_EN_DELAY` | ESP32 EN delay capacitor | 1 uF | 0603 or 0805 candidate package requires derating review | `Capacitor_SMD:C_0603_1608Metric` or `Capacitor_SMD:C_0805_2012Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM boot/reset timing | `BLOCKED_NO_PACKAGE` |
| SW1 | `RESET_EN` | Reset/EN switch | Exact tactile switch MPN not selected | Package not selected | `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` as candidate only | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH mechanical/orientation/access | `BLOCKED_NO_EXACT_PART` |
| R2 | `10k_BOOT_PULLUP` | BOOT/GPIO0 pull-up | 10 k | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM boot strapping | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| SW2 | `BOOT_GPIO0` | BOOT/GPIO0 switch | Exact tactile switch MPN not selected | Package not selected | `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` as candidate only | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH mechanical/orientation/access | `BLOCKED_NO_EXACT_PART` |
| J2 | `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW` | USB-C USB2 receptacle | GCT `USB4105` class; exact suffix not selected | USB4105 16P top-mount horizontal candidate, exact drawing/orientation required | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `SRC_USB4105`, `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH connector/mechanical/orientation | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| R3 | `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW` | USB shield policy option | 0 ohm DNI | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH USB shield/EMC policy | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| R4 | `5.1k_CC1` | USB-C CC1 Rd | 5.1 k | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM USB-C configuration | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| R5 | `5.1k_CC2` | USB-C CC2 Rd | 5.1 k | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM USB-C configuration | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| U3 | `TPD2EUSB30_OR_EQ_NEEDS_REVIEW` | USB D+/D- ESD array | TI `TPD2EUSB30` class or equivalent; exact orderable/package not selected | Package not locked; SOT-23-6 candidate must be checked against selected suffix | `Package_TO_SOT_SMD:SOT-23-6` as candidate only | `SRC_TPD2EUSB30`, `SRC_INSTALLED_KICAD` | HIGH ESD pinout/orientation/routing | `BLOCKED_NO_EXACT_PART` |
| R6 | `22R_USB_D-_NEEDS_REVIEW` | USB D- series resistor | 22 ohm planning value | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM USB signal integrity | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| R7 | `22R_USB_D+_NEEDS_REVIEW` | USB D+ series resistor | 22 ohm planning value | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_ESP32_HW_GUIDE`, `SRC_INSTALLED_KICAD` | MEDIUM USB signal integrity | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| R8 | `2.2k_PWR_LED` | Power LED resistor | 2.2 k | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | LOW/MEDIUM LED current/visibility | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| D2 | `PWR_LED` | Power LED | Exact LED MPN/color not selected | 0603 LED candidate only | `LED_SMD:LED_0603_1608Metric` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM polarity/visibility | `BLOCKED_NO_EXACT_PART` |
| R9 | `2.2k_STATUS_LED` | Status LED resistor | 2.2 k | 0603 planning candidate | `Resistor_SMD:R_0603_1608Metric` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM GPIO/LED current | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| D3 | `STATUS_LED_SIMPLE` | Status LED | Exact LED MPN/color not selected | 0603 LED candidate only | `LED_SMD:LED_0603_1608Metric` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM polarity/GPIO/visibility | `BLOCKED_NO_EXACT_PART` |
| TP1 | `+5V_PROTECTED` | 5 V protected test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP2 | `3V3` | 3.3 V test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP3 | `GND` | GND test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP4 | `EN` | EN test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP5 | `BOOT_GPIO0` | BOOT/GPIO0 test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP6 | `U0TXD_GPIO43` | UART TX test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access/EMI | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP7 | `U0RXD_GPIO44` | UART RX test pad | 1.5 mm pad candidate | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | MEDIUM probe access | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP8 | `USB_D+_OPTIONAL_STUB_REVIEW` | Optional USB D+ test pad | 1.5 mm pad candidate, may be removed if stub risk is unacceptable | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH USB stub/signal integrity | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| TP9 | `USB_D-_OPTIONAL_STUB_REVIEW` | Optional USB D- test pad | 1.5 mm pad candidate, may be removed if stub risk is unacceptable | SMD test pad | `TestPoint:TestPoint_Pad_D1.5mm` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH USB stub/signal integrity | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| MH1 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | Mounting hole | M2.5 planning default | 2.7 mm NPTH | `MountingHole:MountingHole_2.7mm_M2.5` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH enclosure/mechanical | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| MH2 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | Mounting hole | M2.5 planning default | 2.7 mm NPTH | `MountingHole:MountingHole_2.7mm_M2.5` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH enclosure/mechanical | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| MH3 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | Mounting hole | M2.5 planning default | 2.7 mm NPTH | `MountingHole:MountingHole_2.7mm_M2.5` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH enclosure/mechanical | `CANDIDATE_NEEDS_HUMAN_REVIEW` |
| MH4 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | Mounting hole | M2.5 planning default | 2.7 mm NPTH | `MountingHole:MountingHole_2.7mm_M2.5` | `SRC_PROJECT_REQUIREMENTS`, `SRC_INSTALLED_KICAD` | HIGH enclosure/mechanical | `CANDIDATE_NEEDS_HUMAN_REVIEW` |

## Proceed / Block Decision

Schematic footprint assignment should not proceed automatically.

Safe next step is human review of this lock, followed by exact part/package decisions for blocked rows. After LJ accepts package defaults or exact MPNs, the schematic may be edited in a separate backed-up repair pass.
