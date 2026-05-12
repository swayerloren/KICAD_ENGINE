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

## PCB Quality Gate

The enforceable PCB routing-quality workflow now lives under:

- `03_TOOLS/scripts/pcb_quality/`
- `.github/workflows/pcb-quality-gate.yml`

Rules:

- the workflow must compile the gate scripts on normal GitHub runners
- the full live dry-run gate may run only when the runner also has KiCad tooling
  available
- when KiCad is unavailable, the workflow must skip the live-board dry run
  cleanly instead of faking a pass
- the workflow must never treat a Codex summary as proof; the JSON gate result
  is the judge

## Automation Validation

When CI uses calculator scripts, optional third-party EDA tools, or local
automation wrappers, the validation policy comes from:

- `09_ACCURACY_ENGINE/workflows/EDA_AUTOMATION_VERIFICATION_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/CALCULATOR_RESULT_EVIDENCE_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/AUTOMATION_TOOL_RESULT_VALIDATION_RULES.md`

CI may compile or smoke-test tools, but must not claim engineering proof from
tool output alone.

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
