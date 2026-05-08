# Pinout Extraction Rules

## Purpose

Prevent incorrect schematic symbols and symbol-to-footprint mappings.

## Required Extraction

- Exact package or module variant.
- Pin number.
- Pin name.
- Primary function.
- Alternate functions.
- Electrical type.
- Required connection state.
- Special boot/reset/programming behavior.

## Pinout Risks

- Package variants may have different pinouts.
- Modules and bare ICs are not interchangeable.
- Dev board header pins are not package pins.
- Connector pin numbering may be mirrored or orientation-dependent.
- Exposed pads may have electrical and thermal requirements.

## Verification

Pinout status remains `UNVERIFIED_PLACEHOLDER` until every pin is compared against source evidence.

