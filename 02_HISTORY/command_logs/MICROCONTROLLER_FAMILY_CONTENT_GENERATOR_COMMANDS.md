# Microcontroller Family Content Generator Commands

Date: 2026-05-03
Scope: generator creation and validation

| Step | Command / Action | Result |
| --- | --- | --- |
| Startup reads | `Get-Content` for `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `START_HERE.md`, startup indexes, STM32F1 pilot docs, and `PART_SCHEMA.md` | Completed. |
| Existing script inspection | `Get-ChildItem` under `03_TOOLS/scripts` and `03_TOOLS/scripts/datasheet_tree` | `datasheet_tree` did not previously exist. |
| File creation | `apply_patch` for generator, schema, templates, handoff docs, and logs | Completed. |
| Python syntax validation | `python -m py_compile "03_TOOLS\scripts\datasheet_tree\create_microcontroller_family_content.py"` | PASS. |
| JSON parse validation | `python -c "import json ... family_content_schema.json ..."` | PASS. |
| Dry run | `python "03_TOOLS\scripts\datasheet_tree\create_microcontroller_family_content.py" --vendor STMICRO_STM32 --family STM32F0 --representative-part STM32F030C8T6 --dry-run --json` | PASS; no files written. |
| Template listing | `Get-ChildItem` under templates | All requested templates present. |
| Safety scan | `rg` for `UNKNOWN_REQUIRES_SOURCE`, `--force`, `--dry-run`, download/scrape markers | Confirmed conservative markers and no download implementation. |
| Dry-run output check | `Get-ChildItem` for STM32F0 generated target names | No generated files were created by dry run. |
| KiCad edit check | recent-write scan for `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, `.kicad_sym`, `.kicad_mod` | No recent KiCad design/library edits found. |
| Targeted secret scan | `rg` for private-key/API-key/secret/token patterns in `03_TOOLS/scripts/datasheet_tree` | No matches. |
| Cache cleanup | Removed `03_TOOLS\scripts\datasheet_tree\__pycache__` created by syntax validation after checking path was inside repo | Removed. |
| Cache cleanup verification | `Test-Path "03_TOOLS\scripts\datasheet_tree\__pycache__"` | `False`. |
| Rebuild repo index | `python "03_TOOLS\scripts\indexing\build_repo_index.py" --repo-root .` | Completed. |
| Rebuild memory index | `python "03_TOOLS\scripts\indexing\build_memory_index.py" --repo-root .` | Completed. |
| Rebuild history index | `python "03_TOOLS\scripts\indexing\build_history_index.py" --repo-root .` | Completed. |
| Rebuild known problems | `python "03_TOOLS\scripts\indexing\build_known_problems.py" --repo-root .` | Completed. |
| Rebuild AI quality index | `python "03_TOOLS\scripts\ai_quality\build_ai_quality_index.py" --repo-root .` | Completed. |
| Final deliverable check | PowerShell `Test-Path` loop for generator, schema, templates, audit, and AI quality records | All checked paths exist. |
| Final cache check | `Test-Path "03_TOOLS\scripts\datasheet_tree\__pycache__"` | `False`. |
| Final dry-run side-effect check | `Get-ChildItem` for STM32F0 generated target names | No generated files found. |
| Final handoff/index check | `rg` for generator references in `TOOL_INDEX`, `README_GPT`, `FOR CHAT GPT`, and generated indexes | References present. |

## Notes

The secret scan command returned exit code 1 because `rg` returns 1 when no matches are found; this is the expected no-secret result.
