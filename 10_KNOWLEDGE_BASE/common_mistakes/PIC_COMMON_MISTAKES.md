# PIC Common Mistakes

Status: `AI_GUIDANCE_ONLY`

## Purpose

Capture recurring Microchip PIC design mistakes so agents do not create PIC schematics from memory.

## Common Schematic Mistakes

- Treating PIC10, PIC12, PIC16, PIC18, PIC24, PIC32, dsPIC30, and dsPIC33 families as interchangeable.
- Choosing a symbol before checking the exact package-specific pinout.
- Omitting or miswiring MCLR/reset circuitry.
- Omitting ICSP programming/debug header requirements.
- Assuming oscillator requirements from a different PIC family or board.
- Forgetting that some PIC designs are 5 V while others are 3.3 V or lower-voltage only.
- Assuming USB-capable PICs need only D+ and D- without clock, USB power, ESD, connector, and power review.
- Assuming CAN-capable PICs remove the need for a CAN transceiver, termination, protection, and bus connector review.

## Common PCB Mistakes

- Assigning a footprint from package name alone.
- Swapping programming pins or making the programming header inaccessible.
- Placing crystal or resonator components without checking the oscillator section of the datasheet.
- Routing reset/programming/debug lines through noisy regions without review.
- Ignoring decoupling placement at every power pin.

## AI Agent Checks

- Verify exact part number and package suffix.
- Read the datasheet pinout table for that package.
- Check MCLR/reset behavior and programming/debug requirements.
- Check oscillator mode and external component requirements.
- Check voltage domains before connecting to USB, CAN, LIN, UART, I2C, or SPI interfaces.
- Mark all package, pinout, footprint, and voltage details `UNVERIFIED` until sourced.

## Required Human Review

Human review is required for package selection, MCLR/reset strategy, programming/debug header pinout, oscillator design, USB/CAN variants, and any voltage-domain crossing.

