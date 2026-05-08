# STM32F1 Boot, Debug, And Programming Notes

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Programming/Debug Baseline

- Provide SWDIO, SWCLK, NRST, GND, and target voltage reference for SWD.
- SWO is useful when supported but not a substitute for SWDIO/SWCLK.
- JTAG may be available on larger packages but consumes pins and must be planned early.
- ST-LINK, STLINK-V3, STM32CubeProgrammer, and STM32CubeIDE are official ecosystem touchpoints; exact workflows depend on the selected part.

## Boot Mode Rules

- Use AN2606 for system memory bootloader availability.
- Check the exact reference manual for BOOT0, option bytes, boot address selection, secure boot, RDP, TrustZone, and debug authentication behavior.
- Do not assume UART/USB/CAN/FDCAN/I2C/SPI bootloader support from the family name.
- Keep a human-readable boot strap table in the project notes.

## KiCad Schematic Checklist

- BOOT0 or documented boot override path present.
- NRST accessible.
- SWD connector/test pads present and not blocked by conflicting loads.
- Target voltage reference routed to debug connector if connector is used.
- Debug pins are not permanently consumed by boot-sensitive external circuitry.

## Source Links

- AN2606 boot mode: https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf
- ST-LINK tools: https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32.html
- ST-LINK documentation: https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32/documentation.html
