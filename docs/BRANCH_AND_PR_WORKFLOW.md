# Branch And PR Workflow

## Branch Strategy

- `main` is the protected integration branch.
- hardening work can live on branches such as `hardening/execution-contract`.
- repo infrastructure work can use a dedicated branch when needed.

## Expected Flow

1. start from a clean understanding of the worktree
2. stay on the task branch if it already exists and is in scope
3. stage only the files that belong to the task
4. run the relevant validation checks
5. push the branch
6. open or update a pull request to `main`

## PR Expectations

Each PR should clearly state:

- task type
- whether KiCad design files changed
- PCB hash before and after if applicable
- DRC result if applicable
- whether manufacturing outputs were generated
- what validation was run

Use [.github/PULL_REQUEST_TEMPLATE.md](../.github/PULL_REQUEST_TEMPLATE.md).

## Safety Rules

- do not silently include unrelated user changes
- do not stage `.env`, lock files, or backups
- do not treat repo validation as fabrication approval
- do not merge PCB-edit work without the required engineering evidence
