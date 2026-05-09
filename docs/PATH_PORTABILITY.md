# Path Portability

This repo is meant to work from a normal GitHub ZIP extraction or `git clone` without requiring the original maintainer's local paths.

## Core Rule

Use repo-relative paths and live discovery on the current machine.

Do not treat old absolute paths in reports, logs, or generated evidence as current setup truth.

## What You May See

Historical records may still contain paths such as:

- `C:\Users\LJ\GitHub\KICAD_ENGINE`
- `C:\Users\LJ\KICAD_ENGINE`
- `C:\Program Files\KiCad\9.0`
- `%APPDATA%\kicad\9.0`

Those entries are usually one of these:

- historical command output
- archived review evidence
- generated verification artifacts
- machine-specific tool inventory
- example-only documentation

They are preserved so prior work remains auditable. They are not instructions for a new ZIP user.

## What To Use Instead

For current work, use:

- repo-relative paths from the current checkout
- `python health_check.py --no-write`
- `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`
- `python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`
- `TOOLS_INDEX.md`
- `03_TOOLS/TOOLS_INDEX.md`
- `EXTERNAL_DEPENDENCIES.md`
- `LOCAL_SETUP_REQUIREMENTS.md`

## For AI Agents

- Read `00_CODEX_START/PATH_PORTABILITY_RULES.md` during startup.
- Treat `00_CODEX_START/TOOL_INDEX.md` as machine-specific inventory only.
- Treat historical reports and generated review packets as evidence, not setup truth.
- Do not copy `C:\Users\LJ` paths into new commands, docs, scripts, or fixes.
- If KiCad is needed, detect it on the current machine instead of assuming one exact install path.

## For Script Authors

- Accept explicit path overrides when practical.
- Resolve the repo root dynamically.
- Prefer `PATH`, environment variables, and common install-root discovery before falling back to examples in docs.
- Do not require `03_TOOLS/python_envs`, `03_TOOLS/node_envs`, or other private local-only folders to exist.

## Historical Evidence Policy

Historical reports stay as-written unless they are being republished as current instructions.

That means:

- command logs are preserved
- review reports are preserved
- archived sample-intake artifacts are preserved
- old absolute paths remain visible inside those records

The portability fix is to label them correctly and keep current startup/setup docs portable, not to rewrite the archive blindly.
