# Failed Attempt - Compile Scope Too Broad For Dev Infra CI

- Date: `2026-05-08`
- Task: GitHub dev infrastructure setup

## What Failed

The first local Python compile validation used a broad recursive scope over `03_TOOLS` and `14_LAYOUT_AUTOMATION`.

## Root Cause

That scope pulled in vendored repositories, embedded environments, and legacy Python-2 files under third-party tool bundles, which are not appropriate gates for first-party repo CI.

## Resolution

- narrowed compile validation to tracked first-party Python files
- excluded `03_TOOLS/python_envs/`, `03_TOOLS/node_envs/`, `03_TOOLS/repos/`, `03_TOOLS/windows/repos/`, and `03_TOOLS/linux/repos/`
- updated `.github/workflows/ci.yml` to use the narrowed tracked-file compile path
