# Fab Profile Schema

Status: `ACTIVE_SCHEMA`

## Purpose

Define fields for fabrication and assembly profiles used by AI agents when preparing review-only manufacturing outputs.

## Required Status Values

- `VERIFIED_FROM_FAB_DOCUMENTATION`
- `VERIFIED_FROM_USER_CONFIRMED_FAB_RULE`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED_PLACEHOLDER`

## Required Fields

| Field | Required | Notes |
| --- | --- | --- |
| `profile_id` | Yes | Stable uppercase ID. |
| `fab_name` | Yes | Fabricator or generic profile name. |
| `profile_scope` | Yes | PCB fab, assembly, stencil, review output, or generic. |
| `source_url` | Yes | Official source URL or unknown string. |
| `source_revision_or_date` | Yes | Required when verified. |
| `gerber_rules` | Yes | Use unknown string unless sourced. |
| `drill_rules` | Yes | Use unknown string unless sourced. |
| `bom_rules` | Yes | Use unknown string unless sourced. |
| `cpl_pnp_rules` | Yes | Use unknown string unless sourced. |
| `assembly_notes_rules` | Yes | Use unknown string unless sourced. |
| `not_final_label_required` | Yes | Must be true for generated outputs. |
| `verification_status` | Yes | One required status value. |
| `human_review_required` | Yes | Placeholders must be true. |

## Approval Rule

A fab profile is not manufacturability approval. Generated outputs remain `NOT_FINAL` until fab-specific rules, ERC, DRC, BOM, footprint, connector, polarity, mechanical, and visual review gates pass.

