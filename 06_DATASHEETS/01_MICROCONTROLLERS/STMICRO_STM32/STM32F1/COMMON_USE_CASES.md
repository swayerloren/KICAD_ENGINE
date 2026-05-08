# STM32F1 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Legacy industrial controllers
- Simple USB FS devices on supported parts
- Classic CAN 2.0 nodes on supported parts
- Education and reference-board migration

## Design Focus Areas

- legacy ecosystem
- Blue Pill clone risk
- BOOT0/recovery access
- SWD pins not overloaded

## When To Avoid

Avoid for new designs needing current low-power/security features, modern USB-C assumptions, or lifecycle margin without an ST lifecycle check.

## AI Agent Selection Rules

- Do not select `STM32F1` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
