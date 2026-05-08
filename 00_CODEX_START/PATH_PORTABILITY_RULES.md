# Path Portability Rules

The absolute paths in this file are historical/local examples used only to explain how older records should be interpreted. For normal repo work, prefer repo-relative paths.

Status: `ACTIVE_P0_STARTUP_RULE`

Current workspace path for this checkout should be treated as:

`<LOCAL_CHECKOUT>\KICAD_ENGINE`

Historical paths that may still appear in old logs or copied examples include maintainer-machine paths such as:

- `C:\Users\LJ\GitHub\KICAD_ENGINE`
- `C:\Users\LJ\KICAD_ENGINE`

## Agent Rules

- Treat repo-relative paths as authoritative whenever possible.
- Treat old absolute paths as historical unless the file explicitly says they are current.
- Do not use an old absolute path for file edits, script writes, backups, project selection, or payload generation.
- Before editing any file, resolve it under the current workspace root.
- If a task references an old maintainer-machine path, translate it to the current local checkout only after confirming the target exists in this checkout.
- Do not rewrite old command logs merely to normalize paths; preserve historical evidence.
- Public-facing docs and startup files should use repo-relative paths or the current workspace path, not stale local absolute paths.

## Current Active Project Path

The current active project path should be written portably as:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Release Rule

Installer payloads and public release archives must not contain developer-specific absolute paths unless they are clearly marked as examples.
