# Folder Routing Rules

## Purpose

This file tells AI agents where new KiCad Engine files belong. Use it before creating, moving, or reorganizing repo artifacts.

## Routing Map

| Folder | Route Here |
| --- | --- |
| `.codex/` | Workspace-local Codex configuration and prompts. No secrets. |
| `.claude/` | Workspace-local Claude guidance and configuration. No secrets. |
| `.github/` | GitHub Actions workflows, issue templates, release workflow docs. |
| `.prompts/` | Codex, Claude, and shared prompt packs. |
| `.vscode/` | VS Code settings, recommended extensions, tasks, and launch configs. |
| `00_CODEX_START/` | Mandatory startup rules, workflow standards, repo indexes, active project pointers, quality gates. |
| `01_MEMORY/` | Durable global lessons, preferences, workflows, mistakes to avoid, and reusable memory. |
| `02_HISTORY/` | Session logs, command logs, audits, design reviews, verification reports, failed attempts, issue logs, and quality records. |
| `03_TOOLS/` | Scripts, local tool wrappers, read-only analyzers, generated tool indexes, and external tool notes. |
| `04_KICAD_PROJECTS/` | Active KiCad project workspaces and project templates. KiCad file edit gates apply. |
| `05_OUTPUTS/` | Generated outputs, reports, review artifacts, and NOT_FINAL packages. |
| `06_DATASHEETS/` | Datasheet metadata, source links, summaries, missing-document records, and redistribution policies. |
| `07_REFERENCE_DESIGNS/` | Public-source reference design metadata, links, summaries, and review notes that are separate from the formal reference design library. |
| `08_COMPONENT_DATABASE/` | Structured component records, schemas, verification flags, KiCad candidate links, and part-selection notes. |
| `09_ACCURACY_ENGINE/` | Schematic, PCB, verification, and workflow rules that reduce hallucination and unsafe edits. |
| `10_KNOWLEDGE_BASE/` | Reusable circuit patterns, design patterns, checklists, common mistakes, and manufacturing guidance. |
| `11_LIBRARY_FACTORY/` | KiCad symbol, footprint, package-mapping, library-table, and project-local library standards and validators. |
| `12_REFERENCE_DESIGN_LIBRARY/` | Curated reference design records with source, license, verification level, and review constraints. |
| `13_PART_INGESTION/` | New-part datasheet ingestion workflows, extraction rules, templates, and stub-generation scripts. |
| `14_LAYOUT_AUTOMATION/` | Placement/routing assistance plans, constraint extraction plans, autorouter notes, and human layout gates. |
| `15_BENCHMARKS/` | Benchmark methodology, task definitions, scoring rubrics, runner plans, and real benchmark results. |
| `16_INSTALLER/` | Installer coordination docs, release-facing installer plans, packaging notes, and links to installer source. |
| `17_RELEASE_BUILD/` | Release build staging notes, artifact manifests, checksums, and release readiness records. |
| `18_PUBLIC_DOCS/` | Public-facing documentation intended for GitHub, website, or installer users. |
| `19_TEST_PROJECTS/` | Disposable test projects and sample workspaces, clearly marked as tests. |
| `20_CI_CD/` | CI/CD planning, workflow standards, local CI checks, and release automation docs. |
| `21_LICENSE_ATTRIBUTION/` | License, attribution, redistribution, third-party tool, datasheet, and vendor-document audits. |
| `22_SECURITY/` | Security model, secret-handling rules, installer safety notes, and vulnerability response docs. |
| `23_PACKAGE_PROFILES/` | Package creation profiles for review bundles, installer payloads, docs bundles, and release archives. |
| `24_FAB_PROFILES/` | Fabrication-house export profiles, NOT_FINAL manufacturing package rules, and DFM notes. |
| `25_VENDOR_DATABASE/` | Vendor portals, manufacturer metadata, distributor-source notes, lifecycle metadata, and sourcing placeholders. |
| `26_AGENT_QUALITY/` | AI response quality, scoring, evidence, hallucination-risk, and quality-gate support artifacts. |
| `27_EXAMPLES/` | Safe examples, tutorials, starter records, and toy data that must not be confused with production approvals. |
| `28_SUPPLIER_INGESTION/` | Supplier API/CSV ingestion policies, connector scaffolds, normalized supplier metadata, stock/pricing snapshots, and sourcing gap reports. |
| `29_FOOTPRINT_GAP_ANALYSIS/` | Installed KiCad footprint/symbol inventory, candidate matching, high-risk footprint gaps, and missing-footprint backlog reports. |
| `30_SUPPLIER_FOOTPRINT_MATCHES/` | Supplier SKU/MPN to KiCad symbol/footprint/3D candidate match records, confidence rules, and unmatched supplier reports. |
| `31_PLAYWRIGHT_RESEARCH_PIPELINE/` | Playwright-assisted public-page research policies, source profiles, target lists, screenshot evidence, normalized evidence outputs, and dry-run-first browser research scripts. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/` | Controlled open KiCad sample project candidate records, license screening, imported-original evidence copies, normalized samples, review reports, attribution, and benchmark promotion notes. |
| `33_PCB_PRELAYOUT_ENGINE/` | Reusable PCB digital-twin extraction, connector mechanical truth, projected-route planning, variant scoring, and pre-placement/pre-routing gate rules. |
| `34_PCB_LAYOUT_SANDBOX/` | Pre-PCB-edit layout sandbox rules, variant-planning workflow, board-shape/mechanical reasoning, projected routing guidance, and sandbox templates. |
| `99_BACKUPS/` | Pre-edit snapshots and recovery copies. Do not delete. |

## Existing Unnumbered Roots

The repo also contains established unnumbered roots such as `installer/`, `setup/`, `docs/`, and root quickstart files. These remain valid until an explicit migration task changes them.

- `installer/` is the current Electron installer source and payload builder location.
- `setup/` is the current cross-platform setup script location.
- `docs/` is the current public/end-user documentation location.
- `16_INSTALLER/`, `18_PUBLIC_DOCS/`, and `20_CI_CD/` are coordination and indexing layers unless a future migration task moves implementation files.

Do not duplicate large implementation trees into numbered folders without a specific migration plan.

## Routing Questions

Before creating a file, ask:

1. Is this a rule, memory item, history record, script, generated output, or KiCad project file?
2. Is it global or project-specific?
3. Is it source-like or generated?
4. Does it contain a claim that needs evidence?
5. Does it contain private, copyrighted, or redistributable content?
6. Does it belong in an existing legacy implementation root instead of a new numbered index layer?

## Safe Defaults

- Use `02_HISTORY/` for evidence of what happened.
- Use `01_MEMORY/` only for durable reusable lessons.
- Use project `memory/` and `history/` for project-specific facts.
- Use `05_OUTPUTS/` for generated outputs.
- Use `27_EXAMPLES/` for safe examples that are intentionally not production approvals.
- Use `28_SUPPLIER_INGESTION/` for supplier import/normalization scaffolds instead of putting raw supplier data in `08_COMPONENT_DATABASE` or `25_VENDOR_DATABASE`.
- Use `29_FOOTPRINT_GAP_ANALYSIS/` for local installed-KiCad library inventory and footprint gap evidence instead of treating `08_COMPONENT_DATABASE` candidate fields as verified footprints.
- Use `30_SUPPLIER_FOOTPRINT_MATCHES/` when a supplier SKU, JLC/LCSC part number, or supplier package field needs to be tied to a KiCad footprint candidate with explicit confidence and human-review status.
- Use `31_PLAYWRIGHT_RESEARCH_PIPELINE/` for controlled public-page browser evidence, screenshot capture, source profiles, and dry-run research plans; do not route captured browser output directly into verified component or footprint records.
- Use `32_OPEN_KICAD_SAMPLE_INTAKE/` for open KiCad sample project discovery, source/license screening, imported-original preservation, normalized review copies, sample audits, attribution, and benchmark-candidate promotion. Do not put random downloads, edited originals, active user projects, or unlicensed public-payload samples there.
- Use `33_PCB_PRELAYOUT_ENGINE/` for reusable digital-twin, connector-truth, projected-route, and pre-placement/pre-routing gate rules. Put project-specific prelayout outputs in the active project's `reports/prelayout_engine/` folder.
- Use `34_PCB_LAYOUT_SANDBOX/` for reusable sandbox rules, variant-planning workflow, projected routing guidance, and pre-PCB-edit templates. Put project-specific sandbox outputs in the active project's `reports/` folder.
- Use `99_BACKUPS/` for backups before edits.
- Use `03_TOOLS/scripts/indexing/` for safe repo, memory, history, and known-problem index builders.
- Use `01_MEMORY/MASTER_MEMORY_INDEX.md` and `02_HISTORY/MASTER_HISTORY_INDEX.md` as generated master summaries, not as hand-maintained evidence records.

## Prohibited Routing

- Do not put secrets anywhere.
- Do not put KiCad design files in memory, history, prompt, or docs folders.
- Do not put generated reports in standards folders unless the folder explicitly expects generated indexes.
- Do not put vendor PDFs in public-release paths unless redistribution rights are confirmed.
- Do not put personal local logs in installer payloads.
- Do not put production claims in examples.
- Do not put indexing scripts in KiCad project folders.
