# Windows Installer Smoke Test Report

Local time: 2026-05-02 20:36 -04:00

## Summary

Status: PASS for local unsigned Windows build plus packaged-payload smoke test.

This is not a production release approval. The installer is unsigned, uses the default Electron icon, and has not been tested on a clean Windows VM or separate Windows user account.

## Installer Artifact

- Path: `installer/build/windows/KiCad-Engine-Installer-0.1.0-win-x64.exe`
- Size: 100,232,532 bytes.
- SHA-256: `761BEDD1978B1BF9CE5C9B5D4529A794BDEB659149C70FB51EEF8A3AE51AEDDA`
- Authenticode status: `NotSigned`
- Build target: NSIS x64.

## Dependency Status

Detected during smoke test:

- KiCad: found, `9.0.7`.
- Git: found, `git version 2.52.0.windows.1`.
- Python: found, `Python 3.12.10`.
- Node: found, `v22.15.0`.
- npm: found, `10.9.2`.
- VS Code: found.
- winget: found as an available package manager.

No missing required dependencies were observed on this machine. No system dependency install commands were run.

## Smoke Test Method

The GUI EXE was not launched interactively. Instead, the smoke test used the same installer core workspace-copy and health-check modules against the packaged payload at:

`installer/build/windows/win-unpacked/resources/payload`

Temporary target:

`C:\Users\LJ\AppData\Local\Temp\KICAD_ENGINE_INSTALLER_SMOKE_20260503003555\KICAD_ENGINE`

This avoided writing into the real repo or into installed KiCad folders.

## Smoke Test Results

- Workspace folder created: PASS.
- `README.md`, `README_GPT.md`, and `FOR CHAT GPT.MD` present: PASS.
- `06_DATASHEETS` present: PASS.
- `08_COMPONENT_DATABASE` present: PASS.
- Required component database scaffold directories preserved in packaged payload: PASS.
- `.vscode` present: PASS.
- Health check executed from copied workspace: PASS.
- Health result: `PASS=97 WARN=0 FAIL=0`.
- KiCad Program Files modified: NO.
- Files copied by installer core: 668.
- Existing files skipped: 0.

## Issues Found And Fixed

1. Initial Windows build failed because electron-builder tried to extract legacy `winCodeSign-2.6.0.7z`, and 7-Zip could not create Darwin symlinks without Windows symlink privilege.
   - Fix: set `win.signAndEditExecutable: false` for local unsigned Windows smoke builds.

2. The first packaged-payload smoke test lost empty component-database directories because Electron packaging does not preserve empty directories.
   - Fix: updated `build_payload.py` to add small README scaffold files to generated empty directories.

3. Packaged runtime resources initially included payload build scripts containing developer-local sanitization strings.
   - Fix: narrowed Electron `extraResources` to runtime-only payload folders: `repo-template`, `manifests`, and `scripts`.

## Remaining Release Blockers

- Add real installer icon resources.
- Decide whether production builds should re-enable executable resource editing and signing.
- Add Windows code-signing certificate workflow.
- Run the actual GUI EXE on a disposable Windows account or clean VM.
- Validate installer uninstall behavior.
- Generate and publish checksums with release artifacts.
- Confirm SmartScreen/signing behavior for public release.

## Safety Result

- No KiCad design files were modified.
- No writes occurred under `C:\Program Files\KiCad`.
- No tools were installed system-wide.
- No system dependency install commands were run.
- No secrets or private project markers were found in the packaged runtime payload scan.
