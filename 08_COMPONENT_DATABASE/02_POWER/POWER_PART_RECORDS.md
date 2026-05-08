# Power Part Records

Date: 2026-05-02

Status: starter records for common PCB power parts. Records are not design-approved until exact datasheets, packages, pinouts, footprints, and thermal calculations are verified.

Unknown field value:

```text
Unknown - requires source verification
```

## Record Summary

| Record ID | Part / Circuit | Category | Source Status | KiCad Candidate Status |
| --- | --- | --- | --- | --- |
| `POWER_LM2596` | LM2596 | Buck regulator | TI source link recorded | KiCad symbol candidates observed locally |
| `POWER_MP1584` | MP1584 | Buck regulator | MPS source link recorded; lifecycle warning | KiCad exact symbol not observed locally |
| `POWER_AMS1117_3V3` | AMS1117-3.3 | LDO | Vendor source unresolved | KiCad symbol candidates observed locally |
| `POWER_AP2112K_3V3` | AP2112K-3.3 | LDO | Diodes source link recorded | KiCad symbol candidate observed locally |
| `POWER_MCP1700` | MCP1700 | LDO | Microchip source link recorded | KiCad symbol candidates observed locally |
| `POWER_TLV755P` | TLV755P | LDO | TI source link recorded | KiCad symbol candidates observed locally |
| `POWER_MIC5504` | MIC5504 | LDO | Microchip source link recorded | KiCad symbol candidate observed locally |
| `POWER_TPS5430` | TPS5430 | Buck regulator | TI source link recorded | KiCad symbol candidate observed locally |
| `POWER_TPS62177` | TPS62177 | Buck regulator | TI source link recorded | KiCad symbol candidate observed locally |
| `POWER_TP4056` | TP4056 | Linear battery charger | Official source unresolved | KiCad symbol candidate observed locally |
| `POWER_MCP73831` | MCP73831 | Linear battery charger | Microchip source link recorded | KiCad symbol candidates observed locally |
| `GENERIC_RESETTABLE_POLYFUSE` | Generic resettable polyfuse | Overcurrent protection | Littelfuse family source link recorded | KiCad generic symbol and footprints observed locally |
| `GENERIC_SMAJ_TVS_DIODE` | Generic SMAJ TVS diode | Surge protection | Littelfuse family source link recorded | KiCad generic TVS symbol and SMA footprint observed locally |
| `GENERIC_USB_TVS_DIODE` | Generic USB TVS diode | USB ESD protection | TI USB protection application-note link recorded | KiCad generic TVS symbols observed locally |
| `GENERIC_SCHOTTKY_REVERSE_POLARITY_DIODE` | Generic Schottky reverse-polarity diode | Reverse polarity protection | Source placeholder | KiCad generic Schottky symbol and diode footprints observed locally |
| `GENERIC_P_CHANNEL_MOSFET_REVERSE_POLARITY` | Generic P-channel MOSFET reverse-polarity circuit | Reverse polarity protection | TI ideal-diode and reverse-protection source links recorded | KiCad generic PMOS symbols observed locally |

## POWER_LM2596

- Part number: LM2596.
- Vendor: Texas Instruments.
- Family: SIMPLE SWITCHER buck regulator.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/LM2596.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: KiCad symbols indicate TO-263-style `LM2596S` and TO-220-style `LM2596T` variants; verify exact package and suffix from TI.
- KiCad symbol candidates: `Regulator_Switching:LM2596S-3.3`, `Regulator_Switching:LM2596T-3.3`, fixed and adjustable LM2596 variants.
- Common KiCad footprints: `Package_TO_SOT_SMD:TO-263-5_TabPin3`, `Package_TO_SOT_THT:TO-220-5_Vertical`; verify against exact package drawing.
- Thermal warnings: calculate regulator loss, catch diode loss, and copper area; do not rely on module current claims.
- Input/output capacitor warnings: capacitor value, voltage rating, ESR, ripple current, and placement are datasheet-specific.
- Layout warnings: keep input capacitor loop, diode loop, switch node, inductor, and feedback routing under control.
- Use cases: non-space-constrained buck conversion where older/simple parts are acceptable after verification.
- Avoid cases: compact low-noise designs, unverified modules, or new designs where a modern regulator is preferred.
- Common mistakes: omitting catch diode checks, copying module BOMs, undersizing inductor, and ignoring thermal copper.

## POWER_MP1584

- Part number: MP1584.
- Vendor: Monolithic Power Systems.
- Family: high-frequency buck regulator.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.monolithicpower.com/en/products/mp1584.html.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: MPS source identifies SOIC8E family; verify exact package drawing for the orderable suffix.
- KiCad symbol candidates: `Unknown - requires source verification`; consider generic buck-regulator symbol only for rough planning.
- Common KiCad footprints: SOIC-8 exposed-pad candidate only after package drawing verification.
- Thermal warnings: small exposed-pad switching regulators need copper and via review.
- Input/output capacitor warnings: ceramic capacitor stability and ripple ratings must be checked from the datasheet.
- Layout warnings: high-frequency switch node and input loop must be compact; follow vendor layout guidance.
- Use cases: compact buck research candidate when lifecycle and exact source are acceptable.
- Avoid cases: new designs when lifecycle policy rejects not-recommended-for-new-design parts.
- Common mistakes: treating MP1584 modules as verified reference designs and omitting feedback/layout review.

## POWER_AMS1117_3V3

- Part number: AMS1117-3.3.
- Vendor: `Unknown - requires source verification`.
- Family: 1117-style LDO.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: `Unknown - requires source verification`.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: KiCad symbols imply multiple package/suffix families; verify exact vendor, suffix, and package.
- KiCad symbol candidates: `Regulator_Linear:AMS1117-3.3`, `Regulator_Linear:AMS1117CD-3.3`, `Regulator_Linear:AMS1117CS-3.3`.
- Common KiCad footprints: SOT-223 and TO-252-style candidates only after exact suffix verification.
- Thermal warnings: 5V to 3.3V at meaningful current can overheat; calculate heat before use.
- Input/output capacitor warnings: stability and ESR requirements depend on the exact vendor part.
- Layout warnings: provide thermal copper and place capacitors close to pins.
- Use cases: legacy/simple rails only after heat and source verification.
- Avoid cases: low-power battery designs, hot enclosed boards, high-current 3.3V rails, and unverified clone parts.
- Common mistakes: assuming all AMS1117 clones share the same capacitor and thermal requirements.

## POWER_AP2112K_3V3

- Part number: AP2112K-3.3.
- Vendor: Diodes Incorporated.
- Family: AP2112 LDO.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.diodes.com/part/view/AP2112?BackID=9304.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: SOT25/SOT-23-5 style candidate for K suffix; verify exact orderable package and pinout.
- KiCad symbol candidates: `Regulator_Linear:AP2112K-3.3`.
- Common KiCad footprints: `Package_TO_SOT_SMD:SOT-23-5`; verify package drawing.
- Thermal warnings: small LDO package needs dissipation calculation.
- Input/output capacitor warnings: use datasheet capacitor value, dielectric, and placement.
- Layout warnings: keep input and output capacitors close, and do not leave enable floating unless datasheet allows it.
- Use cases: verified small 3.3V rails with modest current.
- Avoid cases: loads that make linear heat excessive.
- Common mistakes: choosing AP2112K because it is popular on dev boards without checking package pinout.

## POWER_MCP1700

- Part number: MCP1700.
- Vendor: Microchip.
- Family: low-quiescent-current LDO.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.microchip.com/en-us/product/MCP1700.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: multiple Microchip package suffixes exist; verify exact suffix and pinout.
- KiCad symbol candidates: `Regulator_Linear:MCP1700x-330xxTT`, `Regulator_Linear:MCP1700x-330xxMB`, and related MCP1700 variants.
- Common KiCad footprints: SOT-23, SOT-89, and TO-92 candidates only after suffix verification.
- Thermal warnings: small packages limit load current at high voltage drop.
- Input/output capacitor warnings: verify output capacitor value and ESR/stability requirements.
- Layout warnings: capacitors close to pins; keep ground return direct.
- Use cases: low-quiescent current 3.3V rails after current and dropout verification.
- Avoid cases: high-current loads, large voltage drop, or startup loads exceeding the part capability.
- Common mistakes: using MCP1700 as a universal 3.3V regulator without load-current review.

## POWER_TLV755P

- Part number: TLV755P.
- Vendor: Texas Instruments.
- Family: low-dropout regulator.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/TLV755P.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: TI product page lists multiple small packages; verify exact voltage and package suffix.
- KiCad symbol candidates: `Regulator_Linear:TLV75533PDBV`, `Regulator_Linear:TLV75533PDRV`, related TLV755 variants.
- Common KiCad footprints: SOT-23-5, WSON, and X2SON candidates only after package drawing verification.
- Thermal warnings: small package thermal performance depends on copper and load.
- Input/output capacitor warnings: verify minimum output capacitance and input bypassing from datasheet.
- Layout warnings: short capacitor loops and correct enable/output discharge assumptions.
- Use cases: modern small regulated rails after exact suffix verification.
- Avoid cases: unverified high-current loads or boards without exposed-pad/thermal review.
- Common mistakes: selecting wrong fixed-voltage suffix or mismatching symbol to package.

## POWER_MIC5504

- Part number: MIC5504.
- Vendor: Microchip.
- Family: MIC550x LDO.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.microchip.com/en-us/product/MIC5504.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: exact output-voltage and package suffix require Microchip datasheet verification.
- KiCad symbol candidates: `Regulator_Linear:MIC5504-3.3YM5`.
- Common KiCad footprints: SOT-23-5 or tiny DFN candidates only after suffix verification.
- Thermal warnings: tiny regulators can overheat quickly despite modest current ratings.
- Input/output capacitor warnings: use datasheet capacitor values and placement.
- Layout warnings: verify enable behavior and pad thermal recommendations.
- Use cases: compact low-current rails when source and package are verified.
- Avoid cases: high-drop, high-current rails.
- Common mistakes: assuming a small LDO current rating is usable without heat calculation.

## POWER_TPS5430

- Part number: TPS5430.
- Vendor: Texas Instruments.
- Family: wide-input buck regulator.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/TPS5430.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: KiCad candidate uses `DDA`; verify exact package drawing and thermal pad.
- KiCad symbol candidates: `Regulator_Switching:TPS5430DDA`.
- Common KiCad footprints: HTSSOP/PowerPAD style candidate only after package drawing verification.
- Thermal warnings: high-current buck designs require thermal pad and copper review.
- Input/output capacitor warnings: verify input RMS ripple, output ripple, and stability requirements.
- Layout warnings: follow TI layout guidance for input loop, catch diode, switch node, feedback, and thermal pad.
- Use cases: higher-power buck research candidate after full datasheet review.
- Avoid cases: casual layouts, breadboard assumptions, and boards without EMI/thermal review.
- Common mistakes: routing feedback near the switch node and omitting thermal vias when required.

## POWER_TPS62177

- Part number: TPS62177.
- Vendor: Texas Instruments.
- Family: small buck regulator.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/TPS62177.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: KiCad candidate uses `DQC`; verify exact package drawing.
- KiCad symbol candidates: `Regulator_Switching:TPS62177DQC`.
- Common KiCad footprints: small SON/VSON candidate only after package drawing verification.
- Thermal warnings: small package thermal behavior must be checked for the selected load.
- Input/output capacitor warnings: use datasheet inductor and capacitor selection tables.
- Layout warnings: compact input loop, inductor placement, feedback routing, and ground return matter.
- Use cases: efficient lower-current rails after exact source verification.
- Avoid cases: loads above verified capability or layouts that cannot handle switching regulator constraints.
- Common mistakes: assuming a small buck is layout-forgiving because the schematic is simple.

## POWER_TP4056

- Part number: TP4056.
- Vendor: `Unknown - requires source verification`.
- Family: single-cell linear charger ecosystem.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: `Unknown - requires source verification`.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: KiCad candidate indicates ESOP-8; verify official manufacturer, package, and exposed pad.
- KiCad symbol candidates: `Battery_Management:TP4056-42-ESOP8`.
- Common KiCad footprints: ESOP-8 exposed-pad candidate only after source verification.
- Thermal warnings: linear charging can dissipate substantial heat; charge current must be programmed and thermally checked.
- Input/output capacitor warnings: charger input and battery-side capacitor requirements are source-specific.
- Layout warnings: battery polarity, thermal pad, charge-current resistor, status LEDs, and protection circuit must be reviewed.
- Use cases: research placeholder for common single-cell Li-ion charger circuits.
- Avoid cases: public-release designs without verified source, battery protection plan, and safety review.
- Common mistakes: assuming TP4056 modules include all needed protection or match the bare IC reference circuit.

## POWER_MCP73831

- Part number: MCP73831.
- Vendor: Microchip.
- Family: single-cell linear charger.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.microchip.com/en-us/product/MCP73831.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: Microchip offers multiple package suffixes; verify exact package and pinout.
- KiCad symbol candidates: `Battery_Management:MCP73831-2-MC`, `Battery_Management:MCP73831-2-OT`, and related variants.
- Common KiCad footprints: SOT-23-5 and DFN candidates only after suffix verification.
- Thermal warnings: linear charger heat is input-to-battery voltage drop times charge current.
- Input/output capacitor warnings: verify input and battery capacitor requirements from datasheet.
- Layout warnings: charge-current programming resistor, status pins, thermal path, and battery connector polarity are critical.
- Use cases: verified single-cell charger designs with defined battery and charge current.
- Avoid cases: unknown batteries, no protection, no thermal plan, or multi-cell packs.
- Common mistakes: treating charger selection as only a schematic symbol choice.

## GENERIC_RESETTABLE_POLYFUSE

- Part number: generic resettable polyfuse.
- Vendor: Generic; Littelfuse PolySwitch family source recorded.
- Family: resettable PTC fuse.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-ptc-devices.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: 0603, 0805, 1206, 1210, 1812, radial, and other families exist; exact part required.
- KiCad symbol candidates: `Device:Polyfuse`, `Device:Polyfuse_Small`.
- Common KiCad footprints: `Fuse:Fuse_0603_1608Metric`, `Fuse:Fuse_0805_2012Metric`, `Fuse:Fuse_1206_3216Metric`, `Fuse:Fuse_1210_3225Metric`, `Fuse:Fuse_1812_4532Metric`.
- Thermal warnings: PTC temperature rise and derating are normal behavior.
- Input/output capacitor warnings: downstream capacitance affects inrush and trip behavior.
- Layout warnings: route fault current safely and avoid heating sensitive parts.
- Use cases: resettable overcurrent protection where slow trip and resistance are acceptable.
- Avoid cases: precision current limiting or semiconductor short-circuit protection without additional measures.
- Common mistakes: using room-temperature hold current as a universal current rating.

## GENERIC_SMAJ_TVS_DIODE

- Part number: generic SMAJ TVS diode.
- Vendor: Generic; Littelfuse SMAJ family source recorded.
- Family: SMAJ TVS.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/surface-mount/smaj.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: SMAJ/SMA package family; exact unidirectional/bidirectional and voltage suffix required.
- KiCad symbol candidates: `Device:D_TVS`, `Device:D_TVS_Bidir`.
- Common KiCad footprints: `Diode_SMD:D_SMA`, `Diode_SMD:D_SMA_Handsoldering`.
- Thermal warnings: pulse-power rating depends on waveform and derating, not package name alone.
- Input/output capacitor warnings: TVS capacitance and clamp behavior can affect protected circuits.
- Layout warnings: place close to connector with a short return path to ground or chassis strategy.
- Use cases: power-input transient clamping after exact voltage and surge selection.
- Avoid cases: high-speed data protection or sustained overvoltage without fuse coordination.
- Common mistakes: selecting standoff voltage too low or clamp voltage too high for downstream parts.

## GENERIC_USB_TVS_DIODE

- Part number: generic USB TVS diode.
- Vendor: Generic.
- Family: USB ESD/TVS.
- Category: `02_POWER`.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/lit/pdf/slvaf82.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: exact array package and channel count require selected part datasheet.
- KiCad symbol candidates: `Device:D_TVS_Dual_AAC`, `Device:D_TVS_Dual_ACA`, `Device:D_TVS_Dual_CAA`, `Device:D_TVS`.
- Common KiCad footprints: SOT-23, SOT-23-6, SOD-923, XSON/USON, or vendor-specific arrays; verify exact part.
- Thermal warnings: ESD parts are not bulk power clamps unless rated for that pulse.
- Input/output capacitor warnings: line capacitance must match USB speed and signal requirements.
- Layout warnings: place at connector, route straight-through when possible, and keep return inductance low.
- Use cases: USB D+/D-, CC, SBU, and VBUS protection after exact part selection.
- Avoid cases: substituting a power TVS on high-speed USB data.
- Common mistakes: ignoring capacitance or leaving CC pins unprotected in harsh interfaces.

## GENERIC_SCHOTTKY_REVERSE_POLARITY_DIODE

- Part number: generic Schottky reverse-polarity diode.
- Vendor: Generic.
- Family: series diode reverse protection.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: `Unknown - requires source verification`.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: SOD-123, SMA, SMB, SMC, and larger packages depending on current and heat.
- KiCad symbol candidates: `Device:D_Schottky`.
- Common KiCad footprints: `Diode_SMD:D_SOD-123`, `Diode_SMD:D_SMA`, `Diode_SMD:D_SMB`, `Diode_SMD:D_SMC`.
- Thermal warnings: forward voltage times current becomes heat.
- Input/output capacitor warnings: inrush current can exceed diode surge rating.
- Layout warnings: diode polarity marking, copper width, and heat spreading must be reviewed.
- Use cases: simple low-cost reverse polarity protection where voltage drop is acceptable.
- Avoid cases: high-current rails, low-drop rails, and battery-powered designs where loss matters.
- Common mistakes: selecting by current rating only and ignoring package heat.

## GENERIC_P_CHANNEL_MOSFET_REVERSE_POLARITY

- Part number: generic P-channel MOSFET reverse-polarity circuit.
- Vendor: Generic.
- Family: MOSFET reverse protection.
- Category: `02_POWER`.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/lit/an/slvae57b/slvae57b.pdf.
- Datasheet local path: `Unknown - requires source verification`.
- Package options: SOT-23, SO-8, PowerPAK, DPAK, and others depending on current and heat.
- KiCad symbol candidates: `Device:Q_PMOS_GDS`, `Device:Q_PMOS_SGD`, `Transistor_FET:Q_PMOS_GDS`, related PMOS symbols.
- Common KiCad footprints: `Package_TO_SOT_SMD:SOT-23`, SO-8 and power MOSFET package candidates after part selection.
- Thermal warnings: conduction loss is current squared times on-resistance; check SOA and copper.
- Input/output capacitor warnings: input capacitance and downstream bulk capacitance affect hot-plug and stress.
- Layout warnings: body diode direction, gate-source protection, trace width, and fault current path are critical.
- Use cases: lower-loss reverse-polarity protection than a series diode when verified.
- Avoid cases: high-voltage transients without gate protection or designs requiring controlled ideal-diode behavior.
- Common mistakes: placing source and drain backward or exceeding gate-source voltage.
