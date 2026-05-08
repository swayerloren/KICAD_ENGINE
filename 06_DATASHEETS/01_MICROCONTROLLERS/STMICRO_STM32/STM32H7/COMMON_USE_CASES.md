# STM32H7 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- High-end HMI/graphics
- Ethernet and USB HS products
- External SDRAM/OctoSPI systems
- High-rate data acquisition and control

## Design Focus Areas

- complex power tree
- VCAP/SMPS/LDO mode
- impedance-controlled interfaces
- external memory and cache effects

## When To Avoid

Avoid for simple low-cost boards or when the layout team cannot verify high-speed memory/USB/Ethernet constraints.

## AI Agent Selection Rules

- Do not select `STM32H7` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
