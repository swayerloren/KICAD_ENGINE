# PCBWay Centroid Format

Status: `ACTIVE_RULES`

## Required Columns

```csv
Designator,Mid X,Mid Y,Rotation,Layer
```

## Rules

- Centroid normally lists SMD placement data.
- `Mid X` and `Mid Y` must be numeric.
- `Rotation` must be numeric.
- `Layer` must be `Top` or `Bottom`.
- Rotations and bottom-side orientation require visual review.

