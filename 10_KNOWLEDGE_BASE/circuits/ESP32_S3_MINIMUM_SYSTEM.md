# ESP32-S3 Minimum System Circuit

## Use Case

Use this pattern for an ESP32-S3 module or bare chip minimum system. Prefer modules unless the user explicitly needs bare-chip RF design.

## Required Evidence

- Exact ESP32-S3 module or chip datasheet.
- Espressif hardware design guidelines.
- Exact KiCad symbol pinout source.
- Exact module footprint drawing and antenna keepout drawing.

## Typical Schematic Block

- 3.3 V power input with adequate local decoupling.
- EN/reset circuit per Espressif guidance.
- Boot/strapping pins handled per the exact module/chip guide.
- UART or USB programming path documented.
- Optional native USB/JTAG connections only when supported by the chosen part.
- Antenna keepout for PCB-antenna modules.

## PCB Review Points

- Keep the antenna keepout clear of copper, planes, traces, components, and enclosure metal as required by the module drawing.
- Place decoupling close to power pins.
- Avoid routing noisy power or clocks under the antenna region.
- Verify module castellated pad footprint against the exact module package.

## Common Mistakes

- Treating ESP32, ESP32-S3, ESP32-C3, and ESP32-C6 strapping pins as interchangeable.
- Forgetting EN pullup/reset behavior.
- Using a WROOM footprint for a MINI module.
- Ignoring antenna keepout.
- Assuming native USB exists on every ESP32-family part.

## Verification Gate

All boot pins, programming pins, power pins, and footprint pads must be checked against the exact module document before schematic approval.

