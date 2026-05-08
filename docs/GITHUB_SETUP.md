# GitHub Setup For KiCad Engine

This repo is designed to work cleanly on GitHub without pretending that GitHub replaces KiCad or human review.

## What GitHub Should Provide Here

- pull requests for all meaningful changes to `main`
- read-only validation through GitHub Actions
- issue templates for repo, PCB, and routing work
- a predictable devcontainer / Codespaces setup for documentation, automation, and review scripts
- branch protection on `main`

## What GitHub Should Not Be Used For Here

- pretending the active PCB is fabrication-ready
- replacing local KiCad GUI review
- editing locked or unsaved KiCad GUI state
- storing secrets in repo files

## Recommended Manual Repo Setup

1. Keep the repo private until the public-release blockers are closed.
2. Configure branch protection on `main` using [.github/BRANCH_PROTECTION_RECOMMENDATIONS.md](../.github/BRANCH_PROTECTION_RECOMMENDATIONS.md).
3. Keep pull requests enabled and require the repo validation workflows to pass.
4. Use issue templates for bugs, routing problems, PCB problems, and feature requests.
5. Use the devcontainer or Codespaces only for repo tooling, docs, and safe validation.

## Current Infrastructure Added

- `.devcontainer/` for local container or Codespaces work
- GitHub Actions workflows under `.github/workflows/`
- issue templates plus PR template
- CODEOWNERS
- branch protection recommendations

## Important Boundary

GitHub infrastructure here helps keep the repo clean and auditable. It does not change the engineering truth of any active KiCad board.
