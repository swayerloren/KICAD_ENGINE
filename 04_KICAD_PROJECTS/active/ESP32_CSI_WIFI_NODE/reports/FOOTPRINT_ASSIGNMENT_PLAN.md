# Footprint Assignment Plan

Project: `ESP32_CSI_WIFI_NODE`  
Date: `2026-05-06`  
Status: `PLAN_ONLY_NOT_APPLIED`  
Schematic edited: `NO`

## Purpose

This report turns the current schematic physical symbol list into a BOM and footprint assignment plan. It is intentionally conservative: it records candidates but does not claim verification.

## Current Inputs

- Current schematic parse: `reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_PARSE.json`
- Current blocker report: `reports/CURRENT_SCHEMATIC_BLOCKERS.md`
- Component planning evidence: `COMPONENT_SELECTION_REPORT.md`
- Datasheet checklist: `DATASHEET_CHECKLIST.md`
- Package-to-footprint rule: `11_LIBRARY_FACTORY/mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md`
- Installed KiCad 9.0 footprint library checked read-only for candidate names.

## Assignment Policy

- Do not assign a footprint from this plan without a later schematic edit prompt and backup.
- Do not update PCB from schematic after assignment unless the schematic-to-PCB gate becomes `PASS`.
- Use exact manufacturer drawing evidence for high-risk parts before marking any footprint verified.
- Keep connector, PMOS, ESD, ESP32 module, regulator, inductor, fuse, TVS, mounting-hole, and test-pad rows human-review-required.

## Candidate Footprints Confirmed Present In Installed KiCad

The following candidate footprint files exist in the installed KiCad 9.0 library and were checked read-only:

- `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal`
- `Fuse:Fuse_1206_3216Metric`
- `Package_TO_SOT_SMD:SOT-23`
- `Diode_SMD:D_SMA`
- `Package_TO_SOT_SMD:TSOT-23-6`
- `Package_TO_SOT_SMD:SOT-23-6`
- `RF_Module:ESP32-S3-WROOM-1`
- `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal`
- `Resistor_SMD:R_0603_1608Metric`
- `Capacitor_SMD:C_0603_1608Metric`
- `Capacitor_SMD:C_0805_2012Metric`
- `Capacitor_SMD:C_1206_3216Metric`
- `Inductor_SMD:L_Vishay_IFSC-1515AH_4x4x1.8mm`
- `Inductor_SMD:L_Murata_LQH55DN_5.7x5.0mm`
- `LED_SMD:LED_0603_1608Metric`
- `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA`
- `TestPoint:TestPoint_Pad_D1.5mm`
- `MountingHole:MountingHole_2.7mm_M2.5`

Presence in installed KiCad is not verification.

## Footprint Assignment Table

| Ref | Current Value | Candidate Footprint | Status | Why |
| --- | --- | --- | --- | --- |
| J1 | `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW` | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` reference candidate | `BLOCKED_NO_EXACT_PART` | Exact jack MPN and drawing are not selected. |
| F1 | `PTC_HOLD_CURRENT_NEEDS_REVIEW` | `Fuse:Fuse_1206_3216Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | 1206L110THYR class candidate exists; derating and exact part review required. |
| Q1 | `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW` | `Package_TO_SOT_SMD:SOT-23` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | AO3401A class uses SOT-23, but S/G/D symbol-footprint mapping is blocked. |
| D1 | `5V_TVS_NEEDS_REVIEW` | `Diode_SMD:D_SMA` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | SMAJ class candidate, polarity and exact TVS review required. |
| C1 | `47uF_>=16V_BULK_NEEDS_REVIEW` | None locked | `BLOCKED_NO_PACKAGE` | Exact capacitor type/package not selected. |
| U1 | `AP63203WU-7_3V3_2A_NEEDS_REVIEW` | `Package_TO_SOT_SMD:TSOT-23-6` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | AP63203 WU/TSOT26 drawing must be checked. |
| L1 | `3.9uH_NEEDS_REVIEW_MPN` | None locked | `BLOCKED_NO_EXACT_PART` | Exact inductor MPN/package not selected. |
| C2 | `10uF_CIN` | `Capacitor_SMD:C_0805_2012Metric` or `Capacitor_SMD:C_1206_3216Metric` | `BLOCKED_NO_PACKAGE` | Voltage/derating/package not selected. |
| C3 | `22uF_COUT` | `Capacitor_SMD:C_0805_2012Metric` or `Capacitor_SMD:C_1206_3216Metric` | `BLOCKED_NO_PACKAGE` | Voltage/derating/package not selected. |
| C4 | `22uF_COUT` | `Capacitor_SMD:C_0805_2012Metric` or `Capacitor_SMD:C_1206_3216Metric` | `BLOCKED_NO_PACKAGE` | Voltage/derating/package not selected. |
| C5 | `100nF_CBST` | `Capacitor_SMD:C_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Small bootstrap cap candidate; package acceptance needed. |
| U2 | `ESP32-S3-WROOM-1U-N16R8` | `RF_Module:ESP32-S3-WROOM-1` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | WROOM-1U compatibility and RF/mechanical details require review. |
| C6 | `10uF_MODULE_DECOUPLING` | `Capacitor_SMD:C_0805_2012Metric` | `BLOCKED_NO_PACKAGE` | Package and derating not selected. |
| C7 | `100nF_MODULE_DECOUPLING` | `Capacitor_SMD:C_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default requires acceptance. |
| R1 | `10k_EN_PULLUP` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default requires acceptance. |
| C8 | `1uF_EN_DELAY` | `Capacitor_SMD:C_0603_1608Metric` or `Capacitor_SMD:C_0805_2012Metric` | `BLOCKED_NO_PACKAGE` | Package and derating not selected. |
| SW1 | `RESET_EN` | `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` reference candidate | `BLOCKED_NO_EXACT_PART` | Exact switch not selected. |
| R2 | `10k_BOOT_PULLUP` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default requires acceptance. |
| SW2 | `BOOT_GPIO0` | `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` reference candidate | `BLOCKED_NO_EXACT_PART` | Exact switch not selected. |
| J2 | `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW` | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Exact suffix, drawing, orientation, and enclosure fit required. |
| R3 | `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | USB shield policy still blocked. |
| R4 | `5.1k_CC1` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default requires acceptance. |
| R5 | `5.1k_CC2` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default requires acceptance. |
| U3 | `TPD2EUSB30_OR_EQ_NEEDS_REVIEW` | `Package_TO_SOT_SMD:SOT-23-6` reference candidate | `BLOCKED_NO_EXACT_PART` | Exact ESD orderable/package and pinout not selected. |
| R6 | `22R_USB_D-_NEEDS_REVIEW` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | USB layout and value review required. |
| R7 | `22R_USB_D+_NEEDS_REVIEW` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | USB layout and value review required. |
| R8 | `2.2k_PWR_LED` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default and LED current review required. |
| D2 | `PWR_LED` | `LED_SMD:LED_0603_1608Metric` | `BLOCKED_NO_EXACT_PART` | LED MPN/color/polarity not selected. |
| R9 | `2.2k_STATUS_LED` | `Resistor_SMD:R_0603_1608Metric` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Package default and GPIO/current review required. |
| D3 | `STATUS_LED_SIMPLE` | `LED_SMD:LED_0603_1608Metric` | `BLOCKED_NO_EXACT_PART` | LED MPN/color/polarity not selected. |
| TP1 | `+5V_PROTECTED` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe accessibility required. |
| TP2 | `3V3` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe accessibility required. |
| TP3 | `GND` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe accessibility required. |
| TP4 | `EN` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe accessibility required. |
| TP5 | `BOOT_GPIO0` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe accessibility required. |
| TP6 | `U0TXD_GPIO43` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe access and EMI review required. |
| TP7 | `U0RXD_GPIO44` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Probe accessibility required. |
| TP8 | `USB_D+_OPTIONAL_STUB_REVIEW` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | USB stub risk must be reviewed. |
| TP9 | `USB_D-_OPTIONAL_STUB_REVIEW` | `TestPoint:TestPoint_Pad_D1.5mm` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | USB stub risk must be reviewed. |
| MH1 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `MountingHole:MountingHole_2.7mm_M2.5` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Enclosure/standoff/keepout review required. |
| MH2 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `MountingHole:MountingHole_2.7mm_M2.5` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Enclosure/standoff/keepout review required. |
| MH3 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `MountingHole:MountingHole_2.7mm_M2.5` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Enclosure/standoff/keepout review required. |
| MH4 | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `MountingHole:MountingHole_2.7mm_M2.5` | `CANDIDATE_NEEDS_HUMAN_REVIEW` | Enclosure/standoff/keepout review required. |

## High-Risk Items

High-risk items requiring LJ/human review before schematic footprint assignment:

- `J1` barrel jack / power input connector.
- `J2` USB-C connector.
- `Q1` AO3401A-class PMOS.
- `U3` USB ESD diode array.
- `U2` ESP32-S3 module.
- `U1` AP63203 regulator.
- `L1` buck inductor.
- `F1` PTC fuse.
- `D1` TVS diode.
- `TP8` and `TP9` optional USB test pads.
- `MH1` through `MH4` mounting holes.

## Final Plan Decision

Schematic footprint assignment can safely proceed now: `NO`.

The next safe step is a human review pass over `PRE_SCHEMATIC_BOM_LOCK.md`, especially to choose exact MPNs and accepted package defaults. After that, a separate backed-up schematic edit pass can assign approved candidates and keep all unresolved high-risk items marked `NEEDS_HUMAN_REVIEW`.
