# Cross-Platform Installer Project Commands

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## npm Metadata Check

Commands:

```powershell
npm view electron version --json
npm view electron-builder version --json
node --version
npm --version
```

Results:

```text
electron: "41.5.0"
electron-builder: "26.8.1"
node: v22.15.0
npm: 10.9.2
```

No packages were installed.

## Payload Rebuild

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

## Static Checks

Command:

```powershell
Get-ChildItem -Path installer\src -Recurse -File -Include *.js | ForEach-Object {
  node --check $_.FullName
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
Write-Output 'Node syntax PASS'
```

Result:

```text
Node syntax PASS
```

Command:

```powershell
python -m json.tool installer\package.json > $null
python -m json.tool installer\payload\manifests\dependencies.windows.json > $null
python -m json.tool installer\payload\manifests\dependencies.macos.json > $null
python -m json.tool installer\payload\manifests\dependencies.linux.json > $null
python -m json.tool installer\payload\manifests\payload.manifest.json > $null
Write-Output 'JSON parse PASS'
```

Result:

```text
JSON parse PASS
```

## npm Script Check

Command:

```powershell
npm run --prefix installer
```

Result:

```text
Scripts available in kicad-engine-installer@0.1.0 via `npm run-script`:
  dev
    electron .
  build:win
    electron-builder --win --config.directories.output=build/windows
  build:mac
    electron-builder --mac --config.directories.output=build/macos
  build:linux
    electron-builder --linux --config.directories.output=build/linux
  package
    electron-builder --dir --config.directories.output=build/package
```

## Dependency Detection Smoke Test

Command:

```powershell
node -e "<dependency check script>"
```

Result summary:

```text
platform: windows
winget: found
kicad: found
git: found
python: found
node: found
npm: found
vscode: found
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

## Installer-Core Smoke Test

Command created a disposable workspace under `05_OUTPUTS/installer_smoke_test`, copied the payload, wrote a setup log, and ran health check.

Result:

```text
copied: 656
skipped: 0
PASS=97 WARN=0 FAIL=0
```

## Forbidden Content Checks

Commands checked for:

- developer-specific LJ paths;
- private project markers;
- secret assignment patterns;
- PDFs, fab outputs, KiCad project/source files, and Python bytecode in the payload.

Result: no matches were reported.

## Protected KiCad File Guard

Command checked for modified KiCad design/source files under `04_KICAD_PROJECTS` after the installer work window.

Result: no modified KiCad design/source files were reported.

## Git State

Command:

```powershell
git status --short
```

Result:

```text
fatal: not a git repository (or any of the parent directories): .git
```
