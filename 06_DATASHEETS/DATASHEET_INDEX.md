# Datasheet Index

Status: `NORMALIZED_FROM_COMPONENT_DATASHEET_VENDOR_MIGRATION`

## Scope

This index is the canonical entry point for datasheet-source work migrated from:

- ESP32 / Espressif intake
- Microcontroller intake
- Datasheet PDF / markdown intake

## Canonical Source Indexes

- [ESP32_SOURCE_INDEX.md](espressif/ESP32_SOURCE_INDEX.md)
- [MICROCONTROLLER_SOURCE_INDEX.md](microcontrollers/MICROCONTROLLER_SOURCE_INDEX.md)
- [SOURCE_REGISTRY.csv](../10_KNOWLEDGE_BASE/source_registry/SOURCE_REGISTRY.csv)
- [SOURCE_LICENSE_STATUS.md](../10_KNOWLEDGE_BASE/source_registry/SOURCE_LICENSE_STATUS.md)

## Migration Snapshot

- `61` unique source-registry entries point to the migrated ESP32/Espressif capture set.
- `6` unique source-registry entries point directly to the migrated generic microcontroller capture set.
- `107` unique source-registry entries point to the migrated datasheet PDF archive.
- `23` unmatched raw PDFs were found in the old archive and were moved to license quarantine pending manual mapping.

## Policy

- Canonical datasheet use is link-first.
- Raw PDFs and extracted PDF markdown remain license-sensitive.
- Quarantined original files are historical evidence, not public source-of-truth.

## Quarantine References

- `21_LICENSE_ATTRIBUTION/license_risk_reviews/`

## Use Pattern

1. Start with the source index for the vendor or component family.
2. Use the source registry row for URL provenance.
3. Pull exact values from an official document or approved local copy only.
4. Treat quarantine-only files as restricted evidence until license review is complete.
