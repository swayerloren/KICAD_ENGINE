# Codespaces Setup

KiCad Engine supports GitHub Codespaces and VS Code devcontainers for repo tooling, validation, and documentation work.

Codespaces is optional. It is not required for local KiCad engineering work, and empty Codespaces prebuild settings are acceptable for this repo right now.

## Good Uses For Codespaces

- reading the repo and startup docs
- editing Markdown, JSON, YAML, and Python helper scripts
- running safe validation scripts
- reviewing reports and workflow outputs
- preparing pull requests

## Bad Uses For Codespaces

- assuming full KiCad GUI design work is available
- treating a Codespace as a replacement for local KiCad review
- generating manufacturing outputs without local verification

## Start A Codespace

1. Open the GitHub repo.
2. Choose `Code -> Codespaces`.
3. Create a new Codespace on the target branch.
4. Wait for the devcontainer bootstrap to complete.
5. Open the repo root and read `README.md`, `CURRENT_STATUS.md`, and `AGENTS.md` before changing anything significant.

## Tooling Available In The Devcontainer

- Python
- Git
- GitHub CLI
- Node.js for basic Markdown tooling
- PowerShell for repo helper scripts

## Important Limitation

KiCad GUI review still happens locally on Windows with KiCad installed. Codespaces should be treated as a safe automation and documentation environment, not as final schematic/PCB visual authority.
