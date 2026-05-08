# STM32F103C8T6 Boot And Debug Notes

Date: 2026-05-03
Status: `AI_PLANNING_CHECKLIST`

Use these notes to avoid boot/debug mistakes in STM32F103C8T6 KiCad work. Exact boot mode behavior must be checked against AN2606 and RM0008 before design approval.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common STM32F1 design practice; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Source Links

- AN2606 system memory boot mode: `VERIFIED_SOURCE_LINK`
- RM0008 reference manual: `VERIFIED_SOURCE_LINK`
- AN2586 hardware development: `VERIFIED_SOURCE_LINK`

## BOOT0 And BOOT1

| Item | Guidance | Status |
| --- | --- | --- |
| BOOT0 default | Provide a deterministic default so the board normally boots user flash. | `INFERRED_FROM_COMMON_DESIGN` |
| BOOT0 recovery | Provide pad/header/button/jumper access so a human can enter system bootloader when needed. | `INFERRED_FROM_COMMON_DESIGN` |
| BOOT1/PB2 | Treat BOOT1 as exact-part behavior that must be checked before reusing PB2 or copying Blue Pill jumpers. | `NEEDS_HUMAN_REVIEW` |
| bootloader interfaces | Do not assume USB, USART, or CAN bootloader support for this exact part without AN2606 section review. | `NEEDS_HUMAN_REVIEW` |

## SWD / ST-Link

| Signal | Minimum Intent | Status |
| --- | --- | --- |
| SWDIO | Keep accessible and avoid permanent conflicts. | `INFERRED_FROM_COMMON_DESIGN` |
| SWCLK | Keep accessible and avoid permanent conflicts. | `INFERRED_FROM_COMMON_DESIGN` |
| NRST | Prefer exposing to debugger and reset button/header. | `INFERRED_FROM_COMMON_DESIGN` |
| GND | Required reference for debug connection. | `INFERRED_FROM_COMMON_DESIGN` |
| target voltage | Expose target-reference voltage if the selected debugger expects it. | `NEEDS_HUMAN_REVIEW` |

## Agent Rules

- Do not disable or repurpose SWD/JTAG pins in schematic review without a documented debug recovery plan.
- Do not assume Blue Pill BOOT0/BOOT1 jumpers are the right human interface for a new board.
- Do not claim bootloader access passed unless it is checked in AN2606 and tested or human-confirmed.
- Mark boot/debug decisions `NEEDS_HUMAN_REVIEW` until the exact programming method is chosen.
