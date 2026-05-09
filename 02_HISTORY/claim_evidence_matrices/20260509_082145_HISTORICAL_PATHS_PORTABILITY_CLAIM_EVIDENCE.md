# Claim Evidence Matrix - Historical Paths Portability

Date: `2026-05-09`
Task type: `DOCS_ONLY`

| Claim | Evidence |
| --- | --- |
| Historical absolute paths are widespread and mostly live in preserved evidence. | Tracked-file classification scan: `409` files with findings, including `276` `HISTORICAL_REPORT` files. |
| Live onboarding now warns users and agents not to trust old local paths. | Updated `README.md`, `ONE_PROMPT_START.md`, `00_CODEX_START/START_HERE.md`, `00_CODEX_START/PATH_PORTABILITY_RULES.md`, and `docs/PATH_PORTABILITY.md`. |
| The KiCad-install audit prompts no longer assume one fixed maintainer-era install path. | Updated `.prompts/codex/01_AUDIT_KICAD_INSTALL.md` and `.prompts/claude/01_AUDIT_KICAD_INSTALL.md`. |
| Two live Python helpers no longer prefer a single fixed KiCad path first. | Updated `03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py` and `03_TOOLS/scripts/project_validation/validate_kicad_project.py`; `python -m py_compile` passed. |
| No KiCad design files changed. | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` returned no files. |
