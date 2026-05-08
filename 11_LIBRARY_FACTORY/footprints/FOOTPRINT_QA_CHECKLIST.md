# Footprint QA Checklist

Use before a custom or candidate footprint is used in a KiCad PCB.

## Source Check

- Exact package or connector MPN verified.
- Package drawing recorded.
- Land pattern recorded or calculation documented.
- Pin 1 orientation documented.

## Geometry Check

- Pad count matches source.
- Pad numbering matches source.
- Pad size and pitch match source.
- Drill sizes and slots match source.
- Exposed pad handled intentionally.
- Courtyard exists and encloses required features.
- Fab outline exists.
- Silkscreen does not overlap pads.
- Origin is intentional.
- 3D model status recorded.

## Risk Check

- Connector orientation reviewed.
- Polarity orientation reviewed.
- RF/USB/CAN/high-current layout requirements identified.
- PNP rotation risk recorded.

## Exit Status

- `FOOTPRINT_VERIFIED`: package drawing and QA complete.
- `UNVERIFIED_FOOTPRINT`: evidence incomplete.
- `REJECTED_FOOTPRINT`: mismatch found and not resolved.

