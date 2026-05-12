# Source License Status

Status: `REGISTRY_NORMALIZED_FROM_MIGRATION_METADATA`

Generated: `2026-05-11T16:42:30`

## Scope

- This folder now contains the canonical normalized source registry derived from archived migration metadata.
- The original metadata files were moved to repo history.
- This registry is metadata only. It does not make all scraped content license-safe for public source-of-truth use.
- Raw copied articles, extracted Markdown, standards text, forum captures, and similar risky materials must still follow the migration ledger and quarantine rules before canonical promotion.

## Registry Snapshot

- Registry rows: `10236`
- Needs review rows: `8875`
- Needs future rescrape rows: `0`

## Trust Label Counts

- `8_low_value_index_or_search`: `3445`
- `1_official_manufacturer_datasheet`: `1752`
- `5_engineering_forum_peer_review`: `1712`
- `3_official_kicad_docs`: `1551`
- `6_blog_tutorial`: `1036`
- `2_official_manufacturer_app_note`: `311`
- `6_blog_or_general_web`: `158`
- `3_fabricator_dfm`: `64`
- `2_official_kicad`: `49`
- `1_official_manufacturer_datasheet_or_app_note`: `38`
- `4_fabricator_docs`: `33`
- `5_peer_review`: `32`
- `4_university_training`: `25`
- `7_low_authority_context`: `14`
- `7_video_index`: `9`
- `3_high_reliability_or_standards`: `7`

## Scrape Status Counts

- `failed`: `7107`
- `not_found_in_outputs`: `1344`
- `success`: `1141`
- `needs_rescrape`: `424`
- `rejected`: `220`

## Policy

- Registry metadata is low-risk to store canonically.
- Source content quality and redistribution rights are still per-source decisions, not implied by registry presence.
- If a later migration step finds unclear license or unsafe copied content, move that content to license quarantine and update the ledger.

## 2026-05-11 Component / Datasheet / Vendor Migration Note

- Migration phase drained the component, datasheet, vendor, CAD-model, and land-pattern intake sources.
- `596` source files were moved in this phase.
- `375` raw capture files were moved to license quarantine.
- `221` low-risk metadata and extraction-log files were moved to migration history.
- Canonical promotion for this phase was link-first: datasheet indexes, component evidence rules, vendor indexes, CAD-model distrust rules, and footprint-gap summaries.

## 2026-05-11 Fab / DFM / Compliance Migration Note

- Migration phase drained the fabrication, harsh-environment, high-reliability, standards, and compliance intake sources.
- `64` source files were moved in this phase.
- `58` raw capture files were moved to license quarantine.
- `6` low-risk metadata files were moved to migration history.
- Canonical promotion for this phase was link-first: DFM summaries, EMC/safety summaries, export rules, and review checklists.

## 2026-05-11 Unsorted / Rejected Drain Note

- Migration phase drained the unsorted and rejected migration residue sources.
- `784` source files were moved in this phase.
- `780` raw copied low-value captures were moved to license quarantine.
- `4` metadata/index files were moved to migration history.
- Durable policy from this phase: raw copied low-value content is not safer just because it is "rejected"; when redistribution rights are unclear, quarantine it instead of preserving a public rejected-payload tree.
