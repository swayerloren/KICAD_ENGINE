# Post-Knowledge-Migration Repo Integrity Commands

Date: `2026-05-12`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python health_check.py --no-write
git status --short
rg -n "knowledge_scrape" START_HERE_FOR_AI_AGENTS.md 00_CODEX_START README_GPT.md "FOR CHAT GPT.MD" AGENTS.md 10_KNOWLEDGE_BASE
rg --files -g ".env" -g ".env.*" -g "*.env" -g "*.pem" -g "*.key" -g "id_rsa*" -g "*.p12" -g "*.pfx" .
rg -n --hidden -S "OPENAI_API_KEY|API_KEY=|SECRET_KEY=|TOKEN=|PASSWORD=|PRIVATE KEY|BEGIN RSA PRIVATE KEY|BEGIN PRIVATE KEY" .
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .
python 03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python -m compileall 03_TOOLS/scripts 03_TOOLS/calculators
rg -n "knowledge_scrape_quarantine|rejected_low_value|KNOWLEDGE_SCRAPE_LICENSE_QUARANTINE" 17_RELEASE_BUILD 23_PACKAGE_PROFILES 24_FAB_PROFILES 18_PUBLIC_DOCS docs
rg -n -S "accessToken|refreshToken|instanceUrl|clientSecret|BEGIN PRIVATE KEY|password|token" .sfdx
git diff --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"
git diff --cached --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"
```

## Notable Results

- `health_check.py --no-write`: `PASS=18 WARN=2 FAIL=0`
- repo index rebuild scripts: `PASS`
- knowledge index rebuild: `PASS`
- memory maintenance: `PASS`, prompt counter reset `4 -> 0`
- `03_TOOLS/scripts` compile: `PASS`
- `03_TOOLS/calculators` compile: `PASS`
- source registry JSON/CSV parse: `PASS`
- `knowledge_scrape/`: `REMOVED`
- active startup/knowledge-link scan: `54` local links checked, `0` missing
- public payload quarantine leakage scan: `0` hits
- staged large-file scan: `0` staged files over `10 MB`
- root-local `.sfdx/`: present, untracked, not ignored

