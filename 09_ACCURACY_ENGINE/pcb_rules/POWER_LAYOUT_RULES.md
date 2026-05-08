# Power Layout Rules

## Scope

Regulators, power inputs, fuses, protection, high-current paths, thermal paths, and return currents.

## Rules

- Follow regulator datasheet layout guidance.
- Keep switcher hot loops small.
- Place input/output capacitors as required by source documents.
- Size traces and copper for current and temperature rise.
- Review thermal pads and vias.
- Keep protection devices close to entry points.
- Separate noisy switching nodes from sensitive analog/RF paths.
- Verify automotive, inductive, or external-cable inputs for transient protection.

## Required Flags

- `POWER_LAYOUT_REVIEW_REQUIRED`
- `THERMAL_REVIEW_REQUIRED`
- `INPUT_PROTECTION_REVIEW_REQUIRED`
- `REGULATOR_STABILITY_REVIEW_REQUIRED`
