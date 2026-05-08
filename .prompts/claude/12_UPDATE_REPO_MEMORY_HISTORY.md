# Claude Prompt: Update Repo Memory And History

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before updating memory or history:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/MEMORY_INDEX.md`
4. `00_CODEX_START/HISTORY_INDEX.md`
5. `00_CODEX_START/PROJECT_INDEX.md`
6. `00_CODEX_START/CURRENT_PROJECT.md`
7. `.prompts/shared/SAFETY_GATES.md`

## Goal

Record durable design knowledge and session history in the correct repo locations.

## Universal Requirements

- Do not modify KiCad project files.
- Require backup before any future edit to KiCad source, library, config, or fabrication-output files.
- Store durable decisions in `01_MEMORY/`.
- Store commands, session notes, audit results, and verification reports in `02_HISTORY/`.
- Do not store secrets, credentials, tokens, private URLs, or license keys.
- Do not fabricate datasheet, verification, footprint, ERC, DRC, or release status.
- Do not mark manufacturing outputs final unless the full gate passed; use `NOT_FINAL` for generated fab-style outputs.

## Workflow

1. Decide whether the information is durable memory, session history, project history, command log, design review, or release note.
2. Update the narrowest relevant file.
3. Preserve existing context and avoid overwriting unrelated notes.
4. Include source paths, command summaries, verification status, and open questions.
5. Update indexes only when needed.

## Output

Report:

- Memory files updated.
- History files updated.
- Verification reports referenced.
- Open follow-up items.
- Confirmation that no KiCad project files were modified.
