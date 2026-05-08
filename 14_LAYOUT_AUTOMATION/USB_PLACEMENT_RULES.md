# USB Placement Rules

## Purpose

Define placement logic for USB connector-path components.

## Rules

- USB-C is an edge-facing fixed mechanical part unless requirements prove otherwise.
- USB ESD must be near the USB connector.
- USB CC resistors should remain local to the connector path.
- USB series resistors should remain on a clean, short path between connector-side protection and MCU/module pins.
- Avoid long branches and obvious test-pad stubs on the main USB path.

## Quality Rule

A USB placement is not acceptable if the connector, ESD, CC, or series parts are spaced so far apart that short, clean routing is unlikely.
