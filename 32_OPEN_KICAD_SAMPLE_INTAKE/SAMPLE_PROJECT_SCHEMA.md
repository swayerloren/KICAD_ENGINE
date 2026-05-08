# Sample Project Schema

Status: `ACTIVE_SCHEMA`

## Required Fields

| Field | Required | Notes |
| --- | --- | --- |
| `sample_id` | Yes | Stable slug, uppercase/lowercase safe, no spaces. |
| `project_name` | Yes | Human-readable source project name. |
| `source_url` | Yes | Canonical source URL. |
| `source_host` | Yes | GitHub, GitLab, official vendor, user-local, etc. |
| `source_owner` | Desired | Author, org, or vendor. |
| `license_name` | Yes | Exact license if known; otherwise `UNKNOWN`. |
| `license_status` | Yes | Use `LICENSE_SCREENING_RULES.md` statuses. |
| `attribution_required` | Yes | `true`, `false`, or `UNKNOWN`. |
| `attribution_text` | Desired | Preserve required credit. |
| `kicad_files_present` | Yes | Record `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` counts. |
| `import_status` | Yes | Candidate/import/review/promotion status. |
| `original_path` | If imported | Path under `imported_originals/`. |
| `normalized_path` | If normalized | Path under `normalized_samples/`. |
| `review_report_path` | If reviewed | Path under `review_reports/`. |
| `public_bundle_status` | Yes | `EXCLUDED_BY_DEFAULT`, `PUBLIC_BUNDLE_ALLOWED`, or blocked status. |
| `benchmark_candidate_status` | Yes | `NOT_CANDIDATE`, `CANDIDATE`, `NEEDS_REVIEW`, or `PROMOTED`. |
| `human_review_required` | Yes | Default `true`. |

## JSON Status Example

```json
{
  "sample_id": "example_open_kicad_project",
  "project_name": "Example Open KiCad Project",
  "source_url": "https://example.invalid/project",
  "license_status": "NEEDS_HUMAN_LICENSE_REVIEW",
  "kicad_files_present": {
    "kicad_pro": 0,
    "kicad_sch": 0,
    "kicad_pcb": 0
  },
  "import_status": "CANDIDATE_LINK_ONLY",
  "public_bundle_status": "EXCLUDED_BY_DEFAULT",
  "human_review_required": true
}
```

## Promotion Rule

No sample may move beyond `CANDIDATE_LINK_ONLY` unless this schema has enough information to preserve source, license, attribution, and review evidence.
