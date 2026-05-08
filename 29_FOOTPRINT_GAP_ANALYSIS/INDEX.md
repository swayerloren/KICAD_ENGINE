# Footprint Gap Analysis Index

## PURPOSE

Route AI agents to the installed-KiCad footprint inventory, high-risk candidate lists, missing-footprint backlog, and read-only scripts.

## WHAT_BELONGS_HERE

| Path | Purpose |
| --- | --- |
| `INSTALLED_KICAD_FOOTPRINT_INVENTORY.md` | Generated summary of installed KiCad footprint libraries and candidate categories. |
| `INSTALLED_KICAD_SYMBOL_INVENTORY.md` | Generated summary of installed KiCad symbol libraries. |
| `MISSING_FOOTPRINT_CANDIDATES.md` | Candidate and missing-footprint list from component database comparison. |
| `HIGH_RISK_FOOTPRINTS.md` | High-risk footprint categories and verification warnings. |
| `CONNECTOR_FOOTPRINT_GAPS.md` | Connector-specific candidate gaps and review requirements. |
| `MCU_MODULE_FOOTPRINT_GAPS.md` | MCU, module, ESP32, STM32, PIC, and RP2040 package gaps. |
| `POWER_PACKAGE_FOOTPRINT_GAPS.md` | Regulator, protection, and power package gaps. |
| `FOOTPRINT_CREATION_BACKLOG.md` | Prioritized unverified footprint creation and verification backlog. |
| `GENERATED_INDEXES/` | JSON and Markdown outputs from read-only scripts. |
| `scripts/` | Read-only inventory, matching, and backlog scripts. |

## WHAT_DOES_NOT_BELONG_HERE

Do not store KiCad project files, custom production libraries, final manufacturing outputs, vendor PDFs, or secrets here.

## AI_AGENT_RULES

- Search results are candidates only.
- Exact footprint verification requires exact part number, package drawing, pad numbering, orientation, courtyard, paste/mask, 3D/mechanical review when useful, and human review for high-risk parts.
- Generic connector footprints remain `UNVERIFIED` until tied to a manufacturer drawing and mating connector.

## SAFE_EDIT_RULES

- Run scripts read-only against installed KiCad folders.
- Write reports only inside this repo.
- Do not modify global KiCad libraries or user-global library tables.

## PUBLIC_RELEASE_NOTES

Generated inventories are local-machine evidence. Public release can include scripts and policies; generated local inventories should be reviewed for path/privacy concerns.

