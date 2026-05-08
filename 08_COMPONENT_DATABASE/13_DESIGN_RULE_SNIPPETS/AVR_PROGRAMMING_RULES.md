# AVR Programming Rules

Date: 2026-05-02

Status: design-rule snippet for ATmega, ATtiny, and newer AVR schematic review.

## Core Rule

AVR programming depends on the exact generation. Older parts commonly use ISP, debugWIRE, JTAG, PDI, TPI, or bootloader workflows. Newer parts may use UPDI. Codex must identify the exact programming interface before placing connectors or assigning pins.

## ISP Rules

- Preserve MOSI, MISO, SCK, RESET, VCC, and GND access for ISP-capable parts.
- Avoid heavy loads or active drivers on SPI programming pins.
- Confirm reset pullup, reset button, and any autoreset circuit do not block programming.
- Do not assume Arduino bootloader programming exists on a bare AVR.

## debugWIRE Rules

- debugWIRE uses the reset pin on supported small AVR devices.
- Switching between debugWIRE and ISP is tool- and fuse-dependent.
- Do not change fuse bits blindly; a wrong SPIEN, DWEN, RSTDISBL, or clock fuse can lock out normal programming.

## UPDI Rules

- For UPDI AVRs, keep the UPDI line accessible and lightly loaded.
- If high-voltage UPDI activation may be needed, avoid circuitry that could be damaged by the high-voltage pulse.
- Do not apply UPDI assumptions to legacy ATmega328P, ATtiny85, or ATmega32U4 without checking the datasheet.

## USB AVR Rules

- Native USB AVRs such as ATmega32U4 need clock, D+/D-, VBUS/UVCC/UCAP, ESD, connector, and bootloader review.
- USB-C connector use requires separate CC resistor and power-role review.

## KiCad Review Checklist

- Programming connector orientation is explicit.
- Programming nets match datasheet pin names.
- Fuse assumptions are recorded.
- Reset and oscillator decisions are compatible with programming recovery.
- KiCad symbol package suffix and footprint are verified against the exact part order code.
