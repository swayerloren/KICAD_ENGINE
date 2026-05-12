# Open KiCad Sample Intake

Status: `CONTROLLED_INTAKE_SYSTEM`

## PURPOSE

Define how KiCad Engine identifies, screens, imports, normalizes, reviews, and
learns from open-source KiCad sample projects without letting random downloads,
unclear licenses, or unreviewed manufacturing outputs pollute the repo.

## WHAT_BELONGS_HERE

- candidate records before import
- preserved imported originals
- normalized working copies
- license and attribution evidence
- schematic and PCB metric reports
- sample quality scorecards
- sample-promotion and anti-copy rules
- dry-run-first intake scripts

## WHAT_DOES_NOT_BELONG_HERE

- active user KiCad projects
- proprietary or unclear-license projects in public payloads
- random repo-root downloads
- edited imported originals
- secrets or credentials

## AI_AGENT_RULES

- Do not randomly download projects into the repo root.
- Do not copy closed, proprietary, unclear-license, or no-license projects as
  bundled samples.
- Do not edit imported originals directly.
- Do not treat sample existence as verification.
- Use sample metrics as comparison evidence only.
- Promote reusable lessons into `07_REFERENCE_DESIGNS/`,
  `12_REFERENCE_DESIGN_LIBRARY/`, or `15_BENCHMARKS/` only after review.

## SAFE_EDIT_RULES

- Register the candidate first.
- Preserve the upstream original under `imported_originals/`.
- Create a normalized working copy before any repair or rewrite experiment.
- Keep audits dry-run-first.
- Exclude public payload use unless license status allows it.

## PUBLIC_RELEASE_NOTES

Imported samples are excluded from public release by default. A sample can be
included only when license review says `PUBLIC_BUNDLE_ALLOWED`, attribution is
complete, and the release manifest explicitly includes it.

## Workflow Files

- `SAMPLE_INTAKE_WORKFLOW.md`
- `SAMPLE_LICENSE_RULES.md`
- `SAMPLE_NORMALIZATION_RULES.md`
- `SAMPLE_QUALITY_SCORECARD.md`
- `SAMPLE_DO_NOT_COPY_RULES.md`
- `SOURCE_SELECTION_RULES.md`
- `LICENSE_SCREENING_RULES.md`
- `SAMPLE_IMPORT_WORKFLOW.md`
- `SAMPLE_REVIEW_WORKFLOW.md`
- `SAMPLE_PROMOTION_RULES.md`

## Folder Roles

| Folder | Purpose |
| --- | --- |
| `candidates/` | Candidate records before import. Source URLs and screening notes only. |
| `imported_originals/` | Preserved original imports. Treat as read-only. |
| `normalized_samples/` | Working copies for analysis, repair experiments, or benchmark adaptation. |
| `review_reports/` | ERC/DRC/visual/license/file/metric audit reports for samples. |
| `benchmark_candidates/` | Samples proposed for `15_BENCHMARKS` after review. |
| `attribution/` | License, attribution, and source-preservation records. |
| `scripts/` | Legacy intake helpers. |
| `templates/` | Reusable candidate, import, license, review, and promotion templates. |

## Learning System Rule

Open-source samples help Codex and Claude compare generated schematics and PCB
layouts against real human-made examples. They are not authoritative truth and
must not override the active project's own gates, datasheets, orientation
proofs, or DRC/ERC evidence.
