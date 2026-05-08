# STM32 USB Rules

Date: 2026-05-02

Status: AI design-rule snippet. Exact USB requirements depend on the selected STM32 part, package, USB peripheral type, connector, and product role.

## Source Baseline

- AN4879 USB hardware and PCB guidelines: https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf
- Exact STM32 datasheet/reference manual.
- USB connector and ESD protection datasheets.

## Rules

- Confirm whether the part supports USB device, host, OTG, FS, HS, ULPI, or crystal-less FS before routing.
- Confirm USB pins are present in the selected package and are not needed for another critical alternate function.
- Use controlled differential routing appropriate for the board stackup and connector placement.
- Add ESD protection close to the connector when exposed externally.
- USB-C device/UFP designs need correct CC resistors and VBUS handling; do not wire only D+/D- and assume compliance.
- Check whether VBUS sensing is required, optional, or prohibited for the exact part/peripheral mode.
- Check clock accuracy requirements. Some STM32 USB implementations need HSE/PLL; some support HSI48/CRS or other crystal-less modes.

## Common Mistakes

- Assuming every STM32 with USB pins has USB DFU bootloader support.
- Reusing USB pins for GPIO and later expecting DFU/recovery.
- Omitting USB-C CC resistors.
- Routing USB through long stubs, headers, or noisy areas.
- Copying Nucleo USB/ST-LINK wiring instead of the user USB interface.

## Verification Checklist

- Exact USB peripheral type identified.
- Connector role and power role defined.
- VBUS/CC/ESD/shield plan documented.
- Clock source verified.
- KiCad differential pair/net names reviewed.
