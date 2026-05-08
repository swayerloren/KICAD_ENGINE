# STM32L4 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Battery IoT nodes
- USB low-power devices on supported parts
- Sensor fusion
- Industrial low-power control

## Design Focus Areas

- low-power clock tree
- USB clocking
- analog rail filtering
- package-specific pin conflicts

## When To Avoid

Avoid if the design needs highest H7-class performance, integrated wireless, or simpler low-cost G0/U0 economics.

## AI Agent Selection Rules

- Do not select `STM32L4` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
