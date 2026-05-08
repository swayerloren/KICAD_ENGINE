# Power Master Index

Date: 2026-05-02

Status: link-first source index for common PCB power parts. No datasheet PDFs were downloaded for this update.

## Purpose

This folder is the source-index side of the power component database. It records where AI agents should go for official datasheets, application notes, layout guidance, and verification evidence before selecting or editing power circuitry in KiCad.

The companion component records live in:

- `08_COMPONENT_DATABASE/02_POWER/POWER_COMPONENT_GUIDE.md`
- `08_COMPONENT_DATABASE/02_POWER/POWER_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/02_POWER/power_part_records.json`
- `08_COMPONENT_DATABASE/14_PART_SELECTION_GUIDES/REGULATOR_SELECTION_GUIDE.md`

## Rules For Agents

- Do not assume a regulator, charger, fuse, TVS, diode, MOSFET, or eFuse is suitable because it appears in this index.
- Do not infer package, pinout, pad geometry, thermal behavior, output capacitor requirements, compensation, or inductor choice from a generic symbol.
- Prefer official manufacturer product pages and datasheets.
- Use vendor evaluation-board schematics and layout examples only as references, not automatic design approval.
- Treat module listings such as LM2596 boards, MP1584 boards, TP4056 boards, and AMS1117 boards as unverified third-party designs unless their exact schematic, BOM, and thermal behavior are reviewed.
- Keep public GitHub releases link-only unless redistribution rights for the PDF are confirmed.

## Power Categories

| Category | Status | Notes |
| --- | --- | --- |
| Buck regulators | PARTIAL | LM2596, MP1584, TPS5430, and TPS62177 starter records exist. Inductor, catch diode, compensation, and thermal checks remain design-specific. |
| LDOs | PARTIAL | AMS1117-3.3, AP2112K-3.3, MCP1700, TLV755P, and MIC5504 starter records exist. Dropout, heat, stability, and capacitor ESR must be checked. |
| Boost regulators | MISSING | No dedicated boost IC records yet. Add only after official source review. |
| Battery chargers | PARTIAL | TP4056 and MCP73831 starter records exist. Cell chemistry, termination, thermistor, charge current, thermal, and protection requirements must be verified. |
| Ideal diode / reverse polarity | PARTIAL | Generic Schottky and P-channel MOSFET reverse-polarity records exist. Dedicated ideal-diode controller records are still missing. |
| eFuses | MISSING | Guidance exists, but no specific eFuse records are present yet. |
| Polyfuses | PARTIAL | Generic resettable polyfuse record exists. Hold current, trip current, voltage, temperature derating, and series resistance must be verified. |
| TVS protection | PARTIAL | Generic SMAJ and USB TVS records exist. Working voltage, clamp voltage, surge pulse, capacitance, and package must be selected from a real datasheet. |
| USB power protection | PARTIAL | Rules exist for USB 5V to 3.3V entry paths. USB-C CC, VBUS, data ESD, inrush, and connector ratings remain project-specific. |
| Automotive 12V input protection | GUIDANCE_ONLY | Rules exist, but no project should claim automotive robustness without transient standard, load-dump, jump-start, reverse-battery, EMI, and thermal verification. |

## Source Index

| Part / Topic | Vendor / Publisher | Document Type | Source URL | Local PDF | Verification Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| LM2596 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/LM2596 | Not bundled | SOURCE_LINK_RECORDED | Verify exact suffix, package, external diode, inductor, capacitor, and thermal design before use. |
| MP1584 | Monolithic Power Systems | Product page and datasheet source | https://www.monolithicpower.com/en/products/mp1584.html | Not bundled | SOURCE_LINK_RECORDED | MPS page marks MP1584 as not recommended for new designs; do not select for new work without lifecycle review. |
| AMS1117-3.3 | Multiple vendors / clone ecosystem | Source placeholder | Unknown - requires source verification | Not bundled | UNVERIFIED_PLACEHOLDER | Do not trust clone modules or generic AMS1117 markings without vendor-specific datasheet and package verification. |
| AP2112K-3.3 | Diodes Incorporated | Product page and datasheet source | https://www.diodes.com/part/view/AP2112?BackID=9304 | Not bundled | SOURCE_LINK_RECORDED | Verify the exact AP2112K orderable part, package, pinout, and capacitor requirements. |
| MCP1700 | Microchip | Product page and datasheet source | https://www.microchip.com/en-us/product/MCP1700 | Not bundled | SOURCE_LINK_RECORDED | Verify package suffix, voltage option, output capacitance, and load-current needs. |
| TLV755P | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/TLV755P | Not bundled | SOURCE_LINK_RECORDED | Verify the fixed-output suffix, package, enable pin behavior, and capacitor requirements. |
| MIC5504 | Microchip | Product page and datasheet source | https://www.microchip.com/en-us/product/MIC5504 | Not bundled | SOURCE_LINK_RECORDED | Verify exact output-voltage suffix and package before schematic use. |
| TPS5430 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/TPS5430 | Not bundled | SOURCE_LINK_RECORDED | High-current buck layout and thermal design are not optional. |
| TPS62177 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/TPS62177 | Not bundled | SOURCE_LINK_RECORDED | Verify package, current target, inductor choice, and sleep-mode behavior. |
| TP4056 | Common Chinese charger IC ecosystem | Source placeholder | Unknown - requires source verification | Not bundled | UNVERIFIED_PLACEHOLDER | KiCad has a TP4056 symbol with a distributor datasheet link, but this record needs official manufacturer verification. |
| MCP73831 | Microchip | Product page and datasheet source | https://www.microchip.com/en-us/product/MCP73831 | Not bundled | SOURCE_LINK_RECORDED | Verify charge-current programming, thermal behavior, status pins, and battery safety requirements. |
| Resettable PTC / polyfuse | Littelfuse PolySwitch family | Product family source | https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-ptc-devices | Not bundled | SOURCE_LINK_RECORDED | Hold/trip current and temperature derating must be selected from the exact part datasheet. |
| SMAJ TVS diode family | Littelfuse | Product family source | https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/surface-mount/smaj | Not bundled | SOURCE_LINK_RECORDED | Select standoff, breakdown, clamp, surge, and polarity from the exact part. |
| eFuse / hot-swap protection | Texas Instruments | Product family source | https://www.ti.com/power-management/power-switches/efuse-hotswap-controllers/overview.html | Not bundled | SOURCE_LINK_RECORDED | eFuse design still needs current-limit, SOA, inrush, fault, and thermal review. |
| Ideal diode controllers | Texas Instruments | Product family source | https://www.ti.com/power-management/power-switches/ideal-diodes-oring-controllers/overview.html | Not bundled | SOURCE_LINK_RECORDED | Useful for reverse protection and ORing, but controller-specific records are still missing. |
| USB ESD and surge protection | Texas Instruments | Application note source | https://www.ti.com/lit/pdf/slvaf82 | Not bundled | SOURCE_LINK_RECORDED | Match device capacitance and voltage ratings to USB speed, Type-C, and VBUS requirements. |
| Automotive 12V/24V battery input protection | Texas Instruments | Reference design source | https://www.ti.com/tool/TIDA-01167 | Not bundled | SOURCE_LINK_RECORDED | Reference only; project must define transient standard and environment. |

## KiCad Library Evidence Observed Locally

Read-only searches of the installed KiCad 9 symbol libraries found starter candidates for several requested parts:

- `Regulator_Switching:LM2596S-3.3`, `Regulator_Switching:LM2596T-3.3`, and related LM2596 variants.
- `Regulator_Switching:TPS5430DDA`.
- `Regulator_Switching:TPS62177DQC`.
- `Regulator_Linear:AMS1117-3.3`, `Regulator_Linear:AMS1117CD-3.3`, and `Regulator_Linear:AMS1117CS-3.3`.
- `Regulator_Linear:AP2112K-3.3`.
- `Regulator_Linear:MCP1700x-330xxTT`, `Regulator_Linear:MCP1700x-330xxMB`, and related MCP1700 variants.
- `Regulator_Linear:MIC5504-3.3YM5`.
- `Regulator_Linear:TLV75533PDBV`, `Regulator_Linear:TLV75533PDRV`, and related TLV755 variants.
- `Battery_Management:MCP73831-*` variants.
- `Battery_Management:TP4056-42-ESOP8`.
- Generic protection symbols including `Device:Polyfuse`, `Device:D_TVS`, `Device:D_TVS_Bidir`, `Device:D_Schottky`, and `Device:Q_PMOS`.

These names are candidates only. Symbol availability is not pinout approval, footprint approval, sourcing approval, or thermal approval.

## Missing Follow-Up Work

- Add source-verified boost regulator records.
- Add source-verified eFuse records for USB, 5V rails, battery inputs, and higher-voltage input paths.
- Add specific ideal-diode controller records.
- Research common USB-C port protection ICs and ESD arrays.
- Research automotive-qualified buck regulators and input protection front ends.
- Create project-specific power-tree review templates that combine schematic, PCB, BOM, footprint, and thermal checks.
