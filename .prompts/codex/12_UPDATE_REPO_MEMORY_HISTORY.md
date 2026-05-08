# Codex Prompt: Update Repo Memory And History

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `00_CODEX_START/MEMORY_INDEX.md`, `00_CODEX_START/HISTORY_INDEX.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`.

## Goal

Update repo memory/history after:

- Work completed: `[WORK_SUMMARY]`
- Files changed: `[FILES_CHANGED]`

## Restrictions

- Do not store secrets.
- Do not rewrite unrelated history.
- Do not modify KiCad project source files.
- Do not record unverified datasheet or footprint claims as durable facts.

## Required Workflow

1. Put durable design/workflow decisions in `01_MEMORY`.
2. Put commands, results, reports, and session notes in `02_HISTORY`.
3. Update `README_GPT.md` and `FOR CHAT GPT.MD` only when repo structure, tools, workflows, active project status, or major context changed.
4. Back up README handoff files before editing if their own instructions require it.
5. Keep all claims realistic and source-scoped.

## Output

Return updated files, what was recorded as durable memory, what was recorded as history, and remaining follow-up items.

## Universal Safety Requirements

- Do not modify KiCad project files while updating memory and history.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source, library, config, or fabrication-output edit.
- Do not store secrets, credentials, private tokens, or license keys.
- Do not fabricate datasheet, ERC, DRC, BOM, footprint, release, or verification status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until the full verification gate passes.
