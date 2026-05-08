# STM32L5 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Secure battery IoT
- TrustZone-aware embedded products
- Low-power industrial controllers
- Secure boot prototypes

## Design Focus Areas

- TrustZone configuration
- debug recovery
- secure boot policy
- low-power domains

## When To Avoid

Avoid if the team cannot manage security lifecycle/provisioning or if a newer U5 part is a better fit.

## AI Agent Selection Rules

- Do not select `STM32L5` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
