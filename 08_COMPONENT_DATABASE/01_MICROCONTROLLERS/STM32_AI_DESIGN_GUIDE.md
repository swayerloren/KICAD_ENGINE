# STM32 AI Design Guide

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

This guide tells Codex, Claude, and similar VS Code agents how to use the STM32 datasheet tree and component database without guessing.

## Required Read Order For STM32 Work

1. `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_AI_MASTER_INDEX.md`
2. Target family `FAMILY_OVERVIEW.md`
3. Target family `SOURCE_LINKS.md`
4. Target family `POWER_CLOCK_RESET_NOTES.md`
5. Target family `BOOT_DEBUG_PROGRAMMING_NOTES.md`
6. Target family `PACKAGE_FOOTPRINT_NOTES.md`
7. `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_PART_RECORDS.md` if an exact part exists there
8. `11_LIBRARY_FACTORY/mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md` before footprint approval

## STM32 Design Gate

A STM32 schematic block is not ready until these are recorded:

- Exact order code.
- Official ST product page.
- Datasheet link.
- Reference manual link.
- Errata link.
- Package drawing link.
- Power pins and decoupling requirements.
- Reset and boot mode evidence.
- SWD/debug plan.
- Clock source requirements.
- USB/CAN/FDCAN evidence if used.
- KiCad symbol candidate checked against pinout.
- KiCad footprint candidate checked against package drawing.
- Human review status for package and connector orientation.

## Do Not Guess

- Operating voltage.
- Absolute maximum ratings.
- Current limits.
- Clock frequency or crystal load capacitance.
- USB clocking mode.
- CAN/FDCAN peripheral availability.
- Package land pattern.
- Pinout or alternate functions.
- Bootloader interface support.
- Lifecycle status.

Use `UNKNOWN_REQUIRES_SOURCE` until verified.

## KiCad Symbol Rules

- Search project-local libraries first, then user/global libraries, then installed KiCad libraries.
- Match exact part number and package.
- Inspect hidden power pins and multi-unit symbol sections.
- Compare all pins used by the design against the official datasheet.
- Treat a KiCad library symbol as `VERIFIED_FROM_KICAD_LIBRARY` only after source comparison.

## KiCad Footprint Rules

- Match exact package drawing, not only package family.
- Check body size, lead count, lead pitch, exposed pad, drill or pad geometry, courtyard, fab layer, silk, and pin-1 orientation.
- BGA/WLCSP/QFN/connector footprints require human review.
- Do not infer Nucleo/Discovery board footprint correctness for a custom part.

## Dev Board Use

- Use ST Nucleo/Discovery/EVAL boards as reference evidence, not as automatic approval.
- Match board revision before extracting circuits.
- Record solder bridges, power muxes, ST-LINK circuitry, jumpers, crystals, protection, and external transceivers.
- Community boards such as Blue Pill/Black Pill need exact board revision and source before use.

## Current Limitations

- The expanded family tree is `SCAFFOLDED_WITH_AI_SUMMARIES`.
- Exact part values remain `UNKNOWN_REQUIRES_SOURCE` unless a specific part record says otherwise.
- Reference manual and errata extraction is still incomplete.
- Package-footprint verification tables are not complete.

## Official Source Starting Points

- STM32 portfolio: https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html
- STM32CubeMX: https://www.st.com/en/development-tools/stm32cubemx.html
- ST-LINK tools: https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32.html
- AN2606 boot mode: https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf
- AN2867 oscillator design: https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf
- AN4879 USB guideline: https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf
