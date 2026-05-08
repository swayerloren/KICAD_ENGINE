# MCU Family Guides Session

Date: 2026-05-02

## Purpose

Create AI-readable MCU family guide pages under `08_COMPONENT_DATABASE/01_MICROCONTROLLERS` so Codex, Claude, and similar agents can make better early design choices without fabricating exact specifications.

## Context Read

- `AGENTS.md`
- `08_COMPONENT_DATABASE/00_INDEX/COMPONENT_DATABASE_README.md`
- `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`

## Files Created

- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/ESPRESSIF_ESP32_FAMILY.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/MICROCHIP_PIC_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/MICROCHIP_AVR_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/RP2040_RP2350_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/NORDIC_NRF52_NRF53_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/NXP_KINETIS_IMXRT_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/TI_MSP430_TM4C_OVERVIEW.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/WCH_CH32_OVERVIEW.md`

## Coverage

Each guide includes:

- What the family is good for.
- Common voltage-level guidance with exact values requiring datasheet verification.
- Programming/debug method guidance.
- Clocking considerations.
- Boot mode considerations.
- USB considerations.
- RF considerations where applicable.
- CAN/LIN/UART/I2C/SPI notes.
- Typical KiCad symbol/footprint issues.
- Common external components.
- Layout warnings.
- Power sequencing warnings.
- Dev board versus bare chip warnings.
- When to avoid the family.
- Datasheets/reference manuals needed.
- How Codex should verify before schematic use.

## Verification

- Confirmed all nine requested files exist.
- Confirmed all guides contain the required section headings.
- Confirmed the guides repeatedly mark exact values/specifications as requiring source or datasheet verification.

## Safety Notes

- No datasheets were downloaded.
- No exact unverified electrical specs were added.
- No KiCad project source files were modified.
- These files are guidance pages, not verified component records.
