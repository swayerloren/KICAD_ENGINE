# Real World Repo Audit Summary

Audit date: `2026-05-12`

Final classification: `AUDIT_COMPLETE_READY_FOR_P0_P1_REPAIR`

## Counts

- Total open findings: `16`
- `P0`: `3`
- `P1`: `9`
- `P2`: `4`
- `P3`: `0`

## Release-Relevant Bottom Line

The repo is not blocked by a discovered live secret leak or an oversized tracked file over `50 MB`.

It is still blocked from a clean public-ready claim because:

- license and attribution decisions are unresolved
- retired migration/public-risk payload still ships
- AI startup guidance still has contradictory surfaces
- the starter ZIP is heavier and noisier than a new user needs

## Open P0 Items

1. `RWA-P0-001`: unresolved public-release/license/attribution gate
2. `RWA-P0-002`: retired migration/quarantine-style payload still in tracked public baseline
3. `RWA-P0-003`: no first-class startup route for GitHub push/public-release safety

## Open P1 Items Most Relevant To Release Readiness

1. `RWA-P1-001`: startup companion docs contradict the canonical route
2. `RWA-P1-003`: `CURRENT_PROJECT.md` defaults new users into a blocked live board
3. `RWA-P1-004`: maintainer-path and workspace portability leaks remain
4. `RWA-P1-005`: baseline ZIP payload is too heavy and noisy
5. `RWA-P1-006`: source registry lacks direct confidence/license fields
6. `RWA-P1-009`: no clean passing end-to-end onboarding/demo path

## Already Mitigated During Audit

`.gitignore` was tightened so `21_LICENSE_ATTRIBUTION/license_risk_reviews/` and `02_HISTORY/knowledge_scrape_migration/datasheet_extraction_logs/` no longer present an accidental-stage risk.

## Immediate Repair Order

1. Apply the safe docs-only startup/public-safety repairs.
2. Re-score the startup path and portability path.
3. Run the file-by-file public-payload keep/exclude/move/generate review.
4. Resolve human decisions on license, attribution, default onboarding state, and demo-path intent.
