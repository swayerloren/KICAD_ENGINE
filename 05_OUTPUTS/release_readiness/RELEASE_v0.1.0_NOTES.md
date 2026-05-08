# KiCad Engine v0.1.0

KiCad Engine is an AI-assisted KiCad workflow and rule engine for local engineering work in VS Code with Codex, Claude, or similar AI coding agents.

## What this release includes

- Repo indexes and navigation docs for understanding the workspace structure
- Prompt packs, startup rules, and workflow guidance for AI-assisted KiCad work
- PCB routing rules, geometry checks, and routing-quality hard-fail logic
- GitHub-facing documentation, issue templates, PR template, and branch workflow guidance
- Codespaces / devcontainer setup for repo docs and script work
- Validation scripts for task contracts, live-state authority, routing geometry, placement readiness, and repo hygiene

## Intended use

- Intended for local VS Code use with Codex or Claude
- Intended to help a human review, edit, validate, and manage KiCad projects more consistently
- Intended as an early/private/internal release for local download and evaluation

## Important warnings

- The active `ESP32_CSI_WIFI_NODE` PCB is **not fabrication-ready**
- Human KiCad review is still required before ordering boards
- This release does **not** certify the active PCB for fabrication, assembly, or production
- Manufacturing-style outputs remain subject to ERC, DRC, BOM, visual review, and human approval

## Current active-project status

- Active project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- PCB exists: `YES`
- Partial routing exists: `YES`
- DRC: `0` rule violations
- Remaining issue: unconnected items and unresolved nets still remain

## Release posture

- Private/internal release: `YES`
- Public release ready: `NO`
- Human KiCad review required before ordering boards: `YES`
