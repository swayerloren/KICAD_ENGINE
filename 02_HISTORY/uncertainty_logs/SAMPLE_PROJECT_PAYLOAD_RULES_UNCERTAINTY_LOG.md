# Uncertainty Log - Sample Project Payload Rules

Date: `2026-05-06`

## Uncertainties

| Item | Status | Required Resolution |
| --- | --- | --- |
| Whether ATtiny85 sample KiCad source files can be bundled publicly | `UNVERIFIED_PENDING_HUMAN_REVIEW` | Human release/license review must change status to `PUBLIC_BUNDLE_ALLOWED`. |
| Whether `ORIGINAL_UPSTREAM_README.md` should be bundled | `NEEDS_HUMAN_LICENSE_REVIEW` | Confirm upstream README redistribution under MIT source context. |
| Public payload builder behavior | `MISSING` | Create and test `17_RELEASE_BUILD/build_public_payload.py` with dry-run default. |
| Existing installer payload builder suitability for public sample payload | `NOT_VERIFIED` | It is not release-specific and lacks dry-run; do not use it as public sample builder yet. |

## Safety Action

Defaulted uncertain sample source files to excluded.
