# Microchip AVR Family Overview

Date: 2026-05-02

Status: family-level guidance. Exact specifications require Microchip/Atmel datasheet, programming documentation, errata, and package drawing verification.

## What This Family Is Good For

- Simple 8-bit embedded control, education, low-complexity products, Arduino-compatible workflows, and legacy AVR designs.
- Designs that need straightforward GPIO, timers, ADC, UART, I2C/TWI, SPI, and low firmware complexity.
- Projects where mature examples and simple toolchains are more important than high performance.

## Common Voltage Levels

- AVR parts span different supply-voltage and clock-speed combinations.
- Some common workflows use 5 V or 3.3 V boards, but exact voltage/frequency limits and IO tolerance require datasheet verification.
- Do not assume Arduino board voltage equals bare-chip requirements.

## Programming And Debug

- Common methods include ISP, UPDI, debugWIRE, JTAG, or bootloader-based programming depending on AVR generation.
- Fuse settings can affect clock, reset, bootloader, brownout, and programming access.
- Verify the exact programming interface and required pins before schematic use.

## Clocking Considerations

- Internal oscillator, external crystal/resonator, PLL, and low-power clock options vary.
- Fuse settings can select clock source and divider behavior.
- Verify oscillator circuit, load capacitors, startup time, and maximum frequency versus voltage from the datasheet.

## Boot Mode Considerations

- Bootloader support varies by part and firmware ecosystem.
- Boot reset vector, fuse bits, reset pin configuration, and bootloader memory sections require exact review.
- Codex must not assume Arduino bootloader behavior applies to a bare AVR.

## USB Considerations

- USB support exists only on specific AVR parts or via external USB-UART/USB bridge circuits.
- Verify native USB availability, clocking, connector, ESD, and bootloader support for the exact part.

## RF Considerations

- AVR MCUs generally do not include RF except for specialized radio-integrated families that require their own docs.
- External radios/modules need separate datasheets and RF layout guidance.

## CAN/LIN/UART/I2C/SPI Notes

- UART, TWI/I2C, SPI, timers, ADC, and LIN/CAN capability vary by part.
- Physical CAN/LIN requires external transceiver support and exact peripheral suitability review.
- SPI programming pins can conflict with application circuits if not designed carefully.

## Typical KiCad Symbol/Footprint Issues

- Similar AVR names can exist in DIP, TQFP, QFN, SOIC, and other packages with different pin numbers.
- KiCad symbols may target package families or common variants; verify pin numbers, power pins, oscillator pins, reset, and programming pins.
- Arduino header symbols are not bare AVR symbols.

## Common External Components

- Decoupling capacitors.
- Reset pullup and programming header where required.
- Crystal/resonator and load capacitors if not using internal oscillator.
- USB bridge or USB connector/protection for USB workflows.
- Pullups for I2C/TWI and external transceivers for buses as needed.

Exact values require source verification.

## Layout Warnings

- Keep programming pins accessible and avoid heavy loads that block programming.
- Place crystal components close to oscillator pins if used.
- Keep analog reference and ADC inputs clean when analog performance matters.

## Power Sequencing Warnings

- Brownout, reset timing, fuse settings, and clock startup behavior can affect reliability.
- Verify programming voltage, reset configuration, and fuse lockout risks.

## Dev Board Vs Bare Chip Warnings

- Arduino and AVR dev boards include regulators, USB bridges, bootloaders, reset circuits, crystals, LEDs, and headers.
- Do not copy board assumptions into a bare-chip design without verifying every support circuit.

## When To Avoid This Family

- When high performance, advanced security, integrated wireless, large memory, or modern peripheral density is required.
- When firmware ecosystem support for the chosen exact AVR is weak.
- When package/lifecycle status cannot be verified.

## Datasheets And Reference Manuals Needed

- Exact AVR datasheet.
- Programming/debug documentation.
- Errata.
- Package drawing.
- Fuse/bootloader documentation.
- Dev board schematic only as supporting evidence.

## How Codex Should Verify Before Schematic Use

1. Identify exact AVR part and package.
2. Verify voltage/frequency relationship, clock source, reset, programming interface, and fuses.
3. Resolve KiCad symbol and footprint candidates.
4. Compare pinout and package to the datasheet.
5. Check required support components, bootloader assumptions, and errata.
6. Keep exact values unknown until verified.

## 2026-05-02 Research Update

Prompt 11 added official-source AVR indexes and part records for ATmega328P, ATtiny85, and ATmega32U4.

Agent-specific additions:

- `06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_AVR/MICROCHIP_AVR_MASTER_INDEX.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/MICROCHIP_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/microchip_part_records.json`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/AVR_PROGRAMMING_RULES.md`

Important handling notes:

- ATmega328P is marked by Microchip as not recommended for new designs; treat it as a legacy/Arduino-ecosystem part unless the user explicitly accepts lifecycle risk.
- ATtiny85 programming commonly depends on SPI ISP/debugWIRE-era assumptions; verify reset, fuses, and recovery before reusing small-board circuits.
- ATmega32U4 has native USB; verify USB clocking, D+/D-, VBUS/UVCC/UCAP behavior, bootloader assumptions, and ESD before schematic approval.
- Arduino, Digispark, Leonardo, and other board schematics are not bare-chip proof.
