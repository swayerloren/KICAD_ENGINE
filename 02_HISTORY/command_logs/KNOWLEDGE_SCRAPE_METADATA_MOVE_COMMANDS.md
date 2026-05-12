# Knowledge Scrape Metadata Move Commands

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Commands Run

```powershell
# Read required migration inputs
Get-Content START_HERE_FOR_AI_AGENTS.md
Get-Content 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv -TotalCount 40
Get-Content 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md
Get-Content 03_TOOLS\scripts\knowledge_migration\README.md

# Inspect source metadata targets
Get-ChildItem knowledge_scrape -Force
Get-ChildItem knowledge_scrape\_source_registry -Recurse -File
Get-ChildItem knowledge_scrape\_raw_inventory -Recurse -File
Get-ChildItem knowledge_scrape\_logs -Recurse -File
Get-ChildItem knowledge_scrape\99_source_logs -Recurse -File

# Update metadata-destination routing in the migration config
apply_patch

# Rebuild ledger/destination map after config adjustment
python 03_TOOLS\scripts\knowledge_migration\classify_knowledge_scrape_items.py --repo-root . --source-root knowledge_scrape --inventory 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_FILE_INVENTORY_BEFORE.csv --config 03_TOOLS\scripts\knowledge_migration\knowledge_migration_config.json --ledger 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv --destination-map 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_DESTINATION_MAP.md --status 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md

# Apply targeted metadata moves from the ledger
python 03_TOOLS\scripts\knowledge_migration\move_knowledge_item.py --repo-root . --ledger 05_OUTPUTS\release_readiness\KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv --original-path <TARGET_PATH> --apply

# Build canonical normalized registry/index outputs
@'...Python normalization script...'@ | python -

# Validate canonical outputs and source absence
python - <<'PY'
# JSON/CSV parse checks plus ledger moved-row checks
PY

Get-ChildItem knowledge_scrape -File -Recurse | Measure-Object
Get-ChildItem knowledge_scrape -Directory
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LIVE_PROJECT_STATE.json -TotalCount 80
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256
git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'
```

## Key Outcomes

- Targeted metadata/log/index files moved: `43`
- Quarantine moves: `0`
- `knowledge_scrape/` file count changed from `2546` to `2503`
- Canonical registry outputs created under `10_KNOWLEDGE_BASE/source_registry/`
- Canonical retrieval indexes created under `10_KNOWLEDGE_BASE/retrieval_indexes/`
- No KiCad design-file state changed during this task
