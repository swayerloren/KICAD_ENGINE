# Installer Architecture

Status: implemented as first Electron installer project; packaged binaries are not production-ready until build and smoke tests pass.

## Architecture Summary

The future installer should be a thin bootstrapper around a transparent local repo payload.

It should:

1. Present the install plan before changing anything.
2. Ask for the installation folder.
3. Create or update the `KICAD_ENGINE` workspace.
4. Run requirement checks.
5. Offer optional installs through official package managers.
6. Configure VS Code workspace files from the repo payload.
7. Create datasheet and component database scaffolding.
8. Run `health_check`.
9. Open VS Code.

## Control Model

The installer should use the existing setup scripts as the implementation substrate:

- `setup/common/create_repo_folders.py`
- `setup/common/build_indexes.py`
- `setup/common/write_setup_report.py`
- `setup/windows/setup_windows.ps1`
- `setup/macos/setup_macos.sh`
- `setup/linux/setup_linux.sh`
- `health_check.py`
- `health_check.ps1`

The installer GUI or packaged wrapper should not duplicate business logic that already exists in scripts. It should orchestrate those scripts and display logs.

## Payload Layout

The packaged payload is generated from `installer/payload/build_payload.py` into `installer/payload/repo-template`.

The packaged payload should contain:

- Startup docs.
- Prompt packs.
- VS Code workspace files.
- Setup scripts.
- Health checks.
- Datasheet scaffolding and source-list metadata.
- Component database scaffolding and placeholders.
- KiCad app intelligence docs and read-only scripts.
- License and release notes.

The payload should not contain:

- KiCad application binaries.
- Restricted datasheet PDFs unless redistribution is confirmed.
- AI credentials or API keys.
- User project backups.
- Generated final fabrication outputs.

Payload generation also creates:

- `installer/payload/payload.manifest.json`
- `installer/payload/PAYLOAD_BUILD_REPORT.md`

The manifest records relative template paths, sizes, SHA-256 hashes, generated clean files, and exclusion summary. It does not record developer-specific absolute source paths.

## Installer Modes

### Check Only

Runs requirement and health checks without writing repo files except optional reports.

### Install Workspace

Creates a new workspace folder and copies the repo payload.

### Repair Workspace

Checks an existing workspace and offers to restore missing repo scaffolding. Must not overwrite user project files without explicit confirmation and backup.

### Update Workspace

Updates versioned repo template files while preserving user projects, memory, history, datasheet additions, component additions, outputs, and backups.

## Execution Order

1. Verify installer signature when available.
2. Ask user for install location.
3. Refuse unsafe paths such as installed KiCad folders.
4. Show payload manifest and changes.
5. Create workspace folder.
6. Copy `installer/payload/repo-template`.
7. Run platform requirement check.
8. Offer optional installs.
9. Run common setup helpers.
10. Run health check.
11. Write setup report.
12. Open VS Code if available.

## Logging

Installer logs should be written under:

- `05_OUTPUTS/setup_reports`
- `05_OUTPUTS/health_checks`

Logs must not include secrets, tokens, or private credentials.

## Failure Behavior

Failures should be recoverable:

- Show the failed command.
- Keep partial reports.
- Avoid rollback that deletes user-created files.
- Offer manual next steps.
- Never leave hidden background services running.

## Versioned Milestones

### v0.1 Repo Template

Create the repo skeleton, startup docs, memory/history rules, safe output folders, and baseline README.

### v0.2 Windows Setup Scripts

Create Windows setup, requirement check, and opt-in install scripts. Confirm the scripts ask before installs and do not modify KiCad project files.

### v0.3 KiCad App Audit

Create read-only installed KiCad audit scripts and path intelligence for Windows KiCad 9 first.

### v0.4 Datasheet/Component Database

Create professional datasheet scaffolding, source policies, metadata schemas, component database structure, and placeholder records.

### v0.5 VS Code Prompt Packs

Create `.vscode` workspace support, Codex prompts, Claude prompts, shared standards, and quickstart docs.

### v0.6 Windows Installer

Build the first real installer artifact for Windows. It should create the workspace, check KiCad, optionally install requirements with confirmation, run health check, and open VS Code.

### v0.7 macOS/Linux Setup

Validate macOS and Linux setup scripts, package-manager detection, health checks, and CLI-oriented workflows.

### v1.0 Public GitHub Release

Publish a public-ready repo and installer release with license, release notes, signing/checksum policy, clean payload, public docs, and a demonstrated sample workflow.
