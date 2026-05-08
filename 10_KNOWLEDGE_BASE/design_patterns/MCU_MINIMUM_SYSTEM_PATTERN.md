# MCU Minimum System Pattern

## Purpose

Define the minimum schematic evidence an AI agent needs before placing a microcontroller into a KiCad design.

## Required Inputs

- Exact part number and package.
- Datasheet and reference manual.
- Programming/debug method.
- Boot mode requirements.
- Clocking plan.
- Power rail voltage and current estimate.

## Pattern

- Create one schematic block for the MCU.
- Group power pins, reset, boot pins, debug pins, clocks, and interfaces visibly.
- Add decoupling and bulk capacitors near the MCU block.
- Add programming/debug connector before optional peripherals.
- Add test points for reset, boot, UART, and key rails when useful.

## KiCad Agent Rules

- Do not use a generic MCU symbol when an exact part symbol exists.
- If the exact symbol is missing, create a symbol plan but do not fabricate pinout.
- Keep all unverified pins marked `Unknown - requires source verification`.
- Run ERC after schematic creation.

## Review Gate

The MCU block is not approved until every power pin, ground pin, reset pin, boot pin, programming pin, and package footprint is source-verified.

