# Repo Push Blocker Repair Commands

Date: `2026-05-12`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
Get-Content START_HERE_FOR_AI_AGENTS.md -TotalCount 120
Get-Content 05_OUTPUTS/release_readiness/POST_KNOWLEDGE_MIGRATION_REPO_INTEGRITY_AUDIT.md -TotalCount 160
Get-Content 05_OUTPUTS/release_readiness/POST_KNOWLEDGE_MIGRATION_SECURITY_SCAN.md -TotalCount 160
Get-Content 05_OUTPUTS/release_readiness/POST_KNOWLEDGE_MIGRATION_NEXT_STEPS.md -TotalCount 160
Get-Content 05_OUTPUTS/release_readiness/GITHUB_PUSH_REPORT.md -TotalCount 160
Get-Content 05_OUTPUTS/release_readiness/GITHUB_PUSH_SECURITY_SCAN.md -TotalCount 160
Get-Content 05_OUTPUTS/release_readiness/GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md -TotalCount 160
Get-Content 05_OUTPUTS/release_readiness/GITHUB_PUSH_PLAN.md -TotalCount 160
Get-Content .gitignore -TotalCount 220
Remove-Item -Recurse -Force .sfdx
git status --short
git diff --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"
git diff --cached --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"
git check-ignore -v .sfdx/sentinel.txt knowledge_scrape/sentinel.txt
git check-ignore -v 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups
git check-ignore -v 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit
git status --ignored --short -- .sfdx 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit installer/build installer/node_modules 03_TOOLS/python_envs 03_TOOLS/node_envs node_modules .tool_cache 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals 99_BACKUPS 05_OUTPUTS/clean_sample_candidate_tests
rg -n -S "ghp_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]+|API_KEY|SECRET|TOKEN|PASSWORD|\.env" .
rg -n -S "ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|API_KEY\s*[:=]\s*\S+|SECRET(?:_KEY)?\s*[:=]\s*\S+|TOKEN\s*[:=]\s*\S+|PASSWORD\s*[:=]\s*\S+|BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY" .
rg --files -g ".env" -g ".env.*" -g "*.env" .
Get-ChildItem -Recurse -File | Where-Object { $_.Length -gt 50MB }
```

## Notable Results

- `.sfdx/` existed before repair, contained Salesforce local tooling metadata,
  and showed `0` high-confidence secret hits
- `.sfdx/` removed from working tree
- `.gitignore` now covers `.sfdx/`, retired `knowledge_scrape/`, project
  backups, and project temp audit reports
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups/` now ignored
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit/`
  now ignored
- no `.env` files found
- no staged files
- dirty KiCad design files still limited to the preexisting schematic path

