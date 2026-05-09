# Command Log - Tool Index Portability Fix

Date: `2026-05-09`

## Commands Run

```powershell
Get-Content -Raw AGENTS.md
Get-Content -Raw README_GPT.md
Get-Content -Raw "FOR CHAT GPT.MD"
Get-Content -Raw 00_CODEX_START/START_HERE.md
Get-Content -Raw 00_CODEX_START/TOOL_INDEX.md
Get-Content -Raw 05_OUTPUTS/release_readiness/PORTABILITY_TOOLCHAIN_AUDIT_REPORT.md
Get-Content -Raw README.md
Get-Content -Raw ONE_PROMPT_START.md
Get-Content -Raw health_check.py
Get-Content -Raw 03_TOOLS/scripts/kicad_discovery/find_kicad.py
Get-Content -Raw 03_TOOLS/scripts/python_env_check.py
Get-Content -Raw TOOLS_INDEX.md
Get-Content -Raw 03_TOOLS/TOOLS_INDEX.md
Get-Content -Raw EXTERNAL_DEPENDENCIES.md
Get-Content -Raw LOCAL_SETUP_REQUIREMENTS.md
Get-Content -Raw docs/HEALTH_CHECK.md
Get-Content -Raw 00_CODEX_START/CURRENT_PROJECT.md
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
rg -n "C:\\Users\\LJ|assume|Location:|Root:|Use .*C:\\Users\\LJ" 00_CODEX_START/TOOL_INDEX.md
git status --short
```

## Important Results

- `check_maintenance_due.py` returned `MAINTENANCE_NOT_DUE`
- `00_CODEX_START/TOOL_INDEX.md` contained extensive machine-local inventory data
- the repo already had a portable tool truth layer, so the correct fix was warning-plus-redirect, not removal
