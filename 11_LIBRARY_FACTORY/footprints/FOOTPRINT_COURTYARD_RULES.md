# Footprint Courtyard Rules

## Purpose

Courtyards help assembly clearance and DRC checking.

## Rules

- Add `F.CrtYd` for top-side footprints.
- Add `B.CrtYd` for bottom-side-only footprints when needed.
- Courtyard should enclose pads, body, and keepout-relevant mechanical features.
- Use clearance appropriate for the assembly process and board density.
- Keep courtyard closed and easy to inspect.

## Connector Notes

Connector courtyards must include body, mating direction, latch features, shell tabs, and mechanical keepouts when source drawings require them.

## Review Gate

Footprints without a meaningful courtyard remain candidate-only unless there is a documented exception.

