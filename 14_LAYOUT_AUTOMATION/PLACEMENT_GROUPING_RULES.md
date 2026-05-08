# Placement Grouping Rules

## Purpose

Define how components are grouped before automatic placement.

## Grouping Principle

Place by function and routing dependency, not by raw reference order.

## Required Groups

- `MECHANICAL`
- `RF`
- `POWER_INPUT`
- `POWER_REGULATION`
- `USB_PATH`
- `MCU_SUPPORT`
- `CONTROL_UI`
- `VISUAL_UI`
- `TEST`
- `LOW_RISK_PASSIVES`

## Rules

- Keep current-flow components in one physical chain for power input and regulation.
- Keep USB connector, ESD, CC, and series resistors in one USB group.
- Keep decoupling capacitors with the IC or module they support.
- Keep reset and boot controls close enough to the target MCU/module but accessible.
- Keep LEDs where they remain visible and do not interfere with cable insertion.
- Keep test pads in orderly rows or columns, not mixed into dense functional clusters.

## Blockers

Placement grouping fails if:

- power-path components are scattered across unrelated areas
- USB protection is not grouped near the connector
- decoupling is not grouped near power pins
- test pads are buried behind connector shells or inaccessible areas
- RF keepout is treated as just another group instead of a hard exclusion area
