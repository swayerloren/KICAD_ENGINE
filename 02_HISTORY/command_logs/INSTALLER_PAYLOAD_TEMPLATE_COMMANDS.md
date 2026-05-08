# Installer Payload Template Commands

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Git State

Command:

```powershell
git status --short
```

Result:

```text
fatal: not a git repository (or any of the parent directories): .git
```

## Build Script Validation

Command:

```powershell
$tokens = $null
$errors = $null
[System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path installer\payload\build_payload.ps1), [ref]$tokens, [ref]$errors) | Out-Null
if ($errors.Count -gt 0) { $errors | ForEach-Object { $_.Message }; exit 1 } else { 'PowerShell parse PASS' }
```

Result:

```text
PowerShell parse PASS
```

## Payload Build

Command:

```powershell
python installer\payload\build_payload.py
```

Result:

```text
Payload template built: C:\Users\LJ\GitHub\KICAD_ENGINE\installer\payload\repo-template
Manifest: C:\Users\LJ\GitHub\KICAD_ENGINE\installer\payload\payload.manifest.json
Report: C:\Users\LJ\GitHub\KICAD_ENGINE\installer\payload\PAYLOAD_BUILD_REPORT.md
```

Generated report summary:

```text
Files included: 655
Total bytes: 1546205
Generated clean files: 29
Excluded items recorded: 43821
Maximum file size: 5242880 bytes
```

## Payload Health Check

Command:

```powershell
python health_check.py --repo-root installer\payload\repo-template --no-write
```

Result:

```text
KiCad Engine Health Check
Repo root: C:\Users\LJ\GitHub\KICAD_ENGINE\installer\payload\repo-template
PASS=97 WARN=0 FAIL=0
```

## Required Item Check

Command checked that the payload includes:

```text
AGENTS.md
README.md
README_GPT.md
FOR CHAT GPT.MD
START_HERE_FOR_USERS.md
START_HERE_FOR_AI_AGENTS.md
QUICKSTART_WINDOWS.md
QUICKSTART_MACOS.md
QUICKSTART_LINUX.md
.vscode
.codex
.claude
.prompts
00_CODEX_START
01_MEMORY
02_HISTORY
03_TOOLS
04_KICAD_PROJECTS
05_OUTPUTS
06_DATASHEETS
08_COMPONENT_DATABASE
setup
health_check.py
health_check.ps1
LICENSE
DISCLAIMER.md
SECURITY.md
```

Result: all required items were present.

## Exclusion Checks

Command:

```powershell
rg -n "C:\\Users\\LJ|C:/Users/LJ|COMMAND_LINK|COMMAND LINK|ESP32_CSI_WIFI_NODE|api[_-]?key\s*[:=]|access[_-]?token\s*[:=]|password\s*[:=]" installer\payload\repo-template installer\payload\payload.manifest.json installer\payload\PAYLOAD_BUILD_REPORT.md
```

Result: no matches.

Command:

```powershell
Get-ChildItem -Path installer\payload\repo-template -Recurse -File -Include *.pdf,*.zip,*.gbr,*.drl,*.step,*.stl,*.kicad_pcb,*.kicad_sch,*.kicad_pro,*.kicad_sym,*.kicad_mod,*.pyc -ErrorAction SilentlyContinue | Select-Object FullName,Length | Select-Object -First 20
```

Result: no matching forbidden artifact files were reported.

Command:

```powershell
rg -n "[^\x00-\x7F]" installer\payload\PAYLOAD_CONTENT_RULES.md installer\payload\PAYLOAD_BUILD_SCRIPT.md installer\payload\build_payload.ps1 installer\payload\build_payload.py installer\README.md installer\INSTALLER_ARCHITECTURE.md installer\PAYLOAD_MANIFEST.md installer\SECURITY_MODEL.md
```

Result: no non-ASCII matches in new payload/build docs and scripts.

## Generated Cache Cleanup

A Python syntax check created `installer\payload\__pycache__`. It was removed after resolving and verifying the target path was inside `installer\payload`.

Result:

```text
Removed generated cache: C:\Users\LJ\GitHub\KICAD_ENGINE\installer\payload\__pycache__
```
