# Future Scraping Workflow

Use this workflow when adding new source material to the knowledge base. The goal is to preserve a durable registry, not just collect files.

## Source Of Truth For Tracking

- `URL_INDEX.csv/json/md` is the permanent URL and page registry.
- `RESCRAPE_QUEUE.csv` is the operational queue for failed, degraded, or replacement scrape work.
- `_source_registry/url_source_lists.csv/json` tracks the imported source-list rows.

## Add New URLs

1. Add the raw URLs to the maintained source lists.
2. Keep the source-list file name stable so provenance remains useful.
3. Rebuild the list import with `_scripts/01_build_raw_inventory.ps1`.
4. Rebuild the URL registry with `_scripts/02_build_url_registry.ps1`.

## Import New Content

1. For `C:\KICAD_SCRAPE\ingest_v2` batches, run `_scripts/10_import_ingest_v2.ps1` first. It inventories the batch, checks `URL_INDEX.csv`, avoids duplicate URL and duplicate-content imports, copies source logs, and rebuilds the main indexes.
2. For older legacy scrape layouts, use `_scripts/03_classify_copy_markdown.ps1`, `_scripts/04_convert_pdfs_to_markdown.ps1`, and `_scripts/05_clean_markdown_for_ai.ps1` in sequence.
3. Always validate the rebuilt `URL_INDEX.csv`, `PDF_INDEX.csv`, and `_CATEGORY_INDEX.md` files before treating the batch as complete.

## Update Rules

- Every imported file should link back to `URL_INDEX` through `url_index_id`.
- Every registry row with a usable local file should have `current_knowledge_file`.
- Duplicates should be tracked with `duplicate_group_id`, not ignored silently.
- If a page is low-value or clearly bad, keep the row in the registry and mark it rejected instead of deleting history.

## When A URL Must Enter RESCRAPE_QUEUE

Add or keep a row in `RESCRAPE_QUEUE.csv` when:
- the scrape failed
- the output file is missing
- the output is too small
- the page is blocked by captcha or login
- the page is noisy raw HTML
- HTML was saved as a fake PDF
- the URL is dead and needs a replacement source
- the content is low quality but still potentially useful

## Recommended Methods

- `powershell_retry`
  - Use for normal retries, transient network errors, or clean direct-download URLs.
- `browser_playwright`
  - Use when the site needs browser rendering, script execution, cookie banners, or dynamic navigation.
- `manual_review`
  - Use when a human needs to inspect the page, confirm relevance, or pick the right artifact.
- `replace_dead_url`
  - Use when the original source moved, was removed, or should be replaced by a better canonical URL.
- `skip_low_value`
  - Use when the page is structurally low-value and not worth more scrape effort.

## Preferred Maintenance Order

1. Update source lists.
2. Refresh raw inventory.
3. Refresh URL registry.
4. Import or recover useful content with the batch-aware importer.
5. Review the rebuilt indexes and validation report.
6. Clean or rescrape only the remaining gaps.
7. Review `RESCRAPE_QUEUE.csv` and `URL_INDEX.md`.
