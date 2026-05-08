# Microchip PIC, dsPIC, And AVR Part Records

Date: 2026-05-02

Status: partial official-source records for AI-assisted KiCad planning. These records are not design-approved until the exact datasheet, errata, programming specification, package drawing, KiCad symbol, and footprint are checked together.

## Record Status Language

- `VERIFIED_FROM_DATASHEET`: A document or product page link was identified from official Microchip sources.
- `VERIFIED_FROM_KICAD_LIBRARY`: A candidate symbol or footprint name was found by read-only search in the installed KiCad 9 stock libraries.
- `UNVERIFIED_PLACEHOLDER`: Exact pinout, electrical limits, package drawing, errata, or layout details still require verification.

## Common Source Set

- PIC master index: `06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_PIC/MICROCHIP_PIC_MASTER_INDEX.md`
- AVR master index: `06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_AVR/MICROCHIP_AVR_MASTER_INDEX.md`
- Microchip programmers/debuggers: https://www.microchip.com/en-us/tools-resources/debug/programmers-debuggers
- PICkit 5 user guide: https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/UserGuides/MPLAB-PICkit-5-In-Circuit-Debugger-User-Guide-DS50003525.pdf
- AVR debugWIRE help: https://developerhelp.microchip.com/xwiki/bin/view/software-tools/ides/x/debugging/avr-debugwire/
- AVR UPDI help: https://developerhelp.microchip.com/mplabx%3Aavr-updi-info

## PIC16F877A

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_PIC16F877A` |
| Vendor | Microchip |
| Family | PIC16 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/PIC16F877A ; product page lists `PIC16F87XA Datasheet` and newer device `PIC16F18877`. |
| KiCad symbol candidates | `MCU_Microchip_PIC16:PIC16F877A-IP`, `MCU_Microchip_PIC16:PIC16F877A-IPT` |
| KiCad footprint candidates | `Package_QFP:TQFP-44_10x10mm_P0.8mm` from KiCad IPT symbol; `Package_DIP:DIP-40_W15.24mm` is a likely DIP candidate but must be checked against the exact package drawing because the local IP symbol has an empty footprint property. |
| Programming/debug notes | Use exact PIC16F87XA programming specification before placing ICSP. Verify MCLR/VPP, PGC, PGD, VDD, VSS, and target-voltage behavior. |
| Voltage notes | Older PIC16 designs are often 5 V oriented, but exact operating range and IO rules require datasheet verification. |
| Oscillator notes | Verify external crystal/resonator or internal oscillator options and configuration bits from the datasheet. |
| Reset/MCLR notes | MCLR/VPP must remain compatible with programming voltage and reset circuit. Do not over-capacitive-load MCLR. |
| Common mistakes | Treating legacy hobby circuits as production proof; confusing 40-pin DIP and 44-pin TQFP pinouts; omitting ICSP access; ignoring newer-device recommendation. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## PIC16F18346

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_PIC16F18346` |
| Vendor | Microchip |
| Family | PIC16 enhanced mid-range |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/PIC16F18346 ; datasheet: https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/PIC16%28L%29F18326-18346-Data-Sheet-40001839F.pdf |
| KiCad symbol candidates | `MCU_Microchip_PIC16:PIC16F18346-GZ`, `MCU_Microchip_PIC16:PIC16F18346-P`, `MCU_Microchip_PIC16:PIC16F18346-SO`, `MCU_Microchip_PIC16:PIC16F18346-SS_0` |
| KiCad footprint candidates | `Package_DFN_QFN:UQFN-20-1EP_4x4mm_P0.5mm_EP2.8x2.8mm`, `Package_DIP:DIP-20_W7.62mm`, `Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm`, `Package_SO:SSOP-20_5.3x7.2mm_P0.65mm` from local KiCad symbols. |
| Programming/debug notes | Verify ICSP pins, MCLR/VPP mode, low-voltage programming, and debug support for the exact package. |
| Voltage notes | Exact F/LF voltage range and oscillator speed relationship require datasheet verification. |
| Oscillator notes | Official page highlights internal oscillator capability; exact frequency, tolerance, and clock configuration require datasheet verification. |
| Reset/MCLR notes | MCLR may interact with programming and configuration bits; keep recovery path accessible. |
| Common mistakes | Ignoring PPS remap constraints; assuming PIC16F877A-era circuits apply; choosing a package suffix without matching the KiCad symbol. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## PIC18F4550

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_PIC18F4550` |
| Vendor | Microchip |
| Family | PIC18 USB |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/PIC18F4550 ; datasheet link observed: https://ww1.microchip.com/downloads/en/DeviceDoc/PIC18F4550%20advanced%20datasheet%20-%2039632a.pdf |
| KiCad symbol candidates | `MCU_Microchip_PIC18:PIC18F4550-IML`, `MCU_Microchip_PIC18:PIC18F4550-IP`, `MCU_Microchip_PIC18:PIC18F4550-IPT` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm`, `Package_DIP:DIP-40_W15.24mm`, `Package_QFP:TQFP-44_10x10mm_P0.8mm` from local KiCad symbols. |
| Programming/debug notes | Verify ICSP, debug support, and USB bootloader assumptions separately. Do not assume USB programming exists. |
| Voltage notes | Exact supply, VUSB, VBUS, and IO limits require datasheet verification. |
| Oscillator notes | USB clocking must be verified from the datasheet; external clock/crystal choices are not optional assumptions. |
| Reset/MCLR notes | Preserve MCLR/VPP and ICSP compatibility while adding reset and USB support circuits. |
| Common mistakes | Copying old USB circuits without VUSB/VBUS review; omitting ESD; assuming 5 V USB and MCU rails are automatically compatible; swapping D+ and D-. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## PIC18F25K80

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_PIC18F25K80` |
| Vendor | Microchip |
| Family | PIC18 CAN-oriented |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/PIC18F25K80 ; direct current datasheet URL not extracted in this pass. |
| KiCad symbol candidates | `MCU_Microchip_PIC18:PIC18F25K80_IML`, `MCU_Microchip_PIC18:PIC18F25K80_ISS` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-28-1EP_6x6mm_P0.65mm_EP4.25x4.25mm`, `Package_SO:SSOP-28_5.3x10.2mm_P0.65mm` from local KiCad symbols. |
| Programming/debug notes | Verify ICSP pin locations for IML/ISS packages and preserve programming access. |
| Voltage notes | Exact operating range and CAN peripheral voltage behavior require datasheet verification. |
| Oscillator notes | CAN timing depends on oscillator tolerance and configuration. Verify before selecting crystal or internal oscillator. |
| Reset/MCLR notes | Keep MCLR/VPP compatible with programming and reset supervision. |
| Common mistakes | Connecting CAN pins directly to a connector; omitting a CAN transceiver, termination, common-mode, and protection review; confusing K80 package variants. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## PIC24FJ64GA002

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_PIC24FJ64GA002` |
| Vendor | Microchip |
| Family | PIC24F |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/PIC24FJ64GA002 ; PIC24F GA family page: https://www.microchip.com/en-us/products/microcontrollers/16-bit-mcus/pic24f-ga |
| KiCad symbol candidates | Unknown - requires source verification. Exact stock KiCad symbol was not found in `MCU_Microchip_PIC24.kicad_sym` during this pass. |
| KiCad footprint candidates | Unknown - requires source verification. |
| Programming/debug notes | Verify PIC24 ICSP/debug pins, PGC/PGD pair selection, MCLR, and any device-specific debug resources. |
| Voltage notes | Exact supply range, 5 V tolerance, analog rails, and regulator/core pins require datasheet verification. |
| Oscillator notes | Verify oscillator source, PLL, low-power oscillator, and PPS-related pin choices from the datasheet. |
| Reset/MCLR notes | MCLR/reset and ICSP must be reviewed with the exact PIC24 programming spec. |
| Common mistakes | Treating PIC24 as an 8-bit PIC with more pins; ignoring PPS; assuming a PIM or Explorer board pinout is the bare part pinout. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `UNVERIFIED_PLACEHOLDER` |

## dsPIC33CK256MP506

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_DSPIC33CK256MP506` |
| Vendor | Microchip |
| Family | dsPIC33CK |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/dsPIC33CK256MP506 ; family data sheet: https://ww1.microchip.com/downloads/aemDocuments/documents/MCU16/ProductDocuments/DataSheets/dsPIC33CK256MP508-Family-Data-Sheet-DS70005349H.pdf |
| KiCad symbol candidates | Unknown - requires source verification. Exact stock KiCad symbol was not found in `DSP_Microchip_DSPIC33.kicad_sym` during this pass. |
| KiCad footprint candidates | Unknown - requires source verification. |
| Programming/debug notes | Verify ICSP/debug support, PGC/PGD pair, MCLR, and dsPIC33CK programming specification before schematic use. |
| Voltage notes | Exact VDD, AVDD, VCAP/core regulator, high-speed analog, and motor-control power-domain requirements require source verification. |
| Oscillator notes | High-performance PWM, ADC, CAN FD, and digital power loops require a verified clock plan. |
| Reset/MCLR notes | Verify reset supervisor, MCLR/VPP, brownout, watchdog, and debug behavior from official docs. |
| Common mistakes | Routing motor-control or digital-power signals without analog/power layout review; treating PIM schematics as production proof; omitting CAN FD transceiver for FDCAN/CAN FD use. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `UNVERIFIED_PLACEHOLDER` |

## PIC32MX250F128D Representative

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_PIC32MX_REPRESENTATIVE_PIC32MX250F128D` |
| Vendor | Microchip |
| Family | PIC32MX |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/PIC32MX250F128D ; PIC32MX family page: https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/32-bit-mcus/pic32-32-bit-mcus/pic32mx |
| KiCad symbol candidates | `MCU_Microchip_PIC32:PIC32MX250F128D-IPT` |
| KiCad footprint candidates | `Package_QFP:TQFP-44_10x10mm_P0.8mm` from local KiCad symbol. |
| Programming/debug notes | Verify PIC32 ICSP, MCLR, PGC/PGD, JTAG/SWD-equivalent Microchip debug interfaces, and Harmony/toolchain support. |
| Voltage notes | Exact 3.3 V requirements, 5 V tolerance, VCAP/core regulator, USB supply, and analog rails require datasheet verification. |
| Oscillator notes | USB and timing-sensitive peripherals need a verified crystal/PLL plan. |
| Reset/MCLR notes | Preserve MCLR and programming/debug pins; verify reset timing and VCAP requirements. |
| Common mistakes | Treating PIC32 like an 8-bit PIC; missing VCAP; assuming 5 V IO; copying PIC32MX470 Curiosity circuits to a different package. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## ATmega328P

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_ATMEGA328P` |
| Vendor | Microchip |
| Family | AVR ATmega |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/ATMEGA328P ; datasheet: https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061B.pdf |
| KiCad symbol candidates | `MCU_Microchip_ATmega:ATmega328P-A`, `MCU_Microchip_ATmega:ATmega328P-M`, `MCU_Microchip_ATmega:ATmega328P-MM`, `MCU_Microchip_ATmega:ATmega328P-P` |
| KiCad footprint candidates | `Package_QFP:TQFP-32_7x7mm_P0.8mm`, `Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm`, `Package_DFN_QFN:QFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm`, `Package_DIP:DIP-28_W7.62mm` from local KiCad symbols. |
| Programming/debug notes | Commonly ISP/debugWIRE era; preserve MOSI/MISO/SCK/RESET/VCC/GND and verify fuses. |
| Voltage notes | Voltage/frequency relationship and IO limits require datasheet verification; Microchip product page marks this part not recommended for new designs. |
| Oscillator notes | Verify internal oscillator, crystal, resonator, clock fuse, CKDIV8, startup time, and bootloader assumptions. |
| Reset/MCLR notes | AVR reset pin is not PIC MCLR; preserve reset for ISP/debugWIRE recovery unless intentionally disabled. |
| Common mistakes | Assuming Arduino Uno circuitry and bootloader apply to a bare chip; changing fuses blindly; using 5 V shields with 3.3 V designs. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## ATtiny85

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_ATTINY85` |
| Vendor | Microchip |
| Family | AVR ATtiny |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Product page: https://www.microchip.com/en-us/product/ATTINY85 ; datasheet: https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2586-AVR-8-bit-Microcontroller-ATtiny25-ATtiny45-ATtiny85_Datasheet.pdf |
| KiCad symbol candidates | `MCU_Microchip_ATtiny:ATtiny85-20M`, `MCU_Microchip_ATtiny:ATtiny85-20P`, `MCU_Microchip_ATtiny:ATtiny85-20S` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm`, `Package_DIP:DIP-8_W7.62mm`, `Package_SO:SOIC-8_5.3x5.3mm_P1.27mm` from local KiCad symbols. |
| Programming/debug notes | Verify SPI ISP and debugWIRE behavior. Small-pin-count loading on programming pins can block recovery. |
| Voltage notes | Exact voltage/frequency limits require datasheet verification. |
| Oscillator notes | Internal oscillator and fuse settings are common sources of bring-up errors; verify calibration and clock source. |
| Reset/MCLR notes | Reset is not PIC MCLR. Do not disable reset via fuse unless high-voltage recovery path is available. |
| Common mistakes | Copying Digispark/Arduino-derived circuits without USB/bootloader proof; overloading reset or SPI pins; setting fuses without recovery. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## ATmega32U4

| Field | Value |
| --- | --- |
| Record ID | `MICROCHIP_ATMEGA32U4` |
| Vendor | Microchip |
| Family | AVR ATmega USB |
| Category | `01_MICROCONTROLLERS` |
| Source documents | Datasheet: https://ww1.microchip.com/downloads/en/devicedoc/atmel-7766-8-bit-avr-atmega16u4-32u4_datasheet.pdf ; product page should be verified before final use. |
| KiCad symbol candidates | `MCU_Microchip_ATmega:ATmega32U4-A`, `MCU_Microchip_ATmega:ATmega32U4-M` |
| KiCad footprint candidates | `Package_QFP:TQFP-44_10x10mm_P0.8mm`, `Package_DFN_QFN:QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm` from local KiCad symbols. |
| Programming/debug notes | Verify ISP/JTAG/bootloader support for the exact package and intended workflow. |
| Voltage notes | Exact USB, core, IO, and regulator-related pins require datasheet verification. |
| Oscillator notes | Native USB designs require verified clocking; do not assume Arduino Leonardo circuitry is sufficient. |
| Reset/MCLR notes | AVR reset and bootloader entry must be explicit; preserve programming recovery. |
| Common mistakes | Omitting UCAP/USB support parts, ESD, VBUS handling, or bootloader path; copying Leonardo/Micro board assumptions into a bare-chip product. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |
