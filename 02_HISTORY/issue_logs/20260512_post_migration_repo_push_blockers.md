# Post-Migration Repo Push Blockers

Date: `2026-05-12`

Status: `OPEN`

## Blockers

1. Untracked `.sfdx/` directory exists at repo root and is not ignored.
2. Large local/generated artifacts exist in the working tree and require commit-scope review even though none are staged.

## Required Resolution

1. Remove or ignore `.sfdx/`.
2. Confirm large local/generated artifacts remain out of the commit scope.

