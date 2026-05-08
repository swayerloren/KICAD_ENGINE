# KiCad Engine And Cloud-First PCB AI Tools

This document compares workflow categories. It does not claim KiCad Engine is better than any commercial platform across all use cases.

KiCad Engine is designed to be stronger for users who want a local-first, KiCad-native, auditable workflow around files they own.

## Cloud Vs Local-First

Many PCB AI tools are cloud-first. That can be useful for collaboration and managed infrastructure.

KiCad Engine is local-first. The repo, KiCad projects, datasheet metadata, component records, scripts, and reports live on the user's machine unless the user chooses to publish or sync them.

## KiCad-Native Vs Separate EDA Environment

Cloud-first PCB AI tools may use their own design environment and data model.

KiCad Engine is built around KiCad-native projects, libraries, `kicad-cli`, KiCad file formats, and local VS Code workflows. It is intended for users who already use KiCad or want to keep KiCad as the source of truth.

## Open Repo Memory Vs Closed Platform Memory

KiCad Engine stores memory, history, prompts, component notes, and review logs in ordinary repo folders. Users can inspect, edit, diff, commit, or delete them.

Closed platform memory may be convenient, but it is usually less visible to Git workflows and local review.

## User-Owned Datasheet And Component Database

KiCad Engine provides a user-owned datasheet and component database scaffold. The database can store source links, summaries, verification status, and KiCad symbol/footprint candidates.

The database is not automatically complete. Its value depends on verified sources and disciplined maintenance.

## CLI-Verifiable Outputs

KiCad Engine prefers `kicad-cli`, file parsers, and report-generating scripts where possible. That makes checks easier to repeat, log, and compare in Git.

CLI checks do not prove a design is correct. They provide evidence for a larger human review process.

## Human Review Gates

KiCad Engine deliberately keeps outputs labeled `NOT_FINAL` until human review gates are complete:

- ERC
- DRC
- BOM review
- Datasheet review
- Symbol and footprint verification
- Connector orientation review
- Mechanical review
- Fab output review

## Git And Version Control

KiCad Engine is designed for normal Git workflows. Docs, prompts, component records, and scripts are plain files.

This is useful for teams that want auditable changes, pull requests, and release checklists around KiCad projects.

## Practical Positioning

KiCad Engine is not a hosted PCB AI service. It is an open local workspace intended to make installed KiCad easier for AI agents to understand and use safely.

It is designed to be a serious open-source alternative for users who value local control, KiCad-native files, visible memory, and repeatable verification over managed cloud workflows.
