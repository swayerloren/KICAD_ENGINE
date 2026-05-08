# Automatic Schematic Close-Up Crops Command Log

Date: `2026-05-03`
Scope: visual verification tooling and read-only active-project smoke test.
KiCad design files edited: `NO`

## Key Commands

```powershell
Get-Content -Path .\AGENTS.md
if (Test-Path .\03_TOOLS\kicad\VISUAL_VERIFICATION_WORKFLOW.md) { Get-Content -Path .\03_TOOLS\kicad\VISUAL_VERIFICATION_WORKFLOW.md } else { 'MISSING: 03_TOOLS\kicad\VISUAL_VERIFICATION_WORKFLOW.md' }
if (Test-Path .\03_TOOLS\kicad\run_schematic_visual_check.ps1) { Get-Content -Path .\03_TOOLS\kicad\run_schematic_visual_check.ps1 } else { 'MISSING: 03_TOOLS\kicad\run_schematic_visual_check.ps1' }
Get-Content -Path .\09_ACCURACY_ENGINE\checklists\SCHEMATIC_READY_FOR_PCB_CHECKLIST.md
Get-Content -Path .\README_GPT.md -TotalCount 260
Get-Content -Path '.\FOR CHAT GPT.MD' -TotalCount 340
Get-Content -Path .\00_CODEX_START\START_HERE.md
Get-Content -Path .\00_CODEX_START\SESSION_START_CHECKLIST.md
Get-Content -Path .\00_CODEX_START\CURRENT_PROJECT.md
Get-Content -Path .\00_CODEX_START\STRUCTURE_STANDARD.md -TotalCount 220
Get-Content -Path .\00_CODEX_START\FOLDER_ROUTING_RULES.md -TotalCount 220
Get-Content -Path .\00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md -TotalCount 220
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch export --help
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch export svg --help
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch export pdf --help
Select-String -Path .\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\renders\schematic_electrical_blockers_20260503\ESP32_CSI_WIFI_NODE.svg -Pattern '<text|C\?|R\?|U\?|Footprint|Library|kicad|Device:' -CaseSensitive:$false
@('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe','C:\Program Files\Google\Chrome\Application\chrome.exe') | ForEach-Object { [PSCustomObject]@{Path=$_; Exists=(Test-Path $_)} }
$errors = $null; [System.Management.Automation.PSParser]::Tokenize((Get-Content -LiteralPath .\03_TOOLS\kicad\run_schematic_visual_check.ps1 -Raw), [ref]$errors)
python -m py_compile .\03_TOOLS\scripts\visual\generate_schematic_closeups.py
.\03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot .\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -CreateDefaultConfig -NoFailOnFindings
python .\health_check.py --repo-root . --no-write
python .\03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .
python .\03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python .\03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python .\03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
python .\03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
git status --short
```

## Validation Results

- PowerShell parser validation: `PASS`.
- Python syntax validation: `PASS`.
- Health check: `PASS=131 WARN=0 FAIL=0`.
- KiCad source file timestamps unchanged after the task:
  - `.kicad_pro`: `2026-05-02 14:46:03`
  - `.kicad_sch`: `2026-05-03 07:36:00`
- Repo, memory, history, known-problems, and AI-quality indexes rebuilt.
- `git status --short` returned `fatal: not a git repository`; Git worktree verification is unavailable in this folder.

## Active-Project Autocrop Smoke Test

Command:

```powershell
.\03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot .\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -CreateDefaultConfig -NoFailOnFindings
```

Outputs:

- Full-page SVG: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.svg`
- Full-page PDF: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.pdf`
- Full-page PNG: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.png`
- Visual block config: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/visual_blocks.json`
- Crop folder: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/crops`
- Review: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/CLOSE_UP_REVIEW.md`
- JSON summary: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/CLOSE_UP_REVIEW.json`

Summary:

- Blocks configured: 13.
- SVG crops generated: 13.
- PNG crops generated: 13.
- Visible unannotated-reference blocks: 0.
- Visible footprint/library-field risk blocks: 3.
- Review status: `FAIL`.

## Failed Attempts

- Initial requested visual workflow files were missing and were created during this task.
- First wrapper smoke test failed because the PowerShell script resolved the Python helper path as repo-root `scripts/visual` instead of `03_TOOLS/scripts/visual`. This was fixed and the wrapper was rerun successfully.
- One ad hoc PowerShell/Python heredoc check used Bash-style redirection and failed; subsequent Python package checks used PowerShell here-string piping.

## Notes

- `-NoFailOnFindings` was used so setup smoke testing could complete while preserving the active project visual-review `FAIL` status.
- The workflow is read-only for KiCad files but writes generated verification artifacts and reports.
- Secret-pattern scan produced one documentation-only match for the word `secrets` in `VISUAL_BLOCK_CONFIG_STANDARD.md`; no credential value was found.
