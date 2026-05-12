# High Risk Footprint Rules

## High-Risk Classes

Treat these as high risk:

- microcontrollers and RF modules
- USB-C connectors
- barrel jacks and other edge connectors
- PMOS and reverse-polarity FETs
- regulators
- ESD and TVS devices
- inductors
- fuses
- polarized capacitors
- diodes and LEDs
- switches
- test pads
- mounting holes

## Additional Required Proof

### Modules and MCUs

- package and pad format match
- exposed pad or antenna notes reviewed when applicable
- orientation and keepout implications documented

### Connectors

- package drawing proof
- mounting-hole or shell details reviewed
- mechanical orientation proof
- 3D-model status recorded

### PMOS / Reverse Polarity

- symbol pin to footprint pad mapping proven
- source, drain, and gate mapping checked explicitly

### Regulators / ESD / TVS / Inductors / Fuses

- package drawing checked
- polarity or pin-1 convention checked when applicable

### Test Pads / Mounting Holes

- correct size family recorded
- electrical or mechanical intent documented

## Gate Rule

If a high-risk symbol lacks its extra proof, the footprint/package gate fails.
