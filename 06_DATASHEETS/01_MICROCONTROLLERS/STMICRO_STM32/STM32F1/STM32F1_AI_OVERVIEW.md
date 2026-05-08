# STM32F1 AI Overview

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

This file gives Codex/Claude an STM32F1 planning overview for KiCad work. It is not a replacement for ST datasheets, RM0008, AN2586, AN2606, AN2867, or AN4879.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common STM32F1 design practice; useful for checklists only.
- `UNVERIFIED`: not checked against source.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use.

## What STM32F1 Is Good For

`VERIFIED_SOURCE_LINK`: ST positions STM32F1 as a mainstream Arm Cortex-M3 MCU family with product lines that include STM32F100, STM32F101, STM32F102, STM32F103, and STM32F105/107.

`VERIFIED_SOURCE_LINK`: ST's STM32F103C8 product page identifies STM32F103C8 as a mainstream performance-line Cortex-M3 MCU with USB and CAN support and an official datasheet/CAD resource path.

`INFERRED_FROM_COMMON_DESIGN`: STM32F1 remains useful for legacy boards, low-cost prototypes, Blue Pill-compatible firmware experiments, educational projects, and designs where the exact STM32F103 ecosystem is required.

`NEEDS_HUMAN_REVIEW`: For new production designs, compare STM32F1 lifecycle, stock, debug tooling, firmware support, and package availability against newer STM32G0/G4/U0/U5 families before committing.

## Product Lines To Consider

| Line | Use Guidance | Status |
| --- | --- | --- |
| STM32F100 | value line; exact peripherals require source review | `VERIFIED_SOURCE_LINK` only |
| STM32F101 | access line; no USB assumption without source review | `VERIFIED_SOURCE_LINK` only |
| STM32F102 | USB-focused line; exact part support requires source review | `VERIFIED_SOURCE_LINK` only |
| STM32F103 | common performance line; STM32F103C8T6 belongs here | `VERIFIED_SOURCE_LINK` |
| STM32F105/107 | connectivity line; Ethernet/USB/CAN decisions require exact part review | `VERIFIED_SOURCE_LINK` only |

## AI Design Rules

- Start from an exact part number, not "STM32F1".
- Use the ST product page and datasheet link before creating a component record.
- Use RM0008 for peripheral, clock, boot, USB, CAN, GPIO alternate-function, and debug behavior.
- Use AN2586 for minimum hardware and reference schematic patterns.
- Use AN2606 before relying on system bootloader behavior.
- Use AN2867 before selecting HSE/LSE crystals or load capacitors.
- Use AN4879 before implementing USB.
- Keep package/footprint mapping blocked until exact package drawing is checked.

## What Must Be Verified Before PCB

| Item | Status | Why |
| --- | --- | --- |
| exact orderable part number | `NEEDS_HUMAN_REVIEW` | Package, temperature range, packing, and lifecycle affect BOM/footprint. |
| pinout and symbol pins | `NEEDS_HUMAN_REVIEW` | KiCad symbol existence is not a pinout audit. |
| package and footprint | `NEEDS_HUMAN_REVIEW` | LQFP-48 candidate must be compared to ST package drawing. |
| BOOT0/BOOT1 strap behavior | `NEEDS_HUMAN_REVIEW` | Incorrect boot pins can block programming/recovery. |
| SWD/JTAG pin access | `NEEDS_HUMAN_REVIEW` | PA13/PA14 and reset access must survive pin mux choices. |
| USB clock/VBUS/pull-up policy | `NEEDS_HUMAN_REVIEW` | USB behavior depends on exact part and circuit policy. |
| VDDA/VSSA/VREF handling | `NEEDS_HUMAN_REVIEW` | Analog behavior and ADC accuracy depend on source-backed rail design. |
| oscillator values | `NEEDS_HUMAN_REVIEW` | Crystal and capacitors must match vendor data and AN2867. |
