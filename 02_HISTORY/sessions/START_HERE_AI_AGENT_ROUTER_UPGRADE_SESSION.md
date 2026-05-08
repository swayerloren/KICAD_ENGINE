# START_HERE AI Agent Router Upgrade Session

Date/time: `2026-05-07 13:36:40 -04:00`

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Request

Upgrade `START_HERE_FOR_AI_AGENTS.md` so future Codex and Claude prompts can start from one short routing file instead of listing many `READ FIRST` files.

## Actions

1. Read the required startup and phase-gate files named by LJ.
2. Checked that requested router target folders/files exist.
3. Replaced the old long startup list in `START_HERE_FOR_AI_AGENTS.md` with a short first-read router.
4. Added the requested sections:
   - Mandatory Minimal Startup
   - Task Router
   - Active Project Rule
   - Phase Gate Rule
   - Prompt Counter Rule
   - Evidence Hierarchy Rule
   - End-of-Work Rule
5. Created this session log, the command log, and the design-review audit.

## Important Decisions

- `START_HERE_FOR_AI_AGENTS.md` now routes to deeper rules but does not replace `AGENTS.md`.
- Future short prompt accepted by the router:

`Read START_HERE_FOR_AI_AGENTS.md and route yourself.`

Agents must then use the Task Router and follow `AGENTS.md` for the full startup chain.

## Scope Confirmation

- KiCad schematic edits: `NO`
- KiCad PCB edits: `NO`
- Routing: `NO`
- Zones: `NO`
- Fabrication outputs: `NO`
- Duplicate startup system: `NO`

## Result

Session result: `START_HERE_ROUTER_UPDATED`

Remaining action: future agents should use the router and still obey `AGENTS.md`.

