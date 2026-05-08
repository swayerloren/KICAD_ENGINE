# Playwright Research Pipeline Commands

Date: 2026-05-03

## Commands Run

| Purpose | Command | Result |
| --- | --- | --- |
| Read startup files | `Get-Content` on `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, and `00_CODEX_START/START_HERE.md` | Completed. |
| Read existing subsystem docs | `Get-Content` on datasheet, component, vendor, supplier, footprint-gap, and supplier-footprint README/policy files | Completed. |
| Create directory skeleton | `New-Item -ItemType Directory -Force` for `31_PLAYWRIGHT_RESEARCH_PIPELINE` subfolders | Created folders. |
| Run pilot dry-run | `node 31_PLAYWRIGHT_RESEARCH_PIPELINE\scripts\dry_run_research_plan.js --target ...\supplier_part_targets.csv --out ...\output\pilot_dry_run` | Passed; 19 targets planned, no live web, no PDFs. |
| Inspect pilot outputs | `Get-Content` on `output\pilot_dry_run\research_plan.json` and generated dry-run report | Completed. |
| JavaScript syntax validation | `node --check` on all pipeline scripts | Passed. |
| Browser capture dry run | `node browser_research_public_page.js --url https://example.com --source dry_run_example --out ...\evidence\dry_run_example` | Passed; no browser launched because `--live` was not provided. |
| Source evidence stub | `node capture_source_evidence.js --source-url https://example.com --source-name dry_run_example --part-number EXAMPLE --out ...\evidence\source_stub_example` | Passed. |
| Research report build | `node build_research_report.js --input ...\output\pilot_dry_run --out ...\reports\PILOT_RESEARCH_OUTPUT_SUMMARY.md` | Passed. |
| Downstream update dry runs | `node update_component_database_stubs.js`; `node update_datasheet_source_indexes.js`; `node update_supplier_indexes.js` | Passed; wrote dry-run reports only. |
| JSON validation | `node -e` parsing `normalized_part_record.template.json` and `scripts/package.json` | Passed. |
| Count pipeline files | PowerShell object counting files, profiles, target CSVs, scripts, and templates | Found 69 files, 16 profiles, 8 target CSVs, 13 script files, 7 templates. |
| Secret-pattern scan | `rg --line-number -i "api[_-]?key\s*[:=]|client[_-]?secret\s*[:=]|password\s*[:=]|token\s*[:=]|secret\s*[:=]" 31_PLAYWRIGHT_RESEARCH_PIPELINE` | Exit code 1; no matches. |
| PDF scan | `Get-ChildItem -LiteralPath '31_PLAYWRIGHT_RESEARCH_PIPELINE' -Recurse -File -Filter '*.pdf'` | No PDF files. |
| KiCad design recent-write scan | `Get-ChildItem -Path '.' -Recurse -Include '*.kicad_sch','*.kicad_pcb','*.kicad_pro','*.kicad_sym','*.kicad_mod'` filtered by recent write time | No results. |
| Risky credential filename scan | `Get-ChildItem` under `31_PLAYWRIGHT_RESEARCH_PIPELINE` for `.env`, `.key`, `.token`, cookies, storage state, and related names | No results. |
| Live-artifact scan | `Get-ChildItem ... | Select-String` for `LIVE_PUBLIC_PAGE`, `live_web_used": true`, `pdfs_downloaded": true`, and `BLOCKED_OR_LOGIN_REQUIRED` | No results. |
| Repo index rebuild | `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .` | Passed. |
| Memory index rebuild | `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .` | Passed. |
| History index rebuild | `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .` | Passed. |
| Known problems rebuild | `python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .` | Passed. |
| AI quality index rebuild | `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .` | Passed and wrote generated AI-quality indexes. |
| Final target file check | `Test-Path` on required pipeline and closeout files | Passed. |
| Final pipeline count check | Counted files, profiles, target CSVs, scripts, and templates under `31_PLAYWRIGHT_RESEARCH_PIPELINE` | 69 files, 16 source profiles, 8 target CSVs, 13 script files, 7 templates. |
| Final safety scans | Re-ran secret-pattern, PDF, live-marker, and KiCad design recent-write scans | No secret-pattern matches, no PDFs, no live markers, no recent KiCad design/library writes. |

## Command Issues

Two attempted live-artifact scans failed because of PowerShell quoting/parameter behavior:

1. `rg --line-number "LIVE_PUBLIC_PAGE|live_web_used\": true|pdfs_downloaded\": true|BLOCKED_OR_LOGIN_REQUIRED" ...`
2. `Select-String ... -Recurse ...`

The check was rerun successfully using `Get-ChildItem -Recurse -File | Select-String`.
