# Repository Map

Legacy KiCad/Codex external repositories belong in:

`03_TOOLS\repos`

Platform-specific helper repositories may live under their platform roots. Windows GUI automation helper repositories belong in:

`03_TOOLS\windows\repos`

Common future repository root:

`03_TOOLS\common\repos`

Linux future repository root:

`03_TOOLS\linux\repos`

## Repository Root Rules
- Legacy repo root: `03_TOOLS\repos`.
- Common repo root: `03_TOOLS\common\repos`.
- Windows repo root: `03_TOOLS\windows\repos`.
- Linux repo root: `03_TOOLS\linux\repos`.
- Accuracy engine root: `09_ACCURACY_ENGINE`.
- Knowledge base root: `10_KNOWLEDGE_BASE`.
- Library factory root: `11_LIBRARY_FACTORY`.
- Reference design library root: `12_REFERENCE_DESIGN_LIBRARY`.
- Part ingestion root: `13_PART_INGESTION`.
- Layout automation root: `14_LAYOUT_AUTOMATION`.
- Benchmarks root: `15_BENCHMARKS`.
- Current KiCad/Codex common repos remain in the legacy root until an approved migration moves them.
- Windows GUI helper repos currently live under `03_TOOLS\windows\repos`.
- Linux-specific repos should be placed under `03_TOOLS\linux\repos` only when a future prompt explicitly approves adding them.
- Do not move, pull, build, install, or edit third-party repos unless explicitly requested.

## Current State
- Approved open-source KiCad/Codex support repositories are cloned under `03_TOOLS\repos`.
- Selected tools have dependencies installed only in isolated workspace environments under `03_TOOLS\python_envs` or `03_TOOLS\node_envs`.
- Third-party repository working trees remain clean and should not be edited directly.
- Project-scoped MCP is configured only for `kicad-mcp-pro` in analysis mode.
- Do not pull changes unless explicitly requested.
- Last inspection: 2026-04-30 final setup audit. All seven requested repositories existed, were inspected without recloning or pulling, and had clean working trees.
- Windows GUI helper repositories were cloned under `03_TOOLS\windows\repos` on 2026-04-30. They are cloned reference/tool repos only; none were installed or built.

## Production Top-Level Folder Map

Use this compact map during startup before routing new files:

| Folder | Role |
| --- | --- |
| `.codex/` | Workspace-local Codex config and prompts; no secrets. |
| `.github/` | GitHub Actions and release automation. |
| `.prompts/` | Codex, Claude, and shared prompt packs. |
| `.vscode/` | VS Code workspace settings, tasks, launch config, and extension recommendations. |
| `00_CODEX_START/` | Startup, safety, structure, routing, index, and AI quality gate control plane. |
| `01_MEMORY/` | Durable reusable global memory and master memory index. |
| `02_HISTORY/` | Session logs, command logs, audits, issue logs, verification reports, AI-quality evidence, and master history index. |
| `03_TOOLS/` | Scripts, local tool wrappers, read-only analyzers, and external tool notes. |
| `04_KICAD_PROJECTS/` | Active projects and templates; KiCad edit gates apply. |
| `05_OUTPUTS/` | Generated outputs, reports, and NOT_FINAL packages. |
| `06_DATASHEETS/` | Datasheet metadata, source links, summaries, policies, and missing-document records. |
| `07_REFERENCE_DESIGNS/` | Link-first reference design notes separate from formal reference design library records. |
| `08_COMPONENT_DATABASE/` | Structured part records, schemas, verification levels, and KiCad candidate links. |
| `09_ACCURACY_ENGINE/` | Schematic, PCB, verification, workflow, and anti-hallucination rules. |
| `10_KNOWLEDGE_BASE/` | Circuit patterns, design patterns, checklists, common mistakes, manufacturing guidance, and AI-agent guidance. |
| `11_LIBRARY_FACTORY/` | Symbol, footprint, package mapping, 3D model, QA, and project-local library standards. |
| `12_REFERENCE_DESIGN_LIBRARY/` | Public-source reference design records with source, license, and verification level. |
| `13_PART_INGESTION/` | Datasheet-to-record workflows, extraction rules, templates, and stub scripts. |
| `14_LAYOUT_AUTOMATION/` | Placement/routing assistance plans, constraint extraction, autorouter notes, and human layout gates. |
| `15_BENCHMARKS/` | Benchmark methodology, tasks, scoring rubrics, and real results only. |
| `16_INSTALLER/` | Installer planning and release-facing installer coordination. |
| `17_RELEASE_BUILD/` | Payload, artifact, checksum, and release checklist planning. |
| `18_PUBLIC_DOCS/` | Public user documentation coordination. |
| `19_TEST_PROJECTS/` | Disposable planning-only or test projects; no real fab-ready outputs. |
| `20_CI_CD/` | CI/CD planning, build matrix, test matrix, and workflow design. |
| `21_LICENSE_ATTRIBUTION/` | License, attribution, datasheet redistribution, vendor document, and public repo risk records. |
| `22_SECURITY/` | Security policy, secret handling, installer safety, script safety, and reporting rules. |
| `23_PACKAGE_PROFILES/` | Package profile schemas and placeholder package-to-footprint rules. |
| `24_FAB_PROFILES/` | Fabrication-house profile schemas and NOT_FINAL output rules. |
| `25_VENDOR_DATABASE/` | Vendor source priority, official document links, lifecycle, and sourcing metadata. |
| `26_AGENT_QUALITY/` | AI scoring, evidence, hallucination-risk, and quality-gate support. |
| `27_EXAMPLES/` | EXAMPLE_ONLY prompt, report, record, datasheet, and scorecard examples. |
| `99_BACKUPS/` | Pre-edit backups and recovery snapshots; do not delete. |
| `docs/` | Current public/end-user docs implementation root. |
| `installer/` | Current Electron installer source and payload builder implementation root. |
| `setup/` | Current cross-platform setup scripts. |

## Accuracy Engine

`09_ACCURACY_ENGINE` contains schematic, PCB, verification, and workflow rules that prevent AI agents from guessing during KiCad design work.

Read the relevant accuracy-engine files before:

- Creating schematics.
- Selecting symbols.
- Verifying pinouts.
- Selecting or approving footprints.
- Creating PCB layouts.
- Reviewing ERC, DRC, BOM, PNP, Gerber, or release packages.

Do not store KiCad project source files, downloaded datasheets, generated manufacturing outputs, or secrets in `09_ACCURACY_ENGINE`.

## Knowledge Base

`10_KNOWLEDGE_BASE` contains reusable AI-readable circuit blocks, design patterns, review checklists, common mistakes, manufacturing package rules, and AI-agent stop/verify guidance.

Read the relevant knowledge-base files before:

- Proposing common schematic circuit blocks.
- Planning MCU minimum systems.
- Planning power trees.
- Planning connector interfaces.
- Planning USB, CAN, LIN, RS485, RF, automotive, or regulator circuits.
- Preparing manufacturing package reviews.

Knowledge-base files are planning aids, not datasheet proof. Exact values, pinouts, footprints, package drawings, connector drawings, stackups, and board-house requirements still require source verification.

Do not store KiCad project source files, downloaded datasheets, generated manufacturing outputs, or secrets in `10_KNOWLEDGE_BASE`.

## Library Factory

`11_LIBRARY_FACTORY` contains symbol creation standards, footprint creation standards, package-to-footprint mapping rules, project-local library rules, and basic read-only validation scripts.

Read the relevant library-factory files before:

- Creating or verifying a KiCad symbol.
- Creating or verifying a KiCad footprint.
- Mapping a symbol to a footprint.
- Mapping a datasheet package or connector drawing to a KiCad footprint.
- Editing project-local symbol or footprint libraries.

Library-factory scripts are read-only QA helpers. They can flag structural issues, but they do not replace datasheet pinout review, package drawing review, connector orientation review, ERC, DRC, or human approval.

Do not store installed KiCad global libraries, user-global library tables, active KiCad project source files, generated manufacturing outputs, or secrets in `11_LIBRARY_FACTORY`.

## Reference Design Library

`12_REFERENCE_DESIGN_LIBRARY` contains link-first public-source reference design records, source/license rules, verification levels, and category-specific checklists.

Read the relevant reference-design files before:

- Using a vendor or open hardware design as evidence.
- Adapting a reference schematic block.
- Learning connector, power, USB, CAN, RF, automotive, MCU, or manufacturing patterns from examples.
- Copying any source file into the repo.

Reference designs are evidence, not automatic approval. Do not copy proprietary designs without permission. Prefer links, summaries, and verification notes unless license and redistribution are clearly reviewed.

Do not store active KiCad project source files, copied proprietary designs, generated manufacturing outputs, unclear-license archives, or secrets in `12_REFERENCE_DESIGN_LIBRARY`.

## Part Ingestion

`13_PART_INGESTION` contains workflows, extraction rules, AI summary templates, and stub generators for adding new parts from user-provided datasheets, source URLs, or local document paths.

Read the relevant part-ingestion files before:

- Adding a new component record.
- Summarizing a user-provided datasheet.
- Creating symbol or footprint checklists from a datasheet.
- Extracting pinout, electrical limits, layout notes, or common mistakes.

Part-ingestion scripts generate placeholders only. They do not scrape websites, download PDFs, redistribute copyrighted documents, parse datasheets automatically, or verify values.

Do not store active KiCad project files, redistributed restricted datasheets, generated manufacturing outputs, or secrets in `13_PART_INGESTION`.

## Layout Automation

`14_LAYOUT_AUTOMATION` contains realistic placement assistance, routing assistance, constraint extraction, KiCad autorouter option, FreeRouting integration, AI placement review, human layout gate, and roadmap documents.

Read the relevant layout automation files before:

- Suggesting AI placement.
- Suggesting routing assistance.
- Considering FreeRouting or another autorouter.
- Comparing before/after DRC for layout changes.
- Claiming any layout automation capability.

Layout automation docs are planning and review guidance unless a future task implements tested scripts. Do not store active KiCad project source files, routed board outputs, autorouter binaries, generated manufacturing outputs, or secrets in `14_LAYOUT_AUTOMATION`.

## Benchmarks

`15_BENCHMARKS` contains benchmark methodology, task definitions, scoring rubrics, and future real run results.

Read the relevant benchmark files before:

- Running a benchmark task.
- Scoring a benchmark run.
- Comparing KiCad Engine to another PCB AI tool.
- Publishing any performance or capability claim based on benchmark results.

Benchmarks are evidence gates, not marketing copy. Do not create fake results, do not backfill scores from memory, and do not store active KiCad project source files, generated manufacturing outputs, secrets, or unreviewed comparison claims in `15_BENCHMARKS`.

## Common Repositories Currently In Legacy Root

These are common/project-intelligence repos by role, but they remain in `03_TOOLS\repos` until migration is explicitly approved:

- `kicad-mcp-pro`
- `kicad-happy`
- `KiCAD-MCP-Server`
- `KiBot`
- `InteractiveHtmlBom`
- `PcbDraw`
- `kicanvas`

Recommended future location for these repos is `03_TOOLS\common\repos`, but moving them now would risk breaking install logs, venv references, command examples, MCP snippets, and tool documentation.

## Repository Records

### kicad-mcp-pro
- Local path: `03_TOOLS\repos\kicad-mcp-pro`
- Source URL: `https://github.com/oaslananka/kicad-mcp-pro.git`
- Current branch: `main`
- Latest commit: `9991061561d1e3551dee03a525c06bf2e2cbaf02`
- Latest commit subject: `chore: sync uv lock for 3.1.8`
- Purpose: MCP-assisted KiCad automation support.
- Status: installed in isolated workspace Python environment; project-scoped MCP configured in analysis mode only.
- Last inspected: 2026-04-30.

### kicad-happy
- Local path: `03_TOOLS\repos\kicad-happy`
- Source URL: `https://github.com/aklofas/kicad-happy.git`
- Current branch: `main`
- Latest commit: `2a7dc4147a8edbbe3694498ff1ba9f06e37244cb`
- Latest commit subject: `fix: handle dict format in power_rails list (#16)`
- Purpose: KiCad helper automation and scripting support.
- Status: installed in isolated workspace Python environment for analysis-only use.
- Last inspected: 2026-04-30.

### KiCAD-MCP-Server
- Local path: `03_TOOLS\repos\KiCAD-MCP-Server`
- Source URL: `https://github.com/mixelpixx/KiCAD-MCP-Server.git`
- Current branch: `main`
- Latest commit: `d3c01e20bd3af96eaaebcdb84baa7ec9908b31e4`
- Latest commit subject: `Merge pull request #139 from mixelpixx/fix/post-pr88-regressions`
- Purpose: MCP server for KiCad integration experiments.
- Status: cloned, not installed, MCP not configured.
- Last inspected: 2026-04-30.

### KiBot
- Local path: `03_TOOLS\repos\KiBot`
- Source URL: `https://github.com/INTI-CMNB/KiBot.git`
- Current branch: `master`
- Latest commit: `367a2e04122aa46413a30e61cb213bfe7223c8c8`
- Latest commit subject: `[DOCs] Updated tags`
- Purpose: Repeatable KiCad checks, exports, and release generation.
- Status: installed in isolated workspace Python environment; not tested against a real project.
- Last inspected: 2026-04-30.

### InteractiveHtmlBom
- Local path: `03_TOOLS\repos\InteractiveHtmlBom`
- Source URL: `https://github.com/openscopeproject/InteractiveHtmlBom.git`
- Current branch: `master`
- Latest commit: `8c13013fc5233cfa31698a777813e87502bdb625`
- Latest commit subject: `Fix dnp detection for kicad variants`
- Purpose: Interactive HTML BOM generation.
- Status: installed in isolated workspace Python environment; help-tested, not project-tested.
- Last inspected: 2026-04-30.

### PcbDraw
- Local path: `03_TOOLS\repos\PcbDraw`
- Source URL: `https://github.com/yaqwsx/PcbDraw.git`
- Current branch: `master`
- Latest commit: `9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f`
- Latest commit subject: `Normalize package name and fix build command`
- Purpose: PCB rendering for documentation and visual review.
- Status: installed in isolated workspace Python environment; help-tested, not project-tested.
- Last inspected: 2026-04-30.

### kicanvas
- Local path: `03_TOOLS\repos\kicanvas`
- Source URL: `https://github.com/theacodes/kicanvas.git`
- Current branch: `main`
- Latest commit: `b031159eb74aaa7eef2b026fd85d35bc05ff2095`
- Latest commit subject: `fix: file loading fails when path contains URL-encoded characters (#192)`
- Purpose: Browser-based KiCad visualization.
- Status: isolated npm build tested under `03_TOOLS\node_envs`; source checkout remains clean.
- Last inspected: 2026-04-30.

## Windows GUI Helper Repository Records

### FlaUI
- Local path: `03_TOOLS\windows\repos\FlaUI`
- Source URL: `https://github.com/FlaUI/FlaUI.git`
- Current branch: `main`
- Latest commit: `7d600d5240ff2b8227cfcc829230cefe8116970a`
- Latest commit subject: `fix unsupporedexception (#704)`
- Purpose: .NET UI Automation library reference for structured Windows desktop automation.
- Status: cloned, not installed, not built, not used to control KiCad.
- Approximate size excluding `.git`: 464 files, 55 folders.
- Last inspected: 2026-04-30.

### FlaUInspect
- Local path: `03_TOOLS\windows\repos\FlaUInspect`
- Source URL: `https://github.com/FlaUI/FlaUInspect.git`
- Current branch: `main`
- Latest commit: `c554b6fac19d3486c4fa3cbf6f37bb6d98eed1d9`
- Latest commit subject: `Update image path in README for FlaUInspect`
- Purpose: UI Automation inspection tool reference for Windows control-tree exploration.
- Status: cloned, not installed, not built, not used to control KiCad.
- Approximate size excluding `.git`: 104 files, 19 folders.
- Last inspected: 2026-04-30.

### AutoHotkey
- Local path: `03_TOOLS\windows\repos\AutoHotkey`
- Source URL: `https://github.com/AutoHotkey/AutoHotkey.git`
- Current branch: `alpha`
- Latest commit: `7320bfffebf2eb5257990c3c24015499faaab6c8`
- Latest commit subject: `Changed built-ins to return unset by default in v2.1 mode.`
- Purpose: Windows hotkey and scripting engine source reference.
- Status: cloned, not built, not installed, not used to control KiCad.
- Approximate size excluding `.git`: 184 files, 9 folders.
- Last inspected: 2026-04-30.

### SikuliX1
- Local path: `03_TOOLS\windows\repos\SikuliX1`
- Source URL: `https://github.com/RaiMan/SikuliX1.git`
- Current branch: `master`
- Latest commit: `17b2f48f5fc38cdea81e6aa0fb336503c5dc0e79`
- Latest commit subject: `Update link for getting SikuliX ready to use`
- Purpose: Image-driven GUI automation reference for future visual workflow experiments.
- Status: cloned, not installed, not built, not used to control KiCad.
- Approximate size excluding `.git`: 538 files, 88 folders.
- Last inspected: 2026-04-30.

## Future Repository Records
When the user explicitly authorizes adding another repository, document:
- Repository name.
- Repository URL.
- Local path under `03_TOOLS\repos`.
- Purpose.
- Install date.
- Required environment.
- Command entry points.
- Known limitations.
- Related history log.
