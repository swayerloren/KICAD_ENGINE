# Power Component Research Status

Date: 2026-05-02

Task: Build a serious AI-readable database for common PCB power parts.

## Completed

- Created `06_DATASHEETS/03_POWER/POWER_MASTER_INDEX.md`.
- Created `08_COMPONENT_DATABASE/02_POWER/POWER_COMPONENT_GUIDE.md`.
- Created `08_COMPONENT_DATABASE/02_POWER/POWER_PART_RECORDS.md`.
- Created `08_COMPONENT_DATABASE/02_POWER/power_part_records.json`.
- Created power design-rule snippets:
  - `POWER_INPUT_PROTECTION_RULES.md`
  - `USB_5V_TO_3V3_RULES.md`
  - `AUTOMOTIVE_12V_POWER_RULES.md`
- Created `08_COMPONENT_DATABASE/14_PART_SELECTION_GUIDES/REGULATOR_SELECTION_GUIDE.md`.
- Updated `06_DATASHEETS/03_POWER/SOURCES.md`.
- Added power records to `08_COMPONENT_DATABASE/00_INDEX/MASTER_COMPONENT_INDEX.md`.

## Researched Source Links

- Texas Instruments LM2596: https://www.ti.com/product/LM2596
- Monolithic Power Systems MP1584: https://www.monolithicpower.com/en/products/mp1584.html
- Diodes Incorporated AP2112: https://www.diodes.com/part/view/AP2112?BackID=9304
- Microchip MCP1700: https://www.microchip.com/en-us/product/MCP1700
- Texas Instruments TLV755P: https://www.ti.com/product/TLV755P
- Microchip MIC5504: https://www.microchip.com/en-us/product/MIC5504
- Texas Instruments TPS5430: https://www.ti.com/product/TPS5430
- Texas Instruments TPS62177: https://www.ti.com/product/TPS62177
- Microchip MCP73831: https://www.microchip.com/en-us/product/MCP73831
- Texas Instruments eFuse/hot-swap family: https://www.ti.com/power-management/power-switches/efuse-hotswap-controllers/overview.html
- Texas Instruments ideal diode controllers: https://www.ti.com/power-management/power-switches/ideal-diodes-oring-controllers/overview.html
- Littelfuse PolySwitch resettable PTC family: https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-ptc-devices
- Littelfuse SMAJ TVS family: https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/surface-mount/smaj
- Texas Instruments USB ESD and surge protection application note: https://www.ti.com/lit/pdf/slvaf82
- Texas Instruments automotive battery input protection reference design: https://www.ti.com/tool/TIDA-01167

## Local KiCad Library Evidence

Read-only local KiCad 9 library searches found candidate symbols for:

- LM2596 variants.
- TPS5430DDA.
- TPS62177DQC.
- AMS1117 variants.
- AP2112K-3.3.
- MCP1700 variants.
- TLV755 variants.
- MIC5504-3.3YM5.
- MCP73831 variants.
- TP4056-42-ESOP8.
- Generic polyfuse, TVS, Schottky diode, and PMOS protection symbols.

These are candidate names only, not verified symbol-to-footprint approvals.

## Known Weaknesses

- TP4056 official manufacturer/source status remains unresolved.
- AMS1117-3.3 vendor-specific source status remains unresolved because the part name is widely cloned.
- MP1584 has a lifecycle warning from the MPS product page and should not be promoted for new designs without user approval.
- No specific boost regulator record exists yet.
- No specific eFuse record exists yet.
- No specific ideal-diode controller record exists yet.
- Automotive rules are guidance only and do not establish automotive qualification.

## Next Research Needed

- Add source-verified boost regulators and buck-boost regulators.
- Add specific USB-C protection ICs and eFuses.
- Add ideal-diode controller records.
- Add automotive-qualified buck and surge-protection records.
- Add exact footprint checks against datasheet package drawings for any part selected in an active KiCad project.
- Add thermal calculation templates for LDOs, bucks, chargers, fuses, TVS diodes, and reverse-protection MOSFETs.

## Validation

- `08_COMPONENT_DATABASE/02_POWER/power_part_records.json` parsed successfully with 16 records.
- Requested files were present after creation.
- ASCII check passed for created and updated files.
- No protected KiCad design files under `04_KICAD_PROJECTS` were modified during this documentation task.
