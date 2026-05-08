# Supplier Footprint Matches Index

## PURPOSE

Route supplier-to-KiCad footprint match records, confidence rules, scripts, and generated reports.

## WHAT_BELONGS_HERE

| Path | Purpose |
| --- | --- |
| `MATCH_SCHEMA.md` | Required supplier-to-KiCad match record fields. |
| `MATCH_CONFIDENCE_RULES.md` | Confidence levels and downgrade/block rules. |
| `HUMAN_REVIEW_REQUIRED_RULES.md` | Human-review triggers and high-risk categories. |
| `matches/digikey/` | Digi-Key supplier match records. |
| `matches/mouser/` | Mouser supplier match records. |
| `matches/jlcpcb/` | JLCPCB supplier match records. |
| `matches/lcsc/` | LCSC supplier match records. |
| `matches/manual_verified/` | Manually entered or reviewed match records, including `EXAMPLE_ONLY` records. |
| `reports/` | Generated match indexes, confidence reports, and unmatched supplier reports. |
| `scripts/` | Safe local scripts for record creation, confidence checking, indexing, and unmatched reporting. |

## WHAT_DOES_NOT_BELONG_HERE

Secrets, private supplier exports, KiCad design files, final footprint approvals without evidence, or downloaded vendor documents with unclear redistribution rights.

## AI_AGENT_RULES

- Read `MATCH_SCHEMA.md`, `MATCH_CONFIDENCE_RULES.md`, and `HUMAN_REVIEW_REQUIRED_RULES.md` before creating or using records.
- Mark example records `EXAMPLE_ONLY`.
- Mark all weak matches `UNVERIFIED` or `MATCHED_BY_PACKAGE_NAME_ONLY`.
- Never use a match record as PCB-ready evidence unless it is drawing-backed and human-review status allows it.

## SAFE_EDIT_RULES

Create and update records only with explicit source fields. Do not delete old records; supersede them with newer evidence and status.

## PUBLIC_RELEASE_NOTES

Example records are safe to publish when clearly marked. Real supplier records need review for private pricing, account metadata, and redistribution restrictions.

