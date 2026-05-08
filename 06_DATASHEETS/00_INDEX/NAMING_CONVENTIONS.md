# Datasheet Naming Conventions

Date: 2026-05-02

Status: strict naming and indexing rules for AI-assisted KiCad work.

## Purpose

This file defines how datasheets, development-board schematics, reference manuals, errata, application notes, package drawings, layout guides, and reference designs must be named and indexed in `06_DATASHEETS`.

The goal is reliable retrieval by Codex, Claude, and similar agents without implying that a document or component is verified just because a file exists.

## Core Rules

- Do not download datasheets unless the user explicitly approves that task.
- Do not rename existing documents unless vendor, part number, document type, revision, and date are verified or the rename is clearly marked as provisional.
- Do not encode unverified electrical values into filenames.
- Do not claim a part, symbol, footprint, or 3D model is verified from filename or folder location alone.
- Every curated document must have a metadata record or an index row.
- Every unknown field must use `Unknown - requires source verification`.

## Folder Rules

- Use numbered top-level categories.
- Use uppercase vendor folders where vendor identity is useful.
- Use uppercase family folders: `ESP32_S3`, `STM32F4`, `PIC18`.
- Avoid spaces in folder and file names.
- Use `99_UNSORTED_INBOX` for uncurated files.
- Use `OTHER` only when vendor or family placement is genuinely unknown.

## Local Filename Standard

Preferred pattern:

```text
VENDOR_PART_FAMILY_PACKAGE_DOCUMENTTYPE_REVISION_DATE.ext
```

When package, revision, or date is unknown, keep the field but mark it explicitly:

```text
VENDOR_PART_FAMILY_PKG_UNKNOWN_DOCUMENTTYPE_REV_UNKNOWN_DATE_UNKNOWN.ext
```

## Filename Field Rules

| Field | Rule | Examples |
| --- | --- | --- |
| `VENDOR` | Uppercase manufacturer or publisher. Use `GENERIC` only for generic connector or reference records. | `ESPRESSIF`, `STMICRO`, `MICROCHIP`, `RASPBERRY_PI`, `TI`, `GENERIC` |
| `PART` | Use the exact part number from the document. Preserve meaningful hyphens. Replace spaces and slashes with hyphens. | `ESP32-S3-WROOM-1U`, `STM32F103C8T6`, `PIC18F4550` |
| `FAMILY` | Use the stable family folder name. | `ESP32_S3`, `STM32F1`, `PIC18`, `RP2040`, `CAN`, `POWER`, `CONNECTOR_RF` |
| `PACKAGE` | Use package or module package if verified. Use `PKG_UNKNOWN` if not verified. | `LQFP-48`, `QFN-56`, `MODULE`, `SOT-223`, `PKG_UNKNOWN` |
| `DOCUMENTTYPE` | Use one of the controlled document type tokens below. | `DATASHEET`, `REFERENCE_MANUAL`, `ERRATA` |
| `REVISION` | Use vendor revision token if known. Use `REV_UNKNOWN` if not verified. | `Rev3`, `v1.7`, `RM0008-Rev21`, `REV_UNKNOWN` |
| `DATE` | Use `YYYY-MM-DD` when a document date is verified, `YYYY-MM` when only month is known, or `DATE_UNKNOWN`. | `2024-06`, `2023-11-15`, `DATE_UNKNOWN` |
| `ext` | Preserve document extension in lowercase unless the source uses a meaningful case. | `pdf`, `md`, `html`, `zip` |

## Controlled Document Type Tokens

Use these tokens in filenames and metadata:

- `DATASHEET`
- `REFERENCE_MANUAL`
- `PROGRAMMING_MANUAL`
- `APPLICATION_NOTE`
- `ERRATA`
- `PACKAGE_DRAWING`
- `LAND_PATTERN`
- `LAYOUT_GUIDE`
- `DESIGN_GUIDE`
- `REFERENCE_DESIGN`
- `DEV_BOARD_SCHEMATIC`
- `DEV_BOARD_USER_GUIDE`
- `DEV_BOARD_BOM`
- `MODULE_DATASHEET`
- `ANTENNA_RF_GUIDE`
- `FAB_ASSEMBLY_REFERENCE`
- `VENDOR_PORTAL_NOTE`

If none fits, use `REFERENCE_DOCUMENT` and explain the reason in metadata.

## Metadata Required For Every Curated Part

The filename is not enough. Each curated part record must include:

- Vendor.
- Part number.
- Family.
- Package.
- Document type.
- Revision.
- Date.
- Source URL.
- Local filename.
- Related KiCad symbol.
- Related KiCad footprint.
- Related KiCad 3D model.
- Voltage range.
- Current limits.
- Absolute maximum ratings.
- Recommended operating conditions.
- Pin count.
- Package type.
- Special layout rules.
- Known errata.
- Lifecycle status.
- Verification status.

Use `Unknown - requires source verification` for any field that has not been checked against an authoritative source.

## Source URL Rule

Do not place full URLs in filenames. Record source URLs in:

- The part record.
- The category `SOURCES.md`.
- `00_INDEX/MASTER_DATASHEET_INDEX.md` when the document is important globally.

## Verification Status Tokens

Use these exact status values:

- `NOT_VERIFIED`
- `SOURCE_URL_RECORDED`
- `REVISION_CHECKED`
- `METADATA_EXTRACTED`
- `SYMBOL_CANDIDATE_LINKED`
- `FOOTPRINT_CANDIDATE_LINKED`
- `SYMBOL_VERIFIED`
- `FOOTPRINT_VERIFIED`
- `USED_IN_REVIEW`
- `SUPERSEDED`

Do not use `VERIFIED` by itself. State what was verified.

## Examples

Provisional filenames where details are not verified:

```text
ESPRESSIF_ESP32-S3-WROOM-1_ESP32_S3_PKG_UNKNOWN_MODULE_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
ESPRESSIF_ESP32-S3-WROOM-1U_ESP32_S3_PKG_UNKNOWN_MODULE_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
STMICRO_STM32F103C8T6_STM32F1_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
MICROCHIP_PIC18F4550_PIC18_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
GENERIC_USB-C-RECEPTACLE_CONNECTOR_USB-C_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
```

Verified filenames can replace unknown tokens only after source review:

```text
VENDOR_PART_FAMILY_PACKAGE_DOCUMENTTYPE_REVISION_YYYY-MM-DD.pdf
```

## Do Not Rename Blindly

During migration, preserve legacy filenames until the record is curated. If a file is renamed later, record the old filename in `DUPLICATES_AND_REVISIONS.md` or the part record.
