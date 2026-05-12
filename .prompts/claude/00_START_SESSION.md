# Claude Prompt: Start Session

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before doing any work:

1. `START_HERE_FOR_AI_AGENTS.md`
2. `AGENTS.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
5. `00_CODEX_START/TASK_ROUTER.md`
6. `.prompts/shared/SAFETY_GATES.md`

Then follow the full `AGENTS.md` startup chain automatically and use
`TASK_ROUTER.md` plus its companion task tables to derive the route-specific
docs for the current task.

## Goal

Start a safe KiCad engineering session and establish the current repo, project, memory, history, and verification context.

## Universal Requirements

- Do not modify KiCad project files until the active project, target files, backup path, verification plan, and rollback plan are confirmed.
- Require a backup before any edit to schematic, PCB, symbol, footprint, project, or fabrication-output files.
- Record meaningful work in `02_HISTORY/`, including commands run and verification results.
- Produce verification reports when checks are run or explain why they could not be run.
- Do not fabricate datasheet claims, electrical limits, lifecycle status, or package data.
- Do not select or approve footprints unless the exact package and manufacturer drawing have been verified.
- Label all generated manufacturing-style outputs `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.

## Session Work

1. Confirm the current working directory.
2. Summarize the active project status from `CURRENT_PROJECT.md`.
3. Identify relevant memory and history files to read for the requested task.
4. State whether the requested task is documentation-only, read-only inspection, project editing, or output generation.
5. Choose the safest control plane: CLI/API first, direct file parsing when safe, GUI discovery only when needed.

## Do Not Modify

- KiCad project source files unless startup and backup gates pass.
- Installed KiCad application folders.
- User global KiCad library tables.
- Datasheet PDFs or redistributed vendor documents without permission review.
- Secrets, credentials, tokens, or private license files.

## Output

Provide a concise session-start summary with:

- Current repo path.
- Active project status.
- Relevant memory/history to inspect next.
- Safety gates required before edits.
- Proposed next action.
