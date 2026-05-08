# Package Profile Schema

Status: `ACTIVE_SCHEMA`

## Purpose

Define the fields required for package profiles used by AI agents when selecting, checking, or creating KiCad footprints.

## Required Unknown String

Use:

```text
Unknown - requires source verification
```

## Required Status Values

- `VERIFIED_FROM_PACKAGE_DRAWING`
- `VERIFIED_FROM_MANUFACTURER_LAND_PATTERN`
- `VERIFIED_FROM_KICAD_LIBRARY_INSPECTION`
- `USER_CONFIRMED`
- `UNVERIFIED_PLACEHOLDER`

## Required Fields

| Field | Required | Notes |
| --- | --- | --- |
| `profile_id` | Yes | Stable uppercase ID. |
| `package_family` | Yes | QFN, QFP, SOIC, SOT, DFN, BGA, MODULE, CONNECTOR, THROUGH_HOLE, or generic. |
| `package_name` | Yes | Exact package name only if sourced. |
| `manufacturer_package_code` | Yes | Use unknown string unless verified. |
| `source_document` | Yes | Package drawing, datasheet, land pattern, or unknown string. |
| `source_url` | Yes | Official URL or unknown string. |
| `source_revision_or_date` | Yes | Date/revision or unknown string. |
| `pin_or_pad_count` | Yes | Exact count only if sourced. |
| `pitch` | Yes | Exact value only if sourced. |
| `body_dimensions` | Yes | Exact values only if sourced. |
| `pad_or_lead_dimensions` | Yes | Exact values only if sourced. |
| `exposed_pad` | Yes | Include status and source. |
| `pin1_orientation` | Yes | Exact orientation or unknown string. |
| `kicad_footprint_candidates` | Yes | Candidate only unless verified. |
| `kicad_3d_model_candidates` | Yes | Candidate only unless verified. |
| `verification_status` | Yes | One required status value. |
| `human_review_required` | Yes | Boolean-like `true` or `false`; placeholders must be `true`. |
| `ai_warnings` | Yes | Warnings against guessing. |

## Approval Rule

A package profile is not footprint approval. A KiCad footprint remains unverified until compared against the exact package drawing or manufacturer land pattern.

