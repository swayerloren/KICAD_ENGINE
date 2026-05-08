# Windows Installer Build

Status: first local unsigned Windows EXE build and packaged-payload smoke test completed on 2026-05-02.

## Prerequisites

- Windows.
- Node.js and npm.
- Git.
- Existing clean payload under `installer/payload/repo-template`.

## Build

From `installer/`:

```powershell
npm install
npm run build:win
```

Expected target:

- NSIS EXE installer under `installer/build/windows`.

Current local build note:

- `electron-builder.yml` sets `win.signAndEditExecutable: false` so local unsigned builds do not require the legacy `winCodeSign` extraction path that can fail without Windows symlink privilege.
- Public release builds still need a proper Windows signing plan, icon resources, clean-machine testing, and checksums before being called production-ready.

## Smoke Test

Before calling the Windows installer usable:

1. Run the EXE on a disposable Windows user account or VM.
2. Choose a user-writable workspace such as `C:\Users\<user>\KICAD_ENGINE`.
3. Confirm no writes occur under `C:\Program Files\KiCad`.
4. Confirm missing dependencies are shown before any install command.
5. Confirm `winget` commands require user confirmation.
6. Confirm workspace copy completes.
7. Confirm `health_check.py` writes a report under `05_OUTPUTS/health_checks`.
8. Confirm VS Code opens the installed workspace when requested.

Do not mark this production-ready until signing, checksum, icon resources, and clean-machine smoke tests are complete.
