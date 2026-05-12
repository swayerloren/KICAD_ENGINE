# License And Attribution Rules

This folder is not legal advice. It is the practical operating policy for
third-party KiCad-adjacent tools used by KiCad Engine.

## Required Metadata Per Tool

Every tool profile must record:

- tool name
- upstream source URL
- observed license
- install method
- distribution mode
- whether bundling is allowed
- whether CI use is acceptable

## Bundling Rule

Do not assume that an upstream tool may be bundled just because it is open
source.

Before bundling any third-party code or binary, confirm:

- the license is identified
- redistribution terms are acceptable
- nested notices are preserved where needed
- the size and maintenance cost are acceptable
- the public ZIP payload remains intentional

## Special Attention Areas

- `AGPL-3.0` and `GPL-*` tools require deliberate redistribution review.
- Official KiCad tools may have acceptable source licenses but still depend on
  a separately installed KiCad runtime.
- Plugin-style tools may generate derivative HTML, Gerber, or BOM artifacts that
  still need review before publication.

## Repo Policy

- First-party wrapper scripts may be tracked.
- Upstream clones, jars, app bundles, and install trees are excluded by default.
- Root `THIRD_PARTY_TOOLS_ATTRIBUTION.md` and
  `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md` must stay aligned with this layer.
