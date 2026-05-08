# Installer Workspace Index

Status: `SCAFFOLD`

## Related Existing Implementation

- `installer/`: current Electron installer source and payload tooling.
- `setup/`: platform setup scripts.

## Next Steps

- Decide whether future installer source remains in `installer/` or migrates into `16_INSTALLER/`.
- Keep public release notes explicit about unsigned/untested builds.


## PURPOSE

Coordinate installer packaging, payload, and release-facing installer status while current source remains in installer/.

## WHAT_BELONGS_HERE

Installer coordination docs, build notes, payload routing notes, and release status summaries.

## WHAT_DOES_NOT_BELONG_HERE

Private signing keys, credentials, silent install scripts, or duplicated Electron source unless migration is approved.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to 2_HISTORY/, 5_OUTPUTS/, or project history/ unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.