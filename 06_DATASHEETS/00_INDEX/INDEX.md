# Datasheet Index

This file is the compact working index for the datasheet library control files. It does not claim that the datasheet database is complete.

| Area | Primary File | Purpose | Status | Notes |
| --- | --- | --- | --- | --- |
| Library policy | `DATASHEET_LIBRARY_README.md` | Explains link-only vs local datasheet handling. | ACTIVE | Public release must follow redistribution rules. |
| Master index | `MASTER_DATASHEET_INDEX.md` | Tracks curated and candidate datasheet records. | ACTIVE_PARTIAL | Source coverage remains incomplete. |
| Missing documents | `MISSING_DATASHEETS.md` and `MISSING.md` | Tracks documents still needed or not verified. | ACTIVE | Use `UNKNOWN_REQUIRES_SOURCE` where exact data is missing. |
| Source lists | `source_lists/` | CSV seed lists for vendor/source research. | ACTIVE_PARTIAL | Records are source links, not verified local datasheets. |
| Redistribution review | `REDISTRIBUTION_REVIEW_REQUIRED.md` | Blocks unreviewed PDFs from public release payloads. | P0_GATE | Must be checked before packaging or GitHub release. |

## Required Agent Checks

Before adding or using a datasheet record:

1. Confirm the target category folder and family folder.
2. Record whether the source is official vendor, official supplier, user-provided, public library, or unknown.
3. Set redistribution status before storing any local file.
4. Keep exact electrical/package claims `UNVERIFIED` until extracted from source.
5. Add missing source gaps to `MISSING_DATASHEETS.md` or the family `NEEDS_RESEARCH.md`.

## Output Status Labels

Use `SOURCE_LINK_ONLY` for links, `LOCAL_PRIVATE_ONLY` for unredistributed local files, `UNKNOWN_REQUIRES_REVIEW` for unclear provenance, and `VERIFIED_BY_DATASHEET` only for specific claims checked against a source.
