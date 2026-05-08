# Installer User Guide

KiCad Engine installer support creates a clean local workspace and opens it in VS Code. It does not install KiCad silently, replace KiCad, collect credentials, or write into installed KiCad folders.

## Installer Status

The installer project lives under `installer/`.

Current intent:

- Windows: EXE build support through Electron Builder.
- macOS: DMG build support through a macOS runner.
- Linux: AppImage and DEB build support through a Linux runner.

Do not treat an installer artifact as production-ready unless the release notes show platform smoke tests, checksums, and signing/notarization status where applicable.

## What The Installer Does

1. Detects your operating system.
2. Lets you choose a workspace folder.
3. Checks for KiCad, `kicad-cli`, Git, Python, Node/npm, and VS Code.
4. Shows missing dependencies.
5. Asks before running any package-manager install command.
6. Copies a clean `KICAD_ENGINE` workspace template.
7. Runs the health check.
8. Writes setup and health reports.
9. Opens VS Code when requested.

## What The Installer Does Not Do

- It does not bundle KiCad in v1.
- It does not modify installed KiCad app folders.
- It does not modify global KiCad libraries.
- It does not store API keys, login tokens, or AI credentials.
- It does not require paid services.
- It does not create final fabrication outputs.

## Default Install Paths

- Windows: `C:\Users\<you>\KICAD_ENGINE`
- macOS: `~/KICAD_ENGINE`
- Linux: `~/KICAD_ENGINE`

Choose a user-writable folder. Do not install into KiCad's application folder or another system-managed directory.

## After Installation

1. Open the installed workspace in VS Code.
2. Read `START_HERE_FOR_USERS.md`.
3. Run the health check task.
4. Log in to Codex, Claude, or your chosen AI tool yourself.
5. Use `.prompts/codex/00_START_SESSION.md` or `.prompts/claude/00_START_SESSION.md`.

## If Something Fails

Read `TROUBLESHOOTING.md`. The installer should leave logs in the workspace or installer log folder. Missing dependencies should be shown as user-action items, not silently installed.
