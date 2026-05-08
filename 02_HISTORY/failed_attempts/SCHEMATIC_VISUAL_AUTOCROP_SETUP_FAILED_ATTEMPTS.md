# Failed Attempts: Schematic Visual Autocrop Setup

Date: `2026-05-03`

## Missing Visual Workflow Files

The requested startup files did not exist at the beginning of the task:

- `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`
- `03_TOOLS/kicad/run_schematic_visual_check.ps1`

Resolution: both files were created.

## PowerShell Wrapper Path Bug

Initial run:

```powershell
.\03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot .\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -CreateDefaultConfig -NoFailOnFindings
```

Result:

`Python visual crop generator not found: C:\Users\LJ\GitHub\KICAD_ENGINE\scripts\visual\generate_schematic_closeups.py`

Cause: the wrapper resolved the Python helper under repo-root `scripts/visual` instead of `03_TOOLS/scripts/visual`.

Resolution: script path resolution was corrected to use the `03_TOOLS` root.

## PowerShell/Python Heredoc Check

An ad hoc Python package check used Bash-style heredoc syntax in PowerShell and failed with parser errors.

Resolution: reran with PowerShell here-string piped to Python.
