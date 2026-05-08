# Payload Manifest

Status: implemented as generated payload scaffold plus manifest.

This document defines what the installer payload should include and exclude. The actual generated payload lives under `installer/payload/repo-template`, with machine-readable manifest `installer/payload/payload.manifest.json`.

## Include

Core repo docs:

- `README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `AGENTS.md`
- `START_HERE_FOR_USERS.md`
- `START_HERE_FOR_AI_AGENTS.md`
- `QUICKSTART_WINDOWS.md`
- `QUICKSTART_MACOS.md`
- `QUICKSTART_LINUX.md`

Startup and agent workflow:

- `00_CODEX_START/`
- `.prompts/`
- `.vscode/`
- `.codex/` with safe examples only.
- `.claude/` scaffold.

Setup and health checks:

- `setup/`
- `health_check.py`
- `health_check.ps1`
- `HEALTH_CHECK_REPORT_TEMPLATE.md`

Tool scripts and docs:

- `03_TOOLS/scripts/`
- `03_TOOLS/kicad_app_intelligence/`
- `03_TOOLS/kicad_library_intelligence/`
- `03_TOOLS/common/`
- `03_TOOLS/windows/` docs and safe scripts only
- `03_TOOLS/linux/` docs and safe scripts only

Knowledge scaffolding:

- `06_DATASHEETS/` scaffolding, indexes, source lists, and permitted metadata.
- `08_COMPONENT_DATABASE/` schemas, placeholders, indexes, and verified metadata where permitted.

Memory/history templates:

- Required index files.
- Public-safe setup history and design review examples if sanitized.

## Exclude

- KiCad application binaries.
- Restricted datasheet PDFs unless redistribution is explicitly permitted.
- User KiCad projects unless they are intentional public examples.
- User backups.
- Generated manufacturing outputs.
- Private command logs.
- API keys, tokens, credentials, license keys, SSH keys, and `.env` files.
- Third-party cloned repos unless license and payload size are explicitly reviewed.
- Python and Node virtual environments.
- Build caches and `__pycache__`.

The implemented builder also excludes:

- `03_TOOLS/repos/`
- `03_TOOLS/windows/repos/`
- `03_TOOLS/python_envs/`
- `03_TOOLS/node_envs/`
- `03_TOOLS/tool_logs/`
- `03_TOOLS/windows/logs/`
- `03_TOOLS/linux/logs/`
- generated KiCad library indexes
- legacy migrated datasheet inbox content
- `.codex/config.toml`

## Build Command

From the repo root:

```powershell
.\installer\payload\build_payload.ps1
```

Cross-platform:

```bash
python installer/payload/build_payload.py
```

## Generated On Install

The installer should generate these locally:

- `05_OUTPUTS/setup_reports/*`
- `05_OUTPUTS/health_checks/*`
- `05_OUTPUTS/setup_indexes/*`
- Missing folder scaffolding through `setup/common/create_repo_folders.py`

## Version Metadata

Every payload should include:

- Installer version.
- Repo template version.
- Build date.
- Git commit or source archive checksum when available.
- Payload manifest checksum.

## Public Release Gate

Before packaging, verify:

- No secrets.
- No restricted datasheet PDFs.
- No final fabrication outputs.
- No machine-local absolute paths in public docs unless explicitly marked as examples.
- License files are present.
- Health check passes on a clean extracted payload.

Current clean-payload validation command:

```powershell
python health_check.py --repo-root installer\payload\repo-template --no-write
```
