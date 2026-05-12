# Package Drawing Proof Rules

## Acceptable Proof

Package proof should come from the exact part or exact package family.

Preferred evidence:

1. manufacturer package drawing
2. manufacturer recommended land pattern
3. trusted library QA record tied to the same package

## Required Checks

- pad count matches
- pad numbering matches
- body or shell style matches when relevant
- pitch matches
- polarity or pin-1 convention matches
- mechanical orientation implications are documented for connectors

## PMOS Special Rule

For PMOS or reverse-polarity FETs, package proof is incomplete until the symbol
pin mapping to footprint pads is explicitly checked.

## Connector Special Rule

For connectors, package proof is incomplete until the footprint is paired with
mechanical orientation truth. A shell outline alone is not enough.

## Not Allowed

- proof by name similarity alone
- proof by DRC alone
- proof by copied footprint text alone
