# STM32F1 Needs Review

Date: 2026-05-03
Status: `OPEN_REVIEW_BACKLOG`

This is the blocker list for promoting STM32F1 pilot content beyond planning.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Open Blockers

| Blocker | Status | Required Evidence |
| --- | --- | --- |
| exact STM32F103C8T6 package/order-code mapping | `NEEDS_HUMAN_REVIEW` | ST datasheet/order-code table. |
| symbol pinout audit | `NEEDS_HUMAN_REVIEW` | Compare KiCad `STM32F103C8Tx` symbol against exact datasheet pin table. |
| footprint package audit | `NEEDS_HUMAN_REVIEW` | Compare KiCad LQFP-48 footprint against ST package drawing. |
| BOOT0/BOOT1 behavior | `NEEDS_HUMAN_REVIEW` | Check AN2606 and RM0008 exact STM32F103 section. |
| SWD/JTAG and remap implications | `NEEDS_HUMAN_REVIEW` | Check RM0008 AFIO/debug sections and project firmware plan. |
| USB hardware policy | `NEEDS_HUMAN_REVIEW` | Check datasheet, RM0008, and AN4879 for clock, pull-up, VBUS, ESD, and routing. |
| VDDA/VSSA/VREF design | `NEEDS_HUMAN_REVIEW` | Check datasheet and AN2586. |
| HSE/LSE crystal values | `NEEDS_HUMAN_REVIEW` | Check AN2867 plus selected crystal datasheet. |
| Blue Pill references | `NEEDS_HUMAN_REVIEW` | Check exact board revision and source/license before using as evidence. |
| errata sheet | `UNVERIFIED` | Add ST errata source link and summarize relevant risks. |

## Rule For KiCad Projects

Any STM32F103C8T6 project using these records must keep schematic-to-PCB gate status blocked until the relevant package, symbol, boot/debug, clock, power, and USB review items are closed or explicitly accepted by a human.
