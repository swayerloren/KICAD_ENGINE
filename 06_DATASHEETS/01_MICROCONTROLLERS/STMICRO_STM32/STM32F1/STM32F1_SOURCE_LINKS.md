# STM32F1 Source Links

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

This is the STM32F1 pilot source-link index. It records official/public source locations only. It does not bundle PDFs, and it does not prove exact schematic, package, or footprint details.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in the named ST document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern that still needs source review.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: review required before schematic/PCB/fab use.

## Official ST Sources

| Topic | Document Type | Source URL | Status | KiCad Engine Use |
| --- | --- | --- | --- | --- |
| STM32F1 series | family page | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | `VERIFIED_SOURCE_LINK` | Family context, product-line scope, migration notes. |
| STM32F103C8 | product page | https://www.st.com/en/microcontrollers-microprocessors/stm32f103c8 | `VERIFIED_SOURCE_LINK` | Official part landing page, datasheet/CAD links, lifecycle checks. |
| STM32F103C8 datasheet | datasheet | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf | `VERIFIED_SOURCE_LINK` | Exact pinout, package, absolute maximum, operating conditions, electrical specs. |
| RM0008 | reference manual | https://www.st.com/resource/en/reference_manual/rm0008-stm32f103xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | Clock tree, reset, boot, GPIO, AFIO, USB, CAN, debug behavior. |
| AN2586 | hardware application note | https://www.st.com/resource/en/application_note/an2586-getting-started-with-stm32f10xxx-hardware-development-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | Minimum hardware and reference schematic guidance. |
| AN2606 | system-memory boot mode | https://www.st.com/resource/en/application_note/an2606-stm32microcontroller-system-memory-boot-mode-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | Bootloader entry and peripheral boot support checks. |
| AN2867 | oscillator design | https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | HSE/LSE design and PCB layout checks. |
| AN4879 | USB hardware/PCB guidance | https://www.st.com/resource/en/application_note/an4879-usb-hardware-design-guidelines-for-stm32-microcontrollers-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | USB FS schematic and PCB checklist source. |
| NUCLEO-F103RB | official board page | https://www.st.com/en/evaluation-tools/nucleo-f103rb.html | `VERIFIED_SOURCE_LINK` | Official dev-board reference path. |
| UM1724 | Nucleo-64 user manual | https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf | `VERIFIED_SOURCE_LINK` | ST-LINK and Nucleo board behavior reference. |

## Public Third-Party Sources

| Topic | Source URL | Status | Use Limits |
| --- | --- | --- | --- |
| STM32F103C8T6 Blue Pill board notes | https://stm32-base.org/boards/STM32F103C8T6-Blue-Pill.html | `VERIFIED_SOURCE_LINK` | Public board reference only. Blue Pill variants are not ST official and cannot prove a user's board revision. |

## Source Use Rules

- Treat URLs as `VERIFIED_SOURCE_LINK`, not `VERIFIED_FROM_DATASHEET`, until the exact section has been checked.
- Do not use package suffix, pinout, voltage, clock, USB, CAN, ADC, or footprint values from memory.
- Do not copy ST PDFs into this repo unless redistribution rights are explicitly confirmed.
- Do not copy third-party schematics or board files unless license compatibility is checked.
