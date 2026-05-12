# REAL_WORLD_REPO_FINAL_AUDIT_COMMANDS

Date: `2026-05-12`
Task type: `AUDIT_ONLY`

## Startup / Routing Reads

- `START_HERE_FOR_AI_AGENTS.md`
- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/START_HERE.md`
- `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
- `00_CODEX_START/TASK_ROUTER.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/CURRENT_PROJECT.md`
- `00_CODEX_START/GITHUB_NAVIGATION.md`
- `00_CODEX_START/CURRENT_GITHUB_STATUS.md`
- `PUBLIC_RELEASE_STATUS.md`
- `PUBLIC_RELEASE_CHECKLIST.md`
- `SECURITY.md`
- `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md`
- `21_LICENSE_ATTRIBUTION/THIRD_PARTY_ATTRIBUTION.md`
- prior repair/audit outputs under `T_E_M_P/real_world_repo_audit/` and
  `05_OUTPUTS/release_readiness/`

## Commands Run

```powershell
python health_check.py --repo-root . --no-write
```

```powershell
python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
```

```powershell
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
```

```powershell
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
```

```powershell
python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .
```

```powershell
git diff --cached --name-only
```

```powershell
git status --short -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro' '*.kicad_prl' '*.kicad_sym' '*.pretty/*'
```

```powershell
git status --short
```

```powershell
rg -n "KNOWLEDGE_RETRIEVAL|GITHUB_PUSH_PUBLIC_RELEASE" START_HERE_FOR_AI_AGENTS.md 00_CODEX_START\AI_AGENT_FAST_CONTEXT.md 00_CODEX_START\TASK_ROUTER.md 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md 00_CODEX_START\TASK_TYPE_TO_ALLOWED_ACTIONS.md 00_CODEX_START\TASK_TYPE_TO_BLOCKERS.md 00_CODEX_START\TASK_TYPE_TO_OUTPUTS.md 00_CODEX_START\TASK_TYPE_TO_KNOWLEDGE_MAP.md 00_CODEX_START\TASK_TYPE_TO_TOOL_MAP.md 00_CODEX_START\TASK_TYPE_TO_RULE_MAP.md CLAUDE.md
```

```powershell
rg -n "knowledge_scrape" START_HERE_FOR_AI_AGENTS.md AGENTS.md README_GPT.md "FOR CHAT GPT.MD" 00_CODEX_START\TASK_ROUTER.md 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md 00_CODEX_START\TASK_TYPE_TO_KNOWLEDGE_MAP.md 10_KNOWLEDGE_BASE\retrieval_indexes\TASK_TO_KNOWLEDGE_MAP.md
```

```powershell
rg -n --hidden --glob '!**/.git/**' --glob '!**/node_modules/**' --glob '!**/.venv/**' --glob '!**/venv/**' --glob '!**/__pycache__/**' -e 'ghp_[A-Za-z0-9]{20,}' .
rg -n --hidden --glob '!**/.git/**' --glob '!**/node_modules/**' --glob '!**/.venv/**' --glob '!**/venv/**' --glob '!**/__pycache__/**' -e 'github_pat_[A-Za-z0-9_]{20,}' .
rg -n --hidden --glob '!**/.git/**' --glob '!**/node_modules/**' --glob '!**/.venv/**' --glob '!**/venv/**' --glob '!**/__pycache__/**' -e 'sk-[A-Za-z0-9]{20,}' .
rg --files -g '.env' -g '.env.*' .
```

```powershell
git check-ignore .sfdx\foo
git check-ignore .env
git check-ignore 03_TOOLS\python_envs\foo
git check-ignore 03_TOOLS\node_envs\foo
git check-ignore 03_TOOLS\repos\foo
git check-ignore 21_LICENSE_ATTRIBUTION\license_risk_reviews\foo.txt
git check-ignore 02_HISTORY\knowledge_scrape_migration\datasheet_extraction_logs\foo.txt
git check-ignore 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\routing_rehearsals\foo.txt
git check-ignore 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\tmp_test\foo.txt
```

```powershell
@'
import csv, json, pathlib
root = pathlib.Path('.')
json_path = root / '10_KNOWLEDGE_BASE' / 'source_registry' / 'SOURCE_REGISTRY.json'
csv_path = root / '10_KNOWLEDGE_BASE' / 'source_registry' / 'SOURCE_REGISTRY.csv'
with json_path.open('r', encoding='utf-8') as f:
    data = json.load(f)
with csv_path.open('r', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
print(data.get('row_count'))
print(len(rows))
'@ | python -
```

```powershell
git ls-files | ForEach-Object { if (Test-Path $_ -PathType Leaf) { (Get-Item $_).Length } }
```

## Notes

- No KiCad design files were edited in this audit pass.
- No staging, commit, or push was performed in this audit pass.
- The final push-readiness classification was based on excluding dirty KiCad
  design files and active-project churn from the commit scope.
