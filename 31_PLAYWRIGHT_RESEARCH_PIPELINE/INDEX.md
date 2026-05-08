# Playwright Research Pipeline Index

Status: `ACTIVE_SCAFFOLD_DRY_RUN_FIRST`

## Core Files

| File | Purpose |
| --- | --- |
| `README.md` | Human and AI orientation. |
| `SOURCE_POLICY.md` | Source order, permitted inputs, and prohibited behavior. |
| `TERMS_AND_RATE_LIMIT_RULES.md` | Rate-limit, terms, blocking, CAPTCHA, and login rules. |
| `PLAYWRIGHT_USAGE_RULES.md` | Browser execution rules and dry-run/live-mode behavior. |
| `DATA_CAPTURE_SCHEMA.md` | Shared capture record fields. |
| `DATASHEET_LINK_CAPTURE_SCHEMA.md` | Datasheet/source-link record fields. |
| `PART_NUMBER_CAPTURE_SCHEMA.md` | Part-number metadata capture fields. |
| `FOOTPRINT_CAPTURE_SCHEMA.md` | KiCad footprint/source evidence fields. |
| `SCREENSHOT_EVIDENCE_RULES.md` | Rules for public-page screenshot evidence. |

## Subfolders

| Folder | Purpose |
| --- | --- |
| `research_targets/` | CSV target lists for controlled research batches. |
| `source_profiles/` | Per-source access, terms, and capture guidance. |
| `scripts/` | Dry-run and guarded live-mode scripts. |
| `output/` | Timestamped normalized JSON outputs. |
| `evidence/` | Timestamped source-evidence records and screenshots. |
| `reports/` | Markdown reports. |
| `templates/` | JSON and Markdown templates. |

## Required First Reads

Before using this pipeline, agents must read:

1. `SOURCE_POLICY.md`
2. `TERMS_AND_RATE_LIMIT_RULES.md`
3. `PLAYWRIGHT_USAGE_RULES.md`
4. The relevant source profile under `source_profiles/`
5. The target CSV under `research_targets/`

## Downstream Rule

Playwright research output is evidence, not truth. Captured browser-page data must remain `UNVERIFIED` until checked against official datasheet/vendor evidence or human review.

