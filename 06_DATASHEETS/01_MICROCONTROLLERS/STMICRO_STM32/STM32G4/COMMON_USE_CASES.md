# STM32G4 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Motor control
- Digital power conversion
- FDCAN nodes
- Analog control loops
- USB-capable control boards on supported parts

## Design Focus Areas

- analog and power ground partitioning
- FDCAN transceiver/protection
- USB/UCPD pins on variants
- switching-noise containment

## When To Avoid

Avoid when the design does not benefit from analog/control features and a simpler G0/U0 device is enough.

## AI Agent Selection Rules

- Do not select `STM32G4` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
