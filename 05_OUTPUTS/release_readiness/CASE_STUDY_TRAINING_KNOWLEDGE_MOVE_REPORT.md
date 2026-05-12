# Case Study / Training Knowledge Move Report

Status: `APPLY_MODE_COMPLETED`

## Scope

Drained these legacy source folders:

- `knowledge_scrape/12_forums_peer_review`
- `knowledge_scrape/15_video_reference_index`
- `knowledge_scrape/16_ai_pcb_failure_modes`
- `knowledge_scrape/17_case_studies_bad_boards`
- `knowledge_scrape/18_case_studies_good_boards`
- `knowledge_scrape/19_university_training`

## Move Summary

- Total files moved: `214`
- Moved to license quarantine: `206`
- Moved to history/metadata archives: `8`
- Remaining `knowledge_scrape` file count after this phase: `831`

## Per-Folder Counts

| Source Folder | Files |
| --- | ---: |
| `12_forums_peer_review` | 17 |
| `15_video_reference_index` | 12 |
| `16_ai_pcb_failure_modes` | 9 |
| `17_case_studies_bad_boards` | 4 |
| `18_case_studies_good_boards` | 32 |
| `19_university_training` | 140 |

## Canonical Outputs Added Or Updated

### Training / peer review / case-study surfaces

- `10_KNOWLEDGE_BASE/training/README.md`
- `10_KNOWLEDGE_BASE/training/UNIVERSITY_TRAINING_INDEX.md`
- `10_KNOWLEDGE_BASE/training/PCB_LAYOUT_TRAINING_SUMMARY.md`
- `10_KNOWLEDGE_BASE/peer_review/README.md`
- `10_KNOWLEDGE_BASE/peer_review/FORUM_SOURCE_POLICY.md`
- `10_KNOWLEDGE_BASE/peer_review/PEER_REVIEW_OBSERVATIONS_INDEX.md`
- `10_KNOWLEDGE_BASE/case_studies/README.md`
- `10_KNOWLEDGE_BASE/case_studies/BAD_BOARD_FAILURE_PATTERNS.md`
- `10_KNOWLEDGE_BASE/case_studies/GOOD_BOARD_PATTERNS.md`
- `10_KNOWLEDGE_BASE/case_studies/CASE_STUDY_SOURCE_INDEX.md`

### Agent-quality and false-pass prevention surfaces

- `26_AGENT_QUALITY/AI_PCB_FAILURE_MODES.md`
- `26_AGENT_QUALITY/CODEX_KICAD_FAILURE_PATTERNS.md`
- `26_AGENT_QUALITY/FALSE_PASS_PATTERNS.md`
- `26_AGENT_QUALITY/AI_AGENT_PCB_REVIEW_CHECKLIST.md`
- `02_HISTORY/known_agent_mistakes/AI_PCB_ROUTING_FAILURE_PATTERNS.md`
- `02_HISTORY/known_agent_mistakes/SCHEMATIC_READABILITY_FAILURE_PATTERNS.md`
- `02_HISTORY/known_agent_mistakes/CONNECTOR_ORIENTATION_FAILURE_PATTERNS.md`
- `09_ACCURACY_ENGINE/verification_rules/LOW_CONFIDENCE_SOURCE_USAGE_RULES.md`
- updates to `FALSE_PASS_PREVENTION_RULES.md` and
  `EVIDENCE_HIERARCHY_RULES.md`

## Source Confidence Handling

| Confidence | Count | Handling |
| --- | ---: | --- |
| `LOW` | 25 | quarantine only |
| `LOW_TO_MEDIUM` | 11 | quarantine only |
| `MEDIUM_MIXED` | 170 | quarantine only |
| `METADATA_ONLY` | 8 | migration history |

## Raw Content Handling

- Raw forum, video, case-study, and mixed training captures were not promoted
  into canonical rule or reference folders.
- Raw copied captures from the six drained folders were moved to:
  `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/`
- Low-risk category metadata such as `.gitkeep` and `_CATEGORY_INDEX.md` was
  moved to:
  `02_HISTORY/knowledge_scrape_migration/case_study_training_metadata/`

## Durable Rule Added

Forums, videos, university training pages, and case studies are now explicitly
`GUIDANCE_ONLY`. They may feed:

- failure-pattern prevention,
- style scorecards,
- and human-review prompts,

but they may not by themselves approve:

- footprints,
- connector orientation,
- routing quality,
- EMC,
- or fabrication readiness.

## Validation

- All `214` target ledger rows are marked `MOVED_VALIDATED`.
- All six target source folders were removed.
- No raw restricted content was promoted into the new canonical docs.
- No KiCad design files were changed by this task.

## Canonical Follow-On Rule

Future migration prompts must continue from:

- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`

