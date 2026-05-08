# Data Capture Schema

Status: `SCHEMA_DRAFT`

## Required Fields

| Field | Required | Notes |
| --- | --- | --- |
| `record_id` | Yes | Stable local ID. |
| `target_part_number` | Yes | Requested part or generic target. |
| `source_name` | Yes | Source profile name. |
| `source_url` | Yes | URL captured or planned. |
| `source_type` | Yes | API, official vendor page, distributor page, public KiCad repo, user CSV, or manual link. |
| `retrieved_at` | Yes | ISO timestamp. |
| `capture_mode` | Yes | `DRY_RUN` or `LIVE_PUBLIC_PAGE`. |
| `verification_status` | Yes | Default `UNVERIFIED`. |
| `source_confidence` | Yes | `OFFICIAL`, `DISTRIBUTOR`, `PUBLIC_LIBRARY`, `USER_PROVIDED`, `UNKNOWN`. |
| `redistribution_status` | Yes | `LINK_ONLY`, `REDISTRIBUTION_CONFIRMED`, `UNKNOWN_REQUIRES_REVIEW`, or `DO_NOT_BUNDLE`. |
| `human_review_required` | Yes | Boolean. |
| `notes` | No | Plain-language caveats. |

## Claim Rule

Captured data must not be converted into engineering claims until it is checked against the correct downstream verification rules.

