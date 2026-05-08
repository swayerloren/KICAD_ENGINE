# Artifact Naming

Status: `ACTIVE_RULES`

## Installer Artifacts

- `KiCad-Engine-Setup-Windows-x64.exe`
- `KiCad-Engine-Setup-macOS-universal.dmg`
- `KiCad-Engine-Setup-Linux-x64.AppImage`
- `KiCad-Engine-Setup-Linux-amd64.deb`

## Payload Artifact

- `KICAD_ENGINE_PAYLOAD.zip`

## Checksum Artifact

- `SHA256SUMS.txt`

## Rules

- Include version in release metadata, not by changing these base artifact names unless release automation requires it.
- Do not use `final` in artifact names unless a human-approved release has passed all gates.
- Manufacturing-style outputs must remain `NOT_FINAL`.

