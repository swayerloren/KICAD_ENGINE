# Path Portability Rules

Status: `ACTIVE_P0_STARTUP_RULE`

Historical reports, generated evidence, and old local audits may still contain maintainer-machine paths. Those records are preserved as evidence. They are not current setup truth.

Use the current checkout portably as:

`<LOCAL_CHECKOUT>\KICAD_ENGINE`

Historical maintainer-machine checkout examples that may still appear in preserved evidence:

- `C:\Users\LJ\GitHub\KICAD_ENGINE`
- `C:\Users\LJ\KICAD_ENGINE`

Common KiCad install roots may also appear in docs and scripts such as:

- `C:\Program Files\KiCad\9.0`
- `C:\Program Files\KiCad\8.0`
- `C:\Program Files\KiCad\7.0`

Treat those install roots as common discovery examples only, not guaranteed current-machine truth.

## Portable Source Of Truth

For current-machine setup truth, use:

- `README.md`
- `ONE_PROMPT_START.md`
- `TOOLS_INDEX.md`
- `03_TOOLS/TOOLS_INDEX.md`
- `EXTERNAL_DEPENDENCIES.md`
- `LOCAL_SETUP_REQUIREMENTS.md`
- `docs/PATH_PORTABILITY.md`
- `docs/HEALTH_CHECK.md`
- `python health_check.py --no-write`
- `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`

## Finding Classes

- `ACTIVE_ONBOARDING_DOC`: current startup and onboarding docs that must be portable.
- `ACTIVE_SCRIPT`: live scripts/config that must use repo-relative paths, overrides, or discovery.
- `ACTIVE_CONFIG`: live non-onboarding docs that may mention common install roots but must not require one machine's checkout path.
- `HISTORICAL_REPORT`: preserved evidence, logs, reviews, and generated verification records. These may contain original machine paths and should not be rewritten blindly.
- `GENERATED_INDEX`: generated inventories or indexes that may include local-machine evidence. Treat as machine-specific unless the file explicitly says otherwise.
- `EXAMPLE_ONLY`: worked examples that may show sample absolute paths only as examples.

## Agent Rules

- Treat repo-relative paths as authoritative whenever possible.
- Treat old absolute checkout paths as historical unless a current file explicitly marks them as active.
- Do not use a historical absolute path for file edits, script writes, backups, project selection, or payload generation.
- Before editing any file, resolve it under the current workspace root.
- If a task references an old maintainer-machine path, translate it to the current checkout only after confirming the target exists there.
- Do not rewrite old command logs, review packets, or archived reports merely to normalize paths; preserve evidence integrity.
- Historical reports, project review artifacts, `_verification` outputs, sample-intake review packets, and command transcripts are evidence records. Do not treat their absolute paths as current configuration.
- Generated indexes and generated inventories may reflect one machine at one point in time. Use live discovery before trusting them for current work.
- Public-facing docs, startup files, and prompt files should use repo-relative paths or clearly marked example paths.
- Scripts must not assume `C:\Users\LJ`. They should accept explicit paths, use repo-root discovery, or probe the current machine safely.

## Current Active Project Path

The current active project path should be written portably as:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Release Rule

Installer payloads and public release archives must not contain developer-specific absolute paths unless they are clearly marked as examples or intentionally preserved evidence.
