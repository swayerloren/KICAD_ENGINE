# Release Workflow Plan

Status: `DRAFT_RELEASE_ONLY`

## Flow

1. Trigger workflow manually or on release candidate tag.
2. Run health and secret checks.
3. Build payload.
4. Build platform artifacts.
5. Generate checksums.
6. Upload artifacts.
7. Create draft release notes.
8. Wait for human review.

## Publishing Rule

Do not publish automatically. A human maintainer must review and publish.

## Release Notes Must Include

- Version.
- Artifact names.
- SHA256 checksums.
- Platform test status.
- Signing/notarization status.
- Known limitations.
- AI/fabrication disclaimer.

