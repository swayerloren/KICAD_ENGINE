# Installer Workspace

## PURPOSE

Hold production-facing installer coordination docs and release-ready installer handoff material.

## WHAT_BELONGS_HERE

- Installer release plans.
- Installer payload routing notes.
- Cross-platform installer checklists.
- Links to implementation under `installer/`.

## Production Planning Files

- `INSTALLER_ARCHITECTURE.md`
- `WINDOWS_INSTALLER_PLAN.md`
- `MACOS_INSTALLER_PLAN.md`
- `LINUX_INSTALLER_PLAN.md`
- `PAYLOAD_MANIFEST.md`
- `SECURITY_MODEL.md`
- `UPDATE_MODEL.md`
- `USER_FLOW.md`

## WHAT_DOES_NOT_BELONG_HERE

- Built binaries unless intentionally staged and documented.
- Node dependencies or package-manager caches.
- Secrets, signing keys, or certificates.
- KiCad installers or bundled KiCad application files.

## AI_AGENT_RULES

- Do not claim installer production readiness without build and smoke-test evidence.
- Do not store credentials or signing material.
- Preserve `installer/` as the implementation source unless migration is explicitly approved.

## SAFE_EDIT_RULES

- Add docs and manifests only.
- Do not delete installer build artifacts from other folders.
- Do not modify system KiCad installation paths.

## PUBLIC_RELEASE_NOTES

Public installer release requires checksums, signing/notarization status where applicable, and platform smoke-test notes.

No binaries are staged here by default.
