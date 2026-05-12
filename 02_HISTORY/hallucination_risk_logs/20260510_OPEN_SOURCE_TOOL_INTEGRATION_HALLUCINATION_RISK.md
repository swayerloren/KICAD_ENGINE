# Hallucination Risk Log

Date: 2026-05-10

## Risk Areas

- tool licenses and install commands could drift upstream over time
- some tools have broad capabilities that vary by version and local install
- `read-only safe` status depends on how the tool is invoked, not just the tool
  name

## Mitigations Used

- documented capabilities conservatively
- marked heavyweight tools `external-only`
- avoided claiming anything was installed unless the dry-run verifier detected it
- kept the repo-default policy to wrappers/docs only

## Result

`RISK_MANAGED_WITH_CONSERVATIVE_WORDING`
