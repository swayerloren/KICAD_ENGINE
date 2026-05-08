# Quickstart macOS

macOS support is for local-first KiCad Engine workflows in VS Code. It uses your installed KiCad app; it does not replace KiCad, bundle KiCad, collect AI credentials, or modify the KiCad app bundle.

## Prerequisites

- macOS.
- KiCad installed locally.
- VS Code.
- Python available as `python3` or `python`.
- Git.
- Codex, Claude, or another AI coding agent installed and logged in by you.
- Node/npm only if building the Electron installer or JavaScript tooling.

Homebrew is optional. KiCad Engine can detect Homebrew and use it for opt-in installs, but it never installs Homebrew silently.

## Check Requirements

From the repo root:

```bash
bash setup/macos/check_macos_requirements.sh
```

The script checks:

- `/Applications/KiCad/KiCad.app`
- `kicad-cli` inside the KiCad app bundle if present
- `kicad-cli` on `PATH`
- Git
- Python
- Node/npm
- VS Code
- Homebrew

Reports are written under `05_OUTPUTS/setup_reports/`.

## Setup

```bash
bash setup/macos/setup_macos.sh
```

To allow opt-in Homebrew prompts for missing tools:

```bash
bash setup/macos/setup_macos.sh --offer-install
```

Each install still requires typing `YES`.

## Open In VS Code

```bash
bash setup/macos/open_vscode_workspace.sh
```

Or open the `KICAD_ENGINE` folder manually in VS Code.

## AI Agent Workflow

1. Log in to your own Codex or Claude tool.
2. Open `.prompts/README.md`.
3. Use `.prompts/codex/00_START_SESSION.md` or `.prompts/claude/00_START_SESSION.md`.
4. Tell the agent it is on macOS and should not assume Windows paths.
5. Prefer `kicad-cli` and file parsing before GUI automation.

## Gatekeeper Note

Unsigned or locally built installer artifacts may trigger macOS Gatekeeper. Only open installers from a trusted source, and prefer signed/notarized release artifacts when available.

## KiCad Safety

- Do not let an agent edit KiCad design files until active project, backup, and verification gates are confirmed.
- Do not modify `/Applications/KiCad` or KiCad app-bundle contents.
- Do not write to global KiCad libraries or user-global library tables without explicit backup and approval.
- Treat all generated fabrication-style outputs as `NOT_FINAL`.
