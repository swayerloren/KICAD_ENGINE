# Knowledge Scrape Unsorted / Rejected Drain Session

Date: `2026-05-11`

## Summary

Completed the actual drain phase for:

- `knowledge_scrape/90_unsorted_review`
- `knowledge_scrape/91_rejected_low_value`

This phase did real movement, not report-only work. The two source folders were
fully dispositioned and removed. Raw low-value copied captures were routed to
license quarantine instead of any public rejected-content tree, while the
metadata/index stub files were preserved in migration history.

## Results

- Target rows drained: `784`
- History-only moves: `4`
- License-quarantine moves: `780`
- `knowledge_scrape` file count before this phase: `791`
- `knowledge_scrape` file count after this phase: `7`

## Validation

- `knowledge_scrape/90_unsorted_review` no longer exists.
- `knowledge_scrape/91_rejected_low_value` no longer exists.
- All `784` targeted ledger rows are now `MOVED_VALIDATED`.
- Only `knowledge_scrape/_scripts/` remains for a later dedicated migration
  phase.
- No KiCad design files were changed in this task.
- Task contract validated as `VALID_TASK_CONTRACT`.
- Repo, memory, history, AI-quality, and known-problem indexes were rebuilt.
