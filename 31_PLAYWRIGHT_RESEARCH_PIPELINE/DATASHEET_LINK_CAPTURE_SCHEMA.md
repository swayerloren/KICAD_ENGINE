# Datasheet Link Capture Schema

Status: `MANDATORY_LINK_ONLY_SCHEMA`

This schema defines how Playwright/API/manual research may record datasheet and reference-document links. It is not permission to download or redistribute PDFs. Captured links remain `SOURCE_LINK_ONLY` or `UNVERIFIED` until document identity, revision, and claims are reviewed.

| Field | Required | Notes |
| --- | --- | --- |
| `manufacturer` | Yes | Manufacturer or vendor. |
| `part_number` | Yes | MPN or generic placeholder. |
| `document_type` | Yes | Datasheet, reference manual, errata, app note, package drawing, board schematic, user manual. |
| `title` | Yes | Source title if available. |
| `source_url` | Yes | Link to source page or direct document URL. |
| `source_profile` | Yes | Matching source profile. |
| `retrieved_at` | Yes | ISO timestamp. |
| `redistribution_status` | Yes | Prefer `LINK_ONLY` unless confirmed. |
| `verification_status` | Yes | Default `UNVERIFIED`. |
| `local_target_folder` | No | Proposed downstream folder; dry-run only unless explicitly applied. |
| `notes` | No | Include access limits and source caveats. |

## Allowed Document Types

- `DATASHEET`
- `REFERENCE_MANUAL`
- `ERRATA`
- `APPLICATION_NOTE`
- `PACKAGE_DRAWING`
- `BOARD_SCHEMATIC`
- `USER_MANUAL`
- `DESIGN_GUIDE`
- `LIBRARY_SOURCE`
- `SUPPLIER_PRODUCT_PAGE`

## Required Status Values

| Field | Allowed Values |
| --- | --- |
| `redistribution_status` | `LINK_ONLY`, `REDISTRIBUTION_CONFIRMED`, `LOCAL_PRIVATE_ONLY`, `UNKNOWN_REQUIRES_REVIEW` |
| `verification_status` | `UNVERIFIED`, `SOURCE_LINK_ONLY`, `OFFICIAL_SOURCE_LINK`, `PARTIALLY_VERIFIED`, `VERIFIED_BY_DATASHEET`, `NEEDS_HUMAN_REVIEW` |
| `source_confidence` | `OFFICIAL_VENDOR`, `OFFICIAL_SUPPLIER`, `PUBLIC_LIBRARY`, `USER_PROVIDED`, `UNKNOWN` |

## Capture Rules

- Prefer official manufacturer pages over direct PDF URLs when revision and terms are clearer on the landing page.
- Record retrieval timestamp and source profile for every link.
- Do not store copied PDF content in this schema.
- Do not promote electrical values, pinouts, lifecycle, or package data from a link record alone.
- If a page is blocked, requires login, shows CAPTCHA, or has unclear terms, record `NEEDS_HUMAN_REVIEW` and stop.

## Downstream Use

Links captured here may update source indexes and component records as `SOURCE_LINK_ONLY`. A separate datasheet review must extract and verify the specific claims before a component, symbol, footprint, or BOM line is approved.
