# AI Entrypoint / Retrieval / Tool Knowledge Move Report

Status: `MOVE_APPLIED_AND_VALIDATED`

Date: `2026-05-11`

## Scope

Drained these `knowledge_scrape/` source folders:

- `00_ai_entrypoints`
- `00_retrieval_indexes`
- `00_source_of_truth`
- `11_calculators_ipc_reference`
- `30_eda_automation_verification`

This phase normalized startup routing, retrieval indexes, calculator policy,
calculator stubs, and automation-result validation into canonical repo
surfaces. It did not create a second START_HERE system.

## Files Moved

- Total moved: `40`
- History-only moves: `18`
- License-quarantine moves: `22`

History-only destinations:

- `02_HISTORY/knowledge_scrape_migration/entrypoint_metadata/`
- `02_HISTORY/knowledge_scrape_migration/retrieval_metadata/`
- `02_HISTORY/knowledge_scrape_migration/source_of_truth_metadata/`
- `02_HISTORY/knowledge_scrape_migration/calculator_metadata/`
- `02_HISTORY/knowledge_scrape_migration/automation_metadata/`

Quarantine destination:

- `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/11_calculators_ipc_reference/`

## Entrypoints Updated

- `START_HERE_FOR_AI_AGENTS.md`
- `00_CODEX_START/TASK_ROUTER.md`
- `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
- `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`

## Retrieval Indexes Updated

- `10_KNOWLEDGE_BASE/retrieval_indexes/MASTER_KNOWLEDGE_INDEX.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/KNOWLEDGE_SOURCE_INDEX.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_KNOWLEDGE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_RULE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_TOOL_MAP.md`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv`

## Calculators Created

- `03_TOOLS/calculators/README.md`
- `03_TOOLS/calculators/trace_width_calculator_stub.py`
- `03_TOOLS/calculators/voltage_divider_calculator.py`
- `03_TOOLS/calculators/buck_feedback_calculator.py`
- `03_TOOLS/calculators/rc_filter_calculator.py`
- `10_KNOWLEDGE_BASE/calculators/README.md`
- `10_KNOWLEDGE_BASE/calculators/PCB_CALCULATOR_SOURCE_INDEX.md`
- `10_KNOWLEDGE_BASE/calculators/CALCULATOR_USE_POLICY.md`

## Automation Validation Surfaces Created

- `09_ACCURACY_ENGINE/workflows/EDA_AUTOMATION_VERIFICATION_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/CALCULATOR_RESULT_EVIDENCE_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/AUTOMATION_TOOL_RESULT_VALIDATION_RULES.md`

## Validation

- Every targeted ledger row moved: `40/40`
- Targeted ledger validation status: `MOVED_VALIDATED`
- Calculator Python compile: `PASS`
- START_HERE task-map links present: `PASS`
- Target source folders still exist: `NO`
- `knowledge_scrape` file count before: `831`
- `knowledge_scrape` file count after: `791`
- Remaining top-level live content folders:
  - `_scripts`
  - `90_unsorted_review`
  - `91_rejected_low_value`
- No KiCad design files changed in this phase: `PASS`

## Durable Rules Added

- Future agents must route startup and knowledge lookup through canonical
  `00_CODEX_START` task maps, not drained `knowledge_scrape` entrypoints.
- Calculator output is a first-pass aid only until the formula/source is
  recorded and validated independently.
- Automation-tool results must be checked by KiCad ERC/DRC, parity, or another
  independent check before they are treated as proof.

