# STM32WL Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Sub-GHz sensor nodes
- LoRa/LPWAN products
- Long-range low-power telemetry
- Wireless industrial monitoring

## Design Focus Areas

- regional RF compliance
- matching network
- antenna/feedline layout
- reference design fidelity

## When To Avoid

Avoid if the project cannot perform RF matching, antenna test, regional compliance review, and exact reference-design matching.

## AI Agent Selection Rules

- Do not select `STM32WL` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
