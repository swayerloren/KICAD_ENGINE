# STM32G4 USB, CAN, And Communication Notes

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Family-Level Communication Warning

FDCAN and USB availability vary. FDCAN still needs an external transceiver and bus protection review.

## USB Checklist

- Exact part has USB peripheral and package exposes required pins: `UNKNOWN_REQUIRES_SOURCE` until verified.
- USB FS/HS/OTG role verified from reference manual.
- USB clock source verified from datasheet/reference manual.
- VBUS sensing/backfeed policy documented.
- USB-C CC resistors, ESD protection, shield policy, and connector orientation reviewed if USB-C is used.
- Differential-pair routing, impedance target, stubs, ESD placement, and connector pinout reviewed.

## CAN/FDCAN Checklist

- Exact peripheral type is verified: classic CAN, bxCAN, FDCAN, or none.
- Alternate-function pins and package availability verified.
- External transceiver selected from a source-backed component record.
- Termination, common-mode choke, TVS/protection, split termination, connector pinout, and bus length/speed are reviewed.
- CAN bootloader support, if needed, verified in AN2606.

## Other Interfaces

- UART/I2C/SPI availability is not enough; verify voltage domain, alternate function, boot/debug conflicts, and package pinout.
- Ethernet, SDMMC, camera, display, external memory, and RF interfaces require layout-specific review.

## Source Links

- USB hardware and PCB guideline AN4879: https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf
- Family page: https://www.st.com/en/microcontrollers-microprocessors/stm32g4-series.html
- Bootloader interface check: https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf
