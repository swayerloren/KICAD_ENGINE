# Sample License Rules

Status: `ACTIVE_LICENSE_GATE`

## Purpose

Keep open-source sample learning material separated from unclear-license or
restricted content.

## Required Checks

1. Record the exact source URL.
2. Preserve the upstream owner/project name.
3. Look for a license file in the local sample copy.
4. Record whether the license appears to cover the KiCad project files.
5. Record whether public bundling is allowed, blocked, or still needs human
   review.

## Allowed Statuses

- `PUBLIC_BUNDLE_ALLOWED`
- `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`
- `EXCLUDED_BY_DEFAULT`
- `NEEDS_HUMAN_LICENSE_REVIEW`
- `PROPRIETARY_OR_RESTRICTED`
- `NO_LICENSE_FOUND`

## Hard Rules

- No sample with `PROPRIETARY_OR_RESTRICTED` status may enter a public payload.
- `NO_LICENSE_FOUND` blocks public bundling.
- `NEEDS_HUMAN_LICENSE_REVIEW` blocks public bundling.
- Attribution must be preserved even when the sample stays internal-only.
- License name similarity alone is not enough; keep the evidence path.

## Public Bundle Safety

If a sample is not clearly approved for public bundling, keep:

- link records
- attribution notes
- review summaries

out of the public payload unless a separate human release review approves the
exact files.
