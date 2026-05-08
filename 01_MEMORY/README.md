# 01_MEMORY

## PURPOSE
Durable global memory for reusable lessons, preferences, workflows, corrections, and quality rules.

## WHAT_BELONGS_HERE
- Global lessons learned.
- Mistakes to avoid.
- Verified and failed workflows.
- User corrections that apply across projects.
- Master memory index.

## WHAT_DOES_NOT_BELONG_HERE
- Raw command logs.
- Temporary observations.
- Secrets or credentials.

## AI_AGENT_RULES
- Add only durable reusable facts.
- Keep project-specific durable facts in project `memory/`.

## SAFE_EDIT_RULES
- Mark entries `UNVERIFIED` unless verified by evidence or user confirmation.
- Link to history evidence where possible.
- Compile current truth through the existing memory/history maintenance workflow; do not create a parallel memory system.
- Use report status tags from `09_ACCURACY_ENGINE/verification_rules/REPORT_STATUS_TAGGING_RULES.md`.
- Preserve old memory entries; mark stale or superseded facts through indexes instead of deleting them.

## PUBLIC_RELEASE_NOTES
- Review for personal paths, private project facts, and secrets before public release.
