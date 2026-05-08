# Linux Setup

These scripts prepare KiCad Engine on Linux for VS Code, metadata, CLI-first KiCad workflows, and headless validation.

## Scripts

- `check_linux_requirements.sh`: read-only dependency check for KiCad, `kicad-cli`, Git, Python, Node/npm, VS Code, distro metadata, and supported package managers.
- `detect_linux_package_manager.sh`: read-only package manager detector for `apt`, `dnf`, `yum`, `pacman`, `flatpak`, and `snap`.
- `install_missing_linux_tools.sh`: optional install helper. It defaults to dry-run. It asks before each install only when `--apply` is passed. For package managers that require root, it prints the exact command unless the script is already running with the needed privilege.
- `open_vscode_workspace.sh`: opens this workspace in VS Code or falls back to `xdg-open`.
- `setup_linux.sh`: runs safe repo setup helpers and health checks.

## Safe First Run

From the repo root:

```bash
bash setup/linux/check_linux_requirements.sh
bash setup/linux/detect_linux_package_manager.sh
```

Then:

```bash
bash setup/linux/setup_linux.sh
```

Open the workspace:

```bash
bash setup/linux/open_vscode_workspace.sh
```

## Optional Installs

```bash
bash setup/linux/setup_linux.sh --offer-install
```

The install helper asks you to type `YES` for each tool after `--apply`. It never silently installs anything. Running `install_missing_linux_tools.sh` directly without `--apply` prints proposed commands and installs nothing.

## Package Manager Coverage

- Ubuntu/Debian: `apt-get`
- Fedora: `dnf`
- RHEL/CentOS legacy: `yum`
- Arch/Manjaro: `pacman`
- Cross-distro app packaging: `flatpak`
- Snap-capable distros: `snap`

Package names and official availability vary by distro. If a package manager cannot install a tool cleanly, use the manual links printed by the scripts.

## Safety

- No tools are installed unless you explicitly confirm.
- Paid tools are not installed.
- API keys, passwords, tokens, and license keys must never be stored in this repo.
- KiCad project files are not edited by setup.
- Global KiCad libraries and user-global KiCad library tables are not modified.
- Generated fabrication-style outputs remain `NOT_FINAL`.
