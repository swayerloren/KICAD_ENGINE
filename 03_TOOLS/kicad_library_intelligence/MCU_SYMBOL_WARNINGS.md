# MCU Symbol Warnings

Date: 2026-05-02

Purpose: warn agents about MCU symbol selection problems in KiCad.

## General MCU Risks

- Exact ordering codes map to package, flash size, temperature grade, peripheral set, and sometimes pinout differences.
- KiCad symbols often use wildcard suffixes such as `x`; agents must map these back to the exact datasheet ordering code.
- Alternate functions are not full pinout verification.
- Hidden power pins and multi-unit symbols can hide ERC mistakes.
- Boot/debug/reset/clock pins must be checked against the target circuit.

## STM32 Example

The generated sample search for `STM32F103C8T6` finds symbol candidates such as:

- `MCU_ST_STM32F1:STM32F103C8Tx`
- `MCU_ST_STM32F1:STM32F103CBTx`

These are candidates only. The exact STM32 ordering code must be checked against the ST datasheet and package drawing before selecting a footprint.

## ESP32 Example

The generated sample search for `ESP32-S3-WROOM-1` finds:

- `RF_Module:ESP32-S3-WROOM-1`
- related ESP32-S3 and WROOM module candidates

The module symbol and footprint still require Espressif module datasheet verification, especially pad numbering, keepout, antenna area, EN/reset, boot straps, power pins, USB pins, and module variant.

## Microchip CAN Example

The generated sample search for `MCP2562FD` finds MCP2562-family symbol candidates but no exact `MCP2562FD` symbol in the sample output. Agents must not substitute MCP2562 symbols for FD variants without datasheet pinout and package verification.

## Required MCU Checks

- Pin count and package.
- Power pins and analog power pins.
- Ground pins and exposed pad if present.
- Reset, boot, strap, and programming/debug pins.
- Oscillator pins and clock source requirements.
- USB, CAN, RF, or high-speed pins.
- Decoupling and power sequencing.
- Footprint field and package drawing.

## Agent Rule

For MCU work, a candidate symbol is the start of verification, not the end.
