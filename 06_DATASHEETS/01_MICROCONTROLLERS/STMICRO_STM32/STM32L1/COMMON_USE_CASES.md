# STM32L1 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Low-power industrial products
- Battery and RTC designs
- Segment LCD products on supported parts
- Legacy L-series maintenance

## Design Focus Areas

- low-power leakage
- LCD pin multiplexing
- VBAT/backup domain
- legacy lifecycle review

## When To Avoid

Avoid for greenfield designs if L4/U0/U5 alternatives provide better support, security, or lifecycle position.

## AI Agent Selection Rules

- Do not select `STM32L1` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
