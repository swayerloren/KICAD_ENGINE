# KiCad Engine

KiCad Engine is a local-first, open-source workspace for AI-assisted KiCad engineering from VS Code.

It does not replace KiCad. It helps Codex, Claude, and similar AI coding agents understand, inspect, validate, and safely automate work around the KiCad app already installed on your machine.

## Current Readiness

Status after the 2026-05-03 production-quality audit:

- Internal/private development: `INTERNAL_ALPHA_READY`
- Public GitHub release: `NOT_READY`
- Installer artifacts: prototype/local-test only unless a release note says otherwise
- Datasheet/component/footprint databases: useful scaffolding and partial source-link records, not complete verified engineering data

Do not treat this repository, an AI response, or any generated report as fabrication approval. Public release blockers are tracked in `05_OUTPUTS/release_readiness/FULL_REPO_BLOCKERS.md` and `05_OUTPUTS/release_readiness/FULL_REPO_NEXT_FIX_PLAN.md`.

## What It Is

KiCad Engine is a repo-based control plane for KiCad projects. It provides:

- Startup rules for AI agents.
- Prompt packs for Codex and Claude.
- VS Code tasks for common checks.
- Installed KiCad app discovery.
- Read-only KiCad library intelligence.
- Datasheet metadata and source-link scaffolding.
- Component records and design-rule notes.
- Reusable circuit patterns, review checklists, common mistakes, and manufacturing package guidance.
- Symbol, footprint, package-mapping, and project-local library factory standards.
- Public-source reference design links, summaries, license records, and verification notes.
- New-part datasheet ingestion workflows and stub generators.
- Realistic placement/routing assistance plans and layout review gates.
- Project validation, ERC, DRC, BOM, and review-output scripts.
- Installer source and clean workspace payload support.

The goal is to make KiCad-native engineering work more transparent, local, auditable, and repeatable when an AI coding agent is helping.

## Repository Structure

KiCad Engine now uses a production-oriented numbered folder model. The authoritative routing docs are:

- `00_CODEX_START/STRUCTURE_STANDARD.md`
- `00_CODEX_START/FOLDER_ROUTING_RULES.md`
- `00_CODEX_START/REPO_STRUCTURE_INDEX.md`

The numbered structure separates startup control, memory, history, tools, KiCad projects, generated outputs, datasheet metadata, reference designs, component intelligence, accuracy rules, reusable knowledge, library standards, ingestion workflows, layout automation planning, benchmarks, installer coordination, release build support, public docs, test projects, CI/CD, license attribution, security, package profiles, fab profiles, vendor metadata, agent quality, and examples.

Existing implementation roots such as `installer/`, `setup/`, and `docs/` remain valid until a documented migration is approved. Folder existence is not a claim that the repo is complete or release-ready.

## Who It Is For

KiCad Engine is for:

- KiCad users who want AI help without moving PCB work into a cloud-first PCB design environment.
- Engineers, makers, and open-source hardware contributors who work from VS Code.
- Users who want Codex, Claude, or another AI coding agent to read project context before making suggestions.
- Teams that want Git history, local files, explicit verification reports, and human review gates.

It is not official KiCad, not affiliated with KiCad, and not a certified engineering approval system.

## How It Uses Installed KiCad

KiCad Engine uses your installed KiCad app and `kicad-cli` where available. It can inspect KiCad paths, read libraries, run CLI checks, and generate reports without modifying installed KiCad folders.

It must not write to:

- `C:\Program Files\KiCad`
- `/Applications/KiCad`
- `/usr/share/kicad`
- User-global KiCad library tables
- Installed KiCad symbol, footprint, or 3D model libraries

KiCad Engine does not bundle KiCad in v1. If KiCad is missing, setup and installer flows should point you to official install paths and ask before installing anything.

## What It Can Do

- Help an AI agent start with the right repo memory, rules, and prompt.
- Audit the installed KiCad app read-only.
- Index stock and project libraries for candidate symbols, footprints, and 3D models.
- Check whether a project has required schematic, PCB, and library files.
- Run ERC and DRC through guarded wrappers when `kicad-cli` is available.
- Export review-only and `NOT_FINAL` manufacturing-style outputs.
- Build local datasheet and component indexes from metadata.
- Flag missing datasheets, missing footprints, connector risks, polarity risks, RF risks, and interface-review needs.
- Use `10_KNOWLEDGE_BASE/` to guide reusable circuit blocks such as USB-C, ESP32-S3 minimum systems, STM32/PIC minimum systems, CAN/LIN/RS485 nodes, power regulators, automotive input protection, RF antenna connectors, and status LED/reset blocks.
- Use `11_LIBRARY_FACTORY/` to guide source-backed KiCad symbol and footprint creation, package-to-footprint mapping, connector footprint review, and project-local library use.
- Use `12_REFERENCE_DESIGN_LIBRARY/` to learn from official vendor and open hardware reference designs while tracking source, license, verification level, and what must not be copied.
- Use `13_PART_INGESTION/` to generate datasheet summary, component record, symbol checklist, footprint checklist, layout warning, and common-mistake stubs from user-provided metadata.
- Use `14_LAYOUT_AUTOMATION/` to plan realistic placement/routing assistance, constraint extraction, FreeRouting experiments, DRC comparison, and human layout review gates.
- Use `15_BENCHMARKS/` to define honest benchmark tasks, scoring rubrics, and future results without fake scores or unsupported comparison claims.
- Keep command reports under `02_HISTORY/` or `05_OUTPUTS/`.

## What It Cannot Do

- Replace KiCad.
- Guarantee a design is electrically correct.
- Guarantee a footprint, symbol, pinout, or datasheet value is correct.
- Certify a board for fabrication.
- Submit manufacturing orders.
- Store Codex, Claude, OpenAI, Anthropic, GitHub, distributor, or fab-house credentials.
- Silently install tools.
- Bypass vendor datasheet copyright or redistribution limits.

## Install

Use one of these paths:

1. Download or clone the repo, then open the folder in VS Code.
2. Use a release installer artifact when a tested release is available.
3. Build the installer from source if you are working on installer development.

Platform quickstarts:

- `QUICKSTART_WINDOWS.md`
- `QUICKSTART_MACOS.md`
- `QUICKSTART_LINUX.md`

Run the health check from the repo root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

or:

```bash
python health_check.py
```

Run the read-only project gate runner on the current golden-path fixture:

```powershell
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"
```

The runner writes `PROJECT_GATE_REPORT.md` and `PROJECT_GATE_REPORT.json` under `05_OUTPUTS/gate_runs/<timestamp>/`. It aggregates existing evidence only; it does not edit KiCad files, run ERC/DRC, or generate fabrication outputs. The current ATtiny85 sample is expected to return `BLOCKED_UNTIL_HUMAN_REVIEW` until its documented ERC, DRC, footprint, connector-orientation, polarity, and human-review blockers are resolved.

## Sample Projects And Golden-Path Demo

KiCad Engine includes a controlled sample-project area for public-safe workflow
demonstrations:

- `19_TEST_PROJECTS/README.md`
- `19_TEST_PROJECTS/SAMPLE_PROJECTS_INDEX.md`
- `19_TEST_PROJECTS/HOW_TO_RUN_SAMPLE_PROJECTS.md`
- `19_TEST_PROJECTS/HOW_TO_INTERPRET_GATE_RESULTS.md`
- `18_PUBLIC_DOCS/HOW_TO_RUN_GOLDEN_PATH_DEMO.md`
- `18_PUBLIC_DOCS/HOW_TO_VERIFY_PROJECT.md`

Current demo fixture:

```text
19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board
```

Honest status:

- It is a controlled demo fixture.
- It is not yet a clean passing design.
- It is blocked until human review and remaining ERC/DRC/footprint issues are resolved.
- Latest one-command gate result: `BLOCKED_UNTIL_HUMAN_REVIEW`.

Inspect sample reports here:

- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/`
- latest `05_OUTPUTS/gate_runs/<timestamp>/PROJECT_GATE_REPORT.md`

Sample projects come from public/open sources only after intake, license
screening, attribution preservation, and public-bundle review. For the current
ATtiny85 fixture, attribution is preserved in
`19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md`.

All generated sample outputs are review artifacts. They are `NOT_FINAL` and must
not be used for manufacturing.

Installer source lives under `installer/`. Windows local unsigned build support exists, and macOS/Linux package support is designed for platform runners. Do not treat installer artifacts as production-ready unless the release notes show platform smoke tests, checksums, and signing/notarization status where applicable.

## Use With VS Code

Open the repo folder in VS Code and review:

- `START_HERE_FOR_USERS.md`
- `START_HERE_FOR_AI_AGENTS.md`
- `.prompts/README.md`
- `.vscode/tasks.json`

Run tasks through `Tasks: Run Task`:

- `KiCad Engine: Run Health Check`
- `KiCad Engine: Audit Installed KiCad App`
- `KiCad Engine: Build Datasheet Index`
- `KiCad Engine: Build Component Database Index`
- `KiCad Engine: Validate a KiCad Project`
- `KiCad Engine: Run ERC`
- `KiCad Engine: Run DRC`
- `KiCad Engine: Export NOT_FINAL Review Package`

## Use With Codex

1. Open the repo in VS Code.
2. Log in to Codex with your own account.
3. Open `.prompts/codex/00_START_SESSION.md`.
4. Paste that prompt into Codex.
5. Use task-specific prompts from `.prompts/codex/`.

Codex should read `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, and the required `00_CODEX_START/` startup files before touching KiCad project files. Project edits require active project confirmation, backup, rollback plan, and verification plan.

Startup and closeout indexes are rebuilt with safe scripts under `03_TOOLS/scripts/indexing/`. These scripts only write generated Markdown/JSON index files and master memory/history summaries; they do not edit KiCad design files.

## Use With Claude

1. Open the repo in VS Code.
2. Log in to Claude with your own account.
3. Open `.prompts/claude/00_START_SESSION.md`.
4. Paste that prompt into Claude.
5. Use task-specific prompts from `.prompts/claude/`.

Claude should follow the same safety gates: no fake datasheet claims, no unverified footprint approval, no unbacked KiCad source edits, and `NOT_FINAL` labels for fabrication-style outputs.

## Datasheet Database

`06_DATASHEETS/` is an AI-friendly datasheet and reference library scaffold. It stores source links, metadata, summaries, naming rules, missing-document reports, and redistribution policy notes.

The datasheet database is not complete. Public releases should prefer links and metadata. Datasheet PDFs may be link-only unless redistribution rights are confirmed.

## Component Database

`08_COMPONENT_DATABASE/` stores structured part intelligence beyond PDFs:

- Part schemas and verification levels.
- Markdown and JSON component records.
- KiCad symbol and footprint candidate notes.
- Design-rule snippets.
- Part-selection guides.

Records may be placeholders. Do not treat a part record as approved unless the verification status and cited sources support that claim.

## Knowledge Base

`10_KNOWLEDGE_BASE/` stores practical circuit patterns, design patterns, checklists, common mistakes, manufacturing package rules, and AI-agent guidance.

It is not a datasheet replacement. Agents must still verify exact values, pinouts, packages, footprints, connector drawings, stackups, and fab-house requirements from source documents before approving a design.

## Library Factory

`11_LIBRARY_FACTORY/` stores standards and basic read-only scripts for KiCad symbols, footprints, package mapping, and project-local libraries.

It does not approve symbols or footprints. Symbol pinouts require exact source evidence, footprint geometry requires exact package or connector drawings, and connector orientation requires human review.

## Reference Design Library

`12_REFERENCE_DESIGN_LIBRARY/` stores link-first reference design records, public source rules, verification levels, category checklists, and templates.

Reference designs are evidence, not automatic approval. Do not copy proprietary designs without permission, and do not reuse schematic/layout/footprint choices without exact source, license, and human review.

## Part Ingestion

`13_PART_INGESTION/` provides a workflow and scripts for adding new parts from user-provided datasheets, local paths, or source links.

It generates structured stubs only. It does not scrape websites, download PDFs, redistribute copyrighted documents, or verify values. AI agents must mark uncertainty clearly until source review is complete.

## Layout Automation

`14_LAYOUT_AUTOMATION/` documents realistic KiCad-native placement and routing assistance paths.

It does not claim complete AI auto-layout or autorouting. It covers placement proposals, high-risk net review, constraint extraction, FreeRouting integration planning, DRC before/after comparison, and human layout review gates.

## Benchmarks

`15_BENCHMARKS/` defines methodology, tasks, and scoring rubrics for measuring KiCad Engine progress.

It does not contain fake results. Public comparisons to other PCB AI tools require actual benchmark runs, preserved artifacts, identical task conditions, reviewer notes, and clear uncertainty.

## NOT_FINAL Output Rule

AI review is not fabrication approval.

Generated manufacturing-style outputs must remain `NOT_FINAL` until ERC, DRC, BOM, symbol, footprint, pinout, datasheet, connector, polarity, mechanical, and visual reviews are complete.

You are responsible for final manufacturing decisions.

## Documentation

Begin here:

- `18_PUBLIC_DOCS/START_HERE_FOR_USERS.md`
- `START_HERE_FOR_USERS.md`
- `USER_MANUAL.md`
- `INSTALLER_USER_GUIDE.md`
- `FAQ.md`
- `TROUBLESHOOTING.md`
- `docs/WHAT_IS_KICAD_ENGINE.md`
- `docs/KICAD_ENGINE_VS_FLUX_AI.md`
- `docs/SAFETY_AND_LIMITATIONS.md`
- `10_KNOWLEDGE_BASE/README.md`
- `10_KNOWLEDGE_BASE/ai_agent_guidance/ANTI_HALLUCINATION_RULES.md`
- `11_LIBRARY_FACTORY/README.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_QA_CHECKLIST.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_QA_CHECKLIST.md`
- `12_REFERENCE_DESIGN_LIBRARY/README.md`
- `12_REFERENCE_DESIGN_LIBRARY/00_INDEX/REFERENCE_RECORD_TEMPLATE.md`
- `13_PART_INGESTION/README.md`
- `13_PART_INGESTION/PART_INGESTION_WORKFLOW.md`
- `14_LAYOUT_AUTOMATION/README.md`
- `14_LAYOUT_AUTOMATION/ROADMAP.md`
- `15_BENCHMARKS/README.md`
- `15_BENCHMARKS/BENCHMARK_METHODOLOGY.md`

## Contribute

Read `CONTRIBUTING.md`, `SECURITY.md`, `DISCLAIMER.md`, and `PUBLIC_RELEASE_CHECKLIST.md` before opening a pull request.

Good contributions include safer scripts, clearer docs, verified component records with citations, better KiCad CLI workflows, and public-release hygiene.

Do not contribute secrets, unsupported datasheet claims, copyrighted PDFs without redistribution permission, or fabrication outputs labeled final without verification evidence.

## License

This repository is released under the MIT License. See `LICENSE`.

Third-party tools, KiCad assets, datasheets, vendor documents, and linked resources may have their own licenses and redistribution rules.
