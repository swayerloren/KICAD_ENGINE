# Failed Attempts - ESP32_CSI_WIFI_NODE Real-World Failure Review

Date: 2026-05-07

## Failed Commands

| Command | Failure | Impact |
|---|---|---|
| `Get-ChildItem -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports' -Filter '*FAILURE*','*RISK*'` | PowerShell `-Filter` accepts a single string, not an array. | No design impact; existing-file checks were completed with `Test-Path`. |
| `git diff -- -- 'path1' 'path2' ...` | Incorrect pathspec separator syntax for this repository state; Git returned usage help. | No design impact; content was verified with `Select-String` and report file checks. |
| `git status --short -- ...` | Current working directory is not inside a Git repository according to Git. | No design impact; file creation was verified by successful `apply_patch` and report content checks. |

## Lesson

Use `Test-Path` and `Select-String` for focused verification when the workspace is not available as a Git repository.
