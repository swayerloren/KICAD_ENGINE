# Level Shifting Rules

Date: 2026-05-02

Status: AI guidance for mixed-voltage digital interfaces. Verify exact translator datasheets before schematic or PCB release.

## Core Rule

Level shifting is interface-specific. A bidirectional auto-direction translator is not a universal fix for every voltage mismatch.

## Identify The Signal Type

Before choosing a translator, classify each signal:

- Open-drain I2C or SMBus.
- Push-pull UART.
- Push-pull SPI.
- Reset, enable, boot, chip-select, or interrupt.
- High-speed clock.
- One-way or bidirectional.
- Weak pullup, strong driver, or externally pulled bus.

## Part Selection Guidance

- Use PCA9306-style translators for I2C/SMBus only when pullups, reference rails, and bus capacitance are verified.
- Use TXS0108E only when the datasheet supports the bus behavior, load, and pullup network.
- Use TXB0108 only for appropriate push-pull signals with light loading; do not assume it works for I2C or heavy capacitive buses.
- For SPI, direction-controlled translators are often safer than auto-direction parts.
- For reset/boot pins, a resistor divider or single-gate translator may be better than an 8-channel auto translator.

## Voltage Domains

- Define side A and side B voltage rails explicitly.
- Check power sequencing and whether either side may be unpowered.
- Check whether pins are overvoltage tolerant when one rail is off.
- Add decoupling near each translator supply pin.
- Tie output-enable pins to a deliberate state.

## Layout Rules

- Place translators near the boundary between voltage domains.
- Keep high-speed SPI and clock traces short.
- Keep I2C pullups close enough for clean rise time but aligned with bus topology.
- Avoid routing translated signals through noisy power regions.
- Label voltage domains in the schematic and PCB where possible.

## Common Mistakes

- Using TXB0108 for I2C.
- Using TXS0108E on a bus with large capacitance or strong pullups without checking the datasheet.
- Forgetting pullups on PCA9306.
- Reversing A-side and B-side rails.
- Leaving OE floating.
- Level-shifting signals that are already compatible.
- Ignoring boot strap timing on MCUs.

## Verification Gate

- Voltage domains are documented.
- Signal direction and drive type are documented.
- Translator datasheet supports the bus.
- Pullups, OE, and decoupling are present.
- Symbol and footprint match the exact package.
- ERC and DRC are run after implementation.
