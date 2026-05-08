# Microchip PIC Master Index

Date: 2026-05-02

Status: official-source link index for AI-assisted KiCad design. Links are preferred over bundled PDFs for public release.

## Official Family Pages

| Family | Official Source | Agent Notes |
| --- | --- | --- |
| PIC10 | https://www.microchip.com/en-us/products/microcontrollers/8-bit-mcus/pic-mcus | Small 8-bit PIC family; exact part, package, MCLR, and programming requirements must be checked. |
| PIC12 | https://www.microchip.com/en-us/products/microcontrollers/8-bit-mcus/pic-mcus | Low-pin-count 8-bit PIC family; programming pins are often shared with application pins. |
| PIC16 | https://www.microchip.com/en-us/products/microcontrollers/8-bit-mcus/pic-mcus | Broad 8-bit family; enhanced mid-range parts can differ sharply from legacy PIC16 parts. |
| PIC18 | https://www.microchip.com/en-us/products/microcontrollers/8-bit-mcus/pic-mcus | Higher-end 8-bit family; USB, CAN, PPS, and voltage behavior are part-specific. |
| PIC24 | https://www.microchip.com/en-us/products/microcontrollers/16-bit-mcus/pic24f-ga | 16-bit PIC family; PPS, low power, and package-specific peripherals require exact review. |
| PIC32MX | https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/32-bit-mcus/pic32-32-bit-mcus/pic32mx | MIPS32-based PIC32 family; USB, CAN, Ethernet, PPS, and Harmony support vary by series. |
| dsPIC30 | https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/dspic-dscs | Legacy digital signal controller family; use only after lifecycle and tool support review. |
| dsPIC33 | https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/dspic-dscs/dspic33c/dspic33ck-single-core-dsc | Motor-control, digital power, and DSP-oriented controllers; PWM, analog, CAN FD, and power layout need care. |

## Product Pages Used In This Pass

| Record | Official Product Source | Data Sheet Source Used |
| --- | --- | --- |
| PIC16F877A | https://www.microchip.com/en-us/product/PIC16F877A | Product page lists `PIC16F87XA Datasheet`; direct PDF not extracted in this pass. |
| PIC16F18346 | https://www.microchip.com/en-us/product/PIC16F18346 | https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/PIC16%28L%29F18326-18346-Data-Sheet-40001839F.pdf |
| PIC18F4550 | https://www.microchip.com/en-us/product/PIC18F4550 | https://ww1.microchip.com/downloads/en/DeviceDoc/PIC18F4550%20advanced%20datasheet%20-%2039632a.pdf |
| PIC18F25K80 | https://www.microchip.com/en-us/product/PIC18F25K80 | Product page only; direct current data-sheet URL not extracted in this pass. |
| PIC24FJ64GA002 | https://www.microchip.com/en-us/product/PIC24FJ64GA002 | Product page only; direct current data-sheet URL not extracted in this pass. |
| dsPIC33CK256MP506 | https://www.microchip.com/en-us/product/dsPIC33CK256MP506 | https://ww1.microchip.com/downloads/aemDocuments/documents/MCU16/ProductDocuments/DataSheets/dsPIC33CK256MP508-Family-Data-Sheet-DS70005349H.pdf |
| PIC32MX250F128D representative | https://www.microchip.com/en-us/product/PIC32MX250F128D | Product page lists `PIC32MX1XX/2XX Family Data Sheet`; direct current data-sheet URL not extracted in this pass. |

## Programming And Debug Sources

| Topic | Official Source | Agent Use |
| --- | --- | --- |
| Programmers and debuggers | https://www.microchip.com/en-us/tools-resources/debug/programmers-debuggers | Identify current PICkit, ICD, ICE, Snap, Atmel-ICE, and Power Debugger families. |
| PICkit 5 user guide | https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/UserGuides/MPLAB-PICkit-5-In-Circuit-Debugger-User-Guide-DS50003525.pdf | Read before assigning PICkit connector pins, target power behavior, or programming mode assumptions. |
| PICkit 5 quick-start guide | https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/Brochures/MPLAB-PICkit-5-In-Circuit-Debugger-Quick-Start-Guide-50003478.pdf | Quick hardware orientation only. |
| PIC16F180XX programming example | https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/ProgrammingSpecifications/PIC16F180XX-Family-Programming-Specification-40002317.pdf | Example of family-specific ICSPDAT/ICSPCLK/MCLR behavior; do not generalize without exact part spec. |

## Development Board Sources

| Board / Platform | Official Source | Agent Use |
| --- | --- | --- |
| Curiosity boards | https://www.microchip.com/en-us/tools-resources/evaluation-boards/curiosity | Broad board-family entry point for 8-, 16-, and 32-bit Microchip dev boards. |
| Curiosity HPC | https://www.microchip.com/en-us/development-tool/DM164136 | 8-bit PIC board with integrated programmer/debugger; reference only. |
| Curiosity PIC32MX470 | https://www.microchip.com/en-us/development-tool/DM320103 | PIC32MX board reference for USB/audio/Bluetooth-style prototyping; not package proof for other PIC32MX parts. |
| PIC24F Curiosity | https://www.microchip.com/en-us/development-tool/DM240004 | PIC24F dev-board reference; separate board support circuits from bare-chip minimum circuit. |
| Explorer 16/32 | https://www.microchip.com/en-us/development-tool/DM240001-2 | Modular 16-/32-bit PIC24, dsPIC33, and PIC32 platform using PIMs; use exact PIM source before copying pinout. |
| Explorer 16/32 developer help | https://developerhelp.microchip.com/xwiki/bin/view/software-tools/mcu-dev-boards/exp16-32/ | Board guide with schematic/BOM source section. |

## KiCad Local Library Findings

Read-only search of the installed KiCad 9 stock libraries found Microchip PIC16, PIC18, PIC32, ATmega, and ATtiny symbols. It did not find exact local stock symbols for `PIC24FJ64GA002` or `dsPIC33CK256MP506` in this pass.

## Agent Handling Rules

- Start from the exact order code, not only family name.
- Check `F`, `LF`, speed, temperature, package, and memory suffixes.
- Verify ICSP pins, MCLR/VPP behavior, low-voltage programming, and debug-reserved resources.
- For USB PICs, verify VUSB/VBUS behavior, oscillator requirements, ESD, connector wiring, and firmware stack support.
- For CAN PICs, add a transceiver, termination strategy, and bus protection; MCU CAN pins alone are not a CAN physical interface.
- Treat Curiosity, Explorer, and PIM schematics as references only.

## Current Gaps

- Exact current datasheet URLs for PIC16F877A, PIC18F25K80, PIC24FJ64GA002, and PIC32MX250F128D should be extracted from Microchip resource tabs in a future pass.
- Exact errata and programming specifications are not fully indexed.
- KiCad candidates have not been pad-by-pad verified.
- Package drawings and land patterns still require datasheet review.
