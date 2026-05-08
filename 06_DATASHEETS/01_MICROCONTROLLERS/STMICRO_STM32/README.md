# STMicroelectronics STM32 Reference Library

Date: 2026-05-02

Status: official-source index and AI guidance. This folder stores links, summaries, and future local documents for STM32 work. It is not a complete datasheet mirror, and no local document should be treated as design-approved without record-level verification.

## Purpose

This library helps Codex, Claude, and other VS Code-based agents reason about STM32 schematic and PCB work without guessing from memory. It points agents to official ST product pages, datasheets, reference manuals, errata, application notes, Nucleo/Discovery board pages, and ST-LINK programming/debug documents.

## Source Policy

- Prefer official ST product pages and documentation pages.
- Link datasheets, manuals, schematics, and application notes instead of bundling PDFs unless redistribution is explicitly confirmed.
- Do not mass-download ST PDFs into a public GitHub release.
- Treat third-party boards such as Blue Pill and Black Pill as community hardware with variant risk, not ST reference designs.
- Treat KiCad symbols and footprints as candidates until the exact ST package drawing and pinout are checked.

## Agent Rules

- Always choose the exact STM32 part number and package before schematic use.
- Verify the datasheet, reference manual, errata, package drawing, and bootloader/boot mode document.
- Check BOOT0, BOOT1 where present, option bytes, NRST, SWDIO, SWCLK, SWO, JTAG pins, oscillator pins, USB pins, CAN/FDCAN pins, VDDA/VSSA/VREF+, VBAT, and all VDD/VSS pins.
- Do not copy Nucleo or Discovery circuits blindly. Board schematics include ST-LINK, jumpers, solder bridges, protection, and board-specific power paths.
- Keep fabrication outputs `NOT_FINAL` until ERC, DRC, BOM, footprint, package, datasheet, and visual review are complete.

## Companion Files

- `STM32_MASTER_INDEX.md`: family, part, application note, and record index.
- `NUCLEO_BOARDS/NUCLEO_BOARD_INDEX.md`: official Nucleo board references.
- `DISCOVERY_BOARDS/DISCOVERY_BOARD_INDEX.md`: official Discovery board references.
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_FAMILY_OVERVIEW.md`: AI-oriented family guidance.
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_PART_RECORDS.md`: bare MCU records.
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_DEV_BOARD_RECORDS.md`: dev-board records.
