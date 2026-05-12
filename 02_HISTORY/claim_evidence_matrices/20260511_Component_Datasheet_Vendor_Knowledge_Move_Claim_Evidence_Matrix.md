# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| `596` files moved | migration ledger rows tagged with `phase=component_datasheet_vendor_knowledge_move` |
| target folders drained | source-folder existence checks returned `False` for all `5` folders |
| raw PDFs quarantined | ledger action `MOVE_TO_LICENSE_QUARANTINE` plus quarantine destination paths |
| canonical indexes created | new files under `06_DATASHEETS`, `08_COMPONENT_DATABASE`, `25_VENDOR_DATABASE`, `29_FOOTPRINT_GAP_ANALYSIS`, `30_SUPPLIER_FOOTPRINT_MATCHES` |
| no KiCad design files changed in this task | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` showed only the preexisting schematic path |
