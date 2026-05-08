# Local Development Setup

This is the normal recommended way to use KiCad Engine: download or clone the repo locally, open it in VS Code, and use Codex or Claude from the repo root while keeping KiCad installed locally for GUI inspection and final engineering review.

Use local development when you need:

- KiCad GUI review
- Windows-specific KiCad workflows
- local board inspection
- interactive Git work
- the same repo rules used by Codespaces, but with local tools

## Recommended Local Tools

- Git
- Python 3.11 or newer
- GitHub CLI
- VS Code
- KiCad installed locally for GUI review and final engineering validation

## Suggested Workflow

1. Download the repo ZIP or clone the repo locally.
2. Start from the repo root.
3. Read `README.md`, `CURRENT_STATUS.md`, `WORKFLOWS_INDEX.md`, `TOOLS_INDEX.md`, and `00_CODEX_START/START_HERE.md`.
4. Use the repo scripts for validation and maintenance.
5. Do KiCad GUI inspection locally when the task actually requires schematic or PCB visual review.

No extra GitHub repositories are required for the normal local workflow unless a specific optional helper is documented for a narrower task.

## Local Vs Codespaces

- Codespaces/devcontainer: repo tooling, documentation, rule-engine work, read-only validation
- local Windows + KiCad: actual GUI review, live schematic inspection, live PCB inspection, final fabrication judgment
