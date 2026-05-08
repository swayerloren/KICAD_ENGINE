# Branch Protection Recommendations

These are recommended GitHub branch protection settings for `main`. This file documents the settings; it does not enable them automatically.

## Recommended Rules For `main`

- require a pull request before merge
- require status checks to pass before merge
- require conversation resolution before merge
- block force pushes
- block branch deletion
- optionally require the branch to be up to date before merge
- optionally require signed commits later if the repo process needs that level of provenance

## Suggested Required Status Checks

Use the job names rather than only the workflow names when selecting required checks:

- `python-and-contracts`
- `docs-and-links`
- `repo-hygiene`

## Merge Strategy Guidance

- Prefer squash merge or rebase merge for repo infrastructure and documentation branches.
- Do not merge when the PR introduces repo-hygiene failures, lock files, env files, or accidental manufacturing artifacts.
- Do not treat a passing repo-infrastructure PR as fabrication approval for any active PCB.

## Manual GitHub Settings Still Needed

The following must still be enabled manually in the GitHub repository settings:

1. open `Settings -> Branches`
2. add a protection rule for `main`
3. require pull requests before merge
4. require the selected status checks
5. enable conversation resolution
6. disable force pushes
7. disable deletion

## Why This Exists

KiCad Engine mixes:

- documentation
- automation
- project state
- real hardware design files

That means repo hygiene matters. Branch protection should stop accidental direct pushes and ensure validation runs before changes land on `main`.
