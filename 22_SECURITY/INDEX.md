# Security Index

Status: `SCAFFOLD`

## Related Existing Docs

- `SECURITY.md`
- `installer/docs/INSTALLER_SECURITY_MODEL.md`
- `PUBLIC_RELEASE_CHECKLIST.md`


## PURPOSE

Store security model, secret-handling rules, installer safety notes, and vulnerability-response material.

## WHAT_BELONGS_HERE

Defensive security docs, secret-scan guidance, report-handling rules, and installer safety constraints.

## WHAT_DOES_NOT_BELONG_HERE

Secrets, tokens, private keys, exploit payloads, or silent credential collection.

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