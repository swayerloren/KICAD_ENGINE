# Project Memory Update Rules

Status: `ACTIVE_RULES`

## Update Order

1. Create a history record first.
2. Decide whether the fact is durable.
3. Update the most specific project memory file.
4. Mark the update `UNVERIFIED` unless human-confirmed.
5. Promote to global memory only if reusable across projects.
6. Update indexes.

## Do Not Store

- Secrets.
- Raw terminal logs.
- Temporary guesses.
- Unverified footprint approval.
- Fabrication approval without full verification and human review.

