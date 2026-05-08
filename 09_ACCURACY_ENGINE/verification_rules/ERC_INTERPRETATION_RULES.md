# ERC Interpretation Rules

## Prime Rule

ERC is evidence, not proof of schematic correctness.

## Do Not Claim

- "Schematic is correct" because ERC is clean.
- "Pinout is verified" because ERC is clean.
- "Power design is valid" because ERC is clean.

## Required Interpretation

For every ERC run, record:

- KiCad version.
- Command or wrapper used.
- Schematic path.
- Report path.
- Error/warning count.
- Whether violations were resolved, accepted, or unresolved.

## Limits

ERC does not verify datasheet accuracy, package pinout, connector orientation, component suitability, power budget, or footprint correctness.
