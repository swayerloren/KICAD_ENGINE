# macOS Installer Plan

Status: `MACOS_RUNNER_REQUIRED`

## Target

Create a macOS DMG or PKG that installs a local KiCad Engine workspace and opens VS Code after a read-only health check.

## Default Path

`~/KICAD_ENGINE`

## Dependency Checks

- `/Applications/KiCad/KiCad.app`
- `kicad-cli` inside the KiCad app bundle when present.
- Git.
- Python 3.
- Node/npm.
- VS Code command-line launcher.
- Homebrew.

## Install Strategy

- Use Homebrew only after the user confirms.
- Do not require Homebrew silently.
- Show manual install instructions when Homebrew is missing or declined.
- Do not modify the KiCad app bundle or global KiCad libraries.

## Build Artifact

Planned artifact name:

`KiCad-Engine-Setup-macOS-universal.dmg`

## Signing And Notarization

Production public release should document whether the artifact is signed and notarized. Unsigned builds must be clearly marked as development/test builds.

## Limitations

macOS packaging should be built and smoke-tested on a macOS runner or local macOS machine. Windows-local packaging is not proof of a working macOS installer.

