# MCU Boot And Strap Rules

## Purpose

Prevent AI agents from omitting reset, boot, programming, oscillator, and strap requirements.

## Required Checks

- Reset pin circuit.
- Boot mode pins.
- Strap pins and default pull states.
- Programming/debug connector.
- Oscillator or crystal requirements.
- Power sequencing and brownout notes.
- USB/JTAG/SWD/ICSP/UART boot interactions.
- Pins that affect flash voltage, boot source, or RF operation.

## Source Requirements

Use datasheets, reference manuals, hardware design guides, and vendor reference schematics. Family-level notes may guide review, but exact pins and values require exact part/package source verification.

## AI Warnings

- Do not assume ESP32, STM32, PIC, AVR, RP2040, Nordic, or WCH boot pins are interchangeable.
- Do not connect strap pins to external circuitry that fights required boot states.
- Do not omit programming connector pins because firmware can be loaded another way.

## Exit Criteria

Every MCU or module must have `BOOT_STRAP_REVIEWED` or `BOOT_STRAP_HUMAN_REVIEW_REQUIRED`.
