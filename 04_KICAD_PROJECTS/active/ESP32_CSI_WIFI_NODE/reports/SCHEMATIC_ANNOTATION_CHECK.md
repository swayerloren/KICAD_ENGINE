# Schematic Annotation Check

Status: `FAIL`

Generated: `2026-05-03T07:53:28`
Schematic: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
BOM lock: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\PRE_SCHEMATIC_BOM_LOCK.md`

## Summary

- Pass: 158
- Warn: 44
- Fail: 44

## Findings

| Status | Code | Reference | Message | Evidence |
| --- | --- | --- | --- | --- |
| `PASS` | `REFERENCE_PRESENT` | `J1` | Reference is present and annotated. | `Connector:Barrel_Jack` |
| `PASS` | `VALUE_PRESENT` | `J1` | Value field is present. | `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `J1` | Physical symbol has no footprint assigned. | `Connector:Barrel_Jack` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `J1` | Physical symbol has no Datasheet property. | `Connector:Barrel_Jack` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR01` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR01` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `#FLG01` | Reference is present and annotated. | `power:PWR_FLAG` |
| `PASS` | `VALUE_PRESENT` | `#FLG01` | Value field is present. | `PWR_FLAG` |
| `PASS` | `REFERENCE_PRESENT` | `F1` | Reference is present and annotated. | `Device:Polyfuse` |
| `PASS` | `VALUE_PRESENT` | `F1` | Value field is present. | `PTC_HOLD_CURRENT_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `F1` | Physical symbol has no footprint assigned. | `Device:Polyfuse` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `F1` | Physical symbol has no Datasheet property. | `Device:Polyfuse` |
| `PASS` | `REFERENCE_PRESENT` | `Q1` | Reference is present and annotated. | `Device:Q_PMOS` |
| `PASS` | `VALUE_PRESENT` | `Q1` | Value field is present. | `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `Q1` | Physical symbol has no footprint assigned. | `Device:Q_PMOS` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `Q1` | Physical symbol has no Datasheet property. | `Device:Q_PMOS` |
| `PASS` | `REFERENCE_PRESENT` | `#FLG02` | Reference is present and annotated. | `power:PWR_FLAG` |
| `PASS` | `VALUE_PRESENT` | `#FLG02` | Value field is present. | `PWR_FLAG` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR03` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR03` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `D1` | Reference is present and annotated. | `Device:D_TVS` |
| `PASS` | `VALUE_PRESENT` | `D1` | Value field is present. | `5V_TVS_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `D1` | Physical symbol has no footprint assigned. | `Device:D_TVS` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `D1` | Physical symbol has no Datasheet property. | `Device:D_TVS` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR05` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR05` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `C1` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C1` | Value field is present. | `47uF_>=16V_BULK_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C1` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C1` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR07` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR07` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `U1` | Reference is present and annotated. | `Regulator_Switching:AP63203WU` |
| `PASS` | `VALUE_PRESENT` | `U1` | Value field is present. | `AP63203WU-7_3V3_2A` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `U1` | Physical symbol has no footprint assigned. | `Regulator_Switching:AP63203WU` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `U1` | Physical symbol has no Datasheet property. | `Regulator_Switching:AP63203WU` |
| `FAIL` | `HIGH_RISK_PART_WITHOUT_VERIFICATION_STATUS` | `U1` | High-risk categories require Verification_Status or explicit NEEDS_REVIEW/BLOCKED marker: regulator. | `Regulator_Switching:AP63203WU / AP63203WU-7_3V3_2A` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR10` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR10` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR11` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR11` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `#FLG03` | Reference is present and annotated. | `power:PWR_FLAG` |
| `PASS` | `VALUE_PRESENT` | `#FLG03` | Value field is present. | `PWR_FLAG` |
| `PASS` | `REFERENCE_PRESENT` | `L1` | Reference is present and annotated. | `Device:L` |
| `PASS` | `VALUE_PRESENT` | `L1` | Value field is present. | `3.9uH_NEEDS_REVIEW_MPN` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `L1` | Physical symbol has no footprint assigned. | `Device:L` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `L1` | Physical symbol has no Datasheet property. | `Device:L` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR12` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR12` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `C2` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C2` | Value field is present. | `10uF_CIN` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C2` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C2` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR14` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR14` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `C3` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C3` | Value field is present. | `22uF_COUT` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C3` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C3` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR15` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR15` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR16` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR16` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `C4` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C4` | Value field is present. | `22uF_COUT` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C4` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C4` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR17` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR17` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR18` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR18` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `C5` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C5` | Value field is present. | `100nF_CBST` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C5` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C5` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `U2` | Reference is present and annotated. | `RF_Module:ESP32-S3-WROOM-1` |
| `PASS` | `VALUE_PRESENT` | `U2` | Value field is present. | `ESP32-S3-WROOM-1U-N16R8` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `U2` | Physical symbol has no footprint assigned. | `RF_Module:ESP32-S3-WROOM-1` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `U2` | Physical symbol has no Datasheet property. | `RF_Module:ESP32-S3-WROOM-1` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR19` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR19` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR20` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR20` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `C6` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C6` | Value field is present. | `10uF_MODULE_DECOUPLING` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C6` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C6` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR21` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR21` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR22` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR22` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `C7` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C7` | Value field is present. | `100nF_MODULE_DECOUPLING` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C7` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C7` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR23` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR23` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR24` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR24` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R1` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R1` | Value field is present. | `10k_EN_PULLUP` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R1` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R1` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR25` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR25` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `C8` | Reference is present and annotated. | `Device:C` |
| `PASS` | `VALUE_PRESENT` | `C8` | Value field is present. | `1uF_EN_DELAY` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `C8` | Physical symbol has no footprint assigned. | `Device:C` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `C8` | Physical symbol has no Datasheet property. | `Device:C` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR26` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR26` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `SW1` | Reference is present and annotated. | `Switch:SW_Push` |
| `PASS` | `VALUE_PRESENT` | `SW1` | Value field is present. | `RESET_EN` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `SW1` | Physical symbol has no footprint assigned. | `Switch:SW_Push` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `SW1` | Physical symbol has no Datasheet property. | `Switch:SW_Push` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR27` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR27` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R2` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R2` | Value field is present. | `10k_BOOT_PULLUP` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R2` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R2` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR28` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR28` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `SW2` | Reference is present and annotated. | `Switch:SW_Push` |
| `PASS` | `VALUE_PRESENT` | `SW2` | Value field is present. | `BOOT_GPIO0` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `SW2` | Physical symbol has no footprint assigned. | `Switch:SW_Push` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `SW2` | Physical symbol has no Datasheet property. | `Switch:SW_Push` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR29` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR29` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `J2` | Reference is present and annotated. | `Connector:USB_C_Receptacle_USB2.0_14P` |
| `PASS` | `VALUE_PRESENT` | `J2` | Value field is present. | `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `J2` | Physical symbol has no footprint assigned. | `Connector:USB_C_Receptacle_USB2.0_14P` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `J2` | Physical symbol has no Datasheet property. | `Connector:USB_C_Receptacle_USB2.0_14P` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR30` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR30` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R3` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R3` | Value field is present. | `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R3` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R3` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR31` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR31` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R4` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R4` | Value field is present. | `5.1k_CC1` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R4` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R4` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR32` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR32` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R5` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R5` | Value field is present. | `5.1k_CC2` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R5` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R5` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR33` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR33` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `U3` | Reference is present and annotated. | `Power_Protection:TPD2EUSB30` |
| `PASS` | `VALUE_PRESENT` | `U3` | Value field is present. | `TPD2EUSB30_OR_EQ_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `U3` | Physical symbol has no footprint assigned. | `Power_Protection:TPD2EUSB30` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `U3` | Physical symbol has no Datasheet property. | `Power_Protection:TPD2EUSB30` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR34` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR34` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R6` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R6` | Value field is present. | `22R_USB_D-_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R6` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R6` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `R7` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R7` | Value field is present. | `22R_USB_D+_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R7` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R7` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `R8` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R8` | Value field is present. | `2.2k_PWR_LED` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R8` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R8` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR35` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR35` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `D2` | Reference is present and annotated. | `Device:LED` |
| `PASS` | `VALUE_PRESENT` | `D2` | Value field is present. | `PWR_LED` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `D2` | Physical symbol has no footprint assigned. | `Device:LED` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `D2` | Physical symbol has no Datasheet property. | `Device:LED` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR36` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR36` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `R9` | Reference is present and annotated. | `Device:R` |
| `PASS` | `VALUE_PRESENT` | `R9` | Value field is present. | `2.2k_STATUS_LED` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `R9` | Physical symbol has no footprint assigned. | `Device:R` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `R9` | Physical symbol has no Datasheet property. | `Device:R` |
| `PASS` | `REFERENCE_PRESENT` | `D3` | Reference is present and annotated. | `Device:LED` |
| `PASS` | `VALUE_PRESENT` | `D3` | Value field is present. | `STATUS_LED_SIMPLE` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `D3` | Physical symbol has no footprint assigned. | `Device:LED` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `D3` | Physical symbol has no Datasheet property. | `Device:LED` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR37` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR37` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `TP1` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP1` | Value field is present. | `+5V_PROTECTED` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP1` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP1` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `TP2` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP2` | Value field is present. | `3V3` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP2` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP2` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR39` | Reference is present and annotated. | `power:+3V3` |
| `PASS` | `VALUE_PRESENT` | `#PWR39` | Value field is present. | `+3V3` |
| `PASS` | `REFERENCE_PRESENT` | `TP3` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP3` | Value field is present. | `GND` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP3` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP3` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `#PWR40` | Reference is present and annotated. | `power:GND` |
| `PASS` | `VALUE_PRESENT` | `#PWR40` | Value field is present. | `GND` |
| `PASS` | `REFERENCE_PRESENT` | `TP4` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP4` | Value field is present. | `EN` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP4` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP4` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `TP5` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP5` | Value field is present. | `BOOT_GPIO0` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP5` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP5` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `TP6` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP6` | Value field is present. | `U0TXD_GPIO43` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP6` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP6` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `TP7` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP7` | Value field is present. | `U0RXD_GPIO44` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP7` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP7` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `TP8` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP8` | Value field is present. | `USB_D+_OPTIONAL_STUB_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP8` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP8` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `TP9` | Reference is present and annotated. | `Connector:TestPoint` |
| `PASS` | `VALUE_PRESENT` | `TP9` | Value field is present. | `USB_D-_OPTIONAL_STUB_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `TP9` | Physical symbol has no footprint assigned. | `Connector:TestPoint` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `TP9` | Physical symbol has no Datasheet property. | `Connector:TestPoint` |
| `PASS` | `REFERENCE_PRESENT` | `MH1` | Reference is present and annotated. | `Mechanical:MountingHole` |
| `PASS` | `VALUE_PRESENT` | `MH1` | Value field is present. | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `MH1` | Physical symbol has no footprint assigned. | `Mechanical:MountingHole` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `MH1` | Physical symbol has no Datasheet property. | `Mechanical:MountingHole` |
| `PASS` | `REFERENCE_PRESENT` | `MH2` | Reference is present and annotated. | `Mechanical:MountingHole` |
| `PASS` | `VALUE_PRESENT` | `MH2` | Value field is present. | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `MH2` | Physical symbol has no footprint assigned. | `Mechanical:MountingHole` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `MH2` | Physical symbol has no Datasheet property. | `Mechanical:MountingHole` |
| `PASS` | `REFERENCE_PRESENT` | `MH3` | Reference is present and annotated. | `Mechanical:MountingHole` |
| `PASS` | `VALUE_PRESENT` | `MH3` | Value field is present. | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `MH3` | Physical symbol has no footprint assigned. | `Mechanical:MountingHole` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `MH3` | Physical symbol has no Datasheet property. | `Mechanical:MountingHole` |
| `PASS` | `REFERENCE_PRESENT` | `MH4` | Reference is present and annotated. | `Mechanical:MountingHole` |
| `PASS` | `VALUE_PRESENT` | `MH4` | Value field is present. | `M2.5_NPTH_2.7mm_NEEDS_REVIEW` |
| `FAIL` | `NO_FOOTPRINT_ASSIGNED` | `MH4` | Physical symbol has no footprint assigned. | `Mechanical:MountingHole` |
| `WARN` | `MISSING_DATASHEET_FIELD` | `MH4` | Physical symbol has no Datasheet property. | `Mechanical:MountingHole` |
| `WARN` | `BOM_LOCK_NOT_FOUND` | `` | BOM lock was requested but does not exist. | `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\PRE_SCHEMATIC_BOM_LOCK.md` |

## Safe Use

- This is an automated screening report, not final engineering approval.
- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.
- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.
