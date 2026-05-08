# Release Workflow README

This folder contains GitHub Actions workflows for building KiCad Engine installer artifacts.

The workflows do not publish public releases automatically. The release workflow creates a draft release only and requires manual `workflow_dispatch`.

## Canonical Workflows

- `build-installer-windows.yml`: builds the Windows NSIS installer on `windows-latest`.
- `build-installer-macos.yml`: builds the macOS DMG on `macos-latest`.
- `build-installer-linux.yml`: builds Linux AppImage and DEB artifacts on `ubuntu-latest`.
- `build-all-installers.yml`: calls all three platform builders and assembles a combined artifact set.
- `release-draft.yml`: calls all three platform builders, assembles assets, and creates a GitHub draft release.

Older experimental workflow names may exist during migration, but the workflows above are the release-builder entry points.

## Artifact Names

Release assets are normalized to:

- `KiCad-Engine-Setup-Windows-x64.exe`
- `KiCad-Engine-Setup-macOS-universal.dmg`
- `KiCad-Engine-Setup-Linux-x64.AppImage`
- `KiCad-Engine-Setup-Linux-amd64.deb`
- `KICAD_ENGINE_PAYLOAD.zip`
- `SHA256SUMS.txt`

Build logs and payload build reports are also uploaded as artifacts.

## Safety Guarantees

- Payload is built before installer packaging.
- Payload health check runs before packaging.
- Optional ripgrep secret scan runs when `rg` is available.
- No secrets are added to workflow files.
- No paid services are required.
- No release is published automatically.
- `release-draft.yml` creates a draft release only.
- `release-draft.yml` refuses missing tags rather than creating a tag implicitly.

## Manual Release Draft Flow

1. Create and push the intended tag yourself.
2. Run `Create Draft Release` manually from GitHub Actions.
3. Provide the existing tag name.
4. Wait for Windows, macOS, and Linux build jobs.
5. Review the draft release assets, logs, and `SHA256SUMS.txt`.
6. Run clean-machine installer smoke tests before publishing.

## Release Gate

Do not publish a public release until:

- Windows installer is signed or unsigned status is intentionally documented.
- macOS DMG is signed, notarized, and Gatekeeper tested.
- Linux AppImage and DEB are smoke-tested on clean systems.
- Payload is checked for secrets, restricted PDFs, generated final fab outputs, and user-specific KiCad project files.
- Checksums match downloaded artifacts.
