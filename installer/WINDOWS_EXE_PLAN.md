# Windows EXE/MSI Plan

Status: planning only.

Windows is the first target platform because current KiCad app intelligence and setup scripts are strongest on Windows.

## Packaging Options

Recommended options to evaluate:

- Tauri desktop shell with a signed EXE/MSI.
- Electron installer with `electron-builder`.
- Lightweight PowerShell bootstrapper packaged as EXE/MSI.
- WiX Toolset MSI for a more traditional Windows installer.

Preferred v0.6 direction:

- Start with a lightweight signed Windows EXE or MSI that wraps existing PowerShell and Python setup scripts.
- Add a GUI only if user testing shows command-line setup is too brittle.

## Windows Install Flow

1. User downloads signed installer.
2. Installer asks for install path, defaulting to a user-writable folder such as `%USERPROFILE%\Documents\KICAD_ENGINE` or `%USERPROFILE%\GitHub\KICAD_ENGINE`.
3. Installer refuses `C:\Program Files\KiCad`, `C:\Windows`, and other unsafe system paths.
4. Installer copies the repo payload.
5. Installer checks:
   - KiCad installed.
   - `kicad-cli` available.
   - Git installed.
   - Python installed.
   - Node installed.
   - VS Code installed.
6. Installer offers optional installs with `winget`.
7. Installer runs:
   - `setup\common\create_repo_folders.py`
   - `setup\common\build_indexes.py`
   - `health_check.ps1`
   - `setup\common\write_setup_report.py`
8. Installer opens VS Code at the workspace if `code` is available.

## Optional Tool Installation

Use `winget` when available:

- Git: `Git.Git`
- Python: `Python.Python.3.12` or current supported Python package.
- Node.js LTS: `OpenJS.NodeJS.LTS`
- VS Code: `Microsoft.VisualStudioCode`
- KiCad: `KiCad.KiCad`

Every install must require explicit confirmation. The installer must show the exact command before running it.

## KiCad Rules

- Do not bundle KiCad in v1.
- Do not write into `C:\Program Files\KiCad`.
- Do not edit user global KiCad library tables.
- Use installed KiCad folders as read-only evidence.
- Use `kicad-cli version` as the first safe executable test.

## Windows Security

- Sign installer binaries before public release.
- Use Authenticode signing for EXE/MSI.
- Publish SHA256 checksums.
- Do not request elevation unless the user chooses a tool install that requires it.
- Keep default workspace install path user-writable to avoid unnecessary admin rights.

## v0.6 Acceptance Criteria

- Clean install on Windows 11 with KiCad already installed.
- Safe failure when KiCad is missing.
- Optional `winget` installs ask before every install.
- Health check completes and writes reports.
- VS Code opens the workspace.
- No AI credentials are requested or stored.
