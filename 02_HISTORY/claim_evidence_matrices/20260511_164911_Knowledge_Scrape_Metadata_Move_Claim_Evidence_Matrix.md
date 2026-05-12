# Knowledge Scrape Metadata Move Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-11T16:49:11`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| Knowledge-scrape metadata, registry files, raw inventory, and source logs were moved out of the source folder into canonical repo locations, and the canonical source registry was regenerated successfully. | 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_METADATA_MOVE_REPORT.md; 02_HISTORY/knowledge_scrape_migration/original_metadata/; 02_HISTORY/knowledge_scrape_migration/source_logs/; 10_KNOWLEDGE_BASE/source_registry/; 10_KNOWLEDGE_BASE/retrieval_indexes/ | `PARTIALLY_VERIFIED` | `HIGH` | `MEDIUM_RISK` | `YES` | This evidence covers only the metadata move phase, not the full technical-content drain. |

## Details

This claim is supported by the updated migration ledger, the metadata-move report, the archived original metadata tree, the canonical SOURCE_REGISTRY outputs, and validation that zero targeted source paths still exist under knowledge_scrape.
