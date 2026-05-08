# Hardcoded Path Portability Audit

Date: `2026-05-08`

## Scope

Tracked docs, prompts, and scripts were searched for:

- `C:\Users\LJ`
- `C:/Users/LJ`
- `C:\Users\LJ\AppData`
- fixed KiCad install paths such as `C:\Program Files\KiCad\9.0`

Post-fix targeted scan count: `162` tracked files with at least one absolute-path hit after excluding ignored local envs/logs and generated release outputs.

## Fixed In This Pass

### User-Facing Or Startup Docs

- `README.md`
- `START_HERE.md`
- `DOWNLOAD_ZIP_START_HERE.md`
- `AGENT_STARTER_PROMPTS.md`
- `LOCAL_SETUP_REQUIREMENTS.md`
- `PORTABILITY_AUDIT.md`
- `docs/LOCAL_DEV_SETUP.md`
- `docs/CODESPACES_SETUP.md`
- `docs/GITHUB_SETUP.md`
- `18_PUBLIC_DOCS/HOW_TO_USE_SAMPLE_PROJECTS_WITH_CODEX.md`
- `README_GPT.md`

Action: moved onboarding to repo-relative wording and `ONE_PROMPT_START.md`.

### Prompt Templates

- `.prompts/codex/*.md`
- `.prompts/claude/*.md`

Action: removed the hardcoded maintainer checkout path and replaced it with generic local-repo wording.

### Path/Tool Guidance

- `00_CODEX_START/PATH_PORTABILITY_RULES.md`
- `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
- `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
- `TROUBLESHOOTING.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_LIBRARY_DISCOVERY_GUIDE.md`
- `03_TOOLS/kicad_library_intelligence/LIBRARY_TABLE_GUIDE.md`

Action: converted maintainer-machine paths to generic examples, `%APPDATA%`, or explicit historical/example language.

## Allowed Or Historical Residuals

### Historical Or Inventory Records

- `00_CODEX_START/TOOL_INDEX.md`
- many files under `04_KICAD_PROJECTS/**/reports/`
- archive sample-project reports under `04_KICAD_PROJECTS/archive/**`
- `README_GPT.md` still references many repo-internal paths, but these are repo-relative context notes rather than a required checkout path

Classification: `HISTORICAL_RECORD` or `MACHINE_SPECIFIC_INVENTORY`

### Generated Library Indexes

- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*.json`
- `29_FOOTPRINT_GAP_ANALYSIS/GENERATED_INDEXES/*`

Classification: `GENERATED_INVENTORY_WITH_MACHINE_LOCAL_URIS`

### Common-Path Fallbacks In Scripts

- `03_TOOLS/scripts/project_validation/validate_kicad_project.py`
- `14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py`
- `03_TOOLS/scripts/kicad_app_audit/*`

Classification: `CONFIGURABLE_COMMON_PATH_FALLBACK`

Reason: these scripts now prefer discovery or overrides first, but they still keep common Windows KiCad path fallbacks.

## Remaining Actionable Gaps

1. Historical tracked reports still contain absolute local paths and may confuse users if read as active setup instructions.
2. Generated KiCad inventory JSON/Markdown files still expose machine-local URIs.
3. `00_CODEX_START/TOOL_INDEX.md` is still valuable but intentionally non-portable; it should remain clearly labeled as a machine-specific inventory source.

## Recommendation

Do not mass-rewrite historical evidence files. Keep the startup path clean, label historical artifacts honestly, and sanitize only the small set of generated indexes or inventory docs that still matter for current onboarding.
