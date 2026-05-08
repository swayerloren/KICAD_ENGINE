# Release Build Plan

Status: `PLANNED_NOT_BUILT`

## Purpose

Define how KiCad Engine release artifacts should be built, checked, named, and staged.

## Release Inputs

- Clean source tree.
- Reviewed payload manifest.
- Passing health check.
- Secret scan.
- License/attribution audit.
- Public docs review.
- Installer build plan or platform build results.

## Build Order

1. Run secret scan.
2. Run health check.
3. Build payload.
4. Run payload dry-run install.
5. Build platform installers on native runners.
6. Generate checksums.
7. Upload artifacts for human review.
8. Draft release notes.

## Public Release Gate

Do not publish automatically. Draft releases require human review before publication.

