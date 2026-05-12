# Component / Datasheet / Vendor Migration Summary

Status: `KNOWLEDGE_SCRAPE_PHASE_5_NORMALIZED`

## Migration Outcome

- Source folders drained: `05`, `06`, `13`, `14`, `21`
- Files moved: `596`
- Raw capture files quarantined: `375`
- Metadata/history files archived: `221`
- Remaining legacy migration-residue file count after this phase: `1109`

## Canonical Surfaces Added

- `06_DATASHEETS/`
- `08_COMPONENT_DATABASE/`
- `25_VENDOR_DATABASE/`
- `29_FOOTPRINT_GAP_ANALYSIS/`
- `30_SUPPLIER_FOOTPRINT_MATCHES/`
- `35_FOOTPRINT_PACKAGE_ENGINE/FOOTPRINT_EVIDENCE_RULES.md`

## Key Rules Formalized

- vendor part number is not footprint proof
- supplier CAD model is not automatically trusted
- raw datasheet PDF redistribution requires license review
- ESP32 modules require antenna keepout and land-pattern proof
- connectors require orientation and mechanical proof
- PMOS/regulator/ESD/TVS parts require pin-mapping proof
