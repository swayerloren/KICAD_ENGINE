# Schematic Block Layout Rules

## Required Blocks

Use distinct visual grouping for:

- input power and protection
- buck regulator
- ESP32 module
- USB-C / ESD / CC / USB2 data path
- reset / boot
- LEDs
- test pads / debug
- mounting holes / mechanical notes

## Layout Rules

1. Each block must occupy a visually coherent region.
2. Passive support parts belong next to the functional block they support.
3. Power entry should appear before regulator and system rails.
4. USB interface parts should sit together, not split across the page.
5. Mechanical notes and mounting-hole notes should not interrupt active circuit
   flow.
6. Block headings are recommended and should match the actual function of the
   region.

## Automatic Audit Expectations

The read-only block-layout audit should detect:

- missing block headings
- missing expected grouped content
- block-flow disorder
- symbols too close together
- symbols that cannot be assigned cleanly to a functional block
