# Linux Installer Build

Status: source support is present. AppImage and DEB artifacts should be built on a Linux runner and smoke-tested across representative distros before release.

## Current Builder Config

`installer/electron-builder.yml` includes Linux targets:

- `AppImage`
- `deb`
- `x64`

The configured artifact name is:

`KiCad-Engine-Installer-${version}-${os}-${arch}.${ext}`

RPM is documented as a future packaging path, but it is not enabled in the first Linux target set until Fedora/RHEL smoke testing is complete.

## Local Linux Prerequisites

- Linux build host or GitHub Actions Linux runner.
- Node.js and npm.
- Python for payload generation and health checks.
- Git.
- Existing clean payload under `installer/payload/repo-template`.

## Build

From the repo root on Linux:

```bash
python3 installer/payload/build_payload.py --source-root . --payload-root installer/payload --max-file-size-mb 5
python3 health_check.py --repo-root installer/payload/repo-template --no-write
cd installer
npm ci
npm run build:linux
```

Expected output folder:

`installer/build/linux`

Expected first artifacts:

- AppImage
- DEB

## GitHub Actions Build

Use:

`.github/workflows/build-linux-installer.yml`

The workflow runs on Ubuntu, builds the clean payload, installs local npm dependencies with `npm ci`, builds Linux artifacts, and uploads `installer/build/linux/**`. It does not install KiCad, collect AI credentials, or modify global KiCad libraries.

## AppImage Strategy

AppImage is the broad-compatibility first Linux artifact. It should be tested on:

- Ubuntu LTS.
- Debian stable.
- Fedora current.
- One Arch-family distro if possible.

AppImage support may still require distro-specific desktop integration and FUSE behavior checks.

## DEB Strategy

DEB is the first package-manager-native target for:

- Ubuntu LTS.
- Debian stable.
- Debian-derived desktop distros.

Validate install/uninstall behavior with a disposable VM before release.

## RPM Strategy

RPM is planned for:

- Fedora.
- RHEL-compatible distros.
- openSUSE only after explicit testing.

Do not enable RPM release artifacts until package metadata, dependency behavior, signing, install paths, and uninstall behavior are tested on Fedora/RHEL-family systems.

## Manual tar.gz Fallback

If AppImage/DEB/RPM is not appropriate, users can install manually:

1. Download a release source archive or clean payload archive.
2. Extract it under `~/KICAD_ENGINE`.
3. Run `bash setup/linux/check_linux_requirements.sh`.
4. Run `bash setup/linux/setup_linux.sh`.
5. Open the folder in VS Code.

The fallback must not include restricted PDFs, final fab outputs, local developer caches, or credentials.

## Smoke Test Checklist

Before calling the Linux installer usable:

1. Test AppImage on Ubuntu/Debian and at least one non-apt distro.
2. Test DEB on Ubuntu/Debian.
3. Choose `~/KICAD_ENGINE`.
4. Confirm no writes occur under `/usr`, `/opt/kicad`, system KiCad folders, or global KiCad libraries.
5. Confirm install commands require explicit user confirmation.
6. Confirm manual install guidance appears when no supported package manager is available.
7. Confirm workspace copy completes.
8. Confirm `README.md`, `06_DATASHEETS`, `08_COMPONENT_DATABASE`, and `.vscode` exist.
9. Confirm health check report generation.
10. Confirm VS Code opens the workspace or folder fallback works.

Do not mark Linux production-ready until AppImage, DEB, and manual fallback behavior are tested on clean systems.
