# Remaining P2/P3 Backlog

Date: 2026-05-03

This backlog intentionally excludes the P0/P1 items fixed in this repair pass.

## P2 Backlog

1. Replace remaining scaffold-heavy README/INDEX files in non-core folders with subsystem-specific content.
2. Regenerate payload template after exclusion rules are reviewed and validated.
3. Add a payload dry-run/report-only mode or update CI to pass an explicit write/build flag.
4. Validate Bash scripts on Linux/macOS or with shellcheck.
5. Add curated public-history summaries so old command logs can be excluded from public release without losing important lessons.
6. Convert link-only datasheet source indexes into verified per-part records for high-risk components.
7. Expand component records with real source links and package drawing status.
8. Build non-generated public examples that are clearly `EXAMPLE_ONLY`.
9. Improve broken-reference scanner to distinguish examples, wildcards, optional folders, and generated future paths.
10. Add public-release attribution summaries for every third-party tool mentioned in docs.

## P3 Backlog

1. Improve installer UX and smoke-test reporting across Windows/macOS/Linux.
2. Add automated public payload audit in CI.
3. Add structured JSON outputs for release readiness scorecards.
4. Build richer footprint-gap reports from installed KiCad libraries.
5. Add schema validation for component/supplier/footprint match records.
6. Create a public release branch/process that excludes private history, local outputs, and copied third-party logs.
7. Continue replacing generic AI-agent prompt wording with tested, task-specific workflows.
8. Add benchmark runner tooling after benchmark tasks are manually reviewed.

## Still Blocked Until Human Review

- Public redistribution of local PDFs.
- Public release archive composition.
- Final release license/attribution review.
- Any claim that KiCad Engine is public-release ready or comparable to commercial cloud PCB AI tools in tested capability.
