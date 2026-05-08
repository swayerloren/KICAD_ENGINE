# STM32F3 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Motor control
- Power conversion control
- Precision analog front-end control
- Comparator/op-amp/ADC-heavy systems

## Design Focus Areas

- analog partitioning
- VREF and VDDA filtering
- comparator/op-amp pin mapping
- motor-control noise containment

## When To Avoid

Avoid when analog features are not needed and a simpler G0/F0/U0 design is sufficient, or when high-end graphics/connectivity are required.

## AI Agent Selection Rules

- Do not select `STM32F3` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
