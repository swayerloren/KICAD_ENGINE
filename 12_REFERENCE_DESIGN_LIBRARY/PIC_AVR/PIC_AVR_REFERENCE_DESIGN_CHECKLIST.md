# PIC And AVR Reference Design Checklist

## Source And License

- Microchip or open hardware owner identified.
- License recorded.
- Redistribution status recorded.

## Technical Review

- Exact MCU family, part, and package identified.
- MCLR/reset reviewed.
- ICSP or programming method reviewed.
- Oscillator circuit reviewed.
- VDD/VSS pins and decoupling reviewed.
- USB/CAN/UART/I2C/SPI interfaces reviewed where present.
- 5 V and 3.3 V compatibility reviewed.

## Reuse Warnings

- Do not load programming pins incorrectly.
- Do not assume board silkscreen pin names equal MCU package pins.
- Do not copy old clone board design choices without source review.

## Human Review Needed

- Programming/debug header.
- Reset/MCLR.
- Voltage-domain compatibility.
- Footprint and pinout.

