# CI CD

## PURPOSE

Hold CI/CD design, workflow documentation, and release automation planning.

## WHAT_BELONGS_HERE

- GitHub Actions design notes.
- CI safety policies.
- Artifact upload/checksum rules.
- Workflow test plans.

## CI/CD Planning Files

- `GITHUB_ACTIONS_PLAN.md`
- `BUILD_MATRIX.md`
- `TEST_MATRIX.md`
- `RELEASE_WORKFLOW_PLAN.md`

## WHAT_DOES_NOT_BELONG_HERE

- Secrets or repository tokens.
- Local machine credentials.
- Unreviewed generated build artifacts.
- KiCad source edits.

## AI_AGENT_RULES

- Do not add secrets.
- Do not auto-publish public releases.
- Prefer draft releases and artifact uploads until human approval.

## SAFE_EDIT_RULES

- Add CI docs and workflow plans.
- Workflow changes must avoid destructive commands.
- Do not require paid services.

## PUBLIC_RELEASE_NOTES

CI should build artifacts, run checks, generate checksums, and upload artifacts without auto-publishing.

Release workflows should create draft releases only unless a human explicitly approves publishing.
