# Symbol Footprint Plan

Status: `EXAMPLE_ONLY_PLANNING_ONLY`

## Symbol Plan

- Search project-local libraries first.
- Search user global libraries only as candidates.
- Search installed KiCad libraries as candidates.
- Verify symbol pins against exact module datasheet.

## Footprint Plan

- Identify exact module land pattern.
- Compare pad count, pad numbering, pad size, pitch, outline, and keepout.
- Mark footprint `UNVERIFIED_FOOTPRINT` until compared to source.
- Require human review for USB connector and module orientation.

## 3D Model Plan

- Use 3D model only as mechanical aid.
- Do not treat 3D model as proof of footprint correctness.

