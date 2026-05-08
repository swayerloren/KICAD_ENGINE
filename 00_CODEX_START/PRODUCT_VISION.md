# KiCad Engine Product Vision

Date: 2026-05-02

## Positioning

KiCad Engine is a local-first AI-assisted KiCad engineering workspace. It is intended to make a user's installed KiCad application dramatically easier for AI coding agents to understand, inspect, automate safely, and use correctly from VS Code or a similar local development environment.

KiCad Engine does not replace KiCad. KiCad remains the source of truth for schematics, PCB layout, libraries, ERC, DRC, and fabrication exports. KiCad Engine wraps that local KiCad installation with structured project folders, startup rules, memory, history, prompts, verification scripts, datasheet organization, and carefully gated automation so agents such as Codex, Claude, and similar VS Code-based assistants can work with less guessing and more evidence.

The long-term product goal is to become a serious open-source KiCad-focused alternative to cloud-first PCB AI tools by being more transparent, local, auditable, reproducible, and KiCad-native.

## What This Repo Is

- A local-first engineering workspace for AI-assisted KiCad work.
- A repo-level control system for AI agents working from VS Code, terminals, and local automation scripts.
- A safety layer around KiCad source files, library files, manufacturing outputs, and GUI automation.
- A place to store durable design decisions in `01_MEMORY` and work records in `02_HISTORY`.
- A tool hub for KiCad CLI, KiBot, MCP analysis, BOM, Gerber, drill, pick-and-place, STEP, visualization, and review workflows.
- A project template and verification framework for real KiCad projects under `04_KICAD_PROJECTS`.
- A datasheet and component evidence workspace under `06_DATASHEETS`.

## What This Repo Is Not

- It is not a replacement for KiCad.
- It is not an autonomous fabrication-approval system.
- It is not a cloud PCB CAD platform.
- It is not a guarantee that AI-generated or AI-edited PCB work is correct.
- It is not ready to claim final manufacturing readiness without ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual verification.
- It is not currently a complete component sourcing, lifecycle, or distributor availability system.

## Intended Users

- KiCad users who want local AI help without handing their full PCB workflow to a cloud-first platform.
- Hardware engineers who want agents to follow explicit review, backup, and verification gates.
- Makers and small teams who want repeatable KiCad project setup, checks, and release preparation.
- Open-source hardware maintainers who want auditable AI-assisted design reviews.
- AI coding agent users working in VS Code with Codex, Claude, or similar assistants.

## Core KiCad Workflows

KiCad Engine should focus on KiCad-native workflows:

- Schematic review and assisted schematic planning.
- PCB review and assisted PCB planning.
- Datasheet-backed component review.
- BOM generation and BOM sanity checks.
- Symbol and footprint mapping checks.
- Footprint geometry, courtyard, pin mapping, and orientation review.
- Connector pinout, keying, polarity, and mechanical orientation review.
- ERC and DRC execution through local KiCad tooling.
- Gerber, drill, pick-and-place, PDF, SVG, STEP, and release package review.
- KiBot and `kicad-cli` based deterministic automation.
- Read-only visualization through tools such as KiCanvas, InteractiveHtmlBom, and PcbDraw where appropriate.
- Safe GUI discovery only when CLI/API/MCP methods cannot answer the question.

## Product Principles

### Local First

The user's local KiCad installation, local files, local scripts, and local verification outputs are the primary environment. Cloud services may be optional in the future, but the core engine should remain usable without uploading designs to a hosted PCB AI platform.

### KiCad Native

The engine should use KiCad file formats, KiCad CLI, KiCad Python APIs, KiCad project structure, KiCad ERC/DRC, and KiCad fabrication outputs. It should not introduce a parallel PCB source format that hides or replaces the KiCad project.

### Agent Neutral

The repo should support Codex, Claude, and other VS Code-based coding agents through plain Markdown instructions, local prompts, scripts, and documented control planes. Agent-specific folders can exist, but the workflow should not depend on a single vendor.

### Evidence Backed

AI recommendations should cite local project files, datasheets, memory, history, command outputs, and verification reports. Guesses should be marked as guesses. Missing evidence should block final claims.

### Safe By Default

The default posture is read-only inspection. Design edits require active project confirmation, backup, stated files, rollback plan, and verification plan. GUI automation starts with discovery only and must not randomly click, type, or save.

### Auditable

Design decisions belong in memory. Commands, verification outputs, review findings, and session records belong in history. Manufacturing-style outputs remain `NOT_FINAL` until the verification gate passes.

### Open And Inspectable

Compared with cloud-first PCB AI tools, KiCad Engine should make its prompts, scripts, checks, assumptions, and outputs visible to the user. A user should be able to inspect why an agent made a recommendation and reproduce the check locally.

## Competitive Position

KiCad Engine should compete with AI PCB design tools by taking a different stance:

- It augments the installed KiCad app instead of replacing it.
- It keeps files local by default.
- It exposes workflow rules and safety gates as plain repo files.
- It records memory and history so review work is traceable.
- It uses deterministic KiCad-native checks before trusting AI conclusions.
- It treats fabrication outputs as engineering artifacts that require review, not as automatic final packages.

The credible claim is not "AI designs a PCB end to end with no review." The credible claim is "AI agents can help a KiCad user move faster while staying inside a transparent, local, reviewable engineering workflow."

## MVP Criteria

A credible public MVP should provide:

- Clear top-level README explaining the local-first KiCad AI engine concept.
- Agent startup rules for Codex, Claude, and general VS Code assistants.
- A documented local setup flow that does not require checking in virtual environments or cloned third-party repos.
- Project templates for new KiCad projects.
- Datasheet and component evidence schema.
- Read-only project inventory.
- Backup script before edits.
- ERC and DRC scripts.
- BOM export and review workflow.
- Gerber/drill/STEP export workflow that marks outputs `NOT_FINAL`.
- A sample project and a clean validation path.
- A release-readiness checklist that refuses final claims when evidence is missing.

## Long-Term Criteria

To become a serious Flux-style competitor in the KiCad ecosystem, KiCad Engine would need:

- A robust component and footprint knowledge base with provenance and review status.
- Agent workflows that can safely propose schematic and PCB changes as patches.
- Automated symbol-footprint-pin mapping checks.
- Datasheet extraction and traceable requirement capture.
- Visual board review and connector-orientation review workflows.
- Regression tests across KiCad versions.
- Public documentation, examples, licenses, contribution rules, and reproducible setup.
- A trustworthy release package workflow with human signoff points.
- Demonstrated real-board case studies with limitations documented.

## Finality Rule

KiCad Engine can assist, inspect, generate reports, and prepare candidate outputs. It must not present fabrication outputs as final unless ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual review gates are complete and the user has accepted the release package.
