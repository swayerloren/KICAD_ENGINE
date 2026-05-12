# Footprint Gap Rules

## Hard Rules

1. Vendor part number is not footprint proof.
2. Supplier CAD model is not automatically trusted.
3. Land-pattern approval requires exact source evidence.
4. Installed KiCad footprint presence is candidate evidence only.
5. High-risk parts require package drawing, pin mapping, orientation proof, and human review where required.

## High-Risk Classes

- ESP32 modules
- USB-C connectors
- barrel jacks
- PMOS reverse-polarity FETs
- regulators and inductors
- ESD and TVS arrays
- test pads and mounting holes
