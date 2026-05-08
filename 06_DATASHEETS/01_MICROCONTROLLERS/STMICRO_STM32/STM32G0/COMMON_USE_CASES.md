# STM32G0 Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- Low-cost product control
- USB-C controller-adjacent designs on supported parts
- Small industrial/sensor boards
- F0/F1 migration review

## Design Focus Areas

- low-pin-count pin conflicts
- SWD access preservation
- BOOT behavior differences from F1
- modern small packages

## When To Avoid

Avoid when DSP/FPU, high-speed external memory, graphics, or wireless radio are required.

## AI Agent Selection Rules

- Do not select `STM32G0` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
