# Playwright Research Scripts

Status: `DRY_RUN_FIRST`

## Rules

- All scripts default to `DRY_RUN`.
- Live browser execution requires `--live`.
- PDF downloads are disabled by default.
- `--download-pdf` requires `--confirm-redistribution-risk` and still should prefer link-only evidence.
- Scripts must not store credentials, cookies, browser profiles, private pages, or raw supplier HTML.
- Scripts must stop if a page requires login, shows CAPTCHA, blocks access, or has unclear terms.
- Captured data remains `UNVERIFIED` until official-source or human review.

## Common Commands

```powershell
node 31_PLAYWRIGHT_RESEARCH_PIPELINE\scripts\dry_run_research_plan.js
node 31_PLAYWRIGHT_RESEARCH_PIPELINE\scripts\build_research_report.js --input 31_PLAYWRIGHT_RESEARCH_PIPELINE\output
node --check 31_PLAYWRIGHT_RESEARCH_PIPELINE\scripts\browser_research_public_page.js
```

Live browser mode is intentionally not used by default.

## Script Responsibilities

| Script | Responsibility | Writes |
| --- | --- | --- |
| `dry_run_research_plan.js` | Convert target CSVs into safe research plans. | Timestamped dry-run output and report files. |
| `browser_research_public_page.js` | Capture one explicitly provided public page only when `--live` is set. | Screenshot evidence and `UNVERIFIED` JSON. |
| `capture_source_evidence.js` | Organize source URL, timestamp, and screenshot evidence. | Evidence summaries. |
| `extract_part_metadata.js` | Extract conservative metadata from allowed source records. | Normalized JSON with `UNVERIFIED` status. |
| `extract_datasheet_links.js` | Identify candidate source links. | Link-only records. |
| `normalize_research_output.js` | Normalize generated records to the template schema. | JSON/Markdown output. |
| `build_research_report.js` | Summarize dry-run or evidence output. | Markdown report. |
| `update_*` scripts | Produce dry-run update reports for downstream folders. | Reports only unless a future reviewed apply mode is implemented. |

## Output Rules

- Timestamp every run folder.
- Keep screenshots under `31_PLAYWRIGHT_RESEARCH_PIPELINE/evidence/`.
- Keep normalized records under `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/`.
- Keep reports under `31_PLAYWRIGHT_RESEARCH_PIPELINE/reports/`.
- Downstream updates must remain dry-run unless a future task implements and audits apply mode.
- Any field captured from a browser page remains `UNVERIFIED` until checked against an official source or human review.

## Failure Rules

Scripts must exit non-zero when a required input is missing, live mode lacks an explicit URL, Playwright is not installed, or a requested PDF download lacks the required risk confirmation. A failure must not delete output or modify downstream databases.
