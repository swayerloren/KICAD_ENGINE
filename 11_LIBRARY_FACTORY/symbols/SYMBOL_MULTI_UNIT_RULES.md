# Symbol Multi-Unit Rules

## When To Use Multi-Unit Symbols

Use multi-unit symbols when:

- The part has many pins and grouping improves readability.
- Power pins should be separated into a power unit.
- Repeated functional blocks exist.
- The established KiCad style for that component family uses units.

## When To Avoid Multi-Unit Symbols

Avoid units when:

- Units make pin mapping harder to verify.
- Pin swaps or hidden dependencies become unclear.
- The part is small enough to remain readable as one unit.

## Required Review

- Verify every unit contains the correct pins.
- Verify no pin appears in multiple units unless intentionally duplicated by KiCad conventions.
- Verify power units are placed in schematics.
- Verify ERC does not hide missing power connections.

## AI Rule

If the agent is uncertain, prefer a simpler visible single-unit symbol for project-local use and document the readability tradeoff.

