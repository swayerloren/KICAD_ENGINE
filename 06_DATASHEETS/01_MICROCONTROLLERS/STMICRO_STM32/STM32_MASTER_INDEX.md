# STM32 Master Index

Date: 2026-05-02

Status: official-source link index for AI-assisted KiCad design. Links are preferred over bundled PDFs for public release.

## Official ST Family Pages

| Family | Official ST URL | Agent Notes |
| --- | --- | --- |
| STM32F0 | https://www.st.com/en/microcontrollers-microprocessors/stm32f0-series.html | Low-cost Cortex-M0 family; verify package-specific USB/CAN availability. |
| STM32F1 | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | Legacy/high-volume Cortex-M3 family; common Blue Pill ecosystem risk. |
| STM32F3 | https://www.st.com/en/microcontrollers-microprocessors/stm32f3-series.html | Mixed-signal Cortex-M4 family; analog pin and reference handling matter. |
| STM32F4 | https://www.st.com/en/microcontrollers-microprocessors/stm32f4-series.html | Cortex-M4 performance family; USB, CAN, clock, and power domains vary by part. |
| STM32F7 | https://www.st.com/en/microcontrollers-microprocessors/stm32f7-series.html | Cortex-M7 high-performance family; caches, external memory, USB HS, and layout need care. |
| STM32G0 | https://www.st.com/en/microcontrollers-microprocessors/stm32g0-series.html | Value Cortex-M0+ family; BOOT and low-pin-count package limits need review. |
| STM32G4 | https://www.st.com/en/microcontrollers-microprocessors/stm32g4-series.html | Mixed-signal/motor-control Cortex-M4 family with FDCAN, analog, USB on many parts. |
| STM32H5 | https://www.st.com/en/microcontrollers-microprocessors/stm32h5-series.html | Cortex-M33 security/performance family; TrustZone and boot/security configuration matter. |
| STM32H7 | https://www.st.com/en/microcontrollers-microprocessors/stm32h7-series.html | High-performance Cortex-M7/M4 family; power domains, VCAP/SMPS/LDO, clocks, and impedance matter. |
| STM32L0 | https://www.st.com/en/microcontrollers-microprocessors/stm32l0-series.html | Ultra-low-power Cortex-M0+ family; leakage and analog/RTC domains matter. |
| STM32L4 | https://www.st.com/en/microcontrollers-microprocessors/stm32l4-series.html | Ultra-low-power Cortex-M4 family; USB, low-power clocks, and analog rails need verification. |
| STM32L5 | https://www.st.com/en/microcontrollers-microprocessors/stm32l5-series.html | Ultra-low-power Cortex-M33 family; security/TrustZone and power domains need review. |
| STM32U0 | https://www.st.com/en/microcontrollers-microprocessors/stm32u0-series.html | Newer low-power entry family; verify library support and boot details. |
| STM32U5 | https://www.st.com/en/microcontrollers-microprocessors/stm32u5-series.html | Ultra-low-power Cortex-M33 family with security and optional SMPS variants. |
| STM32WB | https://www.st.com/en/microcontrollers-microprocessors/stm32wb-series.html | Wireless BLE/802.15.4 family; RF layout and firmware stack ownership matter. |
| STM32WL | https://www.st.com/en/microcontrollers-microprocessors/stm32wl-series.html | Sub-GHz wireless family; RF, matching, certification, and regional band rules matter. |

## Official Application Notes And Reference Topics

| Topic | ST Document Link | Use |
| --- | --- | --- |
| STM32 system memory boot mode | https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf | Determine supported bootloader interfaces and boot pin/option byte behavior by part. |
| STM32F4 hardware getting started | https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf | Practical hardware patterns for power, reset, clock, boot, and debug on STM32F4-class designs. |
| Oscillator design | https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf | HSE/LSE crystal selection, load caps, PCB layout, startup, and drive-level review. |
| USB hardware and PCB guidelines | https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf | USB device/host/OTG clocking, routing, ESD, VBUS, and connector guidance. |
| ST-LINK tools documentation | https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32/documentation.html | ST-LINK/V2, STLINK-V3, SWD/JTAG, probe, and user manual references. |
| STM32 Nucleo board docs | https://www.st.com/en/evaluation-tools/stm32-nucleo-boards/documentation.html | Nucleo user manuals, data briefs, ST-LINK integration, and board-family references. |

## Part Pages Used In This Pass

| Part | Family | Official Product URL | Datasheet Link Used By KiCad 9 Candidate |
| --- | --- | --- | --- |
| STM32F103C8T6 | STM32F1 | https://www.st.com/en/microcontrollers-microprocessors/stm32f103c8.html | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf |
| STM32F401CCU6 | STM32F4 | https://www.st.com/en/microcontrollers-microprocessors/stm32f401cc.html | https://www.st.com/resource/en/datasheet/stm32f401cc.pdf |
| STM32F411CEU6 | STM32F4 | https://www.st.com/en/microcontrollers-microprocessors/stm32f411ce.html | https://www.st.com/resource/en/datasheet/stm32f411ce.pdf |
| STM32F405RGT6 | STM32F4 | https://www.st.com/en/microcontrollers-microprocessors/stm32f405rg.html | https://www.st.com/resource/en/datasheet/stm32f405rg.pdf |
| STM32G030F6P6 | STM32G0 | https://www.st.com/en/microcontrollers-microprocessors/stm32g030f6.html | https://www.st.com/resource/en/datasheet/stm32g030f6.pdf |
| STM32G431CBT6 | STM32G4 | https://www.st.com/en/microcontrollers-microprocessors/stm32g431cb.html | https://www.st.com/resource/en/datasheet/stm32g431cb.pdf |
| STM32H743VIT6 | STM32H7 | https://www.st.com/en/microcontrollers-microprocessors/stm32h743vi.html | https://www.st.com/resource/en/datasheet/stm32h743vi.pdf |
| STM32U575ZIT6 | STM32U5 placeholder | https://www.st.com/en/microcontrollers-microprocessors/stm32u575zi.html | https://www.st.com/resource/en/datasheet/stm32u575zi.pdf |
| STM32WB55RGV6 | STM32WB placeholder | https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html | https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf |

## Record Files

- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/stm32_part_records.json`
- `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_DEV_BOARD_RECORDS.md`

## Board Schematic Pack Links Added

| Board / Family | Official Schematic Evidence | Handling Rule |
| --- | --- | --- |
| NUCLEO-F103RB / NUCLEO-F401RE | MB1136 Nucleo-64 schematic family; direct C03 resource observed: https://www.st.com/resource/en/schematic_pack/mb1136-default-c03_schematic.pdf | Use only after matching the exact board revision; do not treat as package proof for F103C8T6 or F401CCU6. |
| NUCLEO-G431RB | MB1367-G431RB C04/C05 resources observed: https://www.st.com/resource/en/schematic_pack/mb1367-g431rb-c04_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb1367-g431rb-c05_schematic.pdf | Reference-only for G431RB board circuitry; verify package before applying to G431CBT6. |
| NUCLEO-H743ZI | MB1364-H743ZI C01/E01 resources observed: https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-c01_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-e01_schematic.pdf | Historical reference only; check replacement boards before new design work. |
| STM32F4DISCOVERY | MB997-F407VGT6 resources observed: https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-e01_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-g01-schematic.pdf | Use for F4 block study only; not proof for STM32F405RGT6 package or pinout. |
| 32F746GDISCOVERY | Product page lists board-revision schematic resources: https://www.st.com/en/evaluation-tools/32f746gdiscovery.html | Select exact board revision before extracting display, SDRAM, USB, clock, or power blocks. |

## Current Gaps

- Exact reference manuals and errata documents are indexed by product/family page but not fully extracted.
- Package drawing checks are not complete.
- Some official Nucleo and Discovery schematic-pack links are now indexed, but full board-revision extraction is not complete.
- Blue Pill and Black Pill records remain community-board placeholders because there is no single official ST board schematic.
- FDCAN/CAN physical transceiver recommendations must be resolved from the exact transceiver datasheet and project bus requirements.
