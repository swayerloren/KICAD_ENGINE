# Claim Evidence Matrix: MCU Datasheet Tree Upgrade

Date: 2026-05-03

| Claim | Status | Evidence |
| --- | --- | --- |
| 48 MCU family/vendor folders were processed. | `VERIFIED_BY_COMMAND` | `05_OUTPUTS/datasheet_tree/MCU_TREE_GENERATION_RESULTS.json`; rerun JSON. |
| 612 new files were created. | `VERIFIED_BY_COMMAND` | First write pass status counts in generated JSON. |
| 141 weak placeholders were overwritten. | `VERIFIED_BY_COMMAND` | First write pass plus rerun status counts. |
| Existing substantive files were not overwritten with `--force`. | `VERIFIED_BY_COMMAND` | Commands used `--overwrite-weak`, not `--force`; skipped records in generated JSON. |
| Generated files mark unknowns as `UNKNOWN_REQUIRES_SOURCE`. | `VERIFIED_BY_FILE` | Spot checks and template contents under `03_TOOLS/scripts/datasheet_tree/templates`. |
| No PDFs were downloaded or scraped. | `VERIFIED_BY_COMMAND` | Generator code is offline; no web/download commands were run. |
| No KiCad design files were edited. | `VERIFIED_BY_COMMAND` | Final modified-file scan for KiCad source/library file types. |
| Remaining weak folders are non-family support/reference folders. | `VERIFIED_BY_COMMAND` | `$rel` / `$name` search results under `06_DATASHEETS/01_MICROCONTROLLERS`. |
