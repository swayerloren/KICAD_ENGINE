# Linux AppImage/DEB/RPM Plan

Status: planning only.

Linux support should be transparent and distro-aware. The installer should work even when the user prefers manual package installation.

## Packaging Options

Recommended options to evaluate:

- AppImage for a portable GUI wrapper.
- DEB for Debian/Ubuntu.
- RPM for Fedora/RHEL/openSUSE-family users.
- Tarball plus shell setup scripts for advanced users.

## Linux Install Flow

1. User downloads AppImage, DEB, RPM, or tarball.
2. Installer asks for install path, defaulting to `~/KICAD_ENGINE`, `~/Documents/KICAD_ENGINE`, or `~/GitHub/KICAD_ENGINE`.
3. Installer refuses system paths unless package manager semantics require root-owned install metadata.
4. Installer copies the repo payload to a user workspace.
5. Installer checks:
   - KiCad installed or `kicad-cli` available.
   - Git installed.
   - Python available as `python3`.
   - Node installed.
   - VS Code installed or `code` command available.
6. Installer detects `apt`, `dnf`, `pacman`, `flatpak`, or `snap`.
7. Installer offers optional installs through the detected package manager.
8. Installer runs common setup helpers and `health_check.py`.
9. Installer opens VS Code if available.

## Optional Package Manager Commands

Commands must be confirmed before running.

Examples:

- `sudo apt-get install -y git python3 nodejs npm kicad`
- `sudo dnf install -y git python3 nodejs npm kicad`
- `sudo pacman -S --needed git python nodejs npm kicad`
- `flatpak install flathub org.kicad.KiCad`
- `sudo snap install kicad`

VS Code package availability varies by distro. The installer should not assume Microsoft package repositories are configured.

## KiCad Rules

- Do not bundle KiCad in v1.
- Do not write into `/usr/share/kicad`, `/usr/local/share/kicad`, Flatpak app folders, or Snap app folders.
- Do not edit user global KiCad library tables.
- Use installed KiCad files read-only.

## AppImage Notes

An AppImage is useful for a self-contained setup GUI, but it should not hide setup scripts. The payload and logs must remain inspectable.

## DEB/RPM Notes

DEB/RPM packages can install a launcher and payload, but user data must stay in a user-writable workspace. Package uninstall must not delete user KiCad projects, memory, history, outputs, datasheets, or backups.

## Acceptance Criteria

- Works on at least one Debian/Ubuntu target and one Fedora-family target before claiming Linux support.
- Missing package managers fail gracefully.
- Optional installs require confirmation.
- Health check reports accurate platform notes.
- No AI credentials are requested or stored.
