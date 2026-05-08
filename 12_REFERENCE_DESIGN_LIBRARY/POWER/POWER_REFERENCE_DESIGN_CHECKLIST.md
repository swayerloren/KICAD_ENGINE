# Power Reference Design Checklist

## Source And License

- Vendor/project owner identified.
- License and redistribution status recorded.
- Evaluation board or app note revision recorded when available.

## Technical Review

- Input voltage range reviewed.
- Output voltage/current reviewed.
- Regulator package reviewed.
- Inductor, diode, capacitor, and compensation requirements reviewed.
- Thermal path reviewed.
- Layout critical loops reviewed.
- Protection devices reviewed.

## Reuse Warnings

- Do not copy component values without recalculating for the target load.
- Do not copy switching layout without the same package and board constraints.
- Do not copy protection circuits without the target fault environment.

## Human Review Needed

- Thermal margin.
- High-current paths.
- Switching-loop placement.
- Protection/fuse/TVS sizing.

