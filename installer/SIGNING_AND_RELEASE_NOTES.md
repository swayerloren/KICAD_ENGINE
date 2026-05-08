# Signing And Release Notes

Status: planning only.

## Release Artifact Types

Planned artifacts:

- Windows EXE/MSI.
- macOS DMG/PKG.
- Linux AppImage.
- Linux DEB.
- Linux RPM.
- Source archive.
- Payload manifest.
- Checksums.

## Signing Goals

Windows:

- Authenticode-sign EXE/MSI.
- Publish SHA256 checksum.

macOS:

- Sign with Developer ID.
- Notarize with Apple.
- Staple notarization ticket where applicable.
- Publish SHA256 checksum.

Linux:

- Publish SHA256 checksum.
- Consider GPG-signed checksums and packages.
- Preserve distro package metadata for DEB/RPM.

## Release Notes Required Sections

Each installer release should document:

- Installer version.
- Repo template version.
- Supported platforms.
- KiCad versions tested.
- What is included.
- What is not included.
- Known limitations.
- Security notes.
- Upgrade notes.
- Rollback/uninstall guidance.

## Pre-Release Checklist

- No binaries are created from this plan until explicitly approved.
- Health check passes on a clean payload.
- Secret scan passes.
- Restricted datasheet review passes.
- Prompt pack exists.
- VS Code tasks parse.
- Setup scripts parse.
- Windows installer tested on clean Windows VM.
- macOS installer tested on clean macOS machine or VM.
- Linux installers tested on target distros.
- Checksums generated.
- Signature verification documented.

## Public Naming

Use clear artifact names:

- `KICAD_ENGINE_Setup_Windows_x64_vX.Y.Z.exe`
- `KICAD_ENGINE_Windows_x64_vX.Y.Z.msi`
- `KICAD_ENGINE_macOS_universal_vX.Y.Z.dmg`
- `KICAD_ENGINE_Linux_x86_64_vX.Y.Z.AppImage`
- `kicad-engine_X.Y.Z_amd64.deb`
- `kicad-engine-X.Y.Z.x86_64.rpm`

## Not Final Language

Installer release notes must repeat:

- KiCad Engine does not replace KiCad.
- KiCad Engine uses the user's installed KiCad app.
- AI review is assistance, not fabrication approval.
- Manufacturing-style outputs are not final unless all verification gates pass.
