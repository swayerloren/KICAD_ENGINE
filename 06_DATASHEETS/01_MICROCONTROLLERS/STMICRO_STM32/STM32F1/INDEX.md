# STM32F1 Index

Date: 2026-05-03

This index tracks STM32F1 pilot-family files for AI-assisted KiCad work. It is source-link-first and does not imply that exact electrical values, pinouts, package drawings, or footprints are verified.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design practice, not final evidence.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Local AI Files

| Part / Topic | Document Type | Local File | Source URL | Verification Status | Notes |
| --- | --- | --- | --- | --- | --- |
| STM32F1 | AI overview | `STM32F1_AI_OVERVIEW.md` | `STM32F1_SOURCE_LINKS.md` | `VERIFIED_SOURCE_LINK` plus `UNVERIFIED` details | Family-level only. |
| STM32F1 | common part-number guide | `STM32F1_COMMON_PART_NUMBERS.md` | ST STM32F1/ST product selector links | `NEEDS_HUMAN_REVIEW` | Exact ordering code and lifecycle must be checked. |
| STM32F103C8T6 | part record | `STM32F103C8T6_PART_RECORD.md` | ST product page and datasheet link | `VERIFIED_SOURCE_LINK` | Exact package drawing still pending. |
| STM32F103C8T6 | minimum schematic notes | `STM32F103C8T6_SCHEMATIC_NOTES.md` | AN2586, RM0008, product page | `INFERRED_FROM_COMMON_DESIGN` plus source links | Checklist, not approval. |
| STM32F103C8T6 | boot/debug notes | `STM32F103C8T6_BOOT_DEBUG_NOTES.md` | AN2606, RM0008, AN2586 | `NEEDS_HUMAN_REVIEW` | BOOT0/BOOT1 must be checked against exact part. |
| STM32F103C8T6 | power/clock notes | `STM32F103C8T6_POWER_CLOCK_NOTES.md` | AN2586, AN2867, product page | `NEEDS_HUMAN_REVIEW` | Values and crystal load caps are not preapproved. |
| STM32F103C8T6 | package/footprint notes | `STM32F103C8T6_PACKAGE_FOOTPRINT_NOTES.md` | ST datasheet/product page, local KiCad inventory | `NEEDS_HUMAN_REVIEW` | KiCad footprint is candidate only. |
| STM32F103C8T6 | dev-board notes | `STM32F103C8T6_DEV_BOARD_NOTES.md` | NUCLEO-F103RB, STM32-base Blue Pill | `VERIFIED_SOURCE_LINK` | Blue Pill is third-party and variant-prone. |
| STM32F1 | common mistakes | `STM32F1_COMMON_MISTAKES.md` | ST docs and common-design inference | `INFERRED_FROM_COMMON_DESIGN` | Use as checklist. |
| STM32F1 | KiCad symbol/footprint notes | `STM32F1_KICAD_SYMBOL_FOOTPRINT_NOTES.md` | local KiCad inventory | `VERIFIED_FROM_KICAD_LIBRARY` for existence only | Not package approval. |
| STM32F1 | source links | `STM32F1_SOURCE_LINKS.md` | official/public URLs | `VERIFIED_SOURCE_LINK` | Link-only index. |
| STM32F1 | review backlog | `STM32F1_NEEDS_REVIEW.md` | all above | `NEEDS_HUMAN_REVIEW` | Blocks final schematic/PCB approval. |

## External Component Records

| Record | Path | Status |
| --- | --- | --- |
| STM32F103C8T6 component record | `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32F103C8T6.md` | `UNVERIFIED` exact pinout/package/footprint |
| STM32F103C8T6 symbol/footprint match | `08_COMPONENT_DATABASE/12_KICAD_SYMBOL_FOOTPRINT_MATCHES/STM32F103C8T6_MATCH.md` | `NEEDS_HUMAN_REVIEW` before PCB |
