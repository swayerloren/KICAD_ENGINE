# ESP32_CSI_WIFI_NODE Footprint Package Gate Report

Generated: 2026-05-06 15:42 -04:00  
Mode: read-only footprint/package gate after safe schematic repair  
Final classification: `SCHEMATIC_BLOCKED_NEEDS_HUMAN_REVIEW`

## Scope

- Project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- Schematic: `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- PCB edits: `NONE`
- Footprint assignments made: `NONE`

## Gate Standard

Per `09_ACCURACY_ENGINE/verification_rules/FOOTPRINT_DATASHEET_MATCH_RULES.md`, a footprint is verified only when exact MPN, package code, package drawing or land pattern, KiCad footprint path, pad count, numbering, mechanical orientation, and pin 1 marking evidence are recorded.

This gate did not find that evidence for any physical component.

## Summary

| Metric | Result |
| --- | --- |
| Physical schematic symbols parsed | `43` |
| Physical symbols with assigned footprints | `0` |
| Physical symbols with blank footprint fields | `43` |
| Physical symbols with datasheet placeholders only | `43` |
| Duplicate physical references | `0` |
| Footprint gate result | `FAIL` |

Evidence: `reports/SCHEMATIC_ELECTRICAL_FOOTPRINT_GATE_PARSE.json`

## High-Risk Footprint Gate

| Item | Ref(s) | Status | Human review | Reason |
| --- | --- | --- | --- | --- |
| ESP32 module | `U2` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; module land pattern and antenna keepout are not verified to exact selected module. |
| USB-C connector | `J2` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; connector MPN, drawing, pin numbering, shell tabs, board-edge orientation, and 3D/mechanical fit are unverified. |
| USB ESD | `U3` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; package and pinout for selected ESD diode array are unverified. |
| AO3401A/PMOS | `Q1` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; PMOS source/gate/drain mapping to footprint pins is explicitly blocked. |
| AP63203 regulator | `U1` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; package, exposed pad/thermal needs, and switching layout requirements are not verified. |
| Inductor | `L1` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; MPN, current rating, DCR, shielded/unshielded choice, and land pattern are not locked. |
| TVS | `D1` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; polarity/package/clamping selection are not verified. |
| Fuse | `F1` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; hold/trip current and package are not locked. |
| Barrel/input connector | `J1` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprint blank; exact jack geometry, pin numbering, and mechanical orientation are not verified. |
| Switches/buttons | `SW1`, `SW2` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprints blank; exact tactile switch pinout/orientation is not verified. |
| LEDs | `D2`, `D3` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprints blank; polarity/package not verified. |
| Test pads | `TP1`-`TP9` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprints blank; pad size, side, spacing, and access are not selected. |
| Mounting holes | `MH1`-`MH4` | `NEEDS_HUMAN_REVIEW` | `YES` | Footprints blank; drill size, plated/non-plated status, keepout, and chassis/GND policy are unverified. |

## Physical Component Footprint Table

| Ref | Value | Symbol | Footprint | Datasheet/source | Footprint package status | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| `J1` | `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW` | `Connector:Barrel_Jack` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `F1` | `PTC_HOLD_CURRENT_NEEDS_REVIEW` | `Device:Polyfuse` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `Q1` | `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW` | `Device:Q_PMOS` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `D1` | `5V_TVS_NEEDS_REVIEW` | `Device:D_TVS` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `C1` | `47uF_>=16V_BULK_NEEDS_REVIEW` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `U1` | `AP63203WU-7_3V3_2A_NEEDS_REVIEW` | `Regulator_Switching:AP63203WU` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `L1` | `3.9uH_NEEDS_REVIEW_MPN` | `Device:L` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `C2` | `10uF_CIN` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `C3` | `22uF_COUT` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `C4` | `22uF_COUT` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `C5` | `100nF_CBST` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `U2` | `ESP32-S3-WROOM-1U-N16R8` | `RF_Module:ESP32-S3-WROOM-1` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `C6` | `10uF_3V3_BULK` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `C7` | `100nF_3V3_LOCAL` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `R1` | `10k_EN_PULLUP` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `C8` | `100nF_EN_NEEDS_REVIEW` | `Device:C` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `SW1` | `RESET_EN` | `Switch:SW_Push` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R2` | `10k_BOOT_PULLUP` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `SW2` | `BOOT_GPIO0` | `Switch:SW_Push` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `J2` | `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW` | `Connector:USB_C_Receptacle_USB2.0_14P` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R3` | `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R4` | `5.1k_CC1` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `R5` | `5.1k_CC2` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `MEDIUM` |
| `U3` | `TPD2EUSB30_OR_EQ_NEEDS_REVIEW` | `Power_Protection:TPD2EUSB30` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R6` | `22R_USB_D-_NEEDS_REVIEW` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R7` | `22R_USB_D+_NEEDS_REVIEW` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R8` | `2.2k_PWR_LED` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `LOW` |
| `D2` | `PWR_LED` | `Device:LED` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `R9` | `2.2k_STATUS_LED` | `Device:R` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `LOW` |
| `D3` | `STATUS_LED_SIMPLE` | `Device:LED` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP1` | `+5V_PROTECTED` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP2` | `3V3` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP3` | `GND` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP4` | `EN` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP5` | `BOOT_GPIO0` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP6` | `U0TXD_GPIO43` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP7` | `U0RXD_GPIO44` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP8` | `USB_D+_OPTIONAL_STUB_REVIEW` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `TP9` | `USB_D-_OPTIONAL_STUB_REVIEW` | `Connector:TestPoint` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `MH1` | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `Mechanical:MountingHole` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `MH2` | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `Mechanical:MountingHole` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `MH3` | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `Mechanical:MountingHole` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |
| `MH4` | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` | `Mechanical:MountingHole` | `<blank>` | `SOURCE_LINK_REQUIRED` | `UNVERIFIED` | `HIGH` |

## Gate Decision

Footprint/package gate result: `FAIL`

Reason: every physical symbol has a blank footprint and only a placeholder datasheet/source field. No exact package drawing evidence is recorded.

Final classification: `SCHEMATIC_BLOCKED_NEEDS_HUMAN_REVIEW`

PCB update allowed: `NO`

