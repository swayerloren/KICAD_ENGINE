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
2. Rotate, flip, mirror, or reposition symbols before adding local label
   shortcuts.
3. Passive support parts belong next to the functional block they support.
4. Local MCU support parts belong next to the pins they affect and should read
   as one physically wired cluster when the path is short.
5. Power entry should appear before regulator and system rails.
6. USB interface parts should sit together, not split across the page.
7. Power symbols should read naturally with supply generally above the local
   circuitry and return generally below when that improves readability.
8. Short local control connections should prefer direct orthogonal wires over
   avoidable loopback or S-shaped paths.
9. Mechanical notes and mounting-hole notes should not interrupt active circuit
   flow.
10. Block headings are recommended and should match the actual function of the
    region.

## Audit And Human Review Expectations

The read-only block-layout audit plus human review should detect:

- missing block headings
- missing expected grouped content
- block-flow disorder
- symbols too close together
- symbols that cannot be assigned cleanly to a functional block
- symbols left in awkward orientation only to preserve labels
- local MCU support parts detached from the pins they control
- short local control paths using avoidable loopback wiring

Current automation may not catch every one of these layout failures, so human
review remains mandatory.
