# Flux-Level Feature Gap Analysis

Date: 2026-05-03

## Scope

Analyze what KiCad Engine must add to compete with or exceed cloud PCB AI tools such as Flux AI while staying KiCad-native, local-first, transparent, and auditable.

This is a planning and gap-analysis document. It does not claim KiCad Engine currently beats Flux or any other cloud PCB AI platform.

## Public Sources Reviewed

Primary public sources were Flux official pages and documentation:

- Flux product page: https://www.flux.ai/p
- Flux Copilot getting-started guide: https://docs.flux.ai/tutorials/getting-started-copilot
- Flux generative AI use cases: https://docs.flux.ai/tutorials/generative-ai-use-cases
- Flux PCB editor reference: https://docs.flux.ai/reference/reference-pcb-editor
- Flux auto-layout guide: https://docs.flux.ai/tutorials/auto-layout
- Flux simulator tool: https://docs.flux.ai/reference/simulator-tool
- Flux component-library guide: https://docs.flux.ai/tutorials/tutorial-add-part-library
- Flux pricing and availability reference: https://docs.flux.ai/flux/reference/reference-inspector-pricing-and-availability
- Flux layout rules list: https://docs.flux.ai/reference/layout-rules-types
- Flux project reuse guide: https://docs.flux.ai/tutorials/reusing-community-projects
- Flux data portability/export reference: https://docs.flux.ai/reference/data-portability
- Flux PCB editor FAQ: https://docs.flux.ai/faq/faq-s-about-the-pcb-editor

## Market Reality From Public Sources

Flux publicly positions itself around browser-based PCB design with AI planning, schematic assistance, project-context awareness, component research, datasheet/file references, design modification, auto-layout/routing assistance, pricing/availability, built-in simulation, collaboration, reusable projects/templates, DRC, manufacturing exports, and reversible/reviewable AI actions.

KiCad Engine's credible competitive stance is different:

- Use the user's installed KiCad app.
- Keep source files local and user-owned.
- Store prompts, rules, memory, component evidence, and reports in plain files.
- Prefer deterministic KiCad-native checks.
- Require explicit human review gates.
- Expose how AI agents reached conclusions.

To become a serious competitor, KiCad Engine needs much more than documentation. It needs verified data, source-backed part intelligence, KiCad-native writers, project-safe diff/patch tooling, layout assistants, sourcing integrations, simulation workflows, and public sample projects that demonstrate real outcomes.

## Category Gap Analysis

### 1. AI Architecture / Design Planning

- Current repo capability: Product vision, prompt packs, startup rules, component families, and `09_ACCURACY_ENGINE` can guide planning. No structured architecture graph or requirement-to-design compiler exists.
- Required data: Design requirement schema, block-library taxonomy, interface templates, power-domain templates, risk taxonomy, reference architectures.
- Required scripts/tools: Requirements parser, architecture graph generator, block dependency checker, architecture-to-KiCad project planner.
- Required prompts/workflows: Architecture intake prompt, tradeoff prompt, part-selection prompt, "ask missing questions first" workflow.
- KiCad-native integration path: Generate Markdown plan, then approved hierarchical sheet plan, labels, power rails, and component placeholders in a copied KiCad project.
- Risk level: High.
- Difficulty level: High.
- MVP version: v0.9.
- Future advanced version: v1.4 architecture planner with reusable verified blocks and generated review traces.

### 2. Component Research

- Current repo capability: `08_COMPONENT_DATABASE`, part records, family guides, source policies, and placeholder records exist. Many records are still unverified.
- Required data: Verified sources, MPNs, lifecycle, packages, pinouts, design notes, substitutions, distributor IDs, source confidence.
- Required scripts/tools: Source-link validator, part-record linter, distributor metadata importer, component comparison generator.
- Required prompts/workflows: Component research standard, candidate comparison, missing-source escalation.
- KiCad-native integration path: Write selected parts to project BOM fields and component records, not directly to schematic until approved.
- Risk level: Medium.
- Difficulty level: Medium.
- MVP version: v0.8.
- Future advanced version: v1.2 sourced component recommendation engine with offline cache and provenance.

### 3. Datasheet Ingestion

- Current repo capability: Datasheet structure, source lists, metadata schema, link-only policy, and stub scripts exist. No robust PDF parser or source-backed extraction pipeline exists.
- Required data: Vendor source links, document revision, PDF license/redistribution status, extracted pin tables, electrical limits, layout sections.
- Required scripts/tools: PDF/text extractor, table extractor, citation mapper, summary generator, hallucination guard, revision checker.
- Required prompts/workflows: Datasheet extraction workflow, field-by-field verification, "unknown if not sourced" enforcement.
- KiCad-native integration path: Feed verified extracted fields into component records, symbol checks, footprint checks, and schematic support notes.
- Risk level: High.
- Difficulty level: High.
- MVP version: v0.9.
- Future advanced version: v1.5 traceable datasheet knowledge graph with page/section citations.

### 4. Symbol Creation

- Current repo capability: Symbol selection rules and KiCad library indexing exist. No safe symbol writer/generator exists.
- Required data: Pin tables, package pinouts, electrical pin types, hidden power policy, KiCad symbol style rules.
- Required scripts/tools: KiCad `.kicad_sym` parser/writer, symbol diff viewer, pinout linter, symbol-to-datasheet report.
- Required prompts/workflows: Datasheet-to-symbol workflow, symbol review checklist, project-local library workflow.
- KiCad-native integration path: Create project-local `.kicad_sym` libraries only after backup and approval.
- Risk level: High.
- Difficulty level: High.
- MVP version: v1.0.
- Future advanced version: v1.4 source-cited symbol generator with KiCad preview and test fixtures.

### 5. Footprint Creation

- Current repo capability: Footprint rules, high-risk warnings, and KiCad footprint indexing exist. No verified footprint generator exists.
- Required data: Exact package drawings, land pattern dimensions, IPC rules, courtyard rules, 3D model references, connector mating orientation.
- Required scripts/tools: `.kicad_mod` parser/writer, footprint drawing comparator, pad table validator, 3D model alignment checker.
- Required prompts/workflows: Datasheet-to-footprint workflow, footprint verification workflow, connector orientation workflow.
- KiCad-native integration path: Create project-local `.pretty` libraries with source evidence and human review.
- Risk level: Very high.
- Difficulty level: Very high.
- MVP version: v1.1.
- Future advanced version: v1.6 verified footprint generator with dimensional evidence reports.

### 6. Schematic Generation

- Current repo capability: Accuracy rules and prompt packs exist. Repo forbids unapproved KiCad project edits. No schematic generator exists.
- Required data: Component records, verified symbols, pinout evidence, support circuits, net naming rules, power tree.
- Required scripts/tools: KiCad schematic S-expression writer, diff/patch preview, ERC runner, source-evidence checker.
- Required prompts/workflows: Create schematic workflow, review schematic workflow, no-guessing prompts.
- KiCad-native integration path: Generate changes into copied/active-approved `.kicad_sch` files with backups, diffs, ERC, and human review.
- Risk level: Very high.
- Difficulty level: Very high.
- MVP version: v1.1.
- Future advanced version: v1.7 block-level schematic synthesis from verified templates.

### 7. PCB Layout Planning

- Current repo capability: PCB review docs, layout rules snippets, and accuracy rules exist. No placement/routing planner exists.
- Required data: Board outline constraints, keepouts, connectors, mechanical requirements, power/current constraints, interface topology.
- Required scripts/tools: Placement zone planner, constraint extractor, critical-net classifier, board-outline parser.
- Required prompts/workflows: PCB planning prompt, critical routing plan, connector/mechanical review workflow.
- KiCad-native integration path: Generate placement/routing plan as Markdown and optional KiCad drawing/constraint annotations after approval.
- Risk level: High.
- Difficulty level: High.
- MVP version: v1.0.
- Future advanced version: v1.5 interactive layout planning assistant with KiCad overlays.

### 8. Auto-Placement

- Current repo capability: None beyond rules and review guidance.
- Required data: Footprint dimensions, connection graph, mechanical constraints, keepouts, thermal zones, connector requirements.
- Required scripts/tools: Placement optimizer, KiCad PCB writer, collision checker, courtyard checker, placement scoring report.
- Required prompts/workflows: Auto-placement proposal workflow, review/apply/revert workflow.
- KiCad-native integration path: Generate proposed placements in a copied board or separate branch, then run DRC and visual review.
- Risk level: Very high.
- Difficulty level: Very high.
- MVP version: v1.4.
- Future advanced version: v2.0 constraint-aware placement engine with human-in-the-loop approvals.

### 9. Auto-Routing / Routing Assistance

- Current repo capability: No autorouter. Existing scripts can run DRC and export outputs.
- Required data: Net classes, critical nets, differential pairs, impedance targets, keepouts, via rules, layer stack.
- Required scripts/tools: Integration with Freerouting/KiCad routers or custom routing-assist scripts, critical-net router, DRC loop.
- Required prompts/workflows: Critical manual routing prompt, auto-route review prompt, DRC regression workflow.
- KiCad-native integration path: Use KiCad PCB data, project net classes, external router only on copied boards, then import/review.
- Risk level: Very high.
- Difficulty level: Very high.
- MVP version: v1.5 routing assistance, not full autoroute.
- Future advanced version: v2.0 human-guided router with protected critical traces and DRC loop.

### 10. Constraint Management

- Current repo capability: Design-rule snippets and validation scripts exist. No central KiCad constraint model exists.
- Required data: Board house capabilities, net classes, clearance/width/current rules, differential pair rules, impedance assumptions, stackup.
- Required scripts/tools: Constraint schema, KiCad board setup reader/writer, rule linter, fab capability mapper.
- Required prompts/workflows: Constraint intake, fab rule confirmation, net-class review.
- KiCad-native integration path: Map schema to KiCad board setup and design rules after approval.
- Risk level: High.
- Difficulty level: High.
- MVP version: v0.9.
- Future advanced version: v1.4 constraint compiler with board-house presets and KiCad version tests.

### 11. ERC/DRC Interpretation

- Current repo capability: ERC/DRC wrappers, project validation scripts, and interpretation rules exist.
- Required data: Known violation taxonomy, KiCad version output samples, remediation guidance, false-positive patterns.
- Required scripts/tools: ERC/DRC report parser, severity classifier, fix suggestion generator, regression comparison.
- Required prompts/workflows: Interpret-only review prompt, fix-after-approval workflow.
- KiCad-native integration path: Parse `kicad-cli` reports and generate Markdown/JSON review reports.
- Risk level: Medium.
- Difficulty level: Medium.
- MVP version: v0.8.
- Future advanced version: v1.2 guided repair planner with safe patches and before/after reports.

### 12. BOM Generation

- Current repo capability: BOM export wrappers and BOM verification rules exist. Component records are incomplete.
- Required data: MPN, manufacturer, value, package, DNP status, sourcing links, lifecycle, alternates.
- Required scripts/tools: BOM exporter/parser, component database matcher, missing-MPN checker, DNP checker.
- Required prompts/workflows: BOM review workflow, sourcing verification prompt, alternate comparison.
- KiCad-native integration path: Export KiCad BOM from project fields and reconcile against component database.
- Risk level: Medium.
- Difficulty level: Medium.
- MVP version: v0.9.
- Future advanced version: v1.3 source-aware BOM with distributor snapshots and alternates.

### 13. Sourcing / Availability

- Current repo capability: Placeholder source URLs and component records. No live distributor integration.
- Required data: Distributor APIs or exported CSVs, MPNs, stock, price breaks, lifecycle, lead time, substitutions.
- Required scripts/tools: Distributor importers for user-provided CSV/API keys, offline cache, stale-data markers.
- Required prompts/workflows: Sourcing review prompt, alternate-risk workflow, no-live-price warning.
- KiCad-native integration path: Store sourcing evidence in BOM sidecars and component records, not KiCad fields alone.
- Risk level: High.
- Difficulty level: High.
- MVP version: v1.0 with CSV import.
- Future advanced version: v1.5 opt-in distributor connectors with user-owned credentials outside repo.

### 14. Simulation / SPICE

- Current repo capability: KiCad install includes ngspice support; no integrated simulation workflow in KiCad Engine.
- Required data: SPICE models, test benches, simulation intent, expected metrics, source-backed model licenses.
- Required scripts/tools: KiCad/ngspice runner, netlist extractor, model manager, plot/report generator.
- Required prompts/workflows: Simulation setup prompt, model verification prompt, result interpretation workflow.
- KiCad-native integration path: Use KiCad/ngspice project data and write reports under `05_OUTPUTS`.
- Risk level: High.
- Difficulty level: High.
- MVP version: v1.1.
- Future advanced version: v1.6 simulation assistant with reusable test benches and metric extraction.

### 15. Collaboration / Version Control

- Current repo capability: Git-friendly repo layout, memory/history folders, prompt packs, public docs. No integrated Git workflows for KiCad diffs or PR review yet.
- Required data: Change metadata, project snapshots, review reports, diff artifacts, branch strategy.
- Required scripts/tools: KiCad semantic diff, project snapshot, review bundle generator, PR checklist.
- Required prompts/workflows: Review branch workflow, change summary prompt, multi-agent handoff.
- KiCad-native integration path: Keep KiCad source in Git, use generated reports and semantic diffs for reviews.
- Risk level: Medium.
- Difficulty level: Medium.
- MVP version: v0.9.
- Future advanced version: v1.3 KiCad-aware review bot for local Git branches.

### 16. Reusable Project Templates

- Current repo capability: Project template folders and docs exist; no rich verified design-block library.
- Required data: Board archetypes, block templates, constraints, verified components, reference schematics, fab presets.
- Required scripts/tools: Template generator, project scaffold, block copier, evidence checker.
- Required prompts/workflows: Template selection prompt, project creation workflow, block verification checklist.
- KiCad-native integration path: KiCad project templates under `04_KICAD_PROJECTS/templates` with project-local libraries.
- Risk level: Medium.
- Difficulty level: Medium.
- MVP version: v0.9.
- Future advanced version: v1.4 verified design-block marketplace-style local library.

### 17. Reference Designs

- Current repo capability: Datasheet/reference folders and component guides exist. No curated verified reference-design database.
- Required data: Vendor reference designs, app notes, licensing/redistribution status, circuit blocks, source links.
- Required scripts/tools: Reference-design indexer, block evidence extractor, license checker, comparison tool.
- Required prompts/workflows: Reference design review prompt, adapt-with-evidence workflow.
- KiCad-native integration path: Link to references and create project-local KiCad blocks only when license and evidence permit.
- Risk level: High.
- Difficulty level: Medium.
- MVP version: v1.0.
- Future advanced version: v1.5 curated local reference block library with provenance.

### 18. Manufacturing Package Creation

- Current repo capability: NOT_FINAL export wrappers, release docs, payload/checklist, and verification rules exist.
- Required data: Fab-house requirements, stackup, drill specs, BOM/PNP formats, assembly notes, panelization assumptions.
- Required scripts/tools: KiCad export orchestrator, package manifest, Gerber/drill/BOM/PNP/STEP validator, checksum generator.
- Required prompts/workflows: Release package workflow, JLCPCB/PCBWay workflows, human signoff gate.
- KiCad-native integration path: Use `kicad-cli` exports and KiCad source revision; write `NOT_FINAL` packages until approved.
- Risk level: High.
- Difficulty level: Medium.
- MVP version: v1.0.
- Future advanced version: v1.3 board-house-specific release package validators.

### 19. Human Review Gates

- Current repo capability: Strong documentation, prompt gates, `09_ACCURACY_ENGINE`, NOT_FINAL policy, and history logs.
- Required data: Gate templates, signoff records, unresolved-risk register, evidence manifests.
- Required scripts/tools: Gate-status checker, release blocker report, review checklist generator.
- Required prompts/workflows: Human review prompt, release acceptance workflow, unresolved-risk closeout.
- KiCad-native integration path: Tie review gates to KiCad project revision, ERC/DRC reports, BOM, and export package manifest.
- Risk level: Medium.
- Difficulty level: Low to medium.
- MVP version: v0.8.
- Future advanced version: v1.2 auditable review dashboard from local reports.

### 20. Local Privacy And User-Owned Data

- Current repo capability: Strong positioning, local-first docs, no credential storage, no silent installs, link-only datasheet policy.
- Required data: Privacy model, data-flow diagram, opt-in connector policy, secret scan coverage, public payload rules.
- Required scripts/tools: Secret scanner, local-only mode checker, connector permission audit, payload scrubber.
- Required prompts/workflows: Privacy review prompt, public release audit, connector approval flow.
- KiCad-native integration path: Keep KiCad source, reports, prompts, and memory local; optional external services must be explicit.
- Risk level: Medium.
- Difficulty level: Medium.
- MVP version: v0.8.
- Future advanced version: v1.2 privacy/security posture with reproducible local builds and connector sandboxing.

## Cross-Cutting Required Data

To compete seriously, KiCad Engine needs these durable data assets:

- Verified component records with citations.
- Datasheet extraction records with source links and revisions.
- Package drawing and land-pattern evidence.
- Symbol/footprint mapping database.
- KiCad stock library indexes by version.
- Board-house rule profiles.
- Reusable design-block library.
- Reference-design index with license status.
- ERC/DRC report corpus by KiCad version.
- BOM/sourcing data import snapshots.
- Simulation model library with license status.

## Cross-Cutting Required Tooling

Highest-leverage tooling:

- KiCad S-expression parser/writer with diff-safe patches.
- Symbol and footprint validators.
- Footprint-to-datasheet comparator.
- Datasheet extraction and citation pipeline.
- Component database linter.
- KiCad project semantic diff.
- Constraint schema and KiCad rule compiler.
- ERC/DRC parser and recommendation engine.
- NOT_FINAL package exporter and validator.
- Local review gate dashboard.

## Strategic Conclusion

KiCad Engine is currently strongest in safety posture, local-first repo structure, KiCad app discovery, documentation, prompt packs, component/datasheet scaffolding, and human review gates.

It is weakest in action-taking design generation, verified component data depth, symbol/footprint creation, auto-placement, routing assistance, sourcing, simulation, and demonstrated sample workflows.

The realistic claim is:

> KiCad Engine is designed to become stronger for local-first KiCad users who value transparent evidence, local files, Git review, and auditable human gates.

It should not claim Flux-level feature parity until it demonstrates source-backed schematic generation, verified KiCad symbol/footprint workflows, useful layout assistance, sourcing workflows, simulation reports, and manufacturing-package validation on real sample projects.
