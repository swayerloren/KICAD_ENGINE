# AI Start Here

This folder is a local compiled KiCad and PCB engineering knowledge base. It is designed for local AI use, not for blind copy-paste. Every useful claim should be tied back to a source file and a `URL_INDEX` row.

## Start Sequence

1. Open [../URL_INDEX.md](../URL_INDEX.md).
2. Open [../INDEX.md](../INDEX.md).
3. Open [../00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md](../00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md).
4. Open [KNOWLEDGE_MAP.md](KNOWLEDGE_MAP.md).

## Operating Rules

- Every engineering claim must be traceable to:
  - a local file path
  - `source_url`
  - `url_index_id`
- Prefer sources in this order:
  - official manufacturer datasheets
  - official manufacturer app notes
  - official KiCad docs, dev docs, and library rules
  - fabricator docs
  - peer-reviewed forums
  - blogs and tutorials
  - video indexes, Reddit, search pages, and other low-value scrape material
- Do not blindly trust scraped forums, blogs, or generic index pages.
- Do not use `91_rejected_low_value/` as a normal authority source.
- Treat extracted PDF Markdown as search-friendly text only. Original PDFs remain the source of truth for:
  - pinouts
  - package drawings
  - land pattern guidance
  - recommended layout
  - tables
  - figures
- Use the compact routing docs in `../00_engineering_rules/` and `../00_retrieval_indexes/` before falling back to broad folder browsing.

## Default Workflow

1. Use `URL_INDEX.md` to understand status, trust level, and where the local file lives.
2. Use `../00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md` and `../00_retrieval_indexes/CATEGORY_ROUTING_INDEX.md` to choose the right source class and folder.
3. Open the highest-trust local files first.
4. Cross-check risky topics with [SOURCE_TRUST_RULES.md](SOURCE_TRUST_RULES.md).
5. Cite local path plus `url_index_id` in any output that makes an engineering recommendation.
6. For new scrape batches under `C:\KICAD_SCRAPE\ingest_v2`, use `../_scripts/10_import_ingest_v2.ps1` instead of copying files by hand.

## Fast Routing

- KiCad behavior, CLI, DRC/ERC, file formats: start in `01_kicad_core/`, `02_kicad_python_api/`, and `03_kicad_file_formats/`.
- KiCad library and footprint questions: start in `04_kicad_libraries_symbols_footprints/`.
- ESP32 and Espressif hardware: start in `05_esp32_espressif/`.
- MCU pinouts and vendor docs: start in `06_microcontrollers/`.
- USB-C, ESD, and high-speed routing: start in `07_usb_c_high_speed_esd/`.
- Buck converters and power layout: start in `08_power_buck_regulators/`.
- PCB layout, grounding, EMI, and SI: start in `09_pcb_layout_grounding_emi_si/`.
- Fabrication and assembly rules: start in `10_dfm_fabrication_assembly/`.
- Calculators and IPC-style references: start in `11_calculators_ipc_reference/`.
- PDFs: use `14_datasheets_pdf_markdown/` and always check the original PDF when details matter.
