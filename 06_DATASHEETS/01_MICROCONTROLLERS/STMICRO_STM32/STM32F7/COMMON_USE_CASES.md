# STM32F7 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Graphics/HMI
- External SDRAM/flash systems
- Ethernet/USB designs
- High-performance control and audio

## Design Focus Areas

- cache-aware firmware implications
- external memory layout
- USB HS PHY decisions
- Ethernet/RMII/MII constraints

## When To Avoid

Avoid for simple low-power or low-cost products where F0/G0/U0/L0-class parts are sufficient.

## AI Agent Selection Rules

- Do not select `STM32F7` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
