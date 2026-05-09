# KiCad Python Context

KiCad Engine supports two different Python realities:

1. the normal repo/runtime Python used for docs, audits, health checks, task-contract validation, and many helper scripts
2. the KiCad-compatible Python context needed for some `pcbnew` workflows

These are not always the same interpreter.

## The Portability Problem

On Windows, KiCad often bundles its own Python runtime. For example, KiCad 9 may ship `python311.dll` and a local `python.exe`, while the user's normal Python is `3.12`.

In that situation:

- `python health_check.py --no-write` can still work
- `kicad-cli` can still work
- `pcbnew` may fail to import in normal Python
- board-aware scripts should switch to KiCad's own Python context

Typical failure:

```text
ImportError: Module use of python311.dll conflicts with this version of Python.
```

## What To Run

```powershell
python health_check.py --no-write
python 03_TOOLS/scripts/kicad_api/kicad_python_context.py
python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py
```

## What The Results Mean

- `PASS`
  - `pcbnew` imports in the current Python interpreter
- `WARN`
  - the current Python interpreter cannot import `pcbnew`, but KiCad-compatible Python was found and board-aware scripts can re-enter through it
- `FAIL`
  - no workable `pcbnew` context was found

## When You Actually Need pcbnew

You usually do **not** need `pcbnew` for:

- ZIP onboarding
- repo docs
- rule and checklist review
- portability audits
- task-contract validation
- many health checks
- many `kicad-cli` driven checks

You **do** need `pcbnew` for some board-aware automation such as:

- reading board geometry through the KiCad Python API
- extracting placement/routing structures that depend on KiCad objects
- running scripts that intentionally operate on `.kicad_pcb` objects

## Agent Rule

Codex or Claude should not assume `pcbnew` works in the repo's base Python interpreter.

The agent should:

1. use repo-relative paths
2. run the health check
3. detect KiCad and `pcbnew` status on the current machine
4. prefer `kicad-cli` when it can answer the task
5. switch to KiCad-compatible Python only when a real `pcbnew` workflow is required

## CI And Codespaces

GitHub Actions and Codespaces must not require KiCad GUI or `pcbnew`.

They may run:

- health checks
- Python compile checks
- docs checks
- routing-geometry fixture tests
- task-contract validation

They should treat missing `pcbnew` as non-blocking unless a job explicitly targets a board-aware `pcbnew` workflow.
