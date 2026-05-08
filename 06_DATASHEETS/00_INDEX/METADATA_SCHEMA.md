# Datasheet Metadata Schema

Date: 2026-05-02

Status: canonical metadata schema for datasheet and reference records.

## Purpose

This schema defines the minimum fields AI agents need to connect datasheets and reference documents to KiCad symbols, footprints, 3D models, BOM review, ERC/DRC interpretation, and fabrication review.

Unknowns must remain explicit. Do not invent values from memory.

## Required Unknown String

Use this exact value for unchecked fields:

```text
Unknown - requires source verification
```

## Record Types

Allowed `record_type` values:

- `PART`
- `DEV_BOARD`
- `REFERENCE_DOCUMENT`
- `DATASHEET_SUMMARY`

## Verification Status Values

Allowed `verification_status` values:

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

## Document Type Values

Allowed `document_type` values:

- `DATASHEET`
- `MODULE_DATASHEET`
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
- `ANTENNA_RF_GUIDE`
- `FAB_ASSEMBLY_REFERENCE`
- `VENDOR_PORTAL_NOTE`
- `REFERENCE_DOCUMENT`

## Core Part Fields

| Field | Required | Meaning |
| --- | --- | --- |
| `record_type` | Yes | `PART`, `DEV_BOARD`, `REFERENCE_DOCUMENT`, or `DATASHEET_SUMMARY`. |
| `record_id` | Yes | Stable ID using uppercase vendor and part/topic tokens. |
| `vendor` | Yes | Manufacturer or publisher. |
| `part_number` | Yes for parts | Exact part number or generic topic name. |
| `family` | Yes | Component or document family. |
| `package` | Yes | Verified package/module/package drawing name, or unknown string. |
| `document_type` | Yes | Controlled document type token. |
| `document_title` | Yes | Title as printed on the document, or unknown string. |
| `revision` | Yes | Vendor revision, document number, or unknown string. |
| `document_date` | Yes | `YYYY-MM-DD`, `YYYY-MM`, year, or unknown string. |
| `source_url` | Yes | Authoritative URL, or unknown string. |
| `source_access_date` | Yes | Date source URL was checked, or unknown string. |
| `local_filename` | Yes | Local file name if stored, or proposed filename. |
| `local_path` | Yes | Local path if stored, or intended category path. |
| `copyright_note` | Yes | Redistribution/license note or unknown string. |
| `verification_status` | Yes | Controlled status value. |

## KiCad Link Fields

| Field | Required | Meaning |
| --- | --- | --- |
| `related_kicad_symbol` | Yes | Exact library nickname and symbol if verified, candidate if not. |
| `related_kicad_footprint` | Yes | Exact library nickname and footprint if verified, candidate if not. |
| `related_kicad_3d_model` | Yes | 3D model path or unknown string. |
| `symbol_verification_notes` | Yes | How the symbol was checked. |
| `footprint_verification_notes` | Yes | How the footprint was checked. |

## Electrical And Mechanical Fields

| Field | Required | Meaning |
| --- | --- | --- |
| `voltage_range` | Yes | Recommended operating supply or signal voltage range. |
| `current_limits` | Yes | Supply, output, connector, or load current limits. |
| `absolute_maximum_ratings` | Yes | Absolute maximum ratings summary or unknown string. |
| `recommended_operating_conditions` | Yes | Recommended operating conditions summary or unknown string. |
| `pin_count` | Yes | Verified pin/pad count or unknown string. |
| `package_type` | Yes | Package family or mechanical connector type. |
| `special_layout_rules` | Yes | Layout constraints, routing notes, keepouts, thermal rules, RF rules, or unknown string. |
| `known_errata` | Yes | Errata summary or unknown string. |
| `lifecycle_status` | Yes | Active, NRND, obsolete, preview, generic, or unknown string. |

## Optional Review Fields

| Field | Meaning |
| --- | --- |
| `used_in_projects` | Project names where the document was used. |
| `bom_notes` | BOM sourcing, MPN, DNP, or assembly notes. |
| `connector_orientation_notes` | Connector orientation and mating direction notes. |
| `power_budget_notes` | Power or thermal assumptions. |
| `open_questions` | Unresolved issues before design use. |
| `review_history` | Links to history reports that used this record. |

## YAML Skeleton

```yaml
record_type: PART
record_id: VENDOR_PART
vendor: Unknown - requires source verification
part_number: Unknown - requires source verification
family: Unknown - requires source verification
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: Unknown - requires source verification
local_path: Unknown - requires source verification
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify source URL, document revision, package, symbol, footprint, and 3D model before design use.
review_history: []
```
