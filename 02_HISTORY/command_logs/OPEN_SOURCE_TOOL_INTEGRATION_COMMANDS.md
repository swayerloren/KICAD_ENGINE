# Open-Source Tool Integration Commands

Date: 2026-05-10

## Commands Run

```powershell
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content START_HERE_FOR_AI_AGENTS.md
Get-Content README_GPT.md
Get-Content README.md
Get-Content "FOR CHAT GPT.MD"
Get-Content AGENTS.md
Get-Content THIRD_PARTY_TOOLS_ATTRIBUTION.md
Get-Content 21_LICENSE_ATTRIBUTION\LICENSE_AUDIT.md
Get-Content 22_SECURITY\SECURITY_POLICY.md
Get-Content .gitignore
Get-Content .prompts\README.md
Get-Content 00_CODEX_START\TASK_TYPE_TO_REQUIRED_DOCS.md
rg -n "OPEN_SOURCE_TOOL_USE|open-source tool" 00_CODEX_START\TASK_ROUTER.md 00_CODEX_START\TASK_TYPE_TO_ALLOWED_ACTIONS.md 00_CODEX_START\TASK_TYPE_TO_BLOCKERS.md 00_CODEX_START\TASK_TYPE_TO_OUTPUTS.md
New-Item -ItemType Directory -Force -Path 03_TOOLS\open_source_integrations, 03_TOOLS\open_source_integrations\profiles, setup
python -m py_compile setup\verify_optional_kicad_tools.py
python setup\verify_optional_kicad_tools.py --dry-run
powershell -ExecutionPolicy Bypass -File setup\install_optional_kicad_tools_windows.ps1
git diff --name-only -- "*.kicad_sch" "*.kicad_pcb"
git diff --cached --name-only
```

## Result Summary

- prompt counter incremented from `0` to `1`
- maintenance not due
- required startup and route docs were read
- integration layer files were created
- verifier syntax and dry-run checks passed
- no KiCad design files changed
- no staged files were present
