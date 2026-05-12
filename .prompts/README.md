# KiCad Engine Prompt Pack

Date: 2026-05-02

Purpose: reusable prompts for users working with Codex, Claude, or similar AI coding agents from VS Code in this local-first KiCad engineering workspace.

## How To Use

1. Open this repo in VS Code.
2. Tell the agent to read `START_HERE_FOR_AI_AGENTS.md` and route itself correctly, or use one of the start-session prompts below.
3. Let the agent use `00_CODEX_START/TASK_ROUTER.md` and its companion task tables to determine the route-specific docs automatically.
4. Pick a prompt from `.prompts/codex` or `.prompts/claude`.
5. Paste it into the agent chat.
6. Replace bracketed placeholders such as `[PROJECT_PATH]`, `[PART_NUMBER]`, or `[TASK_GOAL]`.
7. Keep generated reports in `02_HISTORY` or `05_OUTPUTS` unless a prompt explicitly requires another safe folder.

## Prompt Families

- `.prompts/codex`: prompts written for Codex-style coding agents.
- `.prompts/claude`: prompts written for Claude-style VS Code agents.
- `.prompts/shared`: standards that both prompt families reference.
- `.prompts/kicad_pipeline`: permanent 17-stage KiCad project pipeline prompts from schematic annotation through `NOT_FINAL` fabrication package export.

## Non-Negotiable Rules

- Read `AGENTS.md` and required startup files first.
- If a task prompt does not enumerate route-specific read-first files, use `START_HERE_FOR_AI_AGENTS.md` plus `00_CODEX_START/TASK_ROUTER.md` instead of asking the user for a larger list.
- Do not edit KiCad project source files unless the active project, scope, backup, verification, and rollback gates are confirmed.
- Do not install tools unless the user explicitly requests that separate task.
- Do not modify installed KiCad files or user-global KiCad config.
- Do not fabricate datasheet facts.
- Do not assert footprints are correct without exact manufacturer drawing verification.
- Do not skip KiCad pipeline gates unless the user explicitly approves an exception and the exception is logged with reason, risk, evidence, and `HUMAN_REVIEW_REQUIRED`.
- Mark manufacturing-style outputs `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, connector, polarity, mechanical, and visual review gates pass.
- Write history logs after meaningful work.

## Shared Standards

- `shared/SAFETY_GATES.md`
- `shared/COMPONENT_RESEARCH_STANDARD.md`
- `shared/DATASHEET_SUMMARY_STANDARD.md`
- `shared/KICAD_VERIFICATION_STANDARD.md`
- `shared/GITHUB_RELEASE_STANDARD.md`

## Recommended Starting Prompt

Use:

- `codex/00_START_SESSION.md` for Codex.
- `claude/00_START_SESSION.md` for Claude.

Those start prompts now route through `START_HERE_FOR_AI_AGENTS.md` and
`00_CODEX_START/TASK_ROUTER.md` so the user does not need to paste a giant
custom `READ FIRST` block.

Then use the task-specific prompts for audits, component research, schematic planning, reviews, validation, exports, and memory/history updates.

For end-to-end KiCad project progression, use `.prompts/kicad_pipeline/01_schematic_annotation_and_completeness.md` through `.prompts/kicad_pipeline/17_export_not_final_fab_package.md` in order.
