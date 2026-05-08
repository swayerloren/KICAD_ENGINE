# Devcontainer

This devcontainer gives KiCad Engine contributors a consistent GitHub Codespaces or local VS Code container environment for:

- Python-based repo scripts
- Git and GitHub CLI workflows
- Markdown and YAML editing
- read-only validation, documentation work, and repo maintenance

## What It Includes

- Python 3.12
- Git
- GitHub CLI
- Node.js for lightweight Markdown tooling
- PowerShell for repo scripts that already use `.ps1`

## What It Does Not Assume

- no KiCad GUI
- no Windows-only KiCad review tools
- no fabrication-output generation
- no secrets or GitHub Environments

Use the devcontainer for repo infrastructure, rule-engine work, and safe validation. Do KiCad GUI inspection and final engineering review locally on Windows with KiCad installed.
