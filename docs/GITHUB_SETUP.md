# GitHub Setup For KiCad Engine

This repo is designed to work cleanly on GitHub without pretending that GitHub replaces KiCad or human review.

GitHub is the distribution and collaboration layer. A user should still be able to download the ZIP or clone the repo, open it in VS Code, and work locally without needing extra hidden repos, private env folders, or personal machine paths.

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

## Current GitHub Limitations For This Repo

- GitHub shows that rulesets may not enforce on this private personal repository unless it is moved to a GitHub Team or organization account.
- If the GitHub UI shows a main ruleset targeting `0` branches, the intended branch target pattern is `main`.
- If enforcement is unavailable, use manual pull-request discipline plus Actions checks.
- GitHub Environments are not needed right now for this repo.
- Codespaces is optional; it is a convenience layer, not a required engineering dependency.
- Codespaces prebuilds can remain empty until the repo actually needs them.

## Current Infrastructure Added

- `.devcontainer/` for local container or Codespaces work
- GitHub Actions workflows under `.github/workflows/`
- issue templates plus PR template
- CODEOWNERS
- branch protection recommendations

## Important Boundary

GitHub should not imply that the active board is fabrication-ready. Local KiCad review, live ERC/DRC evidence, and human signoff remain mandatory before ordering boards.

GitHub infrastructure here helps keep the repo clean and auditable. It does not change the engineering truth of any active KiCad board.
