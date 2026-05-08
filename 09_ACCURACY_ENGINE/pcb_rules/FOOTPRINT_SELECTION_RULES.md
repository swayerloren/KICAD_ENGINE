# Footprint Selection Rules

## Prime Rule

A footprint is unverified until compared against the exact manufacturer package drawing or land pattern.

## Required Evidence

- Exact manufacturer part number.
- Package drawing.
- Recommended land pattern, if provided.
- KiCad footprint file path.
- Pad count and pad numbering comparison.
- Mechanical orientation and pin 1 marking.

## Required Checks

- Body dimensions.
- Pad pitch.
- Pad size and shape.
- Drill diameter for through-hole parts.
- Exposed pad size and paste treatment.
- Courtyard and fab outlines.
- 3D model path and orientation, if available.

## Status Labels

- `FOOTPRINT_VERIFIED_AGAINST_DRAWING`
- `FOOTPRINT_CANDIDATE_ONLY`
- `UNVERIFIED_FOOTPRINT`
- `PROJECT_LOCAL_COPY_RECOMMENDED`

## Required AI Quality Gate

Any response that recommends a footprint must state package drawing status, footprint verification status, and whether human review is required. Generic connector and RF connector footprints are blocked until exact manufacturer drawing and orientation are reviewed.
