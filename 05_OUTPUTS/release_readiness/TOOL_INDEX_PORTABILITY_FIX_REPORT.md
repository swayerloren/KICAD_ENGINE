# Tool Index Portability Fix Report

Date: `2026-05-09`
Task type: `DOCS_ONLY`

## Decision

Keep `00_CODEX_START/TOOL_INDEX.md`, but explicitly mark it as machine-specific local inventory instead of portable tool truth.

Reason:

- `AGENTS.md` and startup docs already reference `00_CODEX_START/TOOL_INDEX.md`
- the file still has value as a local audited inventory record
- moving it would break or weaken the current startup flow
- the portability problem was not the file's existence; it was the lack of a strong warning and portable redirects

## Changes Applied

### `00_CODEX_START/TOOL_INDEX.md`

- added a top-of-file warning block:
  - `WARNING: MACHINE-SPECIFIC INVENTORY`
  - `This file may reflect the original maintainer's local machine.`
  - `Do not use it as portable truth.`
- added explicit command guidance to run:
  - `python health_check.py --no-write`
  - `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`
  - `python 03_TOOLS/scripts/python_env_check.py`
- added portable links to:
  - `README.md`
  - `ONE_PROMPT_START.md`
  - `TOOLS_INDEX.md`
  - `03_TOOLS/TOOLS_INDEX.md`
  - `EXTERNAL_DEPENDENCIES.md`
  - `LOCAL_SETUP_REQUIREMENTS.md`
  - `docs/HEALTH_CHECK.md`
- rewrote the portability note so absolute paths, versions, venv locations, clone locations, and local config paths are clearly inventory-only

### Portable Tool Truth Docs

Updated to explicitly say portable tool truth lives in the repo-facing indexes and health-check path:

- `TOOLS_INDEX.md`
- `03_TOOLS/TOOLS_INDEX.md`
- `00_CODEX_START/START_HERE.md`
- `README.md`
- `ONE_PROMPT_START.md`

## Validation

- `TOOL_INDEX.md` now begins with a machine-specific warning block
- startup prompt text now tells Codex/Claude to use portable repo docs and live discovery scripts as tool truth
- starter docs now point to `health_check.py`, `03_TOOLS/TOOLS_INDEX.md`, `EXTERNAL_DEPENDENCIES.md`, and `docs/HEALTH_CHECK.md`
- no KiCad design files were edited

## Portable Tool Truth Files

- root `TOOLS_INDEX.md`
- `03_TOOLS/TOOLS_INDEX.md`
- `EXTERNAL_DEPENDENCIES.md`
- `LOCAL_SETUP_REQUIREMENTS.md`
- `docs/HEALTH_CHECK.md`
- `health_check.py`
- `03_TOOLS/scripts/kicad_discovery/find_kicad.py`
- `03_TOOLS/scripts/python_env_check.py`

## Expected Result

Future Codex/Claude sessions should still be allowed to read `00_CODEX_START/TOOL_INDEX.md`, but they should no longer mistake it for portable setup truth. The portable startup path now directs them to the repo-facing tool indexes plus live health-check and discovery results first.
