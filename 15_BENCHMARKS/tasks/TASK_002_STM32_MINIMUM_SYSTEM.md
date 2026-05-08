# TASK 002: STM32 Minimum System

Status: `NOT_RUN`

## Objective

Ask an AI agent to plan or create a KiCad-native minimum system for a selected STM32 microcontroller. The task measures whether the agent can avoid guessing around exact part/package selection, boot mode, reset, SWD debug, clocking, power pins, analog supply pins, USB, CAN/FDCAN, symbol choice, and footprint verification.

## Allowed Inputs

- KiCad Engine repo docs and databases.
- Official ST product pages, datasheets, reference manuals, application notes, errata, and board schematics.
- Installed KiCad symbol and footprint libraries.
- User-provided requirements for voltage, clocking, USB, CAN/FDCAN, debug connector, package preference, and board constraints.

## Expected Outputs

- Source-backed minimum-system design plan or disposable schematic output.
- Selected STM32 part and package rationale.
- Component list or BOM draft.
- KiCad symbol candidates and selected symbol rationale.
- KiCad footprint candidates and verification status.
- Power, decoupling, VDDA/VSSA, reset, BOOT0, SWD, clocking, USB, and CAN/FDCAN review notes where applicable.
- ERC report if a schematic is created.
- Human review flags.

## Required Evidence

- Exact STM32 part number and package suffix explicitly named.
- Datasheet/reference citations for pinout, power pins, BOOT0/reset, debug pins, and clocking.
- KiCad symbol candidate matched to the exact part/package or flagged as unverified.
- KiCad footprint matched to exact package drawing or marked `UNVERIFIED_FOOTPRINT`.
- USB and CAN/FDCAN assumptions stated with source-backed constraints when used.
- Human review flags for footprint, connector orientation, oscillator design, power tree, and interface constraints.

## Scoring Focus

- Correct part/package handling.
- Correct symbol and footprint handling.
- Power and decoupling completeness.
- Boot/debug correctness.
- Clocking and analog supply review.
- Source citations.
- Human review flags.
- No hallucinated exact specs.

## Failure Modes

- Using a pinout from a different STM32 package.
- Treating Blue Pill or Nucleo board wiring as proof for a custom bare-MCU design.
- Omitting SWD, BOOT0/reset, VDDA/VSSA, or required decoupling review.
- Selecting a footprint from package name alone.
- Claiming fabrication readiness without ERC/DRC and human review.

