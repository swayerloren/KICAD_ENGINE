# KiCad Docs Knowledge Move Report

Status: `KICAD_DOCS_MOVE_PHASE_COMPLETE`

Generated: `2026-05-11T17:02:23`

## Results

- Source files moved from target folders: `649`
- Normalized docs created: `17`
- Files quarantined: `641`
- Files archived to history: `8`
- Source folders remaining from this phase: `0`
- knowledge_scrape remaining file count: `1854`

## Canonical Outputs

- `10_KNOWLEDGE_BASE/kicad_core/`
- `10_KNOWLEDGE_BASE/kicad_python_api/`
- `10_KNOWLEDGE_BASE/kicad_file_formats/`
- `10_KNOWLEDGE_BASE/kicad_libraries/`
- `03_TOOLS/scripts/kicad_api/safe_pcbnew_helpers.py`

## Archive / Quarantine Outputs

- `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/`
- `02_HISTORY/knowledge_scrape_migration/kicad_docs_import_metadata/`

## Validation Targets

- every file from the four source folders is moved, quarantined, or archived
- the four source folders no longer exist under `knowledge_scrape/`
- destination docs include source-registry references
- no KiCad design files were changed by this task