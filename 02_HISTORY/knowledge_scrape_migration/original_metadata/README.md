# knowledge_scrape

This is a local compiled KiCad and PCB engineering knowledge base. It combines cleaned scraped Markdown, extracted PDF text, original PDFs, and a permanent URL registry so engineering claims can be traced back to source files and source URLs.

Start here:
- [00_ai_entrypoints/AI_START_HERE.md](00_ai_entrypoints/AI_START_HERE.md)
- [URL_INDEX.md](URL_INDEX.md)
- [INDEX.md](INDEX.md)
- [00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md](00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md)
- [00_ai_entrypoints/KNOWLEDGE_MAP.md](00_ai_entrypoints/KNOWLEDGE_MAP.md)

Core rules:
- Treat `URL_INDEX.csv/json/md` as the source registry for future scraping and source tracking.
- Every engineering claim should be traceable to a local file path plus `url_index_id`.
- Prefer official datasheets, manufacturer app notes, KiCad docs, and fabricator docs before using forums or blogs.
- Treat `91_rejected_low_value/` as diagnostic material, not normal reference material.
- Treat extracted PDF Markdown as search-friendly text only. Original PDFs remain the source of truth for pinouts, dimensions, tables, and layout drawings.
- Use `00_engineering_rules/` and `00_retrieval_indexes/` for fast routing before opening broad topic folders.

Key folders:
- `00_ai_entrypoints/`: navigation and operating rules for agents.
- `00_source_of_truth/`: compact routing layer for official datasheets, app notes, KiCad docs, and fabricator rules.
- `00_engineering_rules/`: concise engineering-rule entrypoints for repeated decision types.
- `00_retrieval_indexes/`: quick routing maps and rejected-recovery indexes.
- `01_*` through `15_*`: curated topic folders.
- `14_datasheets_pdf_markdown/`: original PDFs, extracted Markdown, and extraction logs.
- `_raw_inventory/`: input inventory, duplicate candidates, and post-clean reports.
- `_source_registry/`: URL source lists, domain summaries, and scrape status artifacts.
- `_logs/`: build and cleaning logs.

Recommended usage:
1. Open `URL_INDEX.md` to understand registry health, scrape status, and file linkage.
2. Open `00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md` for source priority.
3. Open `INDEX.md` for category counts and generated artifacts.
4. Use `00_ai_entrypoints/KNOWLEDGE_MAP.md` or `00_retrieval_indexes/CATEGORY_ROUTING_INDEX.md` to choose the right folder.
5. Open the highest-trust local files first, then cite `source_url`, `url_index_id`, and local path.
