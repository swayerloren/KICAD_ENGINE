# How To Use Prompt Packs

Prompt packs give Codex, Claude, and similar agents a consistent workflow.

## Folder Layout

- `.prompts/codex/`: Codex prompts.
- `.prompts/claude/`: Claude prompts.
- `.prompts/shared/`: common standards.

## Start A Session

Use one of:

- `.prompts/codex/00_START_SESSION.md`
- `.prompts/claude/00_START_SESSION.md`

Paste the prompt into the agent before asking for project work.

## Choose A Task Prompt

Use a task-specific prompt for:

- KiCad install audit.
- Component research.
- Adding a component record.
- Schematic planning or review.
- PCB review.
- ERC/DRC.
- NOT_FINAL package export.
- Fab package review.
- Debugging a KiCad issue.
- Updating repo memory and history.

## Why It Matters

The prompt pack reduces unsafe assumptions by requiring:

- Startup reads.
- Backup planning.
- History logs.
- Verification reports.
- No fake datasheet claims.
- No unverified footprint approval.
- `NOT_FINAL` output labels.
