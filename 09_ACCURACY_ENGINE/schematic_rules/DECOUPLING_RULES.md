# Decoupling Rules

## Purpose

Prevent missing or arbitrary decoupling decisions.

## Rules

- Use datasheet or reference-design decoupling requirements where available.
- Do not invent capacitor values for exact parts without marking them unverified.
- Place one or more local bypass capacitors per power domain where the source requires it.
- Bulk capacitors must be sized from load, regulator stability, and transient requirements.
- Regulator input/output capacitors must match datasheet stability requirements.
- Crystal load capacitors must be calculated from the crystal and pin capacitance, not guessed.
- Mark all decoupling value assumptions as `UNKNOWN_REQUIRES_SOURCE_VERIFICATION` until sourced.

## Schematic Review Items

- Capacitor value.
- Voltage rating.
- Dielectric class where relevant.
- ESR requirement for regulators.
- Placement requirement for PCB layout.
- Net connection and polarity for electrolytic/tantalum capacitors.

## Exit Criteria

The schematic may use placeholder decoupling only if it is clearly marked as requiring source verification before release.
