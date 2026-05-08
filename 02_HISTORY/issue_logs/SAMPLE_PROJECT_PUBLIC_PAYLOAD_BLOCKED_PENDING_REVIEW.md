# Issue Log - Sample Project Public Payload Blocked Pending Review

Status: `OPEN`

Date: `2026-05-06`

## Issue

The controlled ATtiny85 sample fixture has useful attribution and workflow
documentation, but its KiCad source files and generated evidence must not be
included in public payloads yet.

## Evidence

- `19_TEST_PROJECTS/SAMPLE_PROJECTS_INDEX.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`
- `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.md`

## Current Status

- Public bundle status:
  `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`
- Gate status: `BLOCKED_UNTIL_HUMAN_REVIEW`
- License audit status: `REQUIRES_HUMAN_REVIEW`

## Required Resolution

Before sample source files may be included in a public payload:

1. Human release review must record public bundle status exactly
   `PUBLIC_BUNDLE_ALLOWED`.
2. Attribution must be approved.
3. Included and excluded sample files must be listed.
4. No raw imports, normalized working copies, backups, generated fab outputs,
   or `FAB_READY` files may be bundled.
5. The payload builder must enforce these rules in dry-run before apply mode.

## Current Mitigation

Release rules now default the sample to `LINK_ONLY_PLUS_DOCS`. KiCad source
files, custom footprints, generated visuals, gate-run folders, and fabrication
style outputs are excluded until review is complete.
