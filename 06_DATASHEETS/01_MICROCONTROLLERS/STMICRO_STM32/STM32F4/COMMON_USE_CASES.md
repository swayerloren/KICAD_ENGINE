# STM32F4 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- High-performance control
- USB FS/OTG devices
- Classic CAN nodes on supported parts
- Audio/control boards
- Black Pill-style prototypes with source checks

## Design Focus Areas

- clock tree
- USB clock and routing
- BOOT0 recovery path
- package suffix and footprint matching

## When To Avoid

Avoid when ultra-low power, modern TrustZone/security, or wireless integration is the primary requirement.

## AI Agent Selection Rules

- Do not select `STM32F4` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
