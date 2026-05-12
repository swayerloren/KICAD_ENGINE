# Follow-Up Items

- Drain `knowledge_scrape/_scripts/` in a dedicated final migration phase.
- After `_scripts` is drained, rerun the empty-check validator and remove the
  top-level `knowledge_scrape/` folder entirely if no files remain.
- If full-ledger normalization is needed later, reconcile any older
  non-90/91 rows still marked `MOVED_PENDING_POST_MOVE_VALIDATION`.
