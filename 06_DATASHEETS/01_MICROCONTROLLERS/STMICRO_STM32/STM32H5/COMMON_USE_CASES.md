# STM32H5 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Secure IoT controllers
- Connected industrial nodes
- Modern USB/CAN/Ethernet-adjacent control where supported
- TrustZone-aware products

## Design Focus Areas

- TrustZone/security lifecycle
- debug authentication/recovery
- power domain details
- newer library support

## When To Avoid

Avoid if the team cannot manage security provisioning, debug lockout recovery, or newer-device support maturity.

## AI Agent Selection Rules

- Do not select `STM32H5` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
