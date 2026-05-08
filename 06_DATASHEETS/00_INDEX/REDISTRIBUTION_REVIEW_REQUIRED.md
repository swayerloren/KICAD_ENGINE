# Redistribution Review Required

Status: `P0_PUBLIC_RELEASE_BLOCKER`

This file tracks local datasheet/reference files that must not be included in a public GitHub release or installer payload unless redistribution rights are confirmed by human review.

## Current Local PDF Findings

| File | Status | Required action |
|---|---|---|
| `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/ESP32-S3-WROOM-1U-N16R8.pdf` | `REDISTRIBUTION_REVIEW_REQUIRED` | Confirm redistribution rights or replace with link-only metadata before public release. |
| `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf` | `REDISTRIBUTION_REVIEW_REQUIRED` | Confirm redistribution rights or replace with link-only metadata before public release. |

## Rules

- Do not delete local user files during automated cleanup.
- Do not copy these files into installer payloads.
- Do not include these files in public release archives.
- Prefer official source URLs, document title, revision/date, and local summary stubs.
- Treat local file presence as evidence that review is needed, not as redistribution permission.

## Human Review Fields

Before a vendor document can be bundled, record:

- Vendor/source URL.
- Document title, revision, and date.
- License or terms URL.
- Redistribution permission evidence.
- Reviewer name or initials.
- Review date.
- Approved public-release status.
