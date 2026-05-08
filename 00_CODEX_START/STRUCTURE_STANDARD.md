# KiCad Engine Structure Standard

## Purpose

This file defines the durable top-level structure standard for KiCad Engine. It exists so Codex, Claude, and other VS Code-based agents route new files predictably instead of scattering project memory, tools, docs, outputs, and engineering evidence across unrelated folders.

KiCad Engine is a local-first KiCad AI engineering workspace. It uses the user's installed KiCad application and keeps repo knowledge, project files, generated reports, source-link metadata, validation scripts, prompt packs, release support, and public documentation separated.

## Core Rules

- Do not edit KiCad design files unless the active project, backup plan, verification plan, and rollback plan are confirmed.
- Do not delete or overwrite existing user work.
- Do not store secrets, API keys, tokens, paid-service credentials, or private license keys anywhere in the repo.
- Do not download datasheets or vendor documents unless a task explicitly approves it and redistribution rules are checked.
- Do not mark fabrication-style outputs final unless ERC, DRC, BOM, footprint, pinout, datasheet, connector, polarity, mechanical, and visual review gates are complete.
- Prefer link-only records for vendor documents unless redistribution permission is known.
- Keep generated or experimental output out of source/control folders.
- Preserve existing legacy folders until an explicit migration task approves a move.

## Top-Level Folder Standard

Every production top-level folder should have:

- `README.md` for human-facing orientation.
- `INDEX.md` for AI-readable routing and inventory.
- Clear separation between source files, generated outputs, evidence records, and examples.
- Public-release notes that identify redistribution, privacy, and completeness risks.

Each `README.md` and `INDEX.md` should include these sections:

- `PURPOSE`
- `WHAT_BELONGS_HERE`
- `WHAT_DOES_NOT_BELONG_HERE`
- `AI_AGENT_RULES`
- `SAFE_EDIT_RULES`
- `PUBLIC_RELEASE_NOTES`

## Source Versus Generated Data

Source-like repo assets include:

- Startup rules and prompt packs.
- Markdown standards.
- Read-only scripts.
- Datasheet and component metadata.
- Knowledge-base records.
- Library factory standards.
- Benchmarks and task definitions.
- Installer source and payload rules.

Generated data includes:

- Health-check reports.
- Setup reports.
- KiCad app inventory outputs.
- Validation reports.
- ERC/DRC reports.
- NOT_FINAL review exports.
- Payload manifests and build reports.
- Benchmark run results after actual runs.

Generated data should normally be written under `02_HISTORY/`, `05_OUTPUTS/`, project `history/`, or a clearly named generated subfolder. Do not mix generated reports into source standards unless the folder explicitly calls for generated indexes.

## KiCad Design File Boundary

KiCad project source files belong only in approved project locations such as:

- `04_KICAD_PROJECTS/active/`
- `04_KICAD_PROJECTS/templates/`
- `19_TEST_PROJECTS/` for disposable examples and tests
- Existing finished-reference folders when used read-only

Agents must not touch these file types without the KiCad edit gate:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_sym`
- `.kicad_mod`
- `.pretty/`
- Gerbers
- drill files
- pick-and-place files
- final or manufacturing-style packages

## Public Release Hygiene

Before public release, each top-level folder must be reviewed for:

- Secrets.
- Personal machine paths.
- Copyrighted PDFs or vendor documents with unclear redistribution rights.
- Large generated outputs.
- Fabrication files mislabeled as final.
- Unverified component claims.
- Unverified connector or footprint approvals.
- Installer scripts that install without asking.
- Docs that overpromise AI design, routing, or fabrication readiness.

## AI Agent Expectations

Before creating a new file, agents must:

1. Read `FOLDER_ROUTING_RULES.md`.
2. Choose the narrowest folder that matches the artifact.
3. Prefer existing schemas and templates.
4. Mark unverified engineering claims explicitly.
5. Log meaningful structure changes in `02_HISTORY/`.
6. Rebuild repository, memory, history, AI-quality, and known-problem indexes when startup or routing files change.
7. Update `REPO_STRUCTURE_INDEX.md`, `README_GPT.md`, and `FOR CHAT GPT.MD` when routing or top-level structure changes.

## Index Requirements

Startup and closeout depend on generated indexes. Use these scripts after structure, memory, history, or known-problem changes:

- `python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .`
- `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .`
- `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .`
- `python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .`
- `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`

These scripts are allowed to write only generated index outputs and master index summaries. They must not edit KiCad design files.
