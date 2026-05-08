# Modular Schematic Block Pattern

## Purpose

Keep AI-created schematics understandable by separating functional blocks.

## Recommended Blocks

- Power input and protection.
- Regulators and power tree.
- MCU or main controller.
- Programming/debug.
- Communication interfaces.
- Connectors and harnesses.
- Sensors, drivers, and analog sections.
- Test points and status indicators.

## Naming Rules

- Use descriptive sheet and net names.
- Prefer domain names such as `USB_D_P`, `CANH`, `VBUS_5V`, `3V3`, and `MCU_NRST`.
- Do not create anonymous nets for important interfaces.
- Do not reuse a net name across unrelated domains.

## Agent Workflow

1. Draft the block list in Markdown first.
2. Identify required sources for each block.
3. Create or edit KiCad only after the block plan is approved.
4. Keep a review note for every unverified block.

## Review Gate

If a schematic cannot be explained block by block, stop and reorganize before adding more components.

