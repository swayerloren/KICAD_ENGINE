# Issue Log: Final Production Structure Public Release Blockers

Date: 2026-05-03
Status: OPEN
Severity: HIGH_FOR_PUBLIC_RELEASE

## Issue

KiCad Engine structure is internally usable, but the source workspace is not public-release-ready without release hygiene work.

## Blockers

- Exclude local dependency and environment folders from public source/payload releases.
- Review or exclude PDFs and copied/reference artifacts with unclear redistribution rights.
- Exclude backups, generated outputs, and reference fabrication packages unless explicitly sanitized and documented.
- Scrub or exclude old command logs containing placeholder token/API-key strings copied from third-party docs.
- Verify Git worktree status before release.
- Rebuild and smoke-test installer artifacts on target platforms.
- Keep component/datasheet/package/fab/vendor records marked as placeholders until verified.

## Evidence

- `02_HISTORY/design_reviews/FINAL_PRODUCTION_STRUCTURE_AUDIT.md`
- `05_OUTPUTS/release_readiness/FINAL_STRUCTURE_BLOCKERS.md`
- `05_OUTPUTS/release_readiness/FINAL_STRUCTURE_SCORECARD.md`

## Required Resolution

Resolve or explicitly waive each blocker before claiming `PUBLIC_ALPHA_READY`, `PUBLIC_BETA_READY`, or `PUBLIC_RELEASE_READY`.

