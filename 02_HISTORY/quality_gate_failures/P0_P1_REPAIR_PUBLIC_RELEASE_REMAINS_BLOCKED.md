# Quality Gate Failure: Public Release Remains Blocked

Date: 2026-05-03

Status: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Gate

Public GitHub release readiness.

## Reason

The P0/P1 repair pass improved safety gates, startup wiring, path portability, placeholder cleanup, and script dry-run behavior, but the repo still has unresolved release blockers:

- Local PDFs require redistribution review.
- Historical logs and generated outputs need public-release pruning or curated replacement.
- Bash validation and cross-platform setup verification remain incomplete.
- Component, datasheet, footprint, and supplier data remain partially verified or unverified.
- `ESP32_CSI_WIFI_NODE` remains blocked before PCB update.

## Required Before Passing

- Human legal/release review.
- Clean public payload audit.
- Verified exclusion of unreviewed PDFs, secrets, generated outputs, local environments, and private project data.
- Remaining P2/P3 backlog triage.
