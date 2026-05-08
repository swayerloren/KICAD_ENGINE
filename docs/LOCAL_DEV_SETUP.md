# Local Development Setup

This is the normal recommended way to use KiCad Engine: download or clone the repo locally, open it in VS Code, and use Codex or Claude from the repo root while keeping KiCad installed locally for GUI inspection and final engineering review.

## Required

- KiCad for live schematic and PCB GUI work
- Python 3.11 or newer for repo scripts

## Recommended

- VS Code
- Codex or Claude opened from the repo root
- Git for sync, branch, and pull-request workflows

## Optional

- GitHub CLI
- Codespaces or devcontainer for docs and safe script work
- Node/npm only when a specific optional helper explicitly needs it

## Suggested Local Workflow

1. Download the repo ZIP or clone the repo locally.
2. Open the repo root in VS Code.
3. Run `python health_check.py --no-write`.
4. Read `README.md`, `ONE_PROMPT_START.md`, `CURRENT_STATUS.md`, `WORKFLOWS_INDEX.md`, `TOOLS_INDEX.md`, and `00_CODEX_START/START_HERE.md`.
5. Use the repo scripts with repo-relative paths.
6. Do KiCad GUI inspection locally when the task actually requires schematic or PCB visual review.

No extra GitHub repositories are required for the normal local workflow unless a specific optional helper is documented for a narrower task.

## Local Vs Codespaces

- Codespaces/devcontainer: repo tooling, documentation, rule-engine work, safe validation, and pull-request prep
- local machine + KiCad: actual GUI review, live schematic inspection, live PCB inspection, and final fabrication judgment
