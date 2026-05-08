# Package Footprint Database Index

Status: `ACTIVE_SCAFFOLD`

## Current Contents

- `README.md`: routing and safety rules for package-to-footprint verification.

## Template Sources

- `../00_INDEX/templates/PACKAGE_VERIFICATION_TEMPLATE.md`
- `../00_INDEX/templates/SYMBOL_FOOTPRINT_MATCH_TEMPLATE.md`

## Required Use

Use this folder when a part record needs exact package evidence before KiCad footprint selection. A footprint remains `UNVERIFIED` until the package drawing, pad numbering, orientation, and land pattern have been checked.

## High-Risk Areas

- USB-C receptacles.
- RF connectors.
- Board-to-board connectors.
- Polarity-sensitive packages.
- Thermal-pad packages.
- Modules with keepouts.

