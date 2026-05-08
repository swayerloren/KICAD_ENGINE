# Installer Update Model

Status: `PLANNED`

## Initial Model

KiCad Engine v1 should prefer manual updates through GitHub releases or git pull. Auto-update should not be enabled until update signing, rollback, and user confirmation are designed and tested.

## Update Rules

- Do not auto-update without user approval.
- Do not overwrite user projects, memory, history, datasheets, component records, or local prompt changes.
- Keep update logs.
- Preserve backups when replacing template files.
- Never update KiCad itself silently.

## Future Options

- In-app release notification.
- Download verified payload updates.
- Check SHA256 before applying.
- Offer dry-run update plan.
- Support backup and rollback.

## Blockers Before Auto-Update

- Signed update metadata.
- Rollback plan.
- Merge strategy for user-edited workspace files.
- Security review.
- Cross-platform test coverage.

