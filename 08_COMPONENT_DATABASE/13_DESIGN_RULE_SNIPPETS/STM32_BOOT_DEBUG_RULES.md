# STM32 Boot And Debug Rules

Date: 2026-05-02

Status: AI design-rule snippet. Exact boot behavior requires AN2606 plus the selected part reference manual and errata.

## Source Baseline

- AN2606 STM32 microcontroller system memory boot mode: https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf
- ST-LINK documentation hub: https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32/documentation.html
- Exact part datasheet/reference manual.

## Rules

- Provide SWD access on prototypes: SWDIO, SWCLK, NRST, GND, and target voltage reference.
- Keep SWD pins free from hard loads, strong pulls, LEDs, and incompatible peripherals during reset/debug.
- Add SWO when useful and supported, but do not make it mandatory for basic recovery.
- BOOT0 and boot option bits must be verified per part. Do not assume F1/F4 behavior applies to G0/U5/H5/H7/WB/WL.
- Expose BOOT0 or a documented recovery method during early hardware revisions.
- Verify which system bootloader interfaces are supported for the exact part: USART, USB DFU, CAN, FDCAN, I2C, SPI, or others.
- Never enable readout protection, TrustZone lock, secure boot, or debug authentication changes without a recovery procedure.

## Common Mistakes

- Using PA13/PA14 as ordinary IO while expecting SWD to remain reliable.
- Hiding BOOT0 on a production board before firmware recovery is proven.
- Assuming USB DFU exists because the MCU has USB pins.
- Copying Nucleo ST-LINK circuitry into a product when a simple SWD header is enough.

## Verification Checklist

- AN2606 exact part table checked.
- BOOT0/option-byte behavior documented.
- SWD connector pinout documented.
- NRST behavior reviewed.
- Any debug/security lock settings approved by the user before use.
