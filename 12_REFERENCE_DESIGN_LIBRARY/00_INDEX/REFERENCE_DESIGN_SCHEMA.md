# Reference Design Schema

Use this schema for every reference design record.

## Required Fields

- `design_name`
- `source_url`
- `license`
- `vendor_or_project_owner`
- `category`
- `design_format`
- `components_used`
- `circuit_blocks`
- `what_can_be_learned`
- `what_must_not_be_copied`
- `verification_level`
- `known_issues`
- `human_review_needed`

## Recommended Fields

- `source_type`: official vendor, open hardware, community project, app note, board schematic, evaluation board, unknown.
- `local_files_copied`: yes/no.
- `local_path`: path if files are copied with permission.
- `redistribution_status`: allowed, link-only, unknown, restricted.
- `source_revision_or_date`
- `license_url`
- `attribution_required`
- `compatible_with_public_repo`: yes/no/requires review.
- `related_datasheet_records`
- `related_component_records`
- `related_knowledge_base_patterns`
- `related_accuracy_rules`
- `reviewer`
- `review_date`

## Verification Rule

Every record must use one of these verification levels:

- `VERIFIED`: Source URL, owner, license/redistribution status, format, source date or revision when available, and extracted lesson have been checked against the cited source.
- `PARTIALLY_VERIFIED`: Some facts were checked, but source revision, license, component identity, transferability, or circuit detail still requires review.
- `LINK_ONLY`: A public source link and summary are stored; no local proprietary files are copied.
- `UNVERIFIED`: Placeholder or candidate reference. Do not use as design evidence.

If source URL, license, format, component identity, or source revision is unknown, the record remains `UNVERIFIED` or `LINK_ONLY` and must include `human_review_needed`.

A reference design never proves that a new schematic, footprint, connector orientation, layout, or fab package is correct. It can only provide review evidence that must be checked against the active project's exact sources.

## File Policy

Reference records should be Markdown by default. JSON can be added later for automation, but Markdown is easier for AI agents and human reviewers to read.
