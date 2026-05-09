# Routing Work

This folder is local generated routing scratch space for the active project.

## Current Policy

- Timestamped subfolders are local-only and ignored by Git.
- GitHub should show this folder only by this placeholder `README.md`.
- ZIP users do not need this folder populated for first use.
- Codex or Claude can recreate local routing-work folders during routing or copied-board rehearsal tasks.
- Do not treat this folder as a required dependency for baseline repo use.

## Do Not Commit Blindly

- copied `.kicad_pcb`, `.kicad_pro`, or `.kicad_prl` route-trial boards
- DRC scratch JSON or temporary validation outputs
- broad rehearsal/debug trees
- temporary logs, locks, caches, screenshots, or copied-board folders

## Recreate Locally

- start from the active project
- follow the repo routing workflow and backup rules
- create a fresh local timestamped folder only when the task explicitly needs routing trials or copied-board rehearsal evidence

## First-Use Guidance

- A new user does not need any preexisting `routing_work` payload to use KiCad Engine.
- This folder exists only as a local workspace for generated routing experiments and temporary audit artifacts.
