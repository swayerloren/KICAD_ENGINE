# Test Point Pattern

## Purpose

Make bring-up, debug, and manufacturing test practical without cluttering the design.

## Recommended Test Points

- Input power.
- Each regulator output.
- Ground.
- Reset.
- Boot mode pins.
- Programming/debug interface.
- UART console.
- Important bus signals such as CANH/CANL, USB D+/D-, or I2C lines when useful.

## PCB Rules

- Keep test points accessible after assembly.
- Avoid placing test points under large components or connectors.
- Avoid stubs on high-speed or RF nets unless source-backed and reviewed.
- Label test points clearly on silkscreen when space allows.

## Common Mistakes

- Adding test points that break impedance-controlled routing.
- Forgetting ground test points.
- Placing programming pads where a clip cannot reach them.

## Review Gate

Test points require review for accessibility, net correctness, and signal-integrity impact.

