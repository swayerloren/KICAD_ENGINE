# Post-Knowledge-Migration Repo Integrity Rerun Commands

Date: `2026-05-12`

## Startup / Routing / Maintenance

```powershell
Get-Content START_HERE_FOR_AI_AGENTS.md
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 05_OUTPUTS\release_readiness\REPO_PUSH_BLOCKER_REPAIR_REPORT.md
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
Get-Content "FOR CHAT GPT.MD"
Get-Content 00_CODEX_START\AI_AGENT_FAST_CONTEXT.md
Get-Content 00_CODEX_START\TASK_ROUTER.md
Get-Content 00_CODEX_START\CURRENT_PROJECT.md
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
```

## Health / Index / Maintenance

```powershell
python health_check.py --no-write
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python -m compileall 03_TOOLS\scripts 03_TOOLS\calculators
```

## Registry / Routing / Payload / Security / Git Checks

```powershell
rg -n "knowledge_scrape" START_HERE_FOR_AI_AGENTS.md 00_CODEX_START README_GPT.md "FOR CHAT GPT.MD" AGENTS.md README.md
git status --short
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
git diff --cached --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```

Additional checks were executed through inline Python helpers to:

- parse `SOURCE_REGISTRY.json`
- parse `SOURCE_REGISTRY.csv`
- parse generated startup JSON indexes
- verify task-map / retrieval-map existence
- check active-doc Markdown links
- confirm no quarantine/raw-content references under public/release/package docs
- confirm staged-file count and staged large-file count
- confirm `.sfdx/` and `knowledge_scrape/` absence
- recompute live SHA-256 hashes for sch/pcb/pro

