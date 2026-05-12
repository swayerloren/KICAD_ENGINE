# Engineering Rules Knowledge Move Claim / Evidence Matrix

Date: `2026-05-11`

| Claim | Evidence |
| --- | --- |
| `149` targeted source files were moved out of `knowledge_scrape/` | `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv` plus the target-row count script output |
| The ten targeted source folders were removed | `Test-Path` validation loop over the ten folder paths |
| Canonical enforceable rules/checklists now exist under `09_ACCURACY_ENGINE/` | created files under `09_ACCURACY_ENGINE/pcb_rules/`, `schematic_rules/`, and `checklists/` |
| Raw scraped captures were not left in source-of-truth rule folders | move destinations under `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/` and `02_HISTORY/knowledge_scrape_migration/` |
| No KiCad design files changed in this task | SHA-256 proof for SCH/PCB/PRO plus `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` |
