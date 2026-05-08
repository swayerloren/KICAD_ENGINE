# GitHub Collaboration Files

This folder is only for GitHub-facing collaboration metadata such as:

- issue templates
- pull request templates
- GitHub Actions workflows
- branch protection guidance
- CODEOWNERS
- future GitHub automation metadata when explicitly approved

If you opened this repo on GitHub and want to understand the actual project, start here instead:

- [README.md](../README.md)
- [START_HERE.md](../START_HERE.md)
- [CURRENT_STATUS.md](../CURRENT_STATUS.md)
- [PROJECTS_INDEX.md](../PROJECTS_INDEX.md)
- [WORKFLOWS_INDEX.md](../WORKFLOWS_INDEX.md)

## What Does Not Belong Here

- KiCad schematic or PCB source files
- local-only backups
- copied-board routing rehearsals
- secrets, credentials, or `.env` files
- large build artifacts or manufacturing payloads

## Current Context

- Repo visibility: `PRIVATE`
- Repo release state: `NOT_PUBLIC_RELEASE_READY`
- Active project: `ESP32_CSI_WIFI_NODE`
- Active board state: live PCB exists, partial routing exists, board is not fabrication-ready

The root docs are the canonical repo documentation. `.github/` should stay limited to GitHub collaboration mechanics.

## Key Files Here

- issue templates under `.github/ISSUE_TEMPLATE/`
- pull request template: [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md)
- branch protection guidance: [BRANCH_PROTECTION_RECOMMENDATIONS.md](BRANCH_PROTECTION_RECOMMENDATIONS.md)
- owner guidance: [CODEOWNERS](CODEOWNERS)
- validation workflows under `.github/workflows/`
