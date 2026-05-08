# Windows Installer Build Commands

Local time: 2026-05-02 20:36 -04:00

## Read First

- `installer/README.md`
- `installer/docs/WINDOWS_INSTALLER_BUILD.md`
- `installer/payload/PAYLOAD_CONTENT_RULES.md`

## Build Preparation

```powershell
rg -n "C:\\Users\\LJ|C:/Users/LJ|COMMAND_LINK|COMMAND LINK|ESP32_CSI_WIFI_NODE|api[_-]?key\s*[:=]|access[_-]?token\s*[:=]|password\s*[:=]|BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY|sk-[A-Za-z0-9]{20,}" installer\payload\repo-template installer\payload\payload.manifest.json installer\payload\manifests\payload.manifest.json installer\payload\PAYLOAD_BUILD_REPORT.md
```

Result: no matches found.

```powershell
python installer\payload\build_payload.py --source-root . --payload-root installer\payload --max-file-size-mb 5
```

Result: exit code 0. Payload rebuilt.

```powershell
npm install
```

Result: exit code 0. Installed local installer npm dependencies under `installer/node_modules` and created `installer/package-lock.json`. npm reported 0 vulnerabilities and deprecated transitive package warnings for `inflight`, `rimraf@2`, `glob@7`, and `boolean`.

```powershell
npm run build:win
```

Initial result: failed while extracting `winCodeSign-2.6.0.7z`; 7-Zip could not create Darwin symlinks because the current Windows shell lacks symlink privilege.

```powershell
$env:CSC_IDENTITY_AUTO_DISCOVERY='false'; npm run build:win
```

Result: failed with the same `winCodeSign` symlink extraction issue.

## Fixes Applied

- Updated `installer/electron-builder.yml` with `win.signAndEditExecutable: false` for local unsigned Windows smoke builds.
- Updated `installer/payload/build_payload.py` so empty generated scaffold directories get small README files and survive Electron packaging.
- Updated `installer/electron-builder.yml` so packaged runtime resources include only `payload/repo-template`, `payload/manifests`, and `payload/scripts`.

## Successful Build

```powershell
npm run build:win
```

Result: exit code 0. Built NSIS installer:

- `installer/build/windows/KiCad-Engine-Installer-0.1.0-win-x64.exe`
- Size: 100,232,532 bytes.
- SHA-256: `761BEDD1978B1BF9CE5C9B5D4529A794BDEB659149C70FB51EEF8A3AE51AEDDA`.
- Authenticode status: `NotSigned`.

## Smoke Test

Smoke test method: used packaged resources from `installer/build/windows/win-unpacked/resources/payload`, copied into a temp folder with the installer core, and ran the copied workspace health check.

Temp target:

- `C:\Users\LJ\AppData\Local\Temp\KICAD_ENGINE_INSTALLER_SMOKE_20260503003555\KICAD_ENGINE`

Result:

- Workspace created.
- Required README files found.
- `06_DATASHEETS` found.
- `08_COMPONENT_DATABASE` found.
- `.vscode` found.
- Health check ran with `PASS=97 WARN=0 FAIL=0`.
- `C:\Program Files\KiCad` last-write timestamp was unchanged.
- No system dependency installation commands were run.

## Final Verification

```powershell
npm audit --audit-level=moderate
```

Result: `found 0 vulnerabilities`.

```powershell
rg -n "C:\\Users\\LJ|C:/Users/LJ|COMMAND_LINK|COMMAND LINK|ESP32_CSI_WIFI_NODE|api[_-]?key\s*[:=]|access[_-]?token\s*[:=]|password\s*[:=]|BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY|sk-[A-Za-z0-9]{20,}" installer\build\windows\win-unpacked\resources\payload installer\payload\repo-template installer\payload\payload.manifest.json installer\payload\manifests\payload.manifest.json installer\payload\PAYLOAD_BUILD_REPORT.md
```

Result: no matches found.

```powershell
Get-ChildItem -Path installer\payload\repo-template -Recurse -File -Include *.pdf,*.zip,*.gbr,*.drl,*.step,*.stl,*.kicad_pcb,*.kicad_sch,*.kicad_pro,*.kicad_sym,*.kicad_mod,*.pyc
```

Result: no files returned.

```powershell
Get-ChildItem -LiteralPath '04_KICAD_PROJECTS' -Recurse -File -Include *.kicad_sch,*.kicad_pcb,*.kicad_pro,*.kicad_sym,*.kicad_mod | Where-Object { $_.LastWriteTime -gt (Get-Date).AddMinutes(-180) }
```

Result: no recently modified KiCad design files found.
