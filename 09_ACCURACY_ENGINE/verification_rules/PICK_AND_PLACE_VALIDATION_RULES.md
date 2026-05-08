# Pick-And-Place Validation Rules

Status: `ACTIVE_RULES`

## Hard Rules

- Pick-and-place, CPL, and centroid validation is not orientation approval.
- `Mid X`, `Mid Y`, and `Rotation` must be numeric.
- Units must be millimeters.
- Layer must be `Top` or `Bottom`.
- Rotations must be visually checked against rendered PCB/3D evidence and real part orientation.
- Bottom-side parts must be checked for mirroring.
- Mechanical-only parts must not be included unless required.

## Required Manual Checks

- USB-C mouth/off-board orientation.
- Barrel jack female opening/off-board orientation.
- All connector mating directions.
- IC pin 1.
- Diode and LED polarity.
- Polarized capacitor polarity.

