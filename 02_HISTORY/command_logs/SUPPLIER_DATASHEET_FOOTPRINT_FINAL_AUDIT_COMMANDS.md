# Supplier Datasheet Footprint Final Audit Commands

Date: 2026-05-03

## Commands Run

| Purpose | Command | Result |
| --- | --- | --- |
| Startup reads | `Get-Content` on `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, and startup/policy files | Completed. |
| Datasheet file counts | `Get-ChildItem -LiteralPath '06_DATASHEETS' -Recurse -File` grouped by extension | Found 1,274 Markdown files, 11 CSV files, and 2 PDFs. |
| MCU file counts | `Get-ChildItem -LiteralPath '06_DATASHEETS\01_MICROCONTROLLERS' -Recurse -File` grouped by extension | Found 1,165 Markdown files and 3 CSV files. |
| STM32 master files | `Get-ChildItem -LiteralPath '06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32' -File` | Confirmed STM32 master indexes and CSV files. |
| STM32F1 pilot files | `Get-ChildItem -LiteralPath '06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32F1' -File` | Confirmed STM32F1 pilot content files. |
| PDF scan | `Get-ChildItem -LiteralPath '06_DATASHEETS' -Recurse -File -Filter '*.pdf'` | Found 2 legacy Espressif PDFs. |
| Supplier structure | `Get-ChildItem -LiteralPath '28_SUPPLIER_INGESTION'` and connectors listing | Confirmed 14 connector folders and supplier schema files. |
| Footprint system structure | `Get-ChildItem` on `29_FOOTPRINT_GAP_ANALYSIS` and `30_SUPPLIER_FOOTPRINT_MATCHES` | Confirmed reports, scripts, and match records. |
| Secret scan | `rg --line-number -i "api[_-]?key\s*[:=]|client[_-]?secret\s*[:=]|password\s*[:=]|token\s*[:=]|secret\s*[:=]" 28_SUPPLIER_INGESTION 29_FOOTPRINT_GAP_ANALYSIS 30_SUPPLIER_FOOTPRINT_MATCHES` | Exit code 1, no matches. |
| Credential filename scan | `Get-ChildItem` with risky filename pattern under `28_SUPPLIER_INGESTION` | No files found. |
| Dry-run/default behavior grep | `rg --line-number "DRY_RUN|--live|LIVE_MODE|environment variable|API key|download|scrape|scraping"` | Confirmed dry-run/live-mode guard language. |
| Startup wiring grep | `rg --line-number "28_SUPPLIER_INGESTION|29_FOOTPRINT_GAP_ANALYSIS|30_SUPPLIER_FOOTPRINT_MATCHES|supplier|footprint"` | Confirmed references in `AGENTS.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`; `START_HERE.md` was updated for explicit footprint systems. |
| Connector syntax validation | `python -m py_compile` on four connector scripts and dry-run test script | Passed. |
| Footprint/match syntax validation | `python -m py_compile` on footprint gap and supplier-footprint scripts | Passed. |
| Connector dry-run test | `python 28_SUPPLIER_INGESTION\scripts\test_connectors_dry_run.py` | Passed; wrote `28_SUPPLIER_INGESTION\reports\connector_dry_run\DRY_RUN_TEST_REPORT.md`. |
| AI overview count | PowerShell count of MCU folders with `*_AI_OVERVIEW.md` or `FAMILY_OVERVIEW.md` | Found 48 folders. |
| KiCad project recent-write scan | `Get-ChildItem -Path '.' -Recurse -Include '*.kicad_sch','*.kicad_pcb','*.kicad_pro','*.kicad_sym','*.kicad_mod'` filtered by recent write time | No recent results. |
| Installed KiCad recent-write scan | `Get-ChildItem` under `C:\Program Files\KiCad\9.0\share`, `lib`, and `etc` filtered by recent write time | No recent results. |
| Python cache cleanup | Resolve repo root, verify generated `__pycache__` paths stayed under repo, remove them | Removed 7 generated `__pycache__` folders from validation. |
| Git metadata check | `git status --short` | Failed: this working folder is not recognized as a Git repository. |
| Repo index rebuild | `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .` | Passed. |
| Memory index rebuild | `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .` | Passed. |
| History index rebuild | `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .` | Passed. |
| Known problems rebuild | `python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .` | Passed. |
| AI quality index rebuild | `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .` | Passed and wrote `00_CODEX_START\AI_QUALITY_INDEX.generated.md` and `.json`. |
| Final affected-index refresh | Re-ran history, known-problems, and AI-quality index builders after writing closeout records | Passed. |
| Final target-file sanity check | Checked all required audit, scorecard, blockers, next-steps, session, command, and AI-quality closeout files with `Test-Path` | Passed. |
| Final cache/secret/KiCad safety checks | Checked for leftover `__pycache__`, obvious supplier/footprint secret patterns, recent KiCad design/library writes, and updated startup references | Passed; no cache folders, no secret-pattern matches, no recent KiCad design writes. |
| Final history index refresh | `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .` | Run after final command-log update. |

## Command Issue

An early PDF scan used `Get-ChildItem -LiteralPath '06_DATASHEETS' -Recurse -Include '*.pdf','*.PDF' -File`, which returned noisy/inconclusive output. It was rerun correctly with `-Filter '*.pdf'`; the valid result is the two legacy Espressif PDF paths listed in the final audit.
