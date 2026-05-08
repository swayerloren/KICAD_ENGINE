# Microchip PIC Family Overview

Date: 2026-05-02

Status: family-level guidance. Exact specifications require Microchip datasheet, programming specification, errata, and package drawing verification.

## What This Family Is Good For

- Simple embedded control, legacy product maintenance, low-cost control boards, basic sensor/actuator interfaces, and long-lived industrial-style designs.
- Designs where existing PIC firmware, programmer support, or team familiarity already exists.
- Small deterministic control tasks where a high-end MCU is unnecessary.

## Common Voltage Levels

- PIC families span many voltage ranges and include older 5 V-oriented parts as well as lower-voltage devices.
- IO tolerance, programming voltage, oscillator voltage, analog reference limits, and brownout behavior vary by part.
- Exact values require datasheet verification.

## Programming And Debug

- PIC devices commonly use ICSP-style programming/debug with device-family-specific pin requirements.
- PICkit, ICD, Snap, or other Microchip tools may be used depending on family and device support.
- Programming pins, MCLR behavior, programming voltage, and debug-reserved resources must be checked before schematic use.

## Clocking Considerations

- Internal oscillator, external crystal/resonator, PLL, USB clocking, watchdog, and low-power oscillator options vary.
- USB-capable PIC parts may have stricter clock requirements.
- Verify oscillator circuit, load capacitors, MCLR, and configuration bits for the exact part.

## Boot Mode Considerations

- Bootloader availability is not uniform and often depends on user firmware, device family, or Microchip-provided examples.
- Configuration bits heavily affect clocking, reset, watchdog, brownout, low-voltage programming, and debug behavior.
- Codex must not assume a bootloader exists.

## USB Considerations

- USB support exists only on specific PIC families/parts.
- Verify USB pins, transceiver requirements, VUSB behavior, oscillator requirements, ESD, connector wiring, and firmware support.
- Do not copy a USB reference circuit without matching the exact part and package.

## RF Considerations

- PIC MCUs are generally not integrated RF MCUs.
- RF designs usually require external radios/modules and separate RF layout guidance.
- Keep clock and switching noise away from RF modules and analog sensing circuits.

## CAN/LIN/UART/I2C/SPI Notes

- UART, I2C, SPI, CAN, LIN, and peripheral naming vary across PIC10/12/16/18/24/32/dsPIC families.
- Physical CAN/LIN requires external transceivers.
- Peripheral pin mapping, PPS/remappable pins, and package limitations require exact datasheet review.

## Typical KiCad Symbol/Footprint Issues

- PIC package variants can have different pinouts and footprints under similar part names.
- Symbols may be generic or package-specific; verify pin numbers, power pins, oscillator pins, MCLR, ICSP pins, and alternate functions.
- DIP, SOIC, SSOP, QFN, TQFP, and other package options must not be interchanged.

## Common External Components

- Decoupling capacitors.
- MCLR/reset network when required.
- ICSP/programming connector.
- Crystal/resonator and load capacitors when required.
- USB connector/protection for USB-capable parts.
- CAN/LIN transceivers and protection where applicable.

Exact values require source verification.

## Layout Warnings

- Keep ICSP pins accessible and avoid loading them so programming/debug fails.
- Respect oscillator placement and analog reference/ADC layout when used.
- Watch package pin-1 orientation and legacy through-hole footprint assumptions.

## Power Sequencing Warnings

- MCLR, brownout reset, low-voltage programming, and configuration-bit behavior can affect startup.
- Verify power-up reset timing and programming-voltage constraints from the exact datasheet.

## Dev Board Vs Bare Chip Warnings

- PIC dev boards may include programmer/debug interfaces, jumpers, oscillators, reset circuits, and voltage regulators that are not part of the MCU.
- Do not infer bare-chip schematic requirements from a dev board pinout alone.

## When To Avoid This Family

- When modern high-level tooling, rich RTOS support, integrated radio, or high performance is required.
- When no team/tooling support exists for PIC firmware and programming.
- When exact lifecycle or supply status cannot be verified.

## Datasheets And Reference Manuals Needed

- Exact part datasheet.
- Programming/debug specification.
- Errata.
- Family reference manual if applicable.
- Package drawing.
- USB, oscillator, ADC, CAN, or LIN app notes as needed.
- Dev board schematic only as supporting reference.

## How Codex Should Verify Before Schematic Use

1. Identify exact PIC family, part number, package, and programming tool path.
2. Verify power range, oscillator, reset/MCLR, ICSP pins, and configuration-bit implications.
3. Resolve KiCad symbol/footprint candidates and compare to datasheet pinout/package drawing.
4. Check required external parts and programming connector constraints.
5. Check errata and lifecycle status before promoting the record beyond placeholder.

## 2026-05-02 Research Update

Prompt 11 added official-source indexes and part records for PIC16F877A, PIC16F18346, PIC18F4550, PIC18F25K80, PIC24FJ64GA002, dsPIC33CK256MP506, and a PIC32MX250F128D representative.

Agent-specific additions:

- `06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_PIC/MICROCHIP_PIC_MASTER_INDEX.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/MICROCHIP_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/microchip_part_records.json`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/PIC_ICSP_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/PIC_RESET_OSCILLATOR_RULES.md`

Important handling notes:

- PIC16F877A is a legacy-popular part with newer alternatives called out on the Microchip product page; do not select it for a new design without lifecycle justification.
- PIC16F18346 is a newer low-pin-count PIC16 family member with PPS and integrated peripherals; verify package-specific pins before schematic use.
- PIC18F4550 is a native USB PIC18 class device; USB clock, VUSB/VBUS, connector, ESD, and firmware support must be verified.
- PIC18F25K80 is CAN-oriented; it still requires an external CAN transceiver and termination/protection plan.
- PIC24F, PIC32MX, and dsPIC33 designs require more than 8-bit PIC minimum circuits. Check VCAP/core regulator pins, PPS, oscillator, debug, and package drawings.
