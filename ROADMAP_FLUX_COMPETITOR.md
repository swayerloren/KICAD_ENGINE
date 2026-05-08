# Roadmap: Local-First KiCad Engine As A Cloud PCB AI Competitor

Date: 2026-05-03

## Position

KiCad Engine should not try to become a hosted PCB CAD platform. Its strongest path is to become a serious local-first, KiCad-native, auditable engineering engine for users who want AI help while keeping KiCad and local project files as the source of truth.

The target claim is not "better than Flux at everything." The target claim is:

> Designed to become stronger for local-first KiCad users who need transparent prompts, user-owned data, source-backed component evidence, KiCad-native checks, Git workflows, and human review gates.

## Competitive Requirements

Public Flux documentation shows useful cloud PCB AI feature areas:

- AI project planning and context-aware assistance.
- Component and datasheet research.
- Design modifications from chat.
- Schematic component placement and wiring assistance.
- Auto-layout/routing jobs for simple to medium boards.
- Pricing and availability from distributors.
- Built-in SPICE simulation.
- Real-time browser collaboration and version control.
- Community parts, projects, and templates.
- Manufacturing exports.

KiCad Engine must answer those categories with local, KiCad-native equivalents.

## Milestone Plan

### v0.8 Accuracy And Evidence Foundation

Goal: make guessing visibly unacceptable.

Build:

- `09_ACCURACY_ENGINE` integrated into prompt packs.
- Component record linter.
- Datasheet source-link validator improvements.
- Symbol/footprint candidate report generator.
- ERC/DRC parser prototype.
- Human review gate report.

Exit criteria:

- A sample project review produces evidence status for components, symbols, footprints, connectors, polarity, RF/USB/CAN, ERC, DRC, BOM, and outputs.

### v0.9 Component, Datasheet, And Constraint MVP

Goal: make component research and design constraints machine-checkable.

Build:

- Requirements schema.
- Component evidence schema enforcement.
- Datasheet extraction stubs with citation fields.
- Board-house/fab constraint profiles.
- KiCad net class and rule reader.
- BOM field coverage checker.
- Git-friendly KiCad review bundle.

Exit criteria:

- Agent can propose parts with explicit source evidence and reject missing evidence before schematic work.

### v1.0 Public Local-First KiCad Review Release

Goal: credible public MVP.

Build:

- Public sample project.
- Full health check passing on clean install.
- KiCad app audit on Windows and at least documented macOS/Linux paths.
- ERC/DRC/BOM/footprint/datasheet review workflow.
- NOT_FINAL manufacturing package workflow.
- Public docs and release checklist.

Exit criteria:

- A new user can install/open the repo, audit KiCad, validate a sample project, run checks, and produce a NOT_FINAL review package.

### v1.1 Safe Schematic Generation MVP

Goal: source-backed schematic creation in copied/approved projects.

Build:

- KiCad schematic parser/writer.
- Project-local symbol library workflow.
- Symbol pinout verifier.
- Schematic patch preview.
- ERC-driven correction loop.
- Source-backed component insertion workflow.

Exit criteria:

- Agent can create a small verified schematic block in a copied KiCad project with source evidence, backup, diff, ERC, and review report.

### v1.2 Symbol, Footprint, And Review Dashboard

Goal: reduce high-risk library mistakes.

Build:

- Footprint parser and verifier.
- Package drawing evidence schema.
- Connector orientation review reports.
- Polarity review reports.
- Local review dashboard from JSON/Markdown outputs.
- KiCad semantic diff.

Exit criteria:

- Agent cannot mark a footprint verified unless package drawing evidence is recorded.

### v1.3 Manufacturing And BOM Competitor Layer

Goal: make local KiCad outputs more auditable than cloud one-click exports.

Build:

- Board-house profiles for common fabs.
- BOM and PNP validator.
- Gerber/drill/STEP/package manifest validator.
- Checksum generation.
- Distributor CSV import.
- Sourcing stale-data markers.

Exit criteria:

- Generated packages remain NOT_FINAL until a gate report shows every required review status.

### v1.4 Reusable Design Blocks And Architecture Planner

Goal: compete with cloud templates and forkable project starts while remaining KiCad-native.

Build:

- Verified local design-block library.
- Architecture graph planner.
- Power tree planner.
- Interface template library.
- Project scaffold generator with source-linked blocks.

Exit criteria:

- User can start from verified KiCad-native blocks and see evidence requirements before schematic generation.

### v1.5 Layout Planning And Routing Assistance

Goal: useful local PCB layout help without unsafe autonomous layout claims.

Build:

- Placement zone planner.
- Critical net classifier.
- Constraint-aware placement proposal.
- Optional external router workflow on copied boards.
- DRC regression loop.
- Visual placement/routing review report.

Exit criteria:

- Agent can propose placement/routing changes in a copied board and produce DRC plus visual review evidence, without claiming final layout approval.

### v1.6 Simulation And Advanced Datasheet Intelligence

Goal: close the simulation and datasheet gap.

Build:

- KiCad/ngspice runner.
- Simulation test bench templates.
- Model license tracker.
- Datasheet table extractor.
- Citation-backed electrical-rule extraction.
- Metric extraction from simulation output.

Exit criteria:

- Agent can run a source-backed simulation workflow and report assumptions, models, plots, and limits.

### v2.0 Human-Guided Local AI PCB Engine

Goal: credible advanced local-first competitor for KiCad users.

Build:

- Source-backed block-level schematic synthesis.
- Verified symbol/footprint generation.
- Constraint-aware placement and routing assistance.
- Local knowledge graph for parts, datasheets, symbols, footprints, rules, and reviews.
- Reproducible local test suite across KiCad versions.

Exit criteria:

- Demonstrated real-board case studies with documented limits, review gates, and reproducible local outputs.

## Non-Goals

- Do not replace KiCad.
- Do not hide design source in a proprietary parallel format.
- Do not silently upload project data.
- Do not store AI credentials.
- Do not claim fabrication approval from AI output.
- Do not mark outputs final without recorded human review.

## Immediate Next Actions

1. Add `09_ACCURACY_ENGINE` references to prompt-pack task files.
2. Build a component evidence linter.
3. Build a symbol/footprint candidate report that uses installed KiCad indexes.
4. Build ERC/DRC report parsers.
5. Choose one public sample KiCad project for repeatable demonstrations.
6. Define v0.8 acceptance tests.
