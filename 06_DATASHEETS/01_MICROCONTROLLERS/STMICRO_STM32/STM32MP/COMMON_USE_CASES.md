# STM32MP Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Embedded Linux systems
- Industrial HMI
- Gateway/control products
- High-integration processor boards

## Design Focus Areas

- DDR layout
- PMIC sequencing
- BGA escape
- Linux boot chain
- reference design dependency

## When To Avoid

Avoid if the project does not need Linux/application-class processing or lacks DDR/BGA/high-speed layout capability.

## AI Agent Selection Rules

- Do not select `STM32MP` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
