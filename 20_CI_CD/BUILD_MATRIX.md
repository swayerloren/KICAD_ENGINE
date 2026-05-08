# Build Matrix

Status: `PLANNED`

| Platform | Runner | Artifact | Status |
| --- | --- | --- | --- |
| Windows | `windows-latest` | `KiCad-Engine-Setup-Windows-x64.exe` | Planned |
| macOS | `macos-latest` | `KiCad-Engine-Setup-macOS-universal.dmg` | Planned |
| Linux AppImage | `ubuntu-latest` | `KiCad-Engine-Setup-Linux-x64.AppImage` | Planned |
| Linux DEB | `ubuntu-latest` | `KiCad-Engine-Setup-Linux-amd64.deb` | Planned |
| Payload | all or Ubuntu | `KICAD_ENGINE_PAYLOAD.zip` | Planned |

## Build Rules

- Native platform builds are required for release claims.
- Cross-built artifacts must be labeled experimental unless smoke-tested on target OS.

