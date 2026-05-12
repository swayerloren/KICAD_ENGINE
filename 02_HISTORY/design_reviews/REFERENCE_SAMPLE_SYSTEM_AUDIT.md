# Reference Sample System Audit

Date: `2026-05-10`
Status: `PASS_WITH_LIMITATIONS`

## Scope

Create a controlled open-source KiCad sample learning system that lets
Codex/Claude compare generated schematics and PCB layouts against real
human-made examples without downloading new repos, editing active projects, or
copying unclear-license source into public payloads.

## What Was Added

- new intake workflow, license, normalization, quality-scorecard, and anti-copy
  rules under `32_OPEN_KICAD_SAMPLE_INTAKE/`
- new reference comparison docs under `07_REFERENCE_DESIGNS/`
- new read-only scripts under `03_TOOLS/scripts/sample_intake/`
- startup/handoff updates so future sessions route sample-learning work through
  the controlled intake layer

## Validation

- Python syntax check for all new sample-intake scripts: `PASS`
- `register_sample_candidate.py` dry-run: `PASS`
- `build_reference_style_index.py` dry-run against existing sample fixtures:
  `PASS`
- active KiCad design files changed: `NO`

## Important Limits

- The repo now has a sample-learning system, not a curated gold-standard sample
  corpus.
- Existing imported/normalized samples remain mixed-quality fixtures and must
  not be treated as automatic approval examples.
- Sample metrics are supporting comparison evidence only.

## Outcome

The repo now has an enforceable intake and comparison layer for open-source
KiCad samples, while keeping imported originals read-only and public payloads
link-first by default.
