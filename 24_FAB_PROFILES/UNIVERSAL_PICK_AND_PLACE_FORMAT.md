# Universal Pick-And-Place Format

Status: `ACTIVE_RULES`

Use this internal review format because it maps cleanly to JLCPCB CPL and PCBWay centroid files.

## Columns

```csv
Designator,Mid X,Mid Y,Layer,Rotation
```

## Rules

- Units must be millimeters.
- `Layer` must be `Top` or `Bottom`.
- `Rotation` must be numeric degrees.
- Bottom-side parts must be visually checked for mirroring and rotation.
- Mechanical-only parts must not be included unless explicitly required by the assembly house.
- Rotation validation is only a numeric check; it is not orientation approval.

