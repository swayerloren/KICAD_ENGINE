# Windows Installer Plan

Status: `WINDOWS_FIRST_PLAN`

## Target

Create a Windows installer that creates a local `KICAD_ENGINE` workspace, checks dependencies, optionally helps install missing tools, runs a health check, and opens VS Code.

## Default Path

`C:\Users\<user>\KICAD_ENGINE`

## Dependency Checks

- KiCad app path.
- `kicad-cli`.
- Git.
- Python.
- Node/npm.
- VS Code.
- winget.

## Install Strategy

- Prefer winget where available.
- Ask before each install.
- Show manual instructions when winget is missing or the user declines.
- Do not silently install paid tools.

## Build Artifact

Planned artifact name:

`KiCad-Engine-Setup-Windows-x64.exe`

## Smoke Test

Install into a disposable folder and verify:

- Workspace exists.
- `README.md`, `AGENTS.md`, `.vscode/`, `.prompts/`, `06_DATASHEETS/`, and `08_COMPONENT_DATABASE/` exist.
- Health check runs.
- No write occurred inside `C:\Program Files\KiCad`.

## Limitations

Do not call the Windows installer production-ready until a native Windows build and smoke test pass and checksums are generated.

