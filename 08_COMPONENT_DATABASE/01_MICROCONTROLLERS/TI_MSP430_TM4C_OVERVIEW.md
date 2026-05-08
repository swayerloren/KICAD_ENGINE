# TI MSP430 / TM4C Overview

Date: 2026-05-02

Status: family-level guidance. Exact specifications require TI datasheet, family user guide, errata, package drawing, and reference design verification.

## What This Family Is Good For

- MSP430: low-power sensing, simple control, battery-powered devices, and legacy ultra-low-power TI designs.
- TM4C: ARM Cortex-M control, USB, serial interfaces, motor/control-style applications, and designs already tied to TI/Tiva ecosystem.
- Projects where TI examples, evaluation boards, or existing firmware support drive the choice.

## Common Voltage Levels

- MSP430 and TM4C voltage domains differ significantly by family and part.
- Low-power MSP430 designs require careful attention to supply range, IO limits, analog/reference rails, and low-power modes.
- Exact values require datasheet verification.

## Programming And Debug

- MSP430 devices often use TI-specific debug/programming methods such as JTAG or Spy-Bi-Wire depending on part.
- TM4C designs commonly use ARM debug paths such as JTAG/SWD depending on device and board.
- Verify debug pins, reset, bootloader entry, and production programming path for the exact part.

## Clocking Considerations

- MSP430 clocking often centers on low-power oscillators, DCO/internal clocks, and optional crystals.
- TM4C clocking may include PLLs, USB clock requirements, and external crystal options.
- Verify oscillator components, load capacitors, startup behavior, and low-power clock sources.

## Boot Mode Considerations

- Bootloader, BSL, ROM bootloader, or debug-entry behavior varies by family and part.
- Reset pins, boot configuration pins, and firmware protection settings require exact source review.

## USB Considerations

- USB support exists on selected parts only.
- Verify USB pins, VBUS, ESD, clocking, connector wiring, and bootloader interactions from the exact datasheet/reference design.

## RF Considerations

- MSP430 and TM4C are generally not integrated RF MCU families.
- TI wireless companion parts/modules need separate records, datasheets, and RF layout guidance.

## CAN/LIN/UART/I2C/SPI Notes

- UART, I2C, SPI, timers, ADC, CAN, and other interfaces vary by exact part.
- TM4C parts may include richer connectivity, but physical CAN/LIN still requires external transceivers.
- Pin mux and package limitations must be checked.

## Typical KiCad Symbol/Footprint Issues

- MSP430 part suffixes and package variants matter.
- TM4C high-pin-count symbols can be complex and need power/debug/boot pins verified.
- Do not assume LaunchPad header pinouts are bare-chip pinouts.

## Common External Components

- Decoupling capacitors.
- Debug/programming connector.
- Reset/boot support.
- External crystals where needed.
- USB and CAN/LIN transceiver/protection where applicable.
- Analog reference/filtering for precision measurements.

Exact values require source verification.

## Layout Warnings

- Low-power MSP430 designs require leakage-aware layout, clean analog routing, and careful pullup/pulldown choices.
- TM4C USB/CAN/clock circuits require interface-specific routing review.
- Keep debug pins accessible.

## Power Sequencing Warnings

- MSP430 low-power modes, brownout, reset, and wake sources require exact review.
- TM4C USB and peripheral power states may impose constraints.
- Verify any battery, backup, or regulator interactions.

## Dev Board Vs Bare Chip Warnings

- LaunchPads and eval boards include debug probes, regulators, jumpers, crystals, LEDs, and headers.
- Do not copy LaunchPad pin labels directly to a bare-chip schematic.

## When To Avoid This Family

- When integrated RF, modern high-performance ecosystem support, or large memory is required and another MCU is better suited.
- When toolchain or programmer availability is uncertain.
- When exact lifecycle status cannot be verified.

## Datasheets And Reference Manuals Needed

- Exact part datasheet.
- Family user guide or reference manual.
- Errata.
- Package drawing.
- Debug/programming documentation.
- LaunchPad/eval board schematic only as supporting evidence.

## How Codex Should Verify Before Schematic Use

1. Identify exact MSP430 or TM4C part and package.
2. Verify voltage, clocking, reset, boot/programming/debug, low-power requirements, and interfaces.
3. Resolve KiCad symbol and footprint candidates.
4. Compare pinout and land pattern to the datasheet/package drawing.
5. Check errata and lifecycle before design use.
