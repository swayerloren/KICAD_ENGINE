# Microchip AVR Master Index

Date: 2026-05-02

Status: official-source link index for AVR ATmega and ATtiny AI-assisted KiCad design. Links are preferred over bundled PDFs for public release.

## Official AVR Sources

| Topic | Official Source | Agent Notes |
| --- | --- | --- |
| AVR product area | https://www.microchip.com/en-us/products/microcontrollers/8-bit-mcus/avr-mcus | Entry point for current AVR families. |
| ATtiny family background | https://www.microchip.com/en-us/about/corporate-overview/acquisitions/atmel/attiny | Family-level ATtiny overview and migration context. |
| ATmega328P product page | https://www.microchip.com/en-us/product/ATMEGA328P | Microchip page marks ATmega328P not recommended for new designs. |
| ATmega328P data sheet | https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061B.pdf | ATmega48A/88A/168A/328/P family data sheet. |
| ATtiny85 product page | https://www.microchip.com/en-us/product/ATTINY85 | Product page for ATtiny85. |
| ATtiny25/45/85 data sheet | https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2586-AVR-8-bit-Microcontroller-ATtiny25-ATtiny45-ATtiny85_Datasheet.pdf | ATtiny85 family data sheet. |
| ATmega32U4 data sheet | https://ww1.microchip.com/downloads/en/devicedoc/atmel-7766-8-bit-avr-atmega16u4-32u4_datasheet.pdf | ATmega16U4/32U4 USB AVR data sheet. |

## Programming And Debug Sources

| Topic | Official Source | Agent Use |
| --- | --- | --- |
| Programmers and debuggers | https://www.microchip.com/en-us/tools-resources/debug/programmers-debuggers | Identify current supported Microchip tools. |
| AVR debugWIRE developer help | https://developerhelp.microchip.com/xwiki/bin/view/software-tools/ides/x/debugging/avr-debugwire/ | Understand reset-pin debugWIRE risks and ISP recovery constraints. |
| AVR UPDI high-voltage activation | https://developerhelp.microchip.com/mplabx%3Aavr-updi-info | For newer AVR UPDI designs; avoid loading the UPDI line. |
| AVR programming adapter guide | https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/UserGuides/AVR-ProgrammingAdapter-UserGuide-DS50003533.pdf | Adapter pin mapping and programming interface reference. |

## AVR KiCad Local Library Findings

Read-only search of installed KiCad 9 stock libraries found:

- `MCU_Microchip_ATmega:ATmega328P-A`
- `MCU_Microchip_ATmega:ATmega328P-M`
- `MCU_Microchip_ATmega:ATmega328P-MM`
- `MCU_Microchip_ATmega:ATmega328P-P`
- `MCU_Microchip_ATtiny:ATtiny85-20M`
- `MCU_Microchip_ATtiny:ATtiny85-20P`
- `MCU_Microchip_ATtiny:ATtiny85-20S`
- `MCU_Microchip_ATmega:ATmega32U4-A`
- `MCU_Microchip_ATmega:ATmega32U4-M`

These are candidates only. Verify package suffix, pinout, reset/programming pins, and footprint before schematic use.

## Agent Handling Rules

- Do not assume Arduino board behavior applies to bare AVR parts.
- For ATmega328P, note lifecycle risk for new designs and verify replacement options if the project is not legacy.
- Preserve ISP pins unless the programming path is intentionally different.
- Treat debugWIRE as risky because it uses the reset pin and can affect recovery.
- For newer UPDI AVRs, keep UPDI clear of heavy loads and high-voltage-sensitive circuitry.
- For ATmega32U4, verify USB clocking, D+/D-, VBUS/UVCC/UCAP behavior, bootloader assumptions, and ESD.

## Current Gaps

- Exact errata and programming specifications are not fully indexed.
- Arduino, Xplained, and third-party dev-board schematics are not curated here yet.
- KiCad candidates have not been pad-by-pad verified.
