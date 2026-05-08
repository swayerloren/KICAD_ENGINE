# KiCad Engine Product Gap Audit

Date: 2026-05-02
Workspace inspected: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Scope

This audit reviewed the repo as a local-first AI-assisted KiCad engineering engine. It did not edit KiCad source files, install tools, clone repositories, download datasheets, run ERC/DRC, run GUI automation, or generate manufacturing outputs.

Files and areas inspected included `AGENTS.md`, `README.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, the required `00_CODEX_START` startup files, memory and history indexes, current memory files, prior setup audits, `.codex`, `03_TOOLS`, `04_KICAD_PROJECTS/templates`, `05_OUTPUTS/release_packages`, and `06_DATASHEETS`.

## Product Thesis

The repo has the foundation for a serious local-first KiCad AI engineering workspace. Its strongest idea is not replacing KiCad. Its strongest idea is making installed KiCad safer and easier for AI agents to use through startup rules, project boundaries, memory/history, deterministic checks, and local tools.

That is a credible and differentiated direction versus cloud-first PCB AI tools. The current repo is not yet ready to claim broad public-release maturity or Flux-style competitiveness.

## What Currently Exists

- Root agent rules in `AGENTS.md` with startup order, safety gates, control planes, backup expectations, and verification requirements.
- Startup docs under `00_CODEX_START` for session startup, workflow, safety, control planes, repo map, tool index, memory index, history index, project index, and active project state.
- Memory structure under `01_MEMORY` for global rules, design rules, component preferences, fabrication preferences, coding rules, and project memory.
- History structure under `02_HISTORY` for sessions, command logs, design reviews, ERC/DRC reports, fabrication reviews, and project history.
- `.codex/config.toml` with `kicad-mcp-pro` configured in analysis mode only.
- `.codex/prompts` with Codex-oriented prompts for startup, project creation, existing project review, tool install planning, and verify-before-fab.
- Tool structure under `03_TOOLS`, including common, Windows, and Linux control-plane folders.
- External KiCad support repos under `03_TOOLS/repos`, including `kicad-mcp-pro`, `kicad-happy`, `KiCAD-MCP-Server`, `KiBot`, `InteractiveHtmlBom`, `PcbDraw`, and `kicanvas`.
- Windows GUI helper repos under `03_TOOLS/windows/repos`, including FlaUI, FlaUInspect, AutoHotkey, and SikuliX1.
- Verification and export scripts under `03_TOOLS/scripts`.
- Prior health and setup reports showing no hard blockers in the then-current environment.
- Project templates under `04_KICAD_PROJECTS/templates`.
- Active project folders for `COMMAND_LINK_VERIFIED_REFERENCE` and `ESP32_CSI_WIFI_NODE`.
- Output categories under `05_OUTPUTS`, including `release_packages`.
- `06_DATASHEETS` category folders and two Espressif PDF datasheets under `06_DATASHEETS/ESPRESSIF/ESP32-S3-WROOM-1U`.
- Finished-PCB reference and sample history from earlier work.

## What Is Weak

- The top-level `README.md` is still bootstrap-level and does not yet explain the local-first AI-assisted KiCad engine product clearly enough for public users.
- Many docs and configs still reference `C:\Users\LJ\KICAD_ENGINE`, while this inspected workspace is `C:\Users\LJ\GitHub\KICAD_ENGINE`. This path drift affects `.codex/config.toml`, `README_GPT.md`, `FOR CHAT GPT.MD`, prior audits, and some prompts.
- `FOR CHAT GPT.MD` is partly stale compared with `CURRENT_PROJECT.md`. It still says the active project has no KiCad source files, while `CURRENT_PROJECT.md` says the ESP32 project has a rough schematic draft state.
- `.codex/prompts/START_CODEX_KICAD_ENGINE.md` does not include `00_CODEX_START/CONTROL_PLANES.md` in its startup read list, even though `AGENTS.md` now requires it.
- The current folder does not appear to be a Git repository from the local command line. `git status` cannot be used here to confirm public-release state, changed files, ignored files, or package hygiene.
- No top-level `.vscode` or `.claude` integration exists, even though the product goal includes VS Code-based Codex, Claude, and similar agents.
- No top-level setup, installer, release, or packaging folder exists. `05_OUTPUTS/release_packages` is present but empty.
- Several tool statuses remain "installed/help-tested/not project-tested" or "cloned/not installed." That is appropriate for safety, but it limits product claims.
- The datasheet folder lacks a manifest, source URLs, revision metadata, copyright status, extraction notes, and project-component mapping.
- Component preferences are mostly placeholders plus observations from a reference board. There is no real component database yet.
- Symbol and footprint knowledge is mostly a policy need, not an implemented database.
- Public release hygiene is not established. The workspace contains local tool repos, Python environments, Node workspaces, logs, outputs, backups, and datasheet PDFs that may not belong in a public open-source repo as-is.

## What Is Missing

- A public-facing README that clearly states product purpose, supported workflows, setup, safety model, and limitations.
- License file, contribution guide, code of conduct, security policy, issue templates, and release notes.
- `.gitignore` and packaging policy for local environments, cloned third-party repos, logs, backups, private projects, outputs, and datasheets.
- Reproducible setup scripts that can check prerequisites without installing tools by default.
- VS Code workspace recommendations, tasks, and optional extension guidance.
- Claude-oriented prompt/context files.
- Agent-neutral prompt contracts independent of Codex naming.
- A formal datasheet manifest schema.
- A component database schema.
- A symbol-footprint-pin mapping review schema.
- A footprint verification checklist with package drawings, pin 1, courtyard, paste, mask, drill, and 3D model evidence.
- A connector orientation and mating-part checklist.
- Automated checks for stale paths and out-of-sync handoff files.
- A public sample project that demonstrates the full workflow without private data.
- CI or local regression tests for scripts.
- KiCad version compatibility matrix.
- Public docs explaining how to keep manufacturing outputs `NOT_FINAL`.
- A release installer or bootstrap plan suitable for users who clone the repo fresh.

## Before GitHub Public Release

Build or fix these items first:

- Decide what should be committed to the public repo. Do not publish local virtual environments, generated outputs, backups, private projects, command transcripts with local paths, or third-party cloned repos unless there is a deliberate vendoring strategy.
- Add a public `.gitignore`.
- Add a license and third-party attribution policy.
- Add a proper public `README.md` with local-first KiCad AI positioning, setup, usage, safety gates, and limitations.
- Normalize path assumptions so docs and configs can work from a cloned repo path, not only `C:\Users\LJ\KICAD_ENGINE`.
- Replace hardcoded local paths in example configs with templates or documented user-local setup steps.
- Add `.vscode` recommendations/tasks if VS Code is a primary product surface.
- Add Claude-compatible handoff or prompt files if Claude support is a product claim.
- Create a dry-run setup checker and document optional install steps separately.
- Add a public sample project and expected reports.
- Add tests for PowerShell scripts where practical.
- Add manifest schemas for datasheets, components, and verification reports.
- Add a documentation page explaining legal treatment of datasheets and why they may be user-local rather than redistributed.
- Add release packaging rules that exclude secrets, private projects, backups, downloaded datasheets without permission, and final fabrication claims.

## Before Claiming Serious Flux-Style Competitor Status

The repo needs substantially more product capability before making strong competitor claims:

- Reliable natural-language-to-KiCad workflows that produce reviewable proposed changes, not opaque design mutations.
- Robust schematic analysis beyond ERC, including power tree checks, connector intent, bus consistency, protection circuits, and datasheet-backed electrical limits.
- Robust PCB analysis beyond DRC, including placement intent, connector orientation, assembly risk, thermal paths, keepouts, mounting holes, antenna constraints, and fab-house constraints.
- A real component knowledge graph with datasheet provenance, lifecycle/sourcing status, verified footprints, alternates, and project usage.
- Symbol-footprint-pin mapping validation that catches common AI errors.
- Datasheet extraction pipeline with human review and citations.
- Visual review workflows that compare board renderings, screenshots, 3D/STEP outputs, and expected connector/mechanical orientation.
- Demonstrated end-to-end examples on safe open designs.
- Regression tests across KiCad versions and operating systems.
- A clean installer or bootstrap flow for normal users.
- Clear UX for agent modes: read-only, propose-only, edit-with-backup, verification, release-candidate, and final-release.
- Human signoff integration for all fabrication-critical claims.
- Documented limitations showing when a cloud-first tool may still be more integrated or convenient.

## Risk Areas

### Datasheet Copyright

Datasheets may be copyrighted even when publicly downloadable. Public repo releases should not blindly include downloaded PDFs. The engine needs a manifest with source URLs, access dates, and redistribution status. For public distribution, prefer metadata and user-local download instructions unless permission is clear.

### Package Manager Installs

Tool install scripts can modify user machines, create dependency conflicts, or pull unreviewed code. Default setup should be dry-run and explicit. Optional installs should use isolated environments and avoid global package changes unless the user opts in.

### KiCad Version Drift

KiCad 8, KiCad 9, and future versions may differ in file formats, ERC/DRC behavior, library names, exporters, and Python APIs. Reports should capture KiCad version, and public compatibility should be tested.

### Footprint Accuracy

AI-generated or AI-selected footprints are high risk. Every footprint needs datasheet package drawing review, pad geometry review, pin mapping, courtyard, paste/mask behavior, drill/mechanical checks, and 3D/mechanical evidence where applicable.

### Connector Orientation

Connectors are a common fabrication and assembly failure point. The engine needs explicit checks for pin 1, keying, mating connector, cable exit direction, board-edge orientation, current rating, voltage rating, strain relief, and human-readable silkscreen.

### Fabrication Output Verification

Gerbers, drills, pick-and-place, BOM, STEP, PDFs, and ZIPs must not be considered final simply because they were generated. Release packages need manifest checks, source-to-output traceability, ERC/DRC evidence, BOM/PNP consistency, footprint review, and visual review.

### Unsafe AI Edits

AI agents can corrupt KiCad source files, use stale paths, modify the wrong project, overwrite outputs, or make plausible but wrong electrical decisions. Protected edits must remain gated by active project confirmation, backup, file scope, rollback plan, verification plan, and post-edit ERC/DRC.

## Recommended Build Order

1. Fix public identity: README, product vision, architecture, limitations, and path strategy.
2. Add public release hygiene: license, `.gitignore`, contribution docs, and packaging exclusions.
3. Create schemas for datasheets, components, footprints, and verification manifests.
4. Add a public sample project and script regression tests.
5. Make VS Code and Claude support concrete through repo files, not just claims.
6. Harden verification reports and release package gates.
7. Add evidence-backed component and footprint review workflows.
8. Only then start advertising the project as a serious open-source alternative to cloud-first PCB AI tools.

## Bottom Line

The repo has a strong safety and workflow foundation. Its current public product gap is not raw tooling; it is packaging, path portability, public documentation, component/datasheet/footprint knowledge, reproducible setup, and demonstrated end-to-end examples.

The right near-term claim is: "KiCad Engine is an early local-first AI-assisted KiCad workspace with strong safety gates and a growing toolchain."

The wrong near-term claim is: "KiCad Engine already replaces cloud PCB AI design tools."
