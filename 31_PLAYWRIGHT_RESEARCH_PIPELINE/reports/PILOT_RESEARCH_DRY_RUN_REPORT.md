# Pilot Research Dry-Run Report

Generated: 2026-05-03T16:02:56.859Z
Status: `DRY_RUN_ONLY`

## Summary

The pilot target list was planned without live web browsing, without API calls, and without PDF downloads.

- Target CSV: `31_PLAYWRIGHT_RESEARCH_PIPELINE/research_targets/supplier_part_targets.csv`
- Output JSON: `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/pilot_dry_run/research_plan.json`
- Targets planned: 19
- Live web used: `false`
- PDFs downloaded: `false`
- Verification status for every target: `UNVERIFIED`
- Human review required for every target: `true`

## Pilot Targets

| Priority | Vendor | Part | Category | Preferred Sources | Outputs |
| --- | --- | --- | --- | --- | --- |
| high | STMicro | STM32F103C8T6 | microcontroller | stmicro;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | STMicro | STM32F411CEU6 | microcontroller | stmicro;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Espressif | ESP32-S3-WROOM-1 | module | espressif;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Espressif | ESP32-S3-WROOM-1U | module | espressif;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| medium | Microchip | PIC16F877A | microcontroller | microchip;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| medium | Microchip | PIC18F4550 | microcontroller | microchip;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Raspberry Pi | RP2040 | microcontroller | raspberry_pi;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Microchip | MCP2562FD | communication | microchip;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| medium | Texas Instruments | SN65HVD230 | communication | ti;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Diodes Inc | AP63203 | power_regulator | digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| medium | Texas Instruments | LM2596 | power_regulator | ti;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| medium | Advanced Monolithic Systems | AMS1117-3.3 | ldo_regulator | digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Alpha and Omega Semiconductor | AO3401A | pmos | digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Texas Instruments | TPD2EUSB30ADRTR | esd_array | ti;digikey;mouser;kicad_official_libraries | normalized_part;datasheet_link;footprint_candidates |
| high | Generic | USB-C 16-pin receptacle generic | connector | digikey;mouser;jlcpcb;lcsc;kicad_official_libraries | part_candidates;drawing_links;footprint_candidates |
| high | Generic | U.FL connector generic | rf_connector | digikey;mouser;kicad_official_libraries | part_candidates;drawing_links;footprint_candidates |
| high | Generic | SMA connector generic | rf_connector | digikey;mouser;kicad_official_libraries | part_candidates;drawing_links;footprint_candidates |
| medium | Generic | resettable polyfuse generic | protection | digikey;mouser;kicad_official_libraries | part_candidates;datasheet_links;footprint_candidates |
| medium | Generic | TVS diode generic | protection | digikey;mouser;kicad_official_libraries | part_candidates;datasheet_links;footprint_candidates |

## Interpretation

This dry-run proves target routing and report generation only. It does not verify any datasheet, package drawing, supplier stock, price, lifecycle status, KiCad symbol, KiCad footprint, 3D model, or manufacturing decision.

## Next Safe Step

Use official APIs or official manufacturer pages first. Use Playwright live mode only for a small public-page capture after source-profile review and explicit approval.

