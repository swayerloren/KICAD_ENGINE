# 02_HISTORY

## PURPOSE
Evidence record for sessions, commands, audits, verification runs, issues, and AI quality logs.

## WHAT_BELONGS_HERE
- Session logs.
- Command logs.
- Design reviews.
- Failed attempts.
- Issue logs.
- AI self-reviews, scorecards, claim/evidence matrices, uncertainty logs, and hallucination-risk logs.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- Durable preferences that belong in memory.
- KiCad project source files.

## AI_AGENT_RULES
- Log meaningful work here before closeout.
- Keep command output summaries concise and evidence-linked.

## SAFE_EDIT_RULES
- Do not delete old history records.
- Do not mark generated manufacturing outputs as final.
- Do not hide failures. Mark stale, superseded, false-pass, and historical-only records through maintenance indexes.
- Use `03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py` to compile current truth from existing history.
- Old history remains evidence of what happened, not necessarily current project state.

## PUBLIC_RELEASE_NOTES
- Review for personal paths, private facts, and large/generated artifacts before public release.
