# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| `knowledge_scrape/_scripts` contained `7` live files before the drain | Direct `Get-ChildItem knowledge_scrape -Recurse -Force` listing plus per-file content inspection |
| All `7` live scripts were moved to history-only storage | `Test-Path knowledge_scrape\\_scripts` returned `False` after `Move-Item` and removal, and the destination `.ps1` files exist in `02_HISTORY\\knowledge_scrape_migration\\obsolete_scripts\\` |
| All `50` unresolved ledger rows are now resolved | Ledger verification script reported `unresolved_count: 0` and `status_counts: { \"MOVED_VALIDATED\": 2546 }` |
| `knowledge_scrape/` no longer contains live files | `validate_knowledge_scrape_empty.py --repo-root .` returned `REMAINING_FILE_COUNT: 0`, `REMAINING_DIRECTORY_COUNT: 0`, `VALIDATION_RESULT: EMPTY_OR_REMOVABLE` |
| Active routing still does not depend on `knowledge_scrape/` | `rg -n \"knowledge_scrape\"` on startup/router/retrieval surfaces found history/index references only; no bad active-route references were identified |
| No KiCad design files changed in this task | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` showed only the preexisting dirty schematic path |
