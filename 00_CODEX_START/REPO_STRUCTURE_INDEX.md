# Repository Structure Index

## Purpose

This index summarizes the current production-oriented KiCad Engine repository structure for users and AI agents. It is a routing aid, not a completeness claim.

## Top-Level Structure

| Folder | Status | Purpose |
| --- | --- | --- |
| `.codex/` | Existing | Workspace-local Codex support. |
| `.claude/` | Existing | Claude-oriented local guidance/configuration if present. |
| `.github/` | Existing | GitHub Actions and release workflow support. |
| `.prompts/` | Existing | Prompt packs for Codex, Claude, and shared standards. |
| `.vscode/` | Existing | VS Code workspace settings, tasks, extensions, and launch config. |
| `00_CODEX_START/` | Existing | Startup, workflow, safety, structure, memory/history, and AI quality control plane. |
| `01_MEMORY/` | Existing | Durable global and reusable memory. |
| `02_HISTORY/` | Existing | Session logs, command logs, audits, reviews, verification evidence, and quality records. |
| `03_TOOLS/` | Existing | Scripts, analyzers, tool indexes, and tool integration notes. |
| `04_KICAD_PROJECTS/` | Existing | Active KiCad projects and templates. KiCad edit gates apply. |
| `05_OUTPUTS/` | Existing | Generated reports and NOT_FINAL review outputs. |
| `06_DATASHEETS/` | Existing | Datasheet/reference metadata, source links, summaries, and policy records. |
| `07_REFERENCE_DESIGNS/` | Added | General reference design metadata and link-first notes. |
| `08_COMPONENT_DATABASE/` | Existing | Structured component records and verification metadata. |
| `09_ACCURACY_ENGINE/` | Existing | Accuracy, anti-hallucination, schematic, PCB, and verification rules. |
| `10_KNOWLEDGE_BASE/` | Existing | Reusable circuit patterns, checklists, common mistakes, and manufacturing rules. |
| `11_LIBRARY_FACTORY/` | Existing | Symbol, footprint, package mapping, and library QA standards. |
| `12_REFERENCE_DESIGN_LIBRARY/` | Existing | Curated reference design records and source/license rules. |
| `13_PART_INGESTION/` | Existing | Datasheet-to-record ingestion workflow and stub generators. |
| `14_LAYOUT_AUTOMATION/` | Existing | Placement/routing assistance plans and layout reality checks. |
| `15_BENCHMARKS/` | Existing | Benchmark methodology, tasks, scoring rubrics, and future real results. |
| `16_INSTALLER/` | Added | Installer coordination layer and release-facing installer notes. |
| `17_RELEASE_BUILD/` | Added | Release artifact staging, manifests, checksums, and readiness records. |
| `18_PUBLIC_DOCS/` | Added | Public-facing documentation coordination and publishing layer. |
| `19_TEST_PROJECTS/` | Added | Disposable sample and test projects. |
| `20_CI_CD/` | Added | CI/CD planning and workflow coordination layer. |
| `21_LICENSE_ATTRIBUTION/` | Added | License, attribution, and redistribution audit layer. |
| `22_SECURITY/` | Added | Security model, secret handling, and vulnerability response layer. |
| `23_PACKAGE_PROFILES/` | Added | Release/review/package profile definitions. |
| `24_FAB_PROFILES/` | Added | Fabrication-house profile and NOT_FINAL export guidance. |
| `25_VENDOR_DATABASE/` | Added | Vendor, manufacturer, distributor, lifecycle, and source metadata. |
| `26_AGENT_QUALITY/` | Added | AI quality, evidence, scorecard, and hallucination-risk support layer. |
| `27_EXAMPLES/` | Added | Safe examples and tutorials that are not production approvals. |
| `28_SUPPLIER_INGESTION/` | Added | Supplier API/CSV ingestion, connector scaffolds, normalized supplier metadata, and gap reports. |
| `29_FOOTPRINT_GAP_ANALYSIS/` | Added | Installed KiCad footprint/symbol inventory, candidate matching, high-risk footprint gaps, and missing-footprint backlog reports. |
| `30_SUPPLIER_FOOTPRINT_MATCHES/` | Added | Supplier SKU/MPN to KiCad footprint match records, confidence rules, and unmatched supplier-footprint reports. |
| `31_PLAYWRIGHT_RESEARCH_PIPELINE/` | Added | Dry-run-first public-page evidence capture policies, source profiles, target lists, screenshots, normalized records, and reports. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/` | Added | Controlled open KiCad sample project intake, license screening, imported-original preservation, normalized sample copies, review reports, attribution, and benchmark-candidate promotion. |
| `34_PCB_LAYOUT_SANDBOX/` | Added | Mandatory pre-PCB-edit layout sandbox layer for variant planning, board-shape reasoning, connector/mechanical review, projected routing, and human gate templates. |
| `99_BACKUPS/` | Existing | Pre-edit backups and recovery snapshots. |

## Established Implementation Roots

These unnumbered roots remain part of the repo:

- `installer/`: current Electron installer source, payload builder, manifests, and installer docs.
- `setup/`: current setup and requirement-check scripts for Windows, macOS, Linux, and common helpers.
- `docs/`: current end-user documentation.
- Root quickstart files: public user and AI-agent entry points.

Do not migrate these folders into numbered roots unless a future migration task explicitly approves the move and creates a rollback plan.

## Public Release Notes

This structure is intended to make the repo easier to audit before GitHub release. Folder existence does not prove readiness. Release readiness still requires:

- Health checks.
- Secret scans.
- License and redistribution audits.
- Installer smoke tests.
- Public docs review.
- Evidence-backed component and footprint records.
- Explicit `NOT_FINAL` handling for manufacturing-style outputs.

## Update Rules

Update this index when:

- A top-level folder is added, removed, renamed, or repurposed.
- A legacy implementation root is migrated.
- A public release structure rule changes.
- Agent routing behavior changes.
