# STM32F2 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Legacy high-performance control
- Connectivity-rich embedded boards
- USB/Ethernet-capable designs on supported parts
- Migration review from older ST designs

## Design Focus Areas

- legacy high-performance supply domains
- USB/Ethernet clocking
- larger package footprints
- external memory or PHY routing

## When To Avoid

Avoid for greenfield designs if newer F4/G4/H5/U5 parts meet the requirement with better support or lifecycle position.

## AI Agent Selection Rules

- Do not select `STM32F2` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
