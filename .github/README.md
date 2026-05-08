# .github Folder README

This file explains **only** the `.github/` folder.

It is **not** the main project documentation for KiCad Engine.

The full `KICAD_ENGINE` project lives at the repository root and is intended to be downloaded or cloned locally, then opened in VS Code for use with Codex, Claude, or another AI coding agent.

Start with:

- [../README.md](../README.md)
- [../START_HERE.md](../START_HERE.md)
- [../00_CODEX_START/START_HERE.md](../00_CODEX_START/START_HERE.md)

This `.github/` folder only contains GitHub-facing collaboration metadata such as:

- issue templates
- pull request templates
- GitHub Actions workflows
- branch protection guidance
- CODEOWNERS
- future GitHub automation metadata when explicitly approved

If you opened this repo on GitHub and want to understand the actual project, continue with:

- [../CURRENT_STATUS.md](../CURRENT_STATUS.md)
- [../PROJECTS_INDEX.md](../PROJECTS_INDEX.md)
- [../WORKFLOWS_INDEX.md](../WORKFLOWS_INDEX.md)

## What Does Not Belong Here

- KiCad schematic or PCB source files
- KiCad project-local libraries
- tooling source that belongs under `03_TOOLS/`
- local-only backups
- copied-board routing rehearsals
- secrets, credentials, or `.env` files
- large build artifacts or manufacturing payloads

## Current Context

- Repo visibility: `PRIVATE`
- Repo release state: `NOT_PUBLIC_RELEASE_READY`
- Active project: `ESP32_CSI_WIFI_NODE`
- Active board state: live PCB exists, partial routing exists, board is not fabrication-ready

The root docs are the canonical repo documentation. `.github/` should stay limited to GitHub issue/PR/workflow mechanics and should not be mistaken for the full project.

## Key Files Here

- issue templates under `.github/ISSUE_TEMPLATE/`
- pull request template: [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md)
- branch protection guidance: [BRANCH_PROTECTION_RECOMMENDATIONS.md](BRANCH_PROTECTION_RECOMMENDATIONS.md)
- owner guidance: [CODEOWNERS](CODEOWNERS)
- validation workflows under `.github/workflows/`
