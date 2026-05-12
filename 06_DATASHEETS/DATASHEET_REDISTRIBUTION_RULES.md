# Datasheet Redistribution Rules

## Hard Rules

1. Raw datasheet PDF redistribution requires license review.
2. Extracted PDF markdown inherits the same redistribution risk as the source PDF.
3. Canonical repo docs should prefer source links over copied document payloads.
4. If license is unclear, move the raw file to license quarantine under `21_LICENSE_ATTRIBUTION/license_risk_reviews/`.
5. Public release bundles must not include quarantined datasheet payloads.

## Safe Canonical Alternatives

- source index Markdown
- source registry metadata
- component evidence notes
- package-proof checklists
- high-level engineering summaries

## Current Migration Outcome

The legacy datasheet PDF/markdown intake payload was treated as
license-sensitive. Raw PDFs and extracted markdown were quarantined. Only
indexes, policies, and normalized summaries were promoted to canonical
locations.
