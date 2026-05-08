# Microchip PIC, dsPIC, And AVR Research Status

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Scope Completed

Created or updated:

- `06_DATASHEETS\01_MICROCONTROLLERS\MICROCHIP_PIC\README.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\MICROCHIP_PIC\MICROCHIP_PIC_MASTER_INDEX.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\MICROCHIP_PIC\SOURCES.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\MICROCHIP_AVR\MICROCHIP_AVR_MASTER_INDEX.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\MICROCHIP_AVR\SOURCES.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\MICROCHIP_PIC_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\MICROCHIP_AVR_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\MICROCHIP_PART_RECORDS.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\microchip_part_records.json`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\MICROCHIP_DEV_BOARD_RECORDS.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\PIC_ICSP_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\PIC_RESET_OSCILLATOR_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\AVR_PROGRAMMING_RULES.md`
- `08_COMPONENT_DATABASE\00_INDEX\MASTER_COMPONENT_INDEX.md`

No datasheet PDFs were downloaded. No tools were installed. No KiCad project source files were edited.

## Completed Families

| Family | Status | Notes |
| --- | --- | --- |
| PIC10 | FAMILY_INDEXED | Family included in PIC master index; no part record requested. |
| PIC12 | FAMILY_INDEXED | Family included in PIC master index; no part record requested. |
| PIC16 | PARTIAL_COMPLETE | PIC16F877A and PIC16F18346 records added with ICSP, MCLR, oscillator, and lifecycle warnings. |
| PIC18 | PARTIAL_COMPLETE | PIC18F4550 and PIC18F25K80 records added with USB and CAN warnings. |
| PIC24 | PARTIAL_PLACEHOLDER | PIC24FJ64GA002 record added; exact local KiCad symbol not found in this pass. |
| PIC32MX | PARTIAL_COMPLETE | PIC32MX250F128D representative record added with local KiCad candidate. |
| dsPIC30 | FAMILY_INDEXED | Legacy DSC family indexed; no part record requested. |
| dsPIC33 | PARTIAL_PLACEHOLDER | dsPIC33CK256MP506 record added; exact local KiCad symbol not found in this pass. |
| AVR ATmega | PARTIAL_COMPLETE | ATmega328P and ATmega32U4 records added with lifecycle, ISP/debug, and USB warnings. |
| AVR ATtiny | PARTIAL_COMPLETE | ATtiny85 record added with ISP/debugWIRE/fuse recovery warnings. |

## Part Records Created

- PIC16F877A
- PIC16F18346
- PIC18F4550
- PIC18F25K80
- PIC24FJ64GA002
- dsPIC33CK256MP506
- PIC32MX250F128D representative
- ATmega328P
- ATtiny85
- ATmega32U4

## Dev Board Records Created

- Curiosity Development Board family
- Curiosity HPC DM164136
- PIC24F Curiosity DM240004
- Explorer 16/32 DM240001-2
- Curiosity PIC32MX470 DM320103
- dsPIC33CK Curiosity/PIM placeholder

## KiCad Library Findings

Read-only KiCad 9 stock library searches found candidate symbols and footprints for PIC16F877A, PIC16F18346, PIC18F4550, PIC18F25K80, PIC32MX250F128D, ATmega328P, ATtiny85, and ATmega32U4.

Exact stock KiCad symbols were not found during this pass for:

- PIC24FJ64GA002
- dsPIC33CK256MP506

All KiCad matches remain candidates only. No pad-by-pad verification was performed.

## Missing Documents Or Follow-Up Sources

- Exact current datasheet URLs for PIC16F877A, PIC18F25K80, PIC24FJ64GA002, and PIC32MX250F128D should be extracted from Microchip product resource tabs.
- Exact errata links should be extracted for every recorded part.
- Exact programming specifications should be extracted for every PIC/PIC24/PIC32/dsPIC record.
- Exact package drawings and land-pattern notes should be mapped to KiCad footprint candidates.
- Curiosity, Explorer, and PIM schematic/CAD/BOM resource files should be indexed by board revision.
- ATmega32U4 product page should be verified directly; this pass used the official data-sheet URL and Microchip AVR context.

## Uncertain Specs

- Exact voltage ranges and voltage/frequency relationships are verification-required.
- Exact oscillator circuits and load capacitor values are verification-required.
- Exact MCLR/reset behavior is verification-required for every PIC-family part.
- Exact AVR fuse defaults, bootloader assumptions, and debugWIRE/UPDI recovery paths are verification-required.
- Exact package suffixes are not approved from KiCad candidate names alone.

## Risk Areas

- Datasheet copyright and public redistribution restrictions.
- False confidence from KiCad symbol names without package drawing review.
- PICkit header or ICSP pin swaps.
- MCLR/VPP reset circuits that block programming.
- AVR fuse settings that lock out normal programming.
- ATmega328P lifecycle risk for new designs.
- PIC/AVR 5 V versus 3.3 V assumptions.
- USB PIC/AVR designs without clock, VBUS, VUSB/UCAP, ESD, and connector review.
- CAN PIC/PIC32/dsPIC designs without an external transceiver and termination/protection plan.
- Copying Curiosity, Explorer, Arduino, or PIM circuits without exact board revision verification.

## Next Research Needed

1. Extract exact Microchip errata and programming specification links for each part.
2. Build pad-by-pad symbol and footprint verification checklists for each KiCad candidate.
3. Add board schematic links for Curiosity HPC, PIC24F Curiosity, Curiosity PIC32MX470, Explorer 16/32, and dsPIC33CK references.
4. Add representative PIC10, PIC12, dsPIC30, and newer AVR UPDI part records if they become target families.
5. Build USB-specific design snippets for PIC18F4550 and ATmega32U4.
6. Build CAN-specific design snippets for PIC18F25K80, PIC32MX, and dsPIC33CK.
