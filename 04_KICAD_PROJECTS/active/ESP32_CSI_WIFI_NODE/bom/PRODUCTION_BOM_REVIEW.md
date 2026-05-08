# ESP32_CSI_WIFI_NODE Production BOM Review

Date: 2026-05-07

Mode: `READ_ONLY`

PCB edited: `NO`

Final classification: `BOM_BLOCKED`

## Evidence Reviewed

- `PRE_SCHEMATIC_BOM_LOCK.md`
- `SCHEMATIC_READY_PARTS_LIST.md`
- `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`
- Supplier ingestion policy files under `28_SUPPLIER_INGESTION/`
- Supplier-footprint match rules under `30_SUPPLIER_FOOTPRINT_MATCHES/`

## Review Rules

- Supplier stock, price, lead time, and lifecycle are time-sensitive and were not live-verified in this review.
- No JLC/LCSC part number is locked.
- Supplier package text is not footprint proof.
- No row is production-ready because `PRE_SCHEMATIC_BOM_LOCK.md` records `0` `VERIFIED_EXACT_PACKAGE_DRAWING` footprints.
- High-risk parts keep human review required until exact MPN, package drawing, pin mapping, and orientation evidence are recorded.

## Summary

| Metric | Count |
|---|---:|
| Physical parts reviewed | `43` |
| Exact drawing verified footprints | `0` |
| Candidate footprints needing human review | `30` |
| Blocked by missing exact part | `7` |
| Blocked by missing package | `6` |
| JLC/LCSC part numbers locked | `0` |
| BOM ready for production | `NO` |

## Production BOM Review Table

| Ref | Value | MPN | Footprint | Package | Supplier | JLC/LCSC | Datasheet | Lifecycle / stock | Substitute | Polarity / orientation risk | Manual assembly | DNP/DNI | Critical exact part |
|---|---|---|---|---|---|---|---|---|---:|---|---:|---:|---:|
| J1 | 5.5x2.1 center-positive barrel jack | `BLOCKED_NO_EXACT_PART` | `BarrelJack_CUI_PJ-102AH_Horizontal` candidate only | RA TH barrel jack | `TBD`; PJ-102A reference only | `UNKNOWN` | `SRC_PJ102A_REFERENCE` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO` | `HIGH connector/pin/mechanical` | `LIKELY_MANUAL_OR_REVIEW` | `NO` | `YES` |
| F1 | PTC hold current needs review | `1206L110THYR` class candidate | `Fuse_1206_3216Metric` | 1206 PTC | Littelfuse candidate; supplier TBD | `UNKNOWN` | `SRC_1206L110THYR` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_WITH_DERATING_REVIEW` | `LOW polarity; HIGH current derating` | `TBD` | `NO` | `YES` |
| Q1 | AO3401A-class PMOS | `AO3401A` class candidate | `SOT-23` | SOT-23 | AOS candidate; supplier TBD | `UNKNOWN` | `SRC_AO3401A` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_PINMAP_REVIEW` | `HIGH S/G/D mapping` | `TBD` | `NO` | `YES` |
| D1 | 5 V TVS | `SMAJ5.0A` class candidate | `D_SMA` | SMA / DO-214AC | Littelfuse candidate; supplier TBD | `UNKNOWN` | `SRC_SMAJ5_0A` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_POLARITY_REVIEW` | `HIGH polarity/package` | `TBD` | `NO` | `YES` |
| C1 | 47 uF >=16 V bulk | `TBD` | `NO_SAFE_LOCKED_FOOTPRINT` | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_PACKAGE_DERATING` | `TBD if polarized` | `TBD` | `NO` | `YES` |
| U1 | AP63203 3V3 2A buck | `AP63203WU-7` | `TSOT-23-6` candidate | TSOT26/WU | Diodes Inc candidate; supplier TBD | `UNKNOWN` | `SRC_AP63203` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_REGULATOR_REVIEW` | `HIGH pinout/layout` | `TBD` | `NO` | `YES` |
| L1 | 3.9 uH inductor | `BLOCKED_NO_EXACT_PART` | `NO_SAFE_LOCKED_FOOTPRINT` | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_AP63203` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_CURRENT_HEIGHT_REVIEW` | `LOW polarity; HIGH saturation/height` | `TBD` | `NO` | `YES` |
| C2 | 10 uF buck CIN | `TBD` | `C_0805` or `C_1206` candidate | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_AP63203` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_DERATING` | `LOW if MLCC` | `TBD` | `NO` | `YES` |
| C3 | 22 uF buck COUT | `TBD` | `C_0805` or `C_1206` candidate | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_AP63203` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_STABILITY_REVIEW` | `LOW if MLCC` | `TBD` | `NO` | `YES` |
| C4 | 22 uF buck COUT | `TBD` | `C_0805` or `C_1206` candidate | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_AP63203` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_STABILITY_REVIEW` | `LOW if MLCC` | `TBD` | `NO` | `YES` |
| C5 | 100 nF CBST | 100 nF generic | `C_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_AP63203` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_WITH_VOLTAGE_RATING` | `LOW` | `TBD` | `NO` | `NO` |
| U2 | ESP32-S3-WROOM-1U-N16R8 | `ESP32-S3-WROOM-1U-N16R8` | `ESP32-S3-WROOM-1` candidate | ESP32-S3-WROOM-1U module | Espressif; supplier TBD | `UNKNOWN` | `SRC_ESP32_DATASHEET` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_RF_MODULE_REVIEW` | `HIGH module/RF/mechanical` | `TBD_JLC_CAPABILITY_REVIEW` | `NO` | `YES` |
| C6 | 10 uF module decoupling | `TBD` | `C_0805_2012Metric` candidate | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_DERATING` | `LOW if MLCC` | `TBD` | `NO` | `YES` |
| C7 | 100 nF module decoupling | 100 nF generic | `C_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_WITH_VOLTAGE_RATING` | `LOW` | `TBD` | `NO` | `NO` |
| R1 | 10 k EN pull-up | 10 k generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES` | `LOW` | `TBD` | `NO` | `NO` |
| C8 | 1 uF EN delay | `TBD` | `C_0603` or `C_0805` candidate | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_DERATING_TIMING` | `LOW if MLCC` | `TBD` | `NO` | `YES` |
| SW1 | RESET_EN switch | `BLOCKED_NO_EXACT_PART` | `Panasonic_EVQPUJ_EVQPUA` candidate only | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_MECH_REVIEW` | `HIGH actuator/orientation` | `TBD` | `NO` | `YES` |
| R2 | 10 k BOOT pull-up | 10 k generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES` | `LOW` | `TBD` | `NO` | `NO` |
| SW2 | BOOT/GPIO0 switch | `BLOCKED_NO_EXACT_PART` | `Panasonic_EVQPUJ_EVQPUA` candidate only | `BLOCKED_NO_PACKAGE` | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_MECH_REVIEW` | `HIGH actuator/orientation` | `TBD` | `NO` | `YES` |
| J2 | USB-C receptacle USB2 | GCT `USB4105` class; suffix TBD | `USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` candidate | USB4105 16P top-mount horizontal | GCT candidate; supplier TBD | `UNKNOWN` | `SRC_USB4105` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_DRAWING_REVIEW` | `HIGH connector/orientation` | `TBD_JLC_CAPABILITY_REVIEW` | `NO` | `YES` |
| R3 | 0R DNI shield option | 0 ohm generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES` | `LOW component; HIGH EMC policy` | `TBD` | `YES_DNI_DEFAULT_POLICY_OPEN` | `YES` |
| R4 | 5.1 k CC1 | 5.1 k generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_1PCT_RECOMMENDED` | `LOW` | `TBD` | `NO` | `YES` |
| R5 | 5.1 k CC2 | 5.1 k generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_1PCT_RECOMMENDED` | `LOW` | `TBD` | `NO` | `YES` |
| U3 | USB D+/D- ESD | `BLOCKED_NO_EXACT_PART`; TPD2EUSB30 class | `SOT-23-6` candidate only | `BLOCKED_NO_EXACT_PACKAGE` | TI candidate; supplier TBD | `UNKNOWN` | `SRC_TPD2EUSB30` | `UNKNOWN_NOT_LIVE_CHECKED` | `NO_WITHOUT_PINOUT_CAP_REVIEW` | `HIGH ESD pinout/orientation` | `TBD` | `NO` | `YES` |
| R6 | 22R USB D- | 22 ohm generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_VALUE_TOL_REVIEW` | `LOW; USB placement risk` | `TBD` | `NO` | `YES` |
| R7 | 22R USB D+ | 22 ohm generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_ESP32_HW_GUIDE` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_VALUE_TOL_REVIEW` | `LOW; USB placement risk` | `TBD` | `NO` | `YES` |
| R8 | 2.2 k power LED resistor | 2.2 k generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_LED_CURRENT_REVIEW` | `LOW` | `TBD` | `NO` | `NO` |
| D2 | Power LED | `BLOCKED_NO_EXACT_PART` | `LED_0603_1608Metric` candidate | 0603 LED | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_COLOR_POLARITY_REVIEW` | `HIGH polarity/visibility` | `TBD` | `NO` | `YES` |
| R9 | 2.2 k status LED resistor | 2.2 k generic | `R_0603_1608Metric` | 0603 | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_LED_CURRENT_REVIEW` | `LOW` | `TBD` | `NO` | `NO` |
| D3 | Status LED | `BLOCKED_NO_EXACT_PART` | `LED_0603_1608Metric` candidate | 0603 LED | `TBD` | `UNKNOWN` | `SRC_PROJECT_REQUIREMENTS` | `UNKNOWN_NOT_LIVE_CHECKED` | `YES_AFTER_COLOR_POLARITY_REVIEW` | `HIGH polarity/visibility` | `TBD` | `NO` | `YES` |
| TP1 | +5V protected test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access risk` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |
| TP2 | 3V3 test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access risk` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |
| TP3 | GND test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access risk` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |
| TP4 | EN test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access risk` | `NO_ASSEMBLY_ITEM` | `NO` | `NO` |
| TP5 | BOOT/GPIO0 test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access risk` | `NO_ASSEMBLY_ITEM` | `NO` | `NO` |
| TP6 | U0TXD GPIO43 test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access/EMI risk` | `NO_ASSEMBLY_ITEM` | `NO` | `NO` |
| TP7 | U0RXD GPIO44 test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES` | `Probe/access risk` | `NO_ASSEMBLY_ITEM` | `NO` | `NO` |
| TP8 | USB D+ optional test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES_IF_OMITTED_OR_SHORT_STUB` | `HIGH USB stub risk` | `NO_ASSEMBLY_ITEM` | `DNI_CANDIDATE` | `YES` |
| TP9 | USB D- optional test pad | generic test pad | `TestPoint_Pad_D1.5mm` | SMD test pad | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `YES_IF_OMITTED_OR_SHORT_STUB` | `HIGH USB stub risk` | `NO_ASSEMBLY_ITEM` | `DNI_CANDIDATE` | `YES` |
| MH1 | M2.5 NPTH 2.7 mm | generic mounting hole | `MountingHole_2.7mm_M2.5` | 2.7 mm NPTH | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `NO_WITHOUT_MECH_REVIEW` | `HIGH mechanical` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |
| MH2 | M2.5 NPTH 2.7 mm | generic mounting hole | `MountingHole_2.7mm_M2.5` | 2.7 mm NPTH | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `NO_WITHOUT_MECH_REVIEW` | `HIGH mechanical` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |
| MH3 | M2.5 NPTH 2.7 mm | generic mounting hole | `MountingHole_2.7mm_M2.5` | 2.7 mm NPTH | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `NO_WITHOUT_MECH_REVIEW` | `HIGH mechanical` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |
| MH4 | M2.5 NPTH 2.7 mm | generic mounting hole | `MountingHole_2.7mm_M2.5` | 2.7 mm NPTH | `NOT_PURCHASED_PART` | `NOT_ASSEMBLY_PART` | `SRC_PROJECT_REQUIREMENTS` | `NOT_APPLICABLE` | `NO_WITHOUT_MECH_REVIEW` | `HIGH mechanical` | `NO_ASSEMBLY_ITEM` | `NO` | `YES` |

## Production BOM Decision

`BOM_BLOCKED`

Reason: exact orderable parts, packages, supplier SKUs, JLC/LCSC numbers, lifecycle/stock evidence, and drawing-level footprint verification are incomplete.
