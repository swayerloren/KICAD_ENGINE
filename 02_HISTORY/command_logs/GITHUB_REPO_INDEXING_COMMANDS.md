# GITHUB_REPO_INDEXING_COMMANDS

Date: `2026-05-08`

## Commands Run

```powershell
git status --short --branch
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content README.md
Get-Content CONTRIBUTING.md
Get-Content SECURITY.md
Get-Content .github\README.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\README.md
rg --files 03_TOOLS\scripts
rg --files 14_LAYOUT_AUTOMATION
rg --files 34_PCB_LAYOUT_SANDBOX
rg --files 04_KICAD_PROJECTS
rg --files 05_OUTPUTS\release_readiness
New-Item -ItemType Directory -Force .github\ISSUE_TEMPLATE
git diff --stat
git diff --cached --name-only
git diff --cached --name-only | rg "(\\.lck$|\\.env($|\\.)|secrets|api_keys|local_credentials|99_BACKUPS|routing_rehearsals|copied|imported_originals)"
git add ...
git add -f 05_OUTPUTS\OUTPUTS_INDEX.md
git diff --cached --stat
git commit -m "Add GitHub repo navigation and index layer"
git push -u origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

## Notes

- One attempted `Get-Content FOR CHAT GPT.MD -TotalCount 120` call failed because the path was not quoted; this was corrected with `Get-Content '.\FOR CHAT GPT.MD' -TotalCount 120`.
