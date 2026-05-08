# Troubleshooting

This guide covers common setup and workflow failures.

## KiCad Not Found

Check that KiCad is installed and opens normally.

Windows typical path:

```text
C:\Program Files\KiCad\<version>\
```

macOS typical path:

```text
/Applications/KiCad/KiCad.app
```

Linux depends on the package source. Try:

```bash
which kicad
```

Run the platform requirement script:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup\windows\check_windows_requirements.ps1
```

```bash
bash setup/macos/check_macos_requirements.sh
bash setup/linux/check_linux_requirements.sh
```

## kicad-cli Not Found

Try:

```bash
kicad-cli version
```

On Windows, KiCad may be installed but not on `PATH`. The repo scripts try common install paths first. If needed, use the full path:

```powershell
python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py
```

Do not copy files into the KiCad install folder to fix `PATH`.

## VS Code Not Found

Install VS Code from the official source or your OS package manager. The command-line launcher is usually `code`.

Check:

```bash
code --version
```

If `code` is missing but VS Code opens normally, use VS Code's command palette to install the shell command where supported, or open the folder manually.

## Python Missing

Check:

```bash
python --version
python3 --version
```

Install Python through the official installer or your OS package manager. Do not store virtual environments with secrets in this repo.

## Node Or npm Missing

Node/npm are only required for installer development and JavaScript tooling.

Check:

```bash
node --version
npm --version
```

If you are only using KiCad Engine as a workspace, you may not need Node.

## Permission Problems

Use a user-writable workspace folder, such as:

- Windows: `C:\Users\<you>\KICAD_ENGINE`
- macOS/Linux: `~/KICAD_ENGINE`

Do not install KiCad Engine into KiCad's app folder, `Program Files`, `/Applications/KiCad`, `/usr/share/kicad`, or another system-managed folder.

## Windows PowerShell Execution Policy

If scripts are blocked, run the script with a process-scoped bypass:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

This does not permanently change system policy.

## macOS Gatekeeper

Unsigned or locally built installer artifacts may be blocked by Gatekeeper. Prefer signed and notarized release artifacts when available.

If you intentionally run a trusted unsigned local build, use macOS Security settings or Control-click Open. Do not bypass Gatekeeper for unknown downloads.

## Linux Package Manager Issues

Run:

```bash
bash setup/linux/detect_linux_package_manager.sh
```

KiCad Engine checks for `apt`, `dnf`, `yum`, `pacman`, `flatpak`, and `snap`, but it does not assume one distro. If automated package-manager support is incomplete, use your distro's official KiCad, Python, Git, and VS Code installation instructions.

## Codex Or Claude Not Authenticated

KiCad Engine does not log in to AI tools for you.

Open your Codex, Claude, or other AI coding agent integration and log in with your own account. Do not paste API keys into repo files.

## Missing Datasheets

The datasheet database is not complete. Missing datasheets should be recorded as missing or link-only until a source is verified.

Use:

```bash
python 03_TOOLS/scripts/datasheets/create_missing_datasheet_report.py
```

Do not fabricate specs to fill missing data.

## Missing Footprints

A missing footprint means KiCad cannot resolve the assigned library reference. Check:

- Project-local `fp-lib-table`.
- User-global KiCad library tables.
- Installed KiCad stock libraries.
- Exact manufacturer package drawing.

Do not approve a footprint just because a name looks similar.

## ERC Failures

ERC failures mean schematic issues need review. Common causes include:

- Unconnected pins.
- Power pins not driven.
- Wrong electrical pin type.
- Missing no-connect markers.
- Hierarchical label problems.

Run the ERC task and read the report. Do not treat a clean ERC as full schematic approval.

## DRC Failures

DRC failures mean PCB rule issues need review. Common causes include:

- Clearance violations.
- Unrouted nets.
- Courtyard overlaps.
- Silkscreen over pads.
- Zone or net-class rule conflicts.

Run the DRC task and read the report. Do not treat a clean DRC as proof that footprints, connector orientation, or manufacturing files are correct.
