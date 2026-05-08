# Local Environment Check Commands

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

No dependencies were installed. MCP was not configured. KiCad project files were not edited.

## PATH Probes

```powershell
where.exe kicad
```
Result: exit code 1. `INFO: Could not find files for the given pattern(s).`

```powershell
where.exe kicad-cli
```
Result: exit code 1. `INFO: Could not find files for the given pattern(s).`

```powershell
where.exe python
```
Result: exit code 1. `INFO: Could not find files for the given pattern(s).`

```powershell
where.exe py
```
Result: `C:\Users\LJ\AppData\Local\Microsoft\WindowsApps\py.exe`

```powershell
where.exe pip
```
Result: exit code 1. `INFO: Could not find files for the given pattern(s).`

```powershell
where.exe node
```
Result: `C:\Program Files\nodejs\node.exe`

```powershell
where.exe npm
```
Result:
```text
C:\Program Files\nodejs\npm
C:\Program Files\nodejs\npm.cmd
```

```powershell
where.exe git
```
Result: `C:\Program Files\Git\cmd\git.exe`

```powershell
where.exe codex
```
Result:
```text
C:\Users\LJ\AppData\Roaming\npm\codex
C:\Users\LJ\AppData\Roaming\npm\codex.cmd
c:\Users\LJ\.vscode\extensions\openai.chatgpt-26.422.71525-win32-x64\bin\windows-x86_64\codex.exe
```

## Version Commands

```powershell
kicad --version
```
Result: failed. `The term 'kicad' is not recognized as the name of a cmdlet, function, script file, or operable program.`

```powershell
kicad-cli version
```
Result: failed. `The term 'kicad-cli' is not recognized as the name of a cmdlet, function, script file, or operable program.`

```powershell
python --version
```
Result: failed. `The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.`

```powershell
py --version
```
Result: `Python 3.12.10`

```powershell
pip --version
```
Result: failed. `The term 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program.`

```powershell
py -m pip --version
```
Result: `pip 25.0.1 from C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\Lib\site-packages\pip (python 3.12)`

```powershell
node --version
```
Result: `v22.15.0`

```powershell
npm --version
```
Result: `10.9.2`

```powershell
git --version
```
Result: `git version 2.52.0.windows.1`

```powershell
codex --version
```
Result: `codex-cli 0.80.0`

```powershell
$PSVersionTable.PSVersion
```
Result: `5.1.26100.8115`

```powershell
(Get-Process -Id $PID).Path
```
Result: `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe`

```powershell
$PSHOME
```
Result: `C:\Windows\System32\WindowsPowerShell\v1.0`

## KiCad Program Files Search

```powershell
Test-Path -LiteralPath 'C:\Program Files\KiCad'
```
Result: exists.

```powershell
Get-ChildItem -LiteralPath 'C:\Program Files\KiCad' -Recurse -Filter 'kicad-cli.exe'
```
Result: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`

```powershell
Get-ChildItem -LiteralPath 'C:\Program Files\KiCad' -Recurse -Filter 'kicad.exe'
```
Result: `C:\Program Files\KiCad\9.0\bin\kicad.exe`

```powershell
Get-ChildItem -LiteralPath 'C:\Program Files\KiCad' -Directory
```
Result: `C:\Program Files\KiCad\9.0`

## Full-Path KiCad Version Probe

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' version
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' --version
& 'C:\Program Files\KiCad\9.0\bin\kicad.exe' --version
```
Result: timed out after 124 seconds before returning version output.

Follow-up process check:
```powershell
Get-Process | Where-Object { $_.ProcessName -like 'kicad*' } | Select-Object ProcessName, Id, Path
```
Result: two KiCad processes were present:
```text
kicad 6476  C:\Program Files\KiCad\9.0\bin\kicad.exe
kicad 12952 C:\Program Files\KiCad\9.0\bin\kicad.exe
```

Cleanup command:
```powershell
Stop-Process -Id 6476 -Force
Stop-Process -Id 12952 -Force
```
Result: both probe-launched KiCad processes were stopped. A follow-up process check returned no KiCad processes.

## File Metadata Version Check

```powershell
(Get-Item -LiteralPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe').VersionInfo
```
Result:
```text
FileVersion      : 9.0.7.43852
ProductVersion   : 9.0.7
ProductName      : KiCad EDA
OriginalFilename : kicad.exe
```

```powershell
(Get-Item -LiteralPath 'C:\Program Files\KiCad\9.0\bin\kicad.exe').VersionInfo
```
Result:
```text
FileVersion      : 9.0.7.43852
ProductVersion   : 9.0.7
ProductName      : KiCad EDA
OriginalFilename : kicad.exe
```
