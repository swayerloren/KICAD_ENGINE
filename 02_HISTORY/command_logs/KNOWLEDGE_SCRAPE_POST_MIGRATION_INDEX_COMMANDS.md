# Post-Migration Index Commands

## Commands Run

- `rg -n "knowledge_scrape" ...` on startup, handoff, and index surfaces
- `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .`
- `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .`
- `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .`
- `python 03_TOOLS\scripts\knowledge_migration\rebuild_knowledge_indexes.py --repo-root .`
- `python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply`
- `python` one-off normalization pass for canonical source-registry path fields
- `rg -uuu -l knowledge_scrape` for final remaining-reference audit
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
