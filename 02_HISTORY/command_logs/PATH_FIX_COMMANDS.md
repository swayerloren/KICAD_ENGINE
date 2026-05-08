# PATH Fix Commands

Date: 2026-04-30

Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Scope

Fix user-level PATH readiness for KiCad Engine tools without installing tools, modifying KiCad project files, generating fabrication outputs, changing machine-level PATH, or changing MCP permissions.

## Files Read First

```text
02_HISTORY\design_reviews\KICAD_ENGINE_FINAL_SETUP_AUDIT.md
03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md
00_CODEX_START\TOOL_INDEX.md
AGENTS.md
00_CODEX_START startup files
```

## Confirm Actual Paths

```powershell
Test-Path 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
Test-Path 'C:\Program Files\KiCad\9.0\bin\kicad.exe'
Test-Path 'C:\Program Files\nodejs\node.exe'
Test-Path 'C:\Program Files\nodejs\npm.cmd'
Test-Path 'C:\Program Files\Git\cmd\git.exe'
Get-Command kicad-cli,kicad,python,py,pip,git,node,npm
where.exe kicad-cli; where.exe kicad; where.exe python; where.exe py; where.exe pip; where.exe git; where.exe node; where.exe npm
py -0p
py --version
py -m pip --version
py -3.12 -c "import sys, sysconfig, site; ..."
```

Result:

```text
kicad-cli.exe: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
kicad.exe: C:\Program Files\KiCad\9.0\bin\kicad.exe
py.exe: C:\Users\LJ\AppData\Local\Microsoft\WindowsApps\py.exe
python.exe: C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe
Python Scripts: C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\Scripts
pip module: C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pip
pip.exe: not found
git.exe: C:\Program Files\Git\cmd\git.exe
node.exe: C:\Program Files\nodejs\node.exe
npm: C:\Program Files\nodejs\npm.ps1 and npm.cmd
```

## Direct Full-Path Tests

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' version
& 'C:\Program Files\KiCad\9.0\bin\kicad.exe' --version
& 'C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe' --version
& 'C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe' -m pip --version
& 'C:\Program Files\Git\cmd\git.exe' --version
& 'C:\Program Files\nodejs\node.exe' --version
& 'C:\Program Files\nodejs\npm.cmd' --version
```

Result:

```text
kicad-cli: 9.0.7
kicad.exe --version: exit code 0, no version text printed
Python: 3.12.10
python -m pip: pip 25.0.1
git: 2.52.0.windows.1
node: v22.15.0
npm: 10.9.2
```

## User PATH Update

```powershell
[Environment]::SetEnvironmentVariable('Path', $newUserPath, 'User')
```

Added entries:

```text
C:\Program Files\KiCad\9.0\bin
C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64
C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\Scripts
```

Then reordered only those newly added entries so `python` resolves to Python 3.12 instead of KiCad's bundled Python:

```text
C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64
C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\Scripts
C:\Program Files\KiCad\9.0\bin
```

Machine PATH was not modified.

## Restart-Independent PATH Verification

```powershell
$env:Path = ([Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'))
Get-Command kicad-cli,kicad,python,py,pip,git,node,npm
kicad-cli version
python --version
python -m pip --version
git --version
node --version
npm --version
```

Result:

```text
kicad-cli=C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
kicad=C:\Program Files\KiCad\9.0\bin\kicad.exe
python=C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe
py=C:\Users\LJ\AppData\Local\Microsoft\WindowsApps\py.exe
pip=NOT_FOUND
git=C:\Program Files\Git\cmd\git.exe
node=C:\Program Files\nodejs\node.exe
npm=C:\Program Files\nodejs\npm.ps1
kicad-cli=9.0.7
python=Python 3.12.10
python -m pip=pip 25.0.1
git=git version 2.52.0.windows.1
node=v22.15.0
npm=10.9.2
```

Two earlier new-process wrapper attempts had PowerShell quoting/pipeline construction errors. They did not change PATH or project files; the final encoded-command verification above passed.

## Health Check Rerun

```powershell
$env:Path = ([Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'))
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\kicad_engine_health_check.ps1'
```

Result:

```text
Before: PASS=68 WARN=9 FAIL=0
After:  PASS=72 WARN=5 FAIL=0
```

Report updated:

```text
03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md
```

