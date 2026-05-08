# DRC Interpretation Rules

## Prime Rule

DRC is evidence, not proof of manufacturability.

## Required Interpretation

For every DRC run, record:

- KiCad version.
- Command or wrapper used.
- PCB path.
- Report path.
- Violation count.
- Board setup/rule assumptions.
- Whether zones were refilled before running.

## Limits

DRC does not verify footprint package match, connector orientation, assembly polarity, controlled impedance, board-house capability, enclosure fit, or fab output correctness.
