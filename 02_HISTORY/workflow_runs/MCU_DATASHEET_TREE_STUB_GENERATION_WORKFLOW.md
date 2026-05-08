# Workflow Run: MCU Datasheet Tree Stub Generation

Date: 2026-05-03
Status: `SMOKE_TESTED_ON_REPO_TREE`

## Workflow

Use `03_TOOLS/scripts/datasheet_tree/create_microcontroller_family_content.py` to generate conservative AI-readable microcontroller family content stubs.

## Inputs

- Existing MCU folder tree under `06_DATASHEETS/01_MICROCONTROLLERS`.
- Generator templates under `03_TOOLS/scripts/datasheet_tree/templates`.
- Batch target list covering 48 family/vendor folders.

## Outputs

- 612 new generated Markdown files.
- 141 weak placeholder files replaced using `--overwrite-weak`.
- Generated evidence JSON under `05_OUTPUTS/datasheet_tree`.
- Summary and audit reports.

## Safe Boundaries

- No PDF downloads.
- No web scraping.
- No KiCad design file edits.
- No `--force` overwrite.
- Unknown values remain `UNKNOWN_REQUIRES_SOURCE`.

## Evidence

- `05_OUTPUTS/datasheet_tree/MCU_TREE_GENERATION_RESULTS.json`
- `05_OUTPUTS/datasheet_tree/MCU_TREE_GENERATION_RESULTS_RERUN.json`
- `05_OUTPUTS/datasheet_tree/MCU_TREE_COMPLETION_SUMMARY.md`
- `02_HISTORY/design_reviews/MCU_DATASHEET_TREE_UPGRADE_REPORT.md`
- `02_HISTORY/command_logs/MCU_DATASHEET_TREE_UPGRADE_COMMANDS.md`

## Known Limits

- Stub generation is not datasheet research.
- Source-link fields remain mostly unknown.
- Footprints, symbols, pinouts, and package drawings remain unverified.
- Non-family support folders still need a separate curation pass.
