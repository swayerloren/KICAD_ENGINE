# AI Entrypoint / Retrieval / Tool Knowledge Move Session

Date: `2026-05-11`

## Summary

Completed the actual move/merge phase for:

- `knowledge_scrape/00_ai_entrypoints`
- `knowledge_scrape/00_retrieval_indexes`
- `knowledge_scrape/00_source_of_truth`
- `knowledge_scrape/11_calculators_ipc_reference`
- `knowledge_scrape/30_eda_automation_verification`

Canonical startup routing now uses `START_HERE_FOR_AI_AGENTS.md`,
`00_CODEX_START/TASK_ROUTER.md`, and the new `TASK_TYPE_TO_*_MAP.md` files.
Canonical calculator policy now uses `10_KNOWLEDGE_BASE/calculators/` and
`03_TOOLS/calculators/`. Automation-result validation now uses the new
workflow and verification rules under `09_ACCURACY_ENGINE/`.

## Results

- Moved files: `40`
- History-only moves: `18`
- Quarantine moves: `22`
- `knowledge_scrape` file count before: `831`
- `knowledge_scrape` file count after: `791`

## Validation

- Calculator scripts compiled successfully.
- START_HERE now links the task maps.
- The five target source folders no longer exist.
- No KiCad design files were changed in this task.
- Task contract validated as `VALID_TASK_CONTRACT`.
- Repo, memory, history, AI-quality, and known-problem indexes were rebuilt.
