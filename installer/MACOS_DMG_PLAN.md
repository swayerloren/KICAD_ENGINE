# macOS DMG/PKG Plan

Status: planning only.

macOS support follows Windows after the core installer model is stable.

## Packaging Options

Recommended options to evaluate:

- DMG containing a signed/notarized app wrapper.
- PKG for more traditional installation.
- Tauri app bundle with notarization.
- Lightweight shell bootstrapper plus signed archive for advanced users.

## macOS Install Flow

1. User downloads signed and notarized DMG or PKG.
2. Installer asks for install path, defaulting to a user-writable folder such as `~/Documents/KICAD_ENGINE` or `~/GitHub/KICAD_ENGINE`.
3. Installer refuses system and application folders.
4. Installer copies the repo payload.
5. Installer checks:
   - KiCad installed under `/Applications` or discoverable through `kicad-cli`.
   - `kicad-cli` available.
   - Git installed.
   - Python available as `python3`.
   - Node installed.
   - VS Code installed or `code` command available.
6. Installer offers optional installs through Homebrew when available.
7. Installer runs common setup helpers and `health_check.py`.
8. Installer opens VS Code if available.

## Optional Tool Installation

Use Homebrew when available:

- `brew install git`
- `brew install python`
- `brew install node`
- `brew install --cask visual-studio-code`
- `brew install --cask kicad`

Every install must require explicit confirmation. The installer must show the exact command before running it.

## KiCad Rules

- Do not bundle KiCad in v1.
- Do not write into `/Applications/KiCad` or KiCad support folders.
- Do not edit user global KiCad library tables.
- Treat app-bundle paths and CLI paths as platform-specific and verify them before use.

## Signing And Notarization

Before public macOS release:

- Sign the app or package with a Developer ID certificate.
- Notarize with Apple.
- Staple notarization ticket where applicable.
- Publish SHA256 checksums.

## Acceptance Criteria

- Installer creates a local workspace.
- Health check runs from Python.
- Missing requirements are reported without silent installs.
- Homebrew installs are opt-in only.
- VS Code opens if available.
- No AI credentials are requested or stored.
