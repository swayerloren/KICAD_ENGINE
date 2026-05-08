# Memory Update Rules

Rules for updating KiCad Engine memory without polluting durable knowledge with transient session details.

## Global Memory

Use `01_MEMORY/` for:

- Reusable AI behavior rules.
- Common KiCad workflow lessons.
- Verified cross-project workflows.
- Recurring agent mistakes to avoid.
- User corrections that apply across projects.

Do not use `01_MEMORY/` for:

- Raw terminal output.
- One-off command failures.
- Temporary observations.
- Secrets, tokens, passwords, or private credentials.
- Project-specific decisions that do not generalize.

## Project Memory

Use `04_KICAD_PROJECTS/active/PROJECT/memory/` for:

- Project-specific design decisions.
- Component choices and alternatives.
- Footprint decisions and review status.
- Datasheet/source status.
- User corrections for that project.
- Open design risks.

## History

Use `02_HISTORY/` and project `history/` for:

- Session logs.
- Command logs.
- Failed attempts.
- Issue records.
- User correction evidence.
- Workflow and verification runs.

## Promotion Rules

1. Capture the event in history first.
2. Add project memory only if the event changes durable project behavior.
3. Add global memory only if the event changes reusable repo-wide behavior.
4. Mark status `UNVERIFIED` unless human-confirmed or verified by a repeatable workflow.
5. Link memory entries back to history evidence.

## Maintenance Rules

1. Do not create a replacement for `01_MEMORY` or `02_HISTORY`.
2. Use `03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py` to compile current truth from existing records.
3. Every meaningful report or compiled memory file should include status, generated date/time, project, supersedes, superseded by, evidence files, and current relevance.
4. Replace vague dates with absolute dates when the date is known. If not known, flag `DATE_UNRESOLVED_NEEDS_HUMAN_REVIEW`.
5. Old reports and history must not be deleted automatically. Mark them through supersession indexes.

## Prompt Counter Rules

1. Every meaningful Codex/Claude repo task increments the active project prompt counter.
2. The project counter lives in `04_KICAD_PROJECTS/active/PROJECT/memory/PROMPT_COUNTER.md`.
3. After 5 meaningful repo tasks, memory/history maintenance is required before new engineering work.
4. Casual chat does not count unless repo files are audited or modified.
5. After successful maintenance, reset the counter to 0.
6. The counter does not replace session logs, command logs, or maintenance reports.
