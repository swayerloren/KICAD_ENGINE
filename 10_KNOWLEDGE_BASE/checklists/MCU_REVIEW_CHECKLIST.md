# MCU Review Checklist

## Required Evidence

- Exact MCU or module part number.
- Exact package.
- Datasheet and reference manual.
- Programming/debug method.
- Boot mode requirements.
- Clocking source.

## Review Steps

- Check all power and ground pins.
- Check decoupling.
- Check analog supply pins.
- Check reset and boot pins.
- Check programming/debug pins.
- Check clock pins and load capacitors if used.
- Check USB/CAN/UART/I2C/SPI pin mapping.
- Check symbol pinout against datasheet.
- Check footprint against package drawing.

## Stop Conditions

Stop if any power pin, boot pin, programming pin, package suffix, or footprint is unverified.

