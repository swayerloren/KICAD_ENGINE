# STM32 Discovery Board Index

Date: 2026-05-02

Status: official ST board-link index plus placeholders for future schematic extraction.

## Official Discovery Board Sources

| Board | ST Status Observed | MCU / Focus | Official URL | Agent Use |
| --- | --- | --- | --- | --- |
| STM32F4DISCOVERY / STM32F407G-DISC1 | Active page observed; ST notes replacement order code | STM32F407VG discovery kit | https://www.st.com/en/evaluation-tools/stm32f4discovery.html | F4 reference for ST-LINK, crystal, USB, sensors/audio, and board-level power examples. |
| 32F746GDISCOVERY | Active | STM32F746NG discovery kit | https://www.st.com/en/evaluation-tools/32f746gdiscovery.html | F7 high-performance reference for display, SDRAM, USB, clocks, and complex board bring-up. |
| STM32H7 Discovery placeholder | Requires board selection | STM32H7 Discovery/Eval variants | https://www.st.com/en/evaluation-tools/stm32-mcu-mpu-eval-tools.html | Placeholder until an exact H7 Discovery board is chosen. |
| STM32U5 Discovery placeholder | Requires board selection | STM32U5 Discovery/IoT variants | https://www.st.com/en/evaluation-tools/stm32-mcu-mpu-eval-tools.html | Placeholder until an exact U5 board is chosen. |
| STM32WB Discovery/Nucleo placeholder | Requires board selection | STM32WB wireless boards | https://www.st.com/en/evaluation-tools/nucleo-wb55rg.html | Prefer NUCLEO-WB55RG for WB source work unless a Discovery board is explicitly selected. |

## AI Handling Rules

- Discovery boards are richer than Nucleo boards and often include displays, audio, memories, sensors, radios, power monitors, and solder bridges.
- Extract only the circuit block relevant to the target design.
- Check board revision, schematic revision, BOM, and errata before copying a reference block.
- Never treat a Discovery board's connector pinout as the MCU package pinout.

## Official Schematic Pack References

| Board | Official Schematic Resource Evidence |
| --- | --- |
| STM32F4DISCOVERY / STM32F407G-DISC1 | ST product page lists MB997-F407VGT6-B01, B02, C01, D01, E01, and G01 board schematic PDFs depending on board revision. Direct resources observed include https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-e01_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-g01-schematic.pdf |
| 32F746GDISCOVERY | ST product page lists MB1191 F746NGH6-B02, C01, C02, and C03 board schematic PDFs depending on board revision. Product page: https://www.st.com/en/evaluation-tools/32f746gdiscovery.html |
