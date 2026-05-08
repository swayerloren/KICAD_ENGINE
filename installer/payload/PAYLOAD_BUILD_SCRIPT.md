# Payload Build Script

Status: active build process for `installer/payload/repo-template`.

## Purpose

`build_payload.py` creates the clean workspace template copied by a future installer. It is intentionally stricter than a normal repo copy: it uses allowlists, exclusion rules, generated scaffold files, path sanitization, secret scanning, size limits, and a manifest.

## Commands

From the repo root on Windows:

```powershell
.\installer\payload\build_payload.ps1
```

Cross-platform:

```bash
python installer/payload/build_payload.py
```

Optional arguments:

```bash
python installer/payload/build_payload.py --source-root . --payload-root installer/payload --max-file-size-mb 5
```

Use `--no-clean` only for debugging. Normal builds should clean and recreate `repo-template` to avoid stale development files.

## Outputs

The build creates:

- `installer/payload/repo-template/`
- `installer/payload/payload.manifest.json`
- `installer/payload/PAYLOAD_BUILD_REPORT.md`

## Safety Behavior

The script:

- Copies only approved root files and folders.
- Includes public end-user docs under `docs/` and the root user guides.
- Generates clean state files for memory, history, active project, Codex config examples, Claude scaffolding, outputs, and project folders.
- Excludes backups, logs, generated outputs, third-party repos, Python/Node environments, PDFs, archives, binaries, and KiCad project files outside approved templates.
- Excludes files over the configured maximum size.
- Excludes likely secrets and fails if a blocking secret pattern remains in the payload.
- Replaces developer-specific local paths with placeholders in copied text files.
- Does not delete source files.
- Cleans only `installer/payload/repo-template` after verifying it is under the payload folder.

## Required Verification

After every build:

```powershell
python health_check.py --repo-root installer/payload/repo-template --no-write
rg -n "C:\\Users\\LJ|C:/Users/LJ|COMMAND_LINK|COMMAND LINK|ESP32_CSI_WIFI_NODE" installer/payload/repo-template
```

The health check should pass or explain missing optional local tools. The search should not find private developer paths or private project names in the template.
