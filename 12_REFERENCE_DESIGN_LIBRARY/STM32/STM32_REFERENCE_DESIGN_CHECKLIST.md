# STM32 Reference Design Checklist

## Source And License

- ST or open hardware source identified.
- License and redistribution status recorded.
- Schematic and layout file format recorded.

## Technical Review

- Exact STM32 family, part, and package identified.
- BOOT0/boot mode reviewed.
- NRST circuit reviewed.
- SWD connector reviewed.
- Clocking source reviewed.
- VDDA/VSSA and all power pins reviewed.
- USB, CAN/FDCAN, UART, I2C, and SPI pins reviewed.
- Footprint package drawing checked.

## Reuse Warnings

- Do not copy dev-board ST-Link sections unless intentionally included.
- Do not assume Nucleo pin headers map to bare MCU pins without review.
- Do not copy package assumptions between STM32 families.

## Human Review Needed

- Boot/debug access.
- Clocking.
- Power pins and decoupling.
- Package footprint.

