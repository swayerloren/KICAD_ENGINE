# URL Registry Usage

`URL_INDEX` is the permanent source registry for this knowledge base. Every imported file should be traceable back to a registry row.

## Registry Files

- [../URL_INDEX.csv](../URL_INDEX.csv): canonical machine-readable registry for scripting and bulk edits
- [../URL_INDEX.json](../URL_INDEX.json): structured registry for programmatic consumers
- [../URL_INDEX.md](../URL_INDEX.md): human-readable summary of coverage, quality, and status
- [../RESCRAPE_QUEUE.csv](../RESCRAPE_QUEUE.csv): URLs that need recovery, replacement, or manual review

## Key Fields To Use

- `id`: stable `url_index_id` used inside copied Markdown frontmatter
- `original_url`: raw source URL as first seen
- `normalized_url`: deduplicated comparison key
- `source_domain`: domain routing and trust hint
- `scraped_status`: scrape state such as `success`, `failed`, `rejected`, or `needs_rescrape`
- `source_scraped_file`: original scrape artifact in the source folders
- `current_knowledge_file`: current local Markdown path in `knowledge_scrape`
- `source_file_type`: whether the source was Markdown, PDF, log, or unknown
- `source_of_truth_level`: trust tier label
- `content_quality`: current quality assessment
- `needs_future_rescrape`: whether the row should be revisited later
- `rescrape_reason`: why the future rescrape is needed
- `duplicate_group_id`: duplicate or near-duplicate grouping
- `original_pdf_path` and `extracted_markdown_path`: PDF linkage fields

## How To Link Local Files Back To The Registry

- Copied or generated Markdown should carry:
  - `source_url`
  - `normalized_url`
  - `url_index_id`
- `current_knowledge_file` in `URL_INDEX` is the reverse link from the registry back to the local file.
- When a file moves categories or is rejected, `current_knowledge_file` must be updated.

## How To Add Future URLs

1. Add new URLs to the maintained source lists.
2. Rebuild source-list inventory with `_scripts/01_build_raw_inventory.ps1`.
3. Rebuild the registry with `_scripts/02_build_url_registry.ps1`.
4. Import useful Markdown with `_scripts/03_classify_copy_markdown.ps1`.
5. Convert PDFs with `_scripts/04_convert_pdfs_to_markdown.ps1`.
6. Clean imported Markdown with `_scripts/05_clean_markdown_for_ai.ps1`.

## How To Detect Duplicates

- First compare `normalized_url`.
- Then inspect `duplicate_group_id`.
- Then compare `current_knowledge_file`, `source_scraped_file`, title, and content quality.
- Prefer the record with:
  - higher trust level
  - cleaner content
  - better file linkage
  - a stable canonical local path

## How To Mark A URL For Future Rescrape

Set or update these fields in `URL_INDEX`:
- `needs_future_rescrape = true`
- `rescrape_reason = <specific reason>`
- `scraped_status = needs_rescrape` if there is some content but it is degraded
- `scraped_status = failed` if there is no usable content

Typical reasons:
- output too small
- captcha or blocked page
- raw HTML noise
- HTML saved as PDF
- dead URL that needs replacement
- duplicate page with better canonical source available

## How To Use RESCRAPE_QUEUE

`RESCRAPE_QUEUE.csv` is the execution list for scrape recovery. Each row should include:
- `url`
- `reason`
- `recommended_method`
- `priority`
- `category_guess`
- `source_domain`

Recommended methods:
- `powershell_retry`: normal retry path
- `browser_playwright`: browser-driven scrape needed
- `manual_review`: human inspection required
- `replace_dead_url`: source has moved or disappeared
- `skip_low_value`: no value in spending more scrape effort
