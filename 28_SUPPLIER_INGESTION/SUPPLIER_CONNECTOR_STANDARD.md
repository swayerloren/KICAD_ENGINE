# Supplier Connector Standard

## Purpose

Define the minimum standard for any supplier connector before it is trusted by KiCad Engine.

## Required Files Per Connector

- `README.md`
- `API_NOTES.md`
- `AUTH_REQUIREMENTS.md`
- `RATE_LIMIT_AND_TERMS_NOTES.md`
- `FIELD_MAPPING.md`
- `sample_input.example.json`
- `sample_output.example.json`

## Required Connector Capabilities

- Document official API or approved data-feed path.
- Document authentication requirements without storing credentials.
- Document rate limits and terms notes.
- Map supplier fields to `DATA_NORMALIZATION_SCHEMA.md`.
- Support dry-run or offline CSV/manual input when live API access is unavailable.
- Mark source date, source URL, and verification status.
- Preserve source-specific identifiers without claiming they are universal.

## Prohibited Connector Behavior

- Blind scraping.
- Circumventing supplier protections.
- Storing credentials.
- Downloading datasheets by default.
- Marking footprints as verified from package names alone.
- Claiming live stock/pricing is current without source date.

## Output Requirements

Outputs must include both Markdown and JSON where practical. Generated outputs belong in `normalized/` or `reports/`.
