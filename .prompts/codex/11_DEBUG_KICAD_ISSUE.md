# Codex Prompt: Debug KiCad Issue

You are working in `C:\Users\LJ\GitHub\KICAD_ENGINE` from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `00_CODEX_START/CONTROL_PLANES.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`, and relevant command/history logs.

## Goal

Debug KiCad issue:

- Symptom: `[ISSUE_DESCRIPTION]`
- Project path if relevant: `[PROJECT_PATH_OR_NONE]`

## Restrictions

- Start read-only.
- Do not edit project files unless user separately approves fix scope.
- Do not use GUI control unless explicitly approved.
- Do not modify installed KiCad or user-global config.
- Do not install tools.

## Required Workflow

1. Reproduce or inspect the issue with the safest read-only method.
2. Gather versions, paths, command logs, and relevant files.
3. Prefer direct parsing and `kicad-cli` over GUI automation.
4. If a fix would edit files, stop and state backup/rollback/verification plan.
5. Write history log.

## Output

Provide root-cause hypothesis, evidence, safe next steps, and commands/reports generated. Separate diagnosis from any proposed fix.

## Universal Safety Requirements

- Start with read-only inspection and do not modify KiCad source, installed KiCad files, or user-global KiCad config unless explicitly approved.
- Require backup, rollback plan, verification plan, and history log before any future source or config edit.
- Produce a diagnosis or verification report with exact commands and limitations.
- Do not fabricate datasheet claims, tool behavior, package data, or verification status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until the full verification gate passes.
