# TASK 001: ESP32-S3 Minimum System

Status: `NOT_RUN`.

## Objective

Ask an AI agent to plan or create a KiCad-native minimum system for an ESP32-S3 module-based custom board. The task measures whether the agent can avoid guessing around module variants, boot straps, reset, power, USB/JTAG, antenna keepout, and symbol/footprint selection.

## Allowed Inputs

- KiCad Engine repo docs and databases.
- Official Espressif datasheets, module datasheets, hardware design guidelines, reference designs, and product pages.
- Installed KiCad symbol and footprint libraries.
- User-provided requirements for power input, programming path, USB use, antenna choice, and board constraints.

## Expected Outputs

- Source-backed design plan or disposable schematic output.
- Component list or BOM draft.
- KiCad symbol candidates and selected symbol rationale.
- KiCad footprint candidates and verification status.
- Power tree and decoupling plan.
- EN/reset, boot/strapping, programming/debug, USB, and antenna/RF review notes.
- ERC report if a schematic is created.
- Human review flags.

## Required Evidence

- Module part number and variant explicitly named.
- Datasheet/source citations for pinout, power pins, boot straps, and module keepout.
- KiCad symbol candidate matched to the exact module variant or flagged as unverified.
- KiCad footprint matched to exact module land pattern or marked `UNVERIFIED_FOOTPRINT`.
- USB/JTAG/UART programming path stated with source-backed constraints.
- Antenna keepout and external antenna connector assumptions stated.

## Scoring Focus

- Correct component selection.
- Correct symbol and footprint handling.
- Power and decoupling completeness.
- Boot/debug correctness.
- Source citations.
- Human review flags.
- No hallucinated exact specs.

## Failure Modes

- Confusing ESP32-S3 bare chips with ESP32-S3 modules.
- Confusing WROOM and WROOM-1U antenna requirements.
- Treating a generic ESP32 footprint as verified for a specific module.
- Omitting EN/reset or boot strap review.
- Claiming fabrication readiness without ERC/DRC and human review.
