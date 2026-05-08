# Component Database Index

Status: `ACTIVE_SCAFFOLD`

## Key Areas

- `00_INDEX/`: schema, verification levels, and database rules.
- `01_MICROCONTROLLERS/`: MCU family guides and records.
- `02_POWER/`: regulator, charger, fuse, TVS, and power-protection records.
- `03_COMMUNICATION/`: CAN, LIN, USB, Ethernet, UART bridge, and level-shifter records.
- `04_CONNECTORS/`: connector records and selection guide.
- `13_DESIGN_RULE_SNIPPETS/`: reusable design-rule notes.
- `14_PART_SELECTION_GUIDES/`: selection guidance.
- `15_PACKAGE_FOOTPRINT_DATABASE/`: exact package drawing and KiCad footprint verification records.
- `16_VERIFICATION_RECORDS/`: component verification evidence before promoting records.
- `99_UNVERIFIED_INBOX/`: placeholder and imported records that are not curated.

## Required Use

Agents must cite source status and verification level before using any part record for schematic, footprint, BOM, or layout work.

## Core Starter Placeholder Records

- Markdown: `99_UNVERIFIED_INBOX/core_starter_records/CORE_STARTER_RECORDS.md`
- JSON: `99_UNVERIFIED_INBOX/core_starter_records/core_starter_records.json`

These records are deliberately marked `UNVERIFIED_PLACEHOLDER` and require human review.


## PURPOSE

Store structured part intelligence, schemas, verification states, and KiCad candidate links beyond raw PDFs.

## WHAT_BELONGS_HERE

Part records, JSON records, verification flags, symbol candidates, footprint candidates, layout notes, and selection guides.

## WHAT_DOES_NOT_BELONG_HERE

Datasheet PDF archives, KiCad design source files, fabricated specs, or production-approved footprint claims without evidence.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to 2_HISTORY/, 5_OUTPUTS/, or project history/ unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
