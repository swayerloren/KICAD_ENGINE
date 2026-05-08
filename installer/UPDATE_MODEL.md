# Update Model

Status: planning only.

## Update Goals

Updates should improve the repo template and tooling without damaging user work.

Preserve:

- `04_KICAD_PROJECTS/`
- `01_MEMORY/`
- `02_HISTORY/`
- `05_OUTPUTS/`
- `06_DATASHEETS/` user-added files.
- `08_COMPONENT_DATABASE/` user-added verified records.
- `99_BACKUPS/`
- User-local AI tool configuration.

## Update Types

### Template Update

Updates startup docs, prompt packs, setup scripts, health checks, VS Code tasks, schemas, and examples.

### Tooling Update

Updates repo-owned scripts. Must not update third-party package managers or external repos without user approval.

### Knowledge Update

Adds or updates metadata, summaries, source lists, and verified component records.

### Installer Update

Updates installer wrapper logic and release metadata.

## Update Flow

1. Detect existing workspace.
2. Read installed workspace version.
3. Show diff summary by category.
4. Back up files that will be overwritten.
5. Preserve user project, memory, history, outputs, datasheets, component records, and backups.
6. Apply repo-template updates.
7. Run health check.
8. Write update report.

## Conflict Handling

When a repo-owned file changed locally:

- Do not overwrite silently.
- Create a backup.
- Write conflict report.
- Prefer side-by-side `.new` output when automated merge is unsafe.

## Rollback

Rollback should restore overwritten repo-controlled files from the update backup.

Rollback must not delete user-created projects, outputs, backups, datasheets, or component records.

## Version Files

Future installer should add:

- `VERSION`
- `installer/INSTALLER_VERSION`
- `installer/PAYLOAD_VERSION.json`

Do not add these until a release versioning decision is made.
