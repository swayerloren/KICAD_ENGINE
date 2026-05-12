# 06_DATASHEETS

Status: `LINK_FIRST_CANONICAL_DATASHEET_SURFACE`

## Purpose

Store datasheet source links, normalized source indexes, redistribution policy,
and safe summaries.

## Canonical Files

- [DATASHEET_INDEX.md](DATASHEET_INDEX.md)
- [DATASHEET_SOURCE_POLICY.md](DATASHEET_SOURCE_POLICY.md)
- [DATASHEET_REDISTRIBUTION_RULES.md](DATASHEET_REDISTRIBUTION_RULES.md)
- [espressif/ESP32_SOURCE_INDEX.md](espressif/ESP32_SOURCE_INDEX.md)
- [microcontrollers/MICROCONTROLLER_SOURCE_INDEX.md](microcontrollers/MICROCONTROLLER_SOURCE_INDEX.md)

## What Belongs Here

- official source links
- normalized source indexes
- datasheet metadata
- safe markdown summaries
- redistribution decisions
- missing-document trackers

## What Does Not Belong Here

- raw scraped PDFs without license review
- extracted PDF markdown copied from restricted PDFs
- KiCad design files
- secrets

## Rules

- Prefer official manufacturer datasheets and application notes.
- Raw datasheet PDFs are not public-source-of-truth by default.
- If redistribution rights are unclear, keep source links here and move raw
  copies to `21_LICENSE_ATTRIBUTION/license_risk_reviews/`.
- Use `10_KNOWLEDGE_BASE/source_registry/` for URL-level provenance.
- Do not claim package, pinout, or land-pattern proof from vendor marketing
  text alone.

## Public Release Notes

Public payloads should remain link-first unless redistribution rights for the
original document are explicitly reviewed and recorded.
