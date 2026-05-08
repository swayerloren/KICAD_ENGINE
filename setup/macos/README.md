# macOS Setup

These scripts prepare KiCad Engine on macOS for VS Code, metadata, and CLI-first KiCad workflows.

## Scripts

- `check_macos_requirements.sh`: read-only dependency check for KiCad, `kicad-cli`, Git, Python, Node/npm, VS Code, and Homebrew.
- `install_missing_macos_tools.sh`: optional Homebrew helper. It defaults to dry-run. It asks before each install only when `--apply` is passed and exits with manual instructions if Homebrew is unavailable.
- `open_vscode_workspace.sh`: opens this workspace in VS Code when `code` or the VS Code app bundle is available.
- `setup_macos.sh`: runs safe repo setup helpers and health checks.

## Safe First Run

From the repo root:

```bash
bash setup/macos/check_macos_requirements.sh
```

Then:

```bash
bash setup/macos/setup_macos.sh
```

Open the workspace:

```bash
bash setup/macos/open_vscode_workspace.sh
```

## Optional Installs

```bash
bash setup/macos/setup_macos.sh --offer-install
```

The install helper uses Homebrew only when Homebrew is already installed. It asks you to type `YES` for each install after `--apply`. If Homebrew is missing, it prints manual install links instead of installing Homebrew silently. Running `install_missing_macos_tools.sh` directly without `--apply` prints proposed commands and installs nothing.

## KiCad Paths Checked

- `/Applications/KiCad/KiCad.app`
- `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`
- `/Applications/KiCad.app`
- `/Applications/KiCad.app/Contents/MacOS/kicad-cli`
- `kicad-cli` on `PATH`

## Safety

- No tools are installed unless you explicitly confirm.
- Paid tools are not installed.
- API keys, passwords, tokens, and license keys must never be stored in this repo.
- KiCad project files are not edited by setup.
- The KiCad app bundle and global KiCad libraries are not modified.
