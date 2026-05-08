# Datasheet Redistribution Audit

Purpose: track datasheet, schematic, vendor-reference, and document redistribution risk before public GitHub release. This is a practical audit, not legal advice.

## Policy Position

Public releases should default to link-only records for vendor datasheets, application notes, reference manuals, dev-board schematics, and package drawings unless redistribution rights are clearly confirmed. AI summaries and metadata are acceptable only when they do not copy substantial copyrighted text and clearly cite source links for user verification.

## Local PDF Inventory

Current P0 public-release status: `BLOCKED_UNTIL_HUMAN_REVIEW`.

The local PDFs below must not be copied into a public GitHub release, installer payload, release ZIP/tarball, or generated public sample until redistribution rights are confirmed. The safe default is link-only metadata.

| File/folder | Source | License if known | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|---|
| `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf` | Espressif datasheet, exact source URL not embedded in this audit | Unknown from local file | Public redistribution unclear | Replace with link-only metadata unless Espressif redistribution permission is confirmed | `requires human review`; link-only recommended |
| `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/ESP32-S3-WROOM-1U-N16R8.pdf` | Espressif module/orderable-part document, exact source URL not embedded in this audit | Unknown from local file | Public redistribution unclear | Replace with link-only metadata unless Espressif redistribution permission is confirmed | `requires human review`; link-only recommended |

## Vendor Document Risk Categories

| Document type | Typical source | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|
| Datasheets | Vendor websites and distributors | Often publicly downloadable, but redistribution terms vary | Store URL, metadata, short AI summary, and verification status; do not bundle unless rights are confirmed | link-only recommended |
| Reference manuals | Vendor websites | Redistribution often unclear | Store source link and local summary stub only | link-only recommended |
| Application notes | Vendor websites | Redistribution often unclear | Store source link and summary; avoid copying diagrams/tables | link-only recommended |
| Errata | Vendor websites | Redistribution often unclear | Store source link, affected parts, revision/date, and summary | link-only recommended |
| Package drawings | Vendor websites or distributor CAD portals | Redistribution often unclear and high-risk for footprints | Store source link; require human footprint verification | link-only recommended |
| Dev-board schematics | Vendor websites, GitHub repos, board vendors | Varies by vendor and board | Store source link and license if visible; bundle only if license allows | `requires human review` |
| Reference designs | Vendor websites or GitHub repos | Varies; may include CAD files under specific terms | Prefer link-only; review license before bundling files | `requires human review` |
| Distributor CAD models | SnapEDA, Ultra Librarian, SamacSys, vendor portals | Terms vary and may restrict redistribution | Do not bundle unless explicit redistribution rights exist | `requires human review`; exclude by default |

## Source Lists

The source-list CSV files under `06_DATASHEETS/00_INDEX/source_lists/` are metadata scaffolding. They should remain link-oriented and should not imply that referenced documents are bundled or redistributable.

| File/folder | Source | License if known | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|---|
| `06_DATASHEETS/00_INDEX/source_lists/*.csv` | First-party metadata with vendor portal URLs/placeholders | Project license after review | Likely redistributable as metadata | Keep URLs current; avoid copying vendor document text | likely OK after review |
| `06_DATASHEETS/00_INDEX/*.md` | First-party policy, schema, and index docs | Project license after review | Likely redistributable | Keep policy language conservative and link-only by default | likely OK after review |
| `06_DATASHEETS/**/README.md`, `INDEX.md`, `SOURCES.md`, `MISSING.md` | First-party scaffolding | Project license after review | Likely redistributable | Avoid copied vendor text; use source links | likely OK after review |

## Public Release Rules

- Do not bundle PDFs unless redistribution rights are confirmed and recorded.
- Do not bundle dev-board schematics unless the source license permits redistribution.
- Do not bundle vendor CAD, symbols, footprints, or 3D models unless license terms permit redistribution.
- Prefer source links, revision metadata, and AI-readable summaries.
- Mark every unverified document as `UNVERIFIED_PLACEHOLDER` or equivalent.
- Keep exact electrical values marked as unverified unless sourced from a cited document.
- Maintain `public_redistribution_status` for every source-list row.
- Remove or exclude local migrated PDFs from release archives until a human review approves them.

## Required Human Review Before Bundling

For any vendor document proposed for public inclusion, record:

- Document title.
- Vendor/source URL.
- Download date.
- Document revision and date.
- License or terms page URL.
- Redistribution permission evidence.
- Whether the file may be modified, mirrored, or included in GitHub releases.
- Attribution text required by the vendor.
- Human reviewer and review date.
