# License Screening Rules

Status: `MANDATORY_BEFORE_IMPORT_OR_PUBLIC_BUNDLE`

## Purpose

Prevent KiCad Engine from copying, publishing, or benchmarking projects whose license, attribution, or redistribution status is unclear.

## License Statuses

| Status | Meaning | Public Bundle |
| --- | --- | --- |
| `PUBLIC_BUNDLE_ALLOWED` | License is present and appears compatible with redistribution, with attribution preserved. | Allowed after review. |
| `LINK_ONLY_ALLOWED` | Link and summary are acceptable, but local bundling is not approved. | Not allowed. |
| `NEEDS_HUMAN_LICENSE_REVIEW` | License exists but compatibility or scope is unclear. | Not allowed. |
| `NO_LICENSE_FOUND` | No license was found. | Not allowed. |
| `PROPRIETARY_OR_RESTRICTED` | License prohibits copying or redistribution. | Not allowed. |
| `THIRD_PARTY_CONTENT_RISK` | Project may contain bundled PDFs, CAD models, images, or libraries with separate terms. | Not allowed until resolved. |

## Screening Is Not Legal Advice

Script output is practical risk screening only. A human must review public-bundle decisions and any unclear license.

## Required Checks

- License file exists or source page states a license.
- License covers hardware design files, not only firmware/software.
- Attribution requirements are captured.
- Third-party libraries/assets/documents are identified.
- Vendor datasheets and CAD files are not bundled unless redistribution rights are confirmed.
- Public-release exclusion status is recorded.

## Default Rule

If license status is not clearly `PUBLIC_BUNDLE_ALLOWED`, keep the sample link-only or local-private and exclude it from release payloads.
