# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| All six target folders were drained | `05_OUTPUTS/release_readiness/CASE_STUDY_TRAINING_KNOWLEDGE_MOVE_REPORT.md`, `KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md` |
| `214` files were moved in this phase | `KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv`, phase-tagged rows |
| Forums, videos, and case studies are now guidance-only in canonical docs | `10_KNOWLEDGE_BASE/peer_review/FORUM_SOURCE_POLICY.md`, `10_KNOWLEDGE_BASE/case_studies/README.md`, `09_ACCURACY_ENGINE/verification_rules/LOW_CONFIDENCE_SOURCE_USAGE_RULES.md` |
| Raw captures were not promoted to source-of-truth folders | quarantine destinations in `KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv`, report summary |
| No KiCad design files were changed by this task | SHA-256 values for `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`; `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` |

