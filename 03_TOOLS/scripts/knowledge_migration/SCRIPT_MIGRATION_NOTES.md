# Legacy Script Migration Notes

Status: `FINAL_SCRIPTS_PHASE_RECONCILED`

Generated: `2026-05-12`

## Purpose

This note explains how the final legacy `knowledge_scrape\_scripts\` rows were
resolved.

During the final drain phase, the remaining PowerShell script bodies were
located under `knowledge_scrape\_scripts\` and moved out of the live source
tree. They were not kept as active tooling because they depend on the retired
external `C:\KICAD_SCRAPE` pipeline and are already superseded by the canonical
Python migration/indexing stack. Instead:

- each script was classified `MOVE_TO_HISTORY_ONLY`
- each script file was moved to
  `02_HISTORY\knowledge_scrape_migration\obsolete_scripts\`
- companion note files were kept in the same folder for provenance
- the canonical active tooling remained the Python-based migration/indexing
  stack already under `03_TOOLS\scripts\knowledge_migration\` and
  `03_TOOLS\scripts\indexing\`

## Per-Script Resolution

| Legacy script | Inferred purpose | Final classification | Canonical active replacement |
| --- | --- | --- | --- |
| `01_build_raw_inventory.ps1` | build raw source inventory | `MOVE_TO_HISTORY_ONLY` | `inventory_knowledge_scrape.py` |
| `02_build_url_registry.ps1` | rebuild URL/source registry | `MOVE_TO_HISTORY_ONLY` | canonical source-registry files plus `classify_knowledge_scrape_items.py` |
| `03_classify_copy_markdown.ps1` | import/classify copied Markdown | `MOVE_TO_HISTORY_ONLY` | no direct active replacement; legacy scrape intake is retired |
| `04_convert_pdfs_to_markdown.ps1` | PDF-to-Markdown conversion | `MOVE_TO_HISTORY_ONLY` | no direct active replacement; PDF redistribution stays policy-driven and historical |
| `05_clean_markdown_for_ai.ps1` | clean imported Markdown for local use | `MOVE_TO_HISTORY_ONLY` | no direct active replacement; canonical summaries now live in destination folders |
| `06_build_category_indexes.ps1` | rebuild category indexes | `MOVE_TO_HISTORY_ONLY` | `rebuild_knowledge_indexes.py`, `build_repo_index.py`, `build_history_index.py`, `build_memory_index.py` |
| `10_import_ingest_v2.ps1` | batch import legacy `ingest_v2` scrape payloads | `MOVE_TO_HISTORY_ONLY` | no active executable preserved; provenance remains in `02_HISTORY\knowledge_scrape_migration\source_logs\ingest_v2_import\` |

## Rule

Do not recreate or depend on `knowledge_scrape\_scripts\` for normal agent
operation. Treat the obsolete records as provenance only.
