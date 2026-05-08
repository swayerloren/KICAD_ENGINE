# Open KiCad Sample Intake

Status: `CONTROLLED_INTAKE_SYSTEM`

This subsystem defines how KiCad Engine may identify, screen, import, normalize, review, and optionally promote open KiCad sample projects. It exists to keep real public sample projects useful without letting random downloads, unclear licenses, or unreviewed manufacturing outputs pollute the main repo.

## Purpose

Open KiCad samples can help Codex, Claude, and similar agents learn from complete real-world schematic and PCB projects. They are not automatically trusted. Every sample must pass source, license, file, attribution, and review gates before it can be used as a reference design, benchmark candidate, or public-release payload item.

## Folder Roles

| Folder | Purpose |
| --- | --- |
| `candidates/` | Candidate records before import. Source URLs and screening notes only. |
| `imported_originals/` | Preserved original imports. Treat as read-only. Do not repair or normalize in place. |
| `normalized_samples/` | Working copies for analysis, repair experiments, or benchmark adaptation. |
| `review_reports/` | ERC/DRC/visual/license/file audit reports for samples. |
| `benchmark_candidates/` | Samples proposed for `15_BENCHMARKS` after review. |
| `attribution/` | License, attribution, and source-preservation records. |
| `scripts/` | Safe dry-run-first intake helpers. |
| `templates/` | Reusable candidate, import, license, review, and promotion templates. |

## Required Intake Gate

A sample project may be imported only if:

1. Source URL is recorded.
2. License is present and compatible or marked `NEEDS_HUMAN_LICENSE_REVIEW`.
3. Attribution is preserved.
4. Project contains actual KiCad files: `.kicad_pro`, `.kicad_sch`, and/or `.kicad_pcb`.
5. Original content is stored under `imported_originals/` and treated read-only.
6. A normalized copy is created before analysis, repair, benchmark adaptation, or formatting.
7. Existence is not treated as verification.
8. ERC, DRC, visual, and fab-package checks are recorded when run.
9. Generated outputs are marked `NOT_FINAL`.
10. Public release inclusion is blocked unless license status is `PUBLIC_BUNDLE_ALLOWED`.

## Agent Rules

- Do not randomly download projects into the repo root.
- Do not copy closed, proprietary, unclear-license, or no-license projects as bundled samples.
- Do not edit imported originals directly.
- Do not generate manufacturing outputs from imported samples unless the review workflow authorizes `NOT_FINAL` review exports.
- Do not modify active user projects from this workflow.
- Prefer source links and candidate records before copying files.
- Use `12_REFERENCE_DESIGN_LIBRARY` for reference-design lessons and `15_BENCHMARKS` for benchmark promotion only after review.

## Public Release Rule

Imported samples are excluded from public release by default. A sample can be included in a public payload only when a license review record says `PUBLIC_BUNDLE_ALLOWED`, attribution is complete, large/generated outputs are excluded or justified, and the release manifest explicitly includes it.
