# How To Verify A Footprint

Footprint errors are high-risk. A matching footprint name is not enough.

## Required Evidence

Verify against the exact manufacturer part number and package drawing:

- Package body size.
- Pin or pad count.
- Pad numbering.
- Pad pitch.
- Pad shape and size.
- Drill sizes for through-hole parts.
- Courtyard and keepout.
- Pin 1 marker.
- Connector mating direction.
- Board-edge or mechanical constraints.
- 3D model alignment if used.

## KiCad Inspection

Inspect:

- Assigned footprint in schematic fields.
- Footprint instance in `.kicad_pcb`.
- Project-local `fp-lib-table`.
- User-global and stock library resolution.
- `.kicad_mod` pad definitions.

## High-Risk Parts

Always require human review for:

- USB-C connectors.
- RF connectors.
- Automotive connectors.
- Board-to-board connectors.
- Microcontrollers with many package variants.
- Regulators with exposed pads.
- Crystals and oscillators.
- Polarized parts.

## Approval Language

Use:

```text
Footprint candidate found, not verified.
```

Only use:

```text
Footprint verified against manufacturer drawing.
```

when the drawing and exact KiCad footprint have both been reviewed.
