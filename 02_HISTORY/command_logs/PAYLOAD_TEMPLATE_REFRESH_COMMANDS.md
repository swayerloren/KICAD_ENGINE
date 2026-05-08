# Payload Template Refresh Commands

Local time: 2026-05-02 20:24 -04:00

## Commands Run

```powershell
python installer\payload\build_payload.py --source-root . --payload-root installer\payload --max-file-size-mb 5
```

Result: exit code 0. Rebuilt `installer/payload/repo-template` and regenerated payload manifests and report.

```powershell
python health_check.py --repo-root installer\payload\repo-template --no-write
```

Result: `PASS=97 WARN=0 FAIL=0`.

```powershell
rg -n "C:\\Users\\LJ|C:/Users/LJ|COMMAND_LINK|COMMAND LINK|ESP32_CSI_WIFI_NODE|api[_-]?key\s*[:=]|access[_-]?token\s*[:=]|password\s*[:=]" installer\payload\repo-template installer\payload\payload.manifest.json installer\payload\manifests\payload.manifest.json installer\payload\PAYLOAD_BUILD_REPORT.md
```

Result: exit code 1, meaning no matches found.

```powershell
Get-ChildItem -Path installer\payload\repo-template -Recurse -File -Include *.pdf,*.zip,*.gbr,*.drl,*.step,*.stl,*.kicad_pcb,*.kicad_sch,*.kicad_pro,*.kicad_sym,*.kicad_mod,*.pyc -ErrorAction SilentlyContinue
```

Result: no files returned.

```powershell
python -m py_compile installer\payload\build_payload.py
```

Result: exit code 0.

```powershell
[System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path -LiteralPath 'installer\payload\build_payload.ps1'), [ref]$tokens, [ref]$errors)
```

Result: PowerShell parse OK.

```powershell
Remove-Item -LiteralPath installer\payload\__pycache__ -Recurse -Force
```

Result: removed the generated Python syntax-check cache after confirming it resolved under `installer\payload`.

```powershell
Test-Path installer\payload\__pycache__
```

Result: absent.

## Payload Summary

- Files included: 655.
- Total bytes: 1,546,205.
- Generated clean files: 29.
- Excluded items recorded by builder: 43,821.
- Health check: pass.

## Git Note

`git status --short` returned `fatal: not a git repository (or any of the parent directories): .git`, so file change status was not available through Git in this workspace.
