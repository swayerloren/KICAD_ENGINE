# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| `knowledge_scrape/90_unsorted_review` was drained and removed | `Test-Path knowledge_scrape\\90_unsorted_review` returned `False` |
| `knowledge_scrape/91_rejected_low_value` was drained and removed | `Test-Path knowledge_scrape\\91_rejected_low_value` returned `False` |
| `784` targeted rows were moved and validated | Targeted ledger count script reported `TARGET_ROW_COUNT: 784`, `MOVED_YES_COUNT: 784`, and `MOVED_VALIDATED: 784` |
| Raw low-value copied captures were quarantined instead of promoted | Targeted ledger action counts reported `MOVE_TO_LICENSE_QUARANTINE: 780`; quarantine destination file count matched `780` |
| Only `_scripts` remains under `knowledge_scrape` | Remaining-state check reported `remaining_knowledge_scrape_files=7` and `knowledge_scrape/_scripts` as the only remaining top-level folder |
| No KiCad design files changed in this task | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` showed only the preexisting dirty schematic path |
