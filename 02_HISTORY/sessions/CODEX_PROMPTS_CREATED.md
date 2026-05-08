# Codex Prompts Created

Date: 2026-04-30

## Summary
Created or updated reusable Codex prompt files under `.codex\prompts` for KiCad workspace startup, project creation, project review, fabrication verification, and future tool installation.

## Files Updated
- `.codex\prompts\START_CODEX_KICAD_ENGINE.md`
- `.codex\prompts\NEW_KICAD_PROJECT.md`
- `.codex\prompts\REVIEW_EXISTING_PROJECT.md`
- `.codex\prompts\VERIFY_BEFORE_FAB.md`
- `.codex\prompts\INSTALL_KICAD_TOOLS.md`

## Rules Captured
- Startup prompt requires reading `AGENTS.md`, every `00_CODEX_START` file, active project state, relevant memory/history, installed/missing tool status, and a verification plan.
- New project prompt creates project folders, project docs, project memory, project history, and project index updates while leaving `CURRENT_PROJECT.md` unchanged unless requested.
- Review prompt inspects KiCad project structure and produces a report without editing project files unless requested.
- Fabrication verification prompt requires ERC, DRC, BOM export, footprint checks, datasheet checks, connector checks, polarity/orientation review, power/protection review, mounting hole checks, and edge clearance checks.
- Tool installation prompt requires inspecting existing repos first, installing one tool at a time, recording every command, updating `TOOL_INDEX.md`, and testing MCP permissions before granting write or manufacturing authority.

## Tooling
No tools were installed.
No repositories were cloned.
No MCP configuration was performed.

## Verification
Confirmed the five prompt files and this session log exist. Checked the prompt files for the required startup gates, project creation structure, review scope, fabrication verification checklist, and tool installation safety rules.

## Reverification
Rechecked the prompt files on 2026-04-30 against the requested requirements. No prompt content changes were needed.
