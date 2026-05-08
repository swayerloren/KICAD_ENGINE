# Vendor Schema

Status: `ACTIVE_SCHEMA`

## Purpose

Define fields for vendor and manufacturer source records.

## Required Unknown String

```text
Unknown - requires source verification
```

## Required Fields

| Field | Required | Notes |
| --- | --- | --- |
| `vendor_id` | Yes | Stable uppercase vendor ID. |
| `vendor_name` | Yes | Official vendor/manufacturer name. |
| `category` | Yes | MCU, power, connector, distributor, fab, generic, etc. |
| `official_website` | Yes | Official URL or unknown string. |
| `documentation_portal` | Yes | Official URL or unknown string. |
| `datasheet_policy` | Yes | Link-only unless redistribution is confirmed. |
| `lifecycle_source` | Yes | Official source or unknown string. |
| `preferred_source_priority` | Yes | Official vendor first. |
| `redistribution_notes` | Yes | Human review required if unclear. |
| `last_reviewed` | Yes | Date or unknown string. |
| `verification_status` | Yes | `UNVERIFIED_PLACEHOLDER` unless sourced. |

## Rule

Vendor records are source-routing aids. They do not verify part specs, lifecycle, availability, or design suitability by themselves.

