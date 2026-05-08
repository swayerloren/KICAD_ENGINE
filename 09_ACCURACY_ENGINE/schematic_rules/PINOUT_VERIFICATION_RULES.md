# Pinout Verification Rules

## Purpose

Prevent AI-generated schematics from using guessed or mismatched pinouts.

## Required Evidence

- Datasheet pin table.
- Package-specific pinout diagram.
- Reference manual only when it clearly maps to the exact device/package.
- Vendor module hardware design guide for modules.
- Exact manufacturer drawing for connectors.

## Verification Steps

1. Identify exact part number and package.
2. Identify the KiCad symbol library and symbol name.
3. Extract symbol pin numbers and names.
4. Compare every used pin to the source pin table.
5. Check power, ground, exposed pad, no-connect, boot, reset, oscillator, and programming pins.
6. Record conflicts as blockers.

## High-Risk Cases

- MCUs with multiple packages.
- Modules with castellated pads.
- USB-C receptacles.
- RF connectors/modules.
- CAN/LIN/RS485 transceivers.
- Regulators with exposed pads.
- Connectors with mirrored mating views.

## Rule

If pinout evidence is incomplete, schematic creation may continue only with `SYMBOL_PINOUT_UNVERIFIED` and `HUMAN_REVIEW_REQUIRED`.
## Mandatory Evidence Gate

Pinout claims must cite a datasheet, reference manual, module datasheet, connector drawing, verified KiCad symbol inspection, or explicit user-provided source.

If any pinout is inferred, mark:

`PINOUT_UNVERIFIED`

and block schematic approval until source verification is complete.
