# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| `knowledge_scrape/` is removed from the live repo tree | `Path('knowledge_scrape').exists() -> False`; final validation and emptying reports |
| `.sfdx/` is no longer a push blocker | `Path('.sfdx').exists() -> False`; `.gitignore` line `95`; blocker-repair report |
| Source registry is healthy | `SOURCE_REGISTRY.json` parse OK; `SOURCE_REGISTRY.csv` rows `10236` |
| Startup/task maps are present and no longer route through live `knowledge_scrape/` | existence checks for `TASK_TYPE_TO_*` docs; active-doc `rg` shows historical-only mentions |
| No public payload path includes quarantine raw content | targeted scan across `17_RELEASE_BUILD`, `18_PUBLIC_DOCS`, `23_PACKAGE_PROFILES`, `24_FAB_PROFILES`, and `docs` returned `0` hits |
| No KiCad design files changed in this audit | live SHA-256 hashes unchanged; staged KiCad design files `0` |
| Repo is ready to commit/push only if the dirty schematic is excluded | dirty-file audit shows one `PREEXISTING_DIRTY_FILE`, unstaged |

