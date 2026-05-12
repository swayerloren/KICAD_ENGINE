# KiCad Docs Knowledge Move Session

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Scope

Drain `knowledge_scrape/01_kicad_core`,
`02_kicad_python_api`, `03_kicad_file_formats`, and
`04_kicad_libraries_symbols_footprints` into canonical repo locations.

## What Changed

- Created canonical normalized KiCad docs under:
  - `10_KNOWLEDGE_BASE/kicad_core/`
  - `10_KNOWLEDGE_BASE/kicad_python_api/`
  - `10_KNOWLEDGE_BASE/kicad_file_formats/`
  - `10_KNOWLEDGE_BASE/kicad_libraries/`
- Created `03_TOOLS/scripts/kicad_api/safe_pcbnew_helpers.py`
- Updated repo rules and library/tool READMEs
- Reclassified the four source folders in the migration config and ledger
- Moved `649` source files out of `knowledge_scrape/`
- Removed all four source folders after draining them

## Move Result

- Files moved from target folders: `649`
- Files quarantined: `641`
- Files archived to history: `8`
- Source folders remaining from this phase: `0`
- `knowledge_scrape` file count before phase: `2503`
- `knowledge_scrape` file count after phase: `1854`

## Validation

- Target source files remaining in `knowledge_scrape/`: `0`
- New canonical docs contain source-registry references: `PASS`
- `safe_pcbnew_helpers.py` syntax check: `PASS`
- Task contract validation: `PASS`
- AI-quality closeout records created: `PASS`
- Index rebuild after migration: `PASS`
- No KiCad design-file state changed during this task

## Closeout Records

- Task contract report written:
  - `02_HISTORY/sessions/2026-05-11_kicad_docs_knowledge_move_task_contract_report.md`
- AI-quality records written:
  - `02_HISTORY/ai_self_reviews/20260511_170757_KiCad_Docs_Knowledge_Move_Self_Review.md`
  - `02_HISTORY/ai_scorecards/20260511_170757_KiCad_Docs_Knowledge_Move_Scorecard.md`
  - `02_HISTORY/claim_evidence_matrices/20260511_170757_KiCad_Docs_Knowledge_Move_Claim_Evidence_Matrix.md`
  - `02_HISTORY/uncertainty_logs/20260511_170757_KiCad_Docs_Knowledge_Move_Uncertainty_Log.md`
  - `02_HISTORY/hallucination_risk_logs/20260511_170757_KiCad_Docs_Knowledge_Move_Hallucination_Risk_Log.md`
- Follow-up issue recorded:
  - `02_HISTORY/issue_logs/20260511_170638_Remaining_knowledge_scrape_migration_after_KiCad_docs_move.md`
- Resolved failed-attempt note recorded:
  - `02_HISTORY/failed_attempts/20260511_170717_KiCad_docs_move_closeout_argument_validation_mismatch.md`

## Result

This phase succeeded. The four KiCad documentation/API/file-format/library
folders were drained, canonical summaries were created, raw scrape captures
were removed from `knowledge_scrape/`, and future work should use the new
`10_KNOWLEDGE_BASE/` docs rather than reopening the quarantined captures.
