# Part Schema

Date: 2026-05-02

Status: required schema for records in `08_COMPONENT_DATABASE`.

## Required Unknown String

Use this exact value when a field has not been checked:

```text
Unknown - requires source verification
```

## Required Verification Flags

Every record must use one or more of these flags:

- `VERIFIED_FROM_DATASHEET`
- `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`
- `VERIFIED_FROM_KICAD_LIBRARY`
- `USER_CONFIRMED`
- `UNVERIFIED_PLACEHOLDER`

## Required Fields

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `record_id` | string | Yes | Stable uppercase ID. |
| `part_number` | string | Yes | Exact part number or generic placeholder label. |
| `vendor` | string | Yes | Manufacturer, publisher, generic, or unknown string. |
| `family` | string | Yes | Stable family name. |
| `category` | string | Yes | One of the `08_COMPONENT_DATABASE` category folders. |
| `package` | string | Yes | Exact package only if verified. |
| `kicad_symbol_candidates` | array | Yes | Candidate library symbols, or unknown string. |
| `kicad_footprint_candidates` | array | Yes | Candidate footprints, or unknown string. |
| `kicad_3d_model_candidates` | array | Yes | Candidate 3D models, or unknown string. |
| `datasheet_local_path` | string | Yes | Path under `06_DATASHEETS`, or unknown string. |
| `datasheet_source_url` | string | Yes | Official source URL, or unknown string. |
| `verified_status` | string | Yes | Use one of the verification flags. |
| `verification_flags` | array | Yes | One or more verification flags. |
| `pinout_status` | string | Yes | Verification state for pinout. |
| `footprint_status` | string | Yes | Verification state for footprint. |
| `layout_notes` | array | Yes | Layout constraints or unknown string. |
| `power_notes` | array | Yes | Power constraints or unknown string. |
| `communication_notes` | array | Yes | Interface notes or unknown string. |
| `common_mistakes` | array | Yes | Common design mistakes or unknown string. |
| `ai_warnings` | array | Yes | Warnings for agents. |
| `suitable_use_cases` | array | Yes | Only use verified specifics when researched. |
| `not_suitable_use_cases` | array | Yes | Known bad uses or unknown string. |
| `required_external_parts` | array | Yes | Required support parts or unknown string. |
| `reference_circuits` | array | Yes | Vendor/user reference circuits or unknown string. |
| `known_errata` | array | Yes | Errata or unknown string. |
| `source_confidence` | string | Yes | Verification flag or explanatory status. |
| `last_updated` | string | Yes | `YYYY-MM-DD`. |
| `notes` | array | Yes | Freeform review notes. |

## Core Minimum Fields For Starter Records

Starter records in `99_UNVERIFIED_INBOX` must include at least:

- `part_number`
- `vendor`
- `category`
- `datasheet_path_or_source_url_placeholder`
- `kicad_symbol_candidates`
- `kicad_footprint_candidates`
- `package_drawing_status`
- `three_d_model_status`
- `verification_status`
- `pinout_status`
- `common_mistakes`
- `human_review_required`

These fields are not enough to approve use in a schematic or PCB. They are the minimum safe placeholder fields for routing future research.

## JSON Skeleton

```json
{
  "record_id": "VENDOR_PART",
  "part_number": "Unknown - requires source verification",
  "vendor": "Unknown - requires source verification",
  "family": "Unknown - requires source verification",
  "category": "99_UNVERIFIED_INBOX",
  "package": "Unknown - requires source verification",
  "kicad_symbol_candidates": ["Unknown - requires source verification"],
  "kicad_footprint_candidates": ["Unknown - requires source verification"],
  "kicad_3d_model_candidates": ["Unknown - requires source verification"],
  "datasheet_local_path": "Unknown - requires source verification",
  "datasheet_source_url": "Unknown - requires source verification",
  "verified_status": "UNVERIFIED_PLACEHOLDER",
  "verification_flags": ["UNVERIFIED_PLACEHOLDER"],
  "pinout_status": "UNVERIFIED_PLACEHOLDER",
  "footprint_status": "UNVERIFIED_PLACEHOLDER",
  "layout_notes": ["Unknown - requires source verification"],
  "power_notes": ["Unknown - requires source verification"],
  "communication_notes": ["Unknown - requires source verification"],
  "common_mistakes": ["Treating an unverified placeholder as design-approved."],
  "ai_warnings": ["Do not use this record for schematic, footprint, or layout decisions until source verification is complete."],
  "suitable_use_cases": ["Unknown - requires source verification"],
  "not_suitable_use_cases": ["Unknown - requires source verification"],
  "required_external_parts": ["Unknown - requires source verification"],
  "reference_circuits": ["Unknown - requires source verification"],
  "known_errata": ["Unknown - requires source verification"],
  "source_confidence": "UNVERIFIED_PLACEHOLDER",
  "last_updated": "2026-05-02",
  "notes": ["Placeholder record only."]
}
```
