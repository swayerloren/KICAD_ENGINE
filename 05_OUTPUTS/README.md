# 05_OUTPUTS

## PURPOSE
Generated reports, review artifacts, setup reports, and NOT_FINAL outputs.

## WHAT_BELONGS_HERE
- Health-check reports.
- Validation reports.
- Review outputs.
- NOT_FINAL manufacturing-style exports.

## WHAT_DOES_NOT_BELONG_HERE
- Canonical KiCad source files.
- Secrets.
- Final release artifacts unless routed by release profile.

## AI_AGENT_RULES
- Treat outputs as generated evidence, not source of truth.
- Do not overwrite older outputs.

## SAFE_EDIT_RULES
- Use timestamped folders.
- Keep manufacturing-style outputs marked `NOT_FINAL` unless full verification and human approval exist.

## PUBLIC_RELEASE_NOTES
- Public payloads should exclude large generated outputs unless intentionally included as examples.
