# STM32L0 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Battery sensor nodes
- RTC/wake designs
- Simple low-power control
- Compact low-current embedded products

## Design Focus Areas

- leakage budgeting
- LSE/RTC layout
- VBAT behavior
- low-power pin states

## When To Avoid

Avoid when performance, high-speed interfaces, or large memory dominate over current consumption.

## AI Agent Selection Rules

- Do not select `STM32L0` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
