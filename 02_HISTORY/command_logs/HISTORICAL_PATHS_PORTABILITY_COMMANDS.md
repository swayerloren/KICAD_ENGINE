# Historical Paths Portability Commands

Date: `2026-05-09`
Task type: `DOCS_ONLY`

## Commands Run

```powershell
Get-Content AGENTS.md -TotalCount 260
Get-Content README_GPT.md -TotalCount 220
Get-Content "FOR CHAT GPT.MD" -TotalCount 220
Get-Content 00_CODEX_START/START_HERE.md -TotalCount 260
Get-Content 00_CODEX_START/SESSION_START_CHECKLIST.md -TotalCount 220
Get-Content 00_CODEX_START/STRUCTURE_STANDARD.md -TotalCount 220
Get-Content 00_CODEX_START/FOLDER_ROUTING_RULES.md -TotalCount 220
Get-Content 00_CODEX_START/PATH_PORTABILITY_RULES.md -TotalCount 220
Get-Content 00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md -TotalCount 220
Get-Content 00_CODEX_START/CURRENT_PROJECT.md -TotalCount 220
Get-Content 00_CODEX_START/PROMPT_COUNTER_RULES.md -TotalCount 220
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content 00_CODEX_START/MEMORY_INDEX.generated.md -TotalCount 120
Get-Content 00_CODEX_START/HISTORY_INDEX.generated.md -TotalCount 120
Get-Content 00_CODEX_START/CONTROL_PLANES.md -TotalCount 180
Get-Content 05_OUTPUTS/release_readiness/PORTABILITY_TOOLCHAIN_AUDIT_REPORT.md -TotalCount 260
Get-Content README.md -TotalCount 260
Get-Content ONE_PROMPT_START.md -TotalCount 240
git grep -n -I -e "C:\\Users\\LJ" -e "C:/Users/LJ" -e "C:\\Program Files\\KiCad" -e "C:/Program Files/KiCad" -- README.md ONE_PROMPT_START.md 00_CODEX_START docs health_check.py 03_TOOLS setup installer .github
git grep -n -I -e "C:\\Users\\LJ" -e "C:/Users/LJ" -- . ':(exclude)02_HISTORY/**' ':(exclude)04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history/**'
python - <<'PY'
# tracked-file classification scan for absolute-path findings
PY
Get-Content installer/payload/build_payload.py -TotalCount 920
Get-Content installer/payload/PAYLOAD_BUILD_SCRIPT.md -TotalCount 140
Get-Content .prompts/codex/01_AUDIT_KICAD_INSTALL.md -TotalCount 220
Get-Content .prompts/claude/01_AUDIT_KICAD_INSTALL.md -TotalCount 220
Get-Content .prompts/shared/SAFETY_GATES.md -TotalCount 220
Get-Content 00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md -TotalCount 230
Get-Content 03_TOOLS/scripts/kicad_discovery/README.md -TotalCount 200
Get-Content 03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py -TotalCount 220
Get-Content 03_TOOLS/scripts/project_validation/validate_kicad_project.py -TotalCount 220
Get-Content 03_TOOLS/kicad/run_schematic_visual_check.ps1 -TotalCount 140
Get-Content 03_TOOLS/scripts/kicad_libraries/kicad_library_common.py -TotalCount 180
git status --short
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```

## Key Outputs

- Maintenance check result: `PROMPT_COUNT=3`, `MAINTENANCE_DUE=NO`
- Absolute-path scan summary after fixes:
  - `409` tracked files with findings
  - `276` historical-report files preserved unchanged
  - `13` active scripts with common-path or fallback references
  - `3` onboarding docs with explicitly labeled example/historical path content
- No KiCad design files were included in the diff
