# 01_MICROCONTROLLERS

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Purpose

This folder stores link-first microcontroller datasheet metadata, family planning notes, part-level checklists, KiCad symbol/footprint risk notes, and research backlogs for AI-assisted KiCad work.

## Current Scope

The current scaffold covers Espressif, STMicro STM32, Microchip PIC/dsPIC, Microchip AVR, Raspberry Pi RP2040/RP2350, Nordic, NXP, TI, Silicon Labs, Renesas, Infineon, GigaDevice, WCH, and Atmel legacy folders where present.

The generated files are useful planning stubs. They are not verified datasheets, pinout approval, footprint approval, BOM approval, or PCB layout approval.

## Agent Rules

- Prefer official manufacturer product pages, datasheets, reference manuals, errata, application notes, and board files.
- Do not download PDFs or vendor documents unless a specific task approves it and redistribution rights are checked.
- Do not fabricate exact voltage, current, package, pinout, clock, boot, peripheral, or layout values.
- Keep unknown values marked `UNKNOWN_REQUIRES_SOURCE`.
- Treat symbols and footprints as candidate-only until source-backed pinout and package drawing review is complete.
- Record missing documents in `MISSING.md` and source links in family-level `*_SOURCE_LINKS.md` files.
