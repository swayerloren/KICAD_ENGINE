# Quickstart Linux

Linux support is for VS Code, metadata, CLI/headless KiCad workflows, and installer packaging. KiCad Engine uses your installed KiCad app; it does not replace KiCad, collect AI credentials, or modify global KiCad libraries.

## Prerequisites

- Linux desktop, VM, WSL, or container appropriate for your workflow.
- KiCad installed locally if running KiCad checks.
- `kicad-cli` available for ERC, DRC, and export workflows.
- Git.
- Python available as `python3` or `python`.
- VS Code.
- Codex, Claude, or another AI coding agent installed and logged in by you.
- Node/npm only if building the Electron installer or JavaScript tooling.

## Check Requirements

From the repo root:

```bash
bash setup/linux/check_linux_requirements.sh
bash setup/linux/detect_linux_package_manager.sh
```

The scripts check:

- `kicad`
- `kicad-cli`
- Git
- Python
- Node/npm
- VS Code
- distro metadata from `/etc/os-release`
- package managers: `apt-get`, `dnf`, `yum`, `pacman`, `flatpak`, and `snap`

Reports are written under `05_OUTPUTS/setup_reports/`.

## Setup

```bash
bash setup/linux/setup_linux.sh
```

To allow opt-in install prompts for missing tools:

```bash
bash setup/linux/setup_linux.sh --offer-install
```

Each install requires typing `YES`. For package managers that require root, the script prints the official command unless it is already running with the needed privilege.

## Open In VS Code

```bash
bash setup/linux/open_vscode_workspace.sh
```

Or open the `KICAD_ENGINE` folder manually in VS Code.

## Installer Package Strategy

- AppImage: first broad-compatibility Linux package target.
- DEB: Ubuntu/Debian package target.
- RPM: documented strategy for Fedora/RHEL, not enabled as a first build target until tested.
- tar.gz: manual fallback by extracting/copying the clean repo-template workspace.

## AI Agent Workflow

1. Log in to your own Codex or Claude tool.
2. Open `.prompts/README.md`.
3. Use `.prompts/codex/00_START_SESSION.md` or `.prompts/claude/00_START_SESSION.md`.
4. Tell the agent it is on Linux and should not assume Windows paths.
5. Prefer `kicad-cli` and file parsing before GUI automation.

## Safety

- Do not edit KiCad design files until active project, backup, and verification gates are confirmed.
- Do not write to global KiCad libraries or user-global library tables without explicit backup and approval.
- Do not accept unverified datasheet values or footprint choices.
- Keep generated fabrication-style outputs labeled `NOT_FINAL`.
