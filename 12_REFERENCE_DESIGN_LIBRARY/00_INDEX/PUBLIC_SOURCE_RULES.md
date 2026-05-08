# Public Source Rules

## Preferred Sources

Prefer:

- Official vendor evaluation board schematics and layout notes.
- Vendor hardware design guides.
- Vendor reference designs.
- Open hardware projects with clear licenses.
- Board-house application notes when relevant.

## Link-Only Default

For public GitHub release, store links, summaries, and metadata by default.

Do not copy files unless:

- License is compatible.
- Redistribution is allowed.
- Attribution is recorded.
- File size and public-release policy are acceptable.
- Human review confirms the source is safe to include.

## Verification Status Rule

Every reference item must be marked with one of these statuses:

- `VERIFIED`: Source, owner, license/redistribution status, and the specific lesson have been checked.
- `PARTIALLY_VERIFIED`: Useful source exists, but some source, license, revision, or transferability details remain open.
- `LINK_ONLY`: Public link and summary only; no local copied design files.
- `UNVERIFIED`: Placeholder or candidate source that must not be treated as design evidence.

Agents must not promote a reference design above `LINK_ONLY` based only on search results or memory.

## Prohibited Without Permission

Do not copy:

- Proprietary board designs.
- Vendor files with unclear redistribution rights.
- Paid course/project files.
- Customer project files.
- Forum attachments with unclear ownership.
- Designs that include confidential markings.

## Agent Citation Rule

When using a reference design as evidence, cite:

- Source URL.
- Owner/vendor.
- License or redistribution status.
- What specific lesson is being used.
- What still requires verification in the active design.

## No Blind Copy Rule

Reference designs may inspire review questions and patterns. They must not be copied into an active KiCad project without exact source, license, component, footprint, and human review.
