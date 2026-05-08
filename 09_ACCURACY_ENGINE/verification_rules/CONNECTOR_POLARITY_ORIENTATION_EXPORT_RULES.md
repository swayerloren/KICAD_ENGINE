# Connector Polarity Orientation Export Rules

Status: `ACTIVE_RULES`

## Hard Rules

- Barrel jack orientation must be verified before export approval.
- USB-C orientation must be verified before export approval.
- Connector mating direction must be verified for every connector.
- IC pin 1 must be verified.
- Diode and LED polarity must be verified.
- Polarized capacitor polarity must be verified.
- Pick-and-place rotations must not be trusted blindly.
- Coordinates alone are not proof.

## Evidence Hierarchy

1. KiCad 3D screenshot plus matching footprint geometry.
2. Footprint F.Fab / F.SilkS / F.CrtYd / pad geometry.
3. Manufacturer drawing or product image.
4. BOM/CPL exported data only as a cross-check, not proof.

If evidence is missing or contradictory, classify the export as blocked.

