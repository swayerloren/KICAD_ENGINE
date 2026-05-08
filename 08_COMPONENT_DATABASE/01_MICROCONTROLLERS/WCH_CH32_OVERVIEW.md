# WCH CH32 Overview

Date: 2026-05-02

Status: family-level guidance. Exact specifications require WCH datasheet, reference manual, programming/debug documentation, errata, package drawing, and reference design verification.

## What This Family Is Good For

- Low-cost embedded control where WCH tooling and supply chain are acceptable.
- USB-focused or peripheral-rich low-cost designs depending on exact CH32 family member.
- Projects where cost pressure is high and the engineering team can tolerate extra verification effort.

## Common Voltage Levels

- CH32 devices vary by family and part.
- Many designs use low-voltage MCU rails, but exact supply range, IO tolerance, USB voltage behavior, and analog limits require datasheet verification.
- Do not assume compatibility with STM32 or other ARM/RISC-V families from naming or package similarity.

## Programming And Debug

- Programming/debug methods vary by CH32 family and core architecture.
- WCH-Link or family-specific bootloader/debug flows may be required.
- Verify SWD, single-wire, USB bootloader, UART bootloader, or other programming paths for the exact part before schematic use.

## Clocking Considerations

- Internal/external clocks, USB clock accuracy, PLL behavior, and low-speed clock options vary.
- USB-capable designs require exact clocking review.
- Crystal/load capacitor values and oscillator routing require source verification.

## Boot Mode Considerations

- Boot pins, bootloader modes, reset behavior, option bytes/configuration bits, and debug lock behavior vary.
- Do not assume STM32-style BOOT behavior or pin compatibility.

## USB Considerations

- USB support is common in some CH32 parts but varies by exact device.
- Verify D+/D-, VBUS, ESD, USB-C CC wiring, clocking, bootloader use, and firmware support.

## RF Considerations

- CH32 MCUs are generally not integrated RF devices.
- External radios/modules require separate RF documents and layout guidance.

## CAN/LIN/UART/I2C/SPI Notes

- UART, I2C, SPI, CAN, USB, timers, ADC, and other interfaces vary by exact family member.
- Physical CAN/LIN requires external transceivers and protection.
- Verify peripheral availability, remapping, voltage domains, and package pinout.

## Typical KiCad Symbol/Footprint Issues

- KiCad stock library support may be incomplete or variant-sensitive.
- Similar package names do not prove pin compatibility with STM32 or other MCUs.
- Symbols and footprints may need project-local verification or creation after datasheet review.

## Common External Components

- Decoupling capacitors.
- Programming/debug connector.
- Reset and boot circuitry.
- Crystal/load capacitors where needed.
- USB connector/protection if USB is used.
- CAN/LIN transceiver and protection where applicable.

Exact values require source verification.

## Layout Warnings

- Treat every footprint and pinout as unverified until checked.
- USB, crystal, analog, and high-speed traces require source guidance.
- Avoid assuming reference layouts from other MCU families apply.

## Power Sequencing Warnings

- Reset, bootloader entry, USB power, low-power modes, and debug lock behavior require exact review.
- Verify power-up and brownout behavior before relying on the device in production.

## Dev Board Vs Bare Chip Warnings

- CH32 dev boards may include WCH-Link interfaces, USB circuitry, regulators, boot buttons, oscillators, and example-specific circuits.
- Do not copy a dev board schematic without matching the exact part/package and source documents.

## When To Avoid This Family

- When documentation clarity, long-term lifecycle certainty, broad library support, or conservative production risk is more important than cost.
- When the team cannot validate toolchain, programming, debug, and KiCad library support.
- When a pin-compatible assumption is the only reason for choosing the part.

## Datasheets And Reference Manuals Needed

- Exact part datasheet.
- Reference manual.
- Programming/debug documentation.
- Errata if available.
- Package drawing.
- Eval board schematic and WCH application notes as supporting references.

## How Codex Should Verify Before Schematic Use

1. Identify exact CH32 part, core family, package, and intended programming/debug tool.
2. Verify voltage, boot, reset, clocking, USB, debug, and peripheral availability.
3. Resolve or create KiCad symbol/footprint candidates only after source review.
4. Compare pinout and package drawing manually.
5. Treat STM32-like assumptions as unsafe unless source documents prove compatibility.
