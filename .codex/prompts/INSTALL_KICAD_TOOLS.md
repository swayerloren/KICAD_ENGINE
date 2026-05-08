# Install KiCad Tools

Use this prompt only when the user explicitly asks Codex to install or configure KiCad-related tools.

## Startup Requirements
Before installing anything:
1. Read root `AGENTS.md`.
2. Read all `00_CODEX_START/` files in the required order.
3. Read `00_CODEX_START\TOOL_INDEX.md`.
4. Inspect existing tool repositories and environments first.
5. State the planned tool, install location, commands, rollback plan, and test plan.

## Repository Location
External repositories belong under:

`03_TOOLS\repos`

## Installation Rules
- Install one tool at a time.
- Record every command and important result in `02_HISTORY\command_logs\`.
- Update `00_CODEX_START\TOOL_INDEX.md` after each successful install or configuration change.
- Use isolated environments under `03_TOOLS\python_envs\` or `03_TOOLS\node_envs\` when applicable.
- Do not modify KiCad project files as part of tool installation unless the user explicitly asks.
- Do not continue to the next tool until the current tool has been tested or clearly marked blocked.

## MCP Safety
- Do not configure MCP unless explicitly authorized.
- Never give full write or manufacturing authority to an MCP server until it has been tested on non-critical sample files.
- Keep MCP permissions minimal and document every enabled capability.
- Treat MCP-generated KiCad edits as protected edits requiring backups, review, and verification.

## Completion
After each tool setup:
- Record installed version or commit.
- Record command entry points.
- Record known limitations.
- Record test results.
- Update `TOOL_INDEX.md`.
