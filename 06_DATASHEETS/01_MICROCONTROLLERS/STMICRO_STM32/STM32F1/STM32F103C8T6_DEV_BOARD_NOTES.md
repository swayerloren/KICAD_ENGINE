# STM32F103C8T6 Dev Board Notes

Date: 2026-05-03
Status: `LINK_FIRST_REFERENCE_NOTES`

These notes separate official ST development boards from third-party Blue Pill references.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design practice; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Official ST Reference Path

| Board | Source | Status | Use |
| --- | --- | --- | --- |
| NUCLEO-F103RB | https://www.st.com/en/evaluation-tools/nucleo-f103rb.html | `VERIFIED_SOURCE_LINK` | Official STM32F103 Nucleo board reference path. |
| Nucleo-64 user manual UM1724 | https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | ST-LINK/Nucleo user-manual reference. |

`NEEDS_HUMAN_REVIEW`: NUCLEO-F103RB uses a different exact MCU/package than STM32F103C8T6, so it is a reference for design patterns and ST-LINK behavior, not a direct footprint or pinout match.

## Blue Pill Reference Path

| Board | Source | Status | Use |
| --- | --- | --- | --- |
| STM32F103C8T6 Blue Pill | https://stm32-base.org/boards/STM32F103C8T6-Blue-Pill.html | `VERIFIED_SOURCE_LINK` third-party | Useful for board-level cautions and header/SWD/BOOT examples only. |

## Blue Pill Cautions

- `NEEDS_HUMAN_REVIEW`: Blue Pill is not an official ST board.
- `NEEDS_HUMAN_REVIEW`: Board variants, resistor values, regulators, crystals, USB circuits, and MCU authenticity can vary.
- `INFERRED_FROM_COMMON_DESIGN`: A Blue Pill-style board typically exposes BOOT0, BOOT1/PB2, reset, SWD, USB, power LED, and user LED, but a user's board must be checked visually and electrically.
- `NEEDS_HUMAN_REVIEW`: Do not copy a Blue Pill schematic into a new KiCad project without checking source license, exact circuit, and known board issues.

## Agent Rules

- Prefer official ST Nucleo docs for source-backed patterns.
- Use Blue Pill only as a warning/reference source.
- If the user asks to clone a Blue Pill, require board revision, schematic source, and explicit license/permission review.
