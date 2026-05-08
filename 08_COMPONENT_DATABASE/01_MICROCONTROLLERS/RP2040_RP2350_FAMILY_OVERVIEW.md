# RP2040 / RP2350 Family Overview

Date: 2026-05-02

Status: family-level guidance. Exact specifications require Raspberry Pi datasheet, hardware design guide, errata, package drawing, and reference design verification.

## What This Family Is Good For

- Low-cost microcontroller designs with strong community tooling.
- USB devices, sensor/control nodes, small data acquisition, programmable IO workflows, and educational/prototyping products.
- Designs that benefit from PIO-style peripheral flexibility.

## Common Voltage Levels

- Designs commonly use low-voltage digital rails, but exact supply requirements, IO limits, flash voltage, USB VBUS behavior, and regulator needs vary by part and design.
- Exact values require source verification.

## Programming And Debug

- Common workflows include USB bootloader and SWD-style debug/programming paths depending on board design and toolchain.
- Boot and debug behavior depends on support circuitry, external memory, and board wiring.
- Verify programming connector, boot select, reset/run, and debug pins from the exact hardware design guide.

## Clocking Considerations

- External crystal/clock and PLL behavior require exact verification.
- USB timing, flash interface, and PIO-driven timing-sensitive interfaces may impose clock constraints.
- Crystal frequency, load capacitance, and layout need source review.

## Boot Mode Considerations

- Boot mode and external flash behavior are central to bare-chip designs.
- Do not assume a dev board's boot button, flash part, or USB path applies to a custom board.
- Verify boot ROM behavior, boot select pins, flash requirements, and reset/run circuitry.

## USB Considerations

- USB design requires connector, ESD, routing, VBUS handling, and clocking review.
- USB-C needs CC resistors appropriate to the role.
- Verify exact USB recommendations from the hardware design guide.

## RF Considerations

- Bare RP2040/RP2350 parts are not RF MCUs.
- RF appears only through external radios/modules or specific dev boards; those require separate datasheets and RF layout guidance.

## CAN/LIN/UART/I2C/SPI Notes

- UART, I2C, SPI, PWM, PIO-based interfaces, and other serial functions depend on pin mux and firmware design.
- Physical CAN/LIN requires external controllers/transceivers unless a chosen part/reference design explicitly supports the needed function.
- Verify voltage domains, pullups, bus protection, and firmware constraints.

## Typical KiCad Symbol/Footprint Issues

- Bare-chip symbols must be distinguished from Pico-style module/dev-board symbols.
- External flash and boot circuitry are not optional just because a dev board hides them.
- Footprint, exposed pad, and package orientation require exact package drawing review.

## Common External Components

- External flash where required.
- Crystal and load capacitors where required.
- Decoupling capacitors and regulator support.
- USB connector and ESD protection if USB is used.
- Reset/run, boot-select, and debug connector support.

Exact values require source verification.

## Layout Warnings

- Flash routing, USB routing, crystal placement, power decoupling, and exposed-pad treatment must be reviewed.
- Keep noisy regulators away from crystal, USB, analog, or sensitive clock nets.
- Do not copy Pico board geometry unless it matches the custom constraints.

## Power Sequencing Warnings

- Power rails, regulator startup, reset/run behavior, USB VBUS, and external flash availability can affect boot.
- Verify any power-domain or sequencing notes in the exact design guide.

## Dev Board Vs Bare Chip Warnings

- Pico and other boards include flash, power, USB, boot buttons, debug access, connectors, and mechanical assumptions.
- A bare chip design is not just the dev-board pinout copied into a schematic.

## When To Avoid This Family

- When integrated RF is required without an external module.
- When high analog performance, safety certification, or mature industrial ecosystem requirements dominate.
- When external flash or USB boot architecture is unacceptable.

## Datasheets And Reference Manuals Needed

- Exact chip datasheet.
- Hardware design guide.
- Errata.
- Package drawing.
- Reference design and dev board schematic.
- External flash datasheet if used.
- USB connector/protection datasheets if used.

## How Codex Should Verify Before Schematic Use

1. Identify exact chip, package, and intended board architecture.
2. Verify flash, clock, boot, reset/run, USB, debug, and regulator requirements.
3. Resolve KiCad symbol and footprint candidates.
4. Compare pinout and footprint to the datasheet and package drawing.
5. Check reference design differences from the target custom board.
6. Keep all exact values unknown until source evidence is recorded.
