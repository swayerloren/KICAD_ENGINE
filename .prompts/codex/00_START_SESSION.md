# Codex Prompt: Start KiCad Engine Session

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read:

1. `START_HERE_FOR_AI_AGENTS.md`
2. `AGENTS.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
5. `00_CODEX_START/TASK_ROUTER.md`
6. `.prompts/shared/SAFETY_GATES.md`

Then follow the full `AGENTS.md` startup chain automatically and use
`TASK_ROUTER.md` plus its companion task tables to derive the route-specific
docs for the current task. Then read the relevant `01_MEMORY` and `02_HISTORY`
entries.

## Task

Start a safe KiCad Engine session. Summarize:

- Active project name and path.
- Current task mode.
- Whether KiCad project source edits are allowed.
- Relevant tools and scripts.
- Relevant memory/history.
- Required backup and verification gates.

## Restrictions

- Do not edit KiCad project files.
- Do not modify installed KiCad files or user-global KiCad config.
- Do not install tools.
- Do not make datasheet or footprint claims without source evidence.

## Output

Return a concise session readiness summary and recommended next action. If any KiCad source edit is requested later, require backup, rollback, ERC/DRC, history log, and verification report.

## Universal Safety Requirements

- Require active project confirmation, backup, rollback plan, verification plan, and history log before any KiCad source edit.
- Do not fabricate datasheet claims, electrical limits, lifecycle status, package data, or verification status.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
