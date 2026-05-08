# STM32U5 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Secure battery IoT
- Low-power USB devices on supported parts
- Sensor hubs
- High-integration embedded products

## Design Focus Areas

- SMPS versus LDO order codes
- TrustZone/debug policy
- low-power measurement design
- complex power pins

## When To Avoid

Avoid when exact power-domain review is not possible or when a simpler G0/L0 design meets requirements.

## AI Agent Selection Rules

- Do not select `STM32U5` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
