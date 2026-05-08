# macOS Installer Build

Status: source support is present. macOS DMG/PKG artifacts must be built on a macOS runner; this Windows workspace cannot produce or smoke-test a real macOS installer.

## Current Builder Config

`installer/electron-builder.yml` includes macOS targets:

- `dmg`
- `pkg`
- `x64`
- `arm64`

The configured artifact name is:

`KiCad-Engine-Installer-${version}-${os}-${arch}.${ext}`

## Local macOS Prerequisites

- macOS runner or macOS development machine.
- Node.js and npm.
- Python for payload generation and health checks.
- Git.
- Existing clean payload under `installer/payload/repo-template`.
- Apple Developer certificate and notarization credentials for public release builds.

## Unsigned Developer Build

From the repo root on macOS:

```bash
python3 installer/payload/build_payload.py --source-root . --payload-root installer/payload --max-file-size-mb 5
python3 health_check.py --repo-root installer/payload/repo-template --no-write
cd installer
npm ci
CSC_IDENTITY_AUTO_DISCOVERY=false npm run build:mac
```

Expected output folder:

`installer/build/macos`

Expected targets:

- DMG
- PKG

Unsigned builds are for local smoke testing only. They are not public release artifacts.

## GitHub Actions Build

Use:

`.github/workflows/build-macos-installer.yml`

The workflow runs on a macOS runner, builds the clean payload, installs local npm dependencies with `npm ci`, and uploads macOS build artifacts. It does not install KiCad, collect AI credentials, or modify global KiCad libraries.

## Smoke Test Checklist

Before calling the macOS installer usable:

1. Run the DMG/PKG on a disposable macOS account or VM.
2. Choose `~/KICAD_ENGINE`.
3. Confirm no writes occur under `/Applications/KiCad`, `/Applications/KiCad/KiCad.app`, or app-bundle internals.
4. Confirm global KiCad libraries and user-global library tables are not modified.
5. Confirm missing dependencies are displayed before any install option.
6. Confirm Homebrew commands require explicit user confirmation.
7. Confirm manual install guidance appears if Homebrew is unavailable.
8. Confirm workspace copy completes.
9. Confirm `README.md`, `06_DATASHEETS`, `08_COMPONENT_DATABASE`, and `.vscode` exist.
10. Confirm health check report generation.
11. Confirm VS Code opens the workspace when requested.

## Release Gates

Do not mark macOS production-ready until:

- DMG and PKG build on macOS CI.
- App and installer are signed.
- Artifacts are notarized and stapled.
- Gatekeeper validation passes on a clean machine.
- Checksums are generated and published.
- A clean-machine smoke test report is recorded.
