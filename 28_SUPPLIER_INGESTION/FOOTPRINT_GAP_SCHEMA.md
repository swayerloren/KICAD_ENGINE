# Footprint Gap Schema

## Purpose

Capture package and footprint risk from supplier/manufacturer metadata without falsely approving KiCad footprints.

## Fields

- `manufacturer_part_number`
- `supplier_sku`
- `supplier_package_text`
- `manufacturer_package_text`
- `pin_count`
- `package_drawing_url`
- `package_drawing_status`
- `kicad_symbol_candidates`
- `kicad_footprint_candidates`
- `footprint_match_status`
- `risk_level`
- `risk_notes`
- `human_review_required`

## Status Values

- `FOOTPRINT_VERIFIED_AGAINST_DRAWING`
- `CANDIDATE_ONLY`
- `PACKAGE_TEXT_ONLY`
- `UNVERIFIED`
- `CONFLICTING_PACKAGE_DATA`
- `REQUIRES_HUMAN_REVIEW`

## Rules

- Supplier package text can help find candidates but cannot verify a footprint.
- Connector footprints require exact manufacturer drawing and orientation review.
- Polarity-sensitive and mechanically constrained parts require human review unless exact evidence exists.
