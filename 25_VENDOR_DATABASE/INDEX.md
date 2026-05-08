# Vendor Database Index

Status: `ACTIVE_SCAFFOLD`

## Folder Map

- `00_INDEX/`: vendor schema and source rules.
- `ESPRESSIF/`: Espressif source and lifecycle records.
- `STMICRO/`: STMicroelectronics source and lifecycle records.
- `MICROCHIP/`: Microchip source and lifecycle records.
- `TI/`: Texas Instruments source and lifecycle records.
- `NXP/`: NXP source and lifecycle records.
- `NORDIC/`: Nordic Semiconductor source and lifecycle records.
- `RASPBERRY_PI/`: Raspberry Pi source and lifecycle records.
- `MOLEX/`: Molex connector source records.
- `TE_CONNECTIVITY/`: TE Connectivity connector source records.
- `JST/`: JST connector source records.
- `WURTH/`: Wurth Elektronik source records.
- `GENERIC_SUPPLIERS/`: distributor and marketplace metadata templates.

## Related Existing Data

- `06_DATASHEETS/00_INDEX/source_lists/`
- `08_COMPONENT_DATABASE/`

## Core Files

- `00_INDEX/VENDOR_SCHEMA.md`
- `00_INDEX/VENDOR_SOURCE_PRIORITY_RULES.md`
- `00_INDEX/OFFICIAL_DOC_LINK_RULES.md`
- `00_INDEX/PART_LIFECYCLE_STATUS_RULES.md`


## PURPOSE

Store vendor, manufacturer, distributor, lifecycle, source portal, and sourcing metadata.

## WHAT_BELONGS_HERE

Source portals, manufacturer notes, distributor placeholders, lifecycle notes, and source-confidence metadata.

## WHAT_DOES_NOT_BELONG_HERE

Paid account credentials, scraped restricted data, unlicensed documents, or unverified pricing/availability claims.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to `02_HISTORY/`, `05_OUTPUTS/`, or project history unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
