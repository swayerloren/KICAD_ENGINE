# STM32U0 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Low-power entry products
- Sensor/control nodes
- Modern replacement candidates for F0/L0-class designs
- Small IoT peripherals

## Design Focus Areas

- newer library support
- low-power modes
- small packages
- exact boot/debug behavior

## When To Avoid

Avoid when a mature ecosystem sample base or higher performance/peripheral set is more important than low-power entry cost.

## AI Agent Selection Rules

- Do not select `STM32U0` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
