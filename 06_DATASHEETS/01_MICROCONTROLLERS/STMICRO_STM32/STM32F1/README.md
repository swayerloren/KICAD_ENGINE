# STM32F1

Path: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F1/`

## Purpose

This folder is the first STM32 pilot family folder for KiCad Engine. It stores link-first STM32F1 source records, AI-readable design notes, part-level checklists, and KiCad symbol/footprint risk notes for AI-assisted schematic and PCB work.

## Current Status

Classification: `SCAFFOLDED_WITH_AI_SUMMARIES`

This folder is useful for planning and review, but it is not a complete verified STM32F1 database. No copyrighted ST PDFs are bundled here. Official ST documents are recorded as source links and must be checked before exact schematic, BOM, footprint, or manufacturing decisions.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: an official or public source URL is recorded and suitable for follow-up review.
- `VERIFIED_FROM_DATASHEET`: a value or rule was checked against the exact datasheet/reference document section. Use sparingly and cite the document.
- `INFERRED_FROM_COMMON_DESIGN`: a common STM32F1 design practice or board pattern that still needs source review for a specific product.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: high-risk electrical, mechanical, footprint, connector, or boot/debug decision requiring engineer review.

## Pilot Files

- `STM32F1_AI_OVERVIEW.md`
- `STM32F1_COMMON_PART_NUMBERS.md`
- `STM32F103C8T6_PART_RECORD.md`
- `STM32F103C8T6_SCHEMATIC_NOTES.md`
- `STM32F103C8T6_BOOT_DEBUG_NOTES.md`
- `STM32F103C8T6_POWER_CLOCK_NOTES.md`
- `STM32F103C8T6_PACKAGE_FOOTPRINT_NOTES.md`
- `STM32F103C8T6_DEV_BOARD_NOTES.md`
- `STM32F1_COMMON_MISTAKES.md`
- `STM32F1_KICAD_SYMBOL_FOOTPRINT_NOTES.md`
- `STM32F1_SOURCE_LINKS.md`
- `STM32F1_NEEDS_REVIEW.md`

## Agent Rules

- Prefer ST product pages, ST datasheets, ST reference manuals, ST application notes, and official board pages.
- Use public third-party board references only as design examples, never as fabrication approval.
- Do not download or add copyrighted datasheets unless redistribution rights are confirmed and the user approves the specific task.
- Do not claim a KiCad symbol, footprint, BOM entry, pinout, boot setting, or board output is verified from folder presence alone.
- Keep all unverified footprint, package, Blue Pill, BOOT, USB, VDDA/VSSA, and oscillator details marked `NEEDS_HUMAN_REVIEW`.
