# Knowledge Scrape Metadata Move Report

Status: `METADATA_MOVE_PHASE_COMPLETE`

Generated: `2026-05-11T16:42:30`

## Results

- File count before: `2546`
- File count after: `2503`
- Moved files: `43`
- Quarantined files: `0`
- Source registry destination: `10_KNOWLEDGE_BASE/source_registry`

## Validation Targets

- Moved source files no longer exist in `knowledge_scrape/`.
- Archived originals exist under `02_HISTORY/knowledge_scrape_migration/original_metadata/` or `source_logs/`.
- Normalized registry/index files exist under `10_KNOWLEDGE_BASE/`.
- Technical category folders were intentionally left in place for later phases.

## Key Canonical Files

- `10_KNOWLEDGE_BASE/source_registry/SOURCE_REGISTRY.csv`
- `10_KNOWLEDGE_BASE/source_registry/SOURCE_REGISTRY.json`
- `10_KNOWLEDGE_BASE/retrieval_indexes/MASTER_KNOWLEDGE_INDEX.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/KNOWLEDGE_SOURCE_INDEX.md`
