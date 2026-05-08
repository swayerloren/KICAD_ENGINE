# Using With Codex

Status: `PUBLIC_DRAFT`

## Setup

1. Open KiCad Engine in VS Code.
2. Log in to Codex with your own account.
3. Read `.prompts/codex/00_START_SESSION.md`.
4. Start with inspection or planning before edits.

## Required Agent Behavior

Codex must read `AGENTS.md`, startup files, memory/history, and relevant accuracy rules before touching KiCad project files.

## Safe Requests

- Audit installed KiCad.
- Inspect project structure.
- Research a component.
- Create a component record stub.
- Run health check.
- Run ERC/DRC through guarded scripts.
- Export `NOT_FINAL` review outputs.

## Unsafe Without Gates

- Editing `.kicad_sch`, `.kicad_pcb`, libraries, or fab outputs.
- Selecting unverified footprints.
- Claiming fabrication readiness.

