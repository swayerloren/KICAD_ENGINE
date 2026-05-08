# Public Payload Exclude Rules

Status: `ACTIVE_RELEASE_RULES`

Last updated: `2026-05-06`

## Purpose

This file defines content that must be excluded from public release payloads,
installer workspace templates, and curated public archives unless a documented
human release review approves a narrow exception.

When this file conflicts with an allowlist, the exclusion wins.

## Always Exclude

| Pattern / Path | Reason |
| --- | --- |
| `**/.env` | Secrets risk. |
| `**/*.key` | Secrets risk. |
| `**/*.token` | Secrets risk. |
| `**/*secret*` | Secrets risk unless file is a public policy doc and reviewed. |
| `**/*api_key*` | Secrets risk. |
| `**/local_credentials.*` | Local credential risk. |
| `**/private_config.*` | Local credential risk. |
| `**/.git/` | Repository internals. |
| `**/node_modules/` | Dependency cache. |
| `**/__pycache__/` | Generated cache. |
| `**/.venv/` | Local environment. |
| `**/venv/` | Local environment. |
| `03_TOOLS/repos/` | Third-party repo copies require separate license review. |
| `03_TOOLS/python_envs/` | Local environment. |
| `03_TOOLS/node_envs/` | Local environment. |
| `03_TOOLS/tool_logs/` | Local/generated logs. |
| `03_TOOLS/windows/repos/` | Third-party repo copies require separate license review. |
| `03_TOOLS/windows/logs/` | Local/generated logs. |
| `03_TOOLS/linux/repos/` | Third-party repo copies require separate license review. |
| `03_TOOLS/linux/logs/` | Local/generated logs. |
| `99_BACKUPS/` | User/local backups. |
| `02_HISTORY/` | Personal/local session history unless a curated public record is specifically approved. |
| `05_OUTPUTS/` | Generated outputs unless a small, reviewed, public sample report is intentionally included. |
| `installer/build/` | Build output. |
| `installer/dist/` | Build output. |
| `installer/node_modules/` | Dependency cache. |
| `installer/payload/repo-template/` | Generated payload output; do not recursively bundle generated output. |
| `installer/payload/payload.manifest.json` | Generated output. |
| `installer/payload/PAYLOAD_BUILD_REPORT.md` | Generated output. |
| `17_RELEASE_BUILD/build/` | Build output if created. |
| `17_RELEASE_BUILD/dist/` | Build output if created. |

## Datasheet And Vendor Document Exclusions

Exclude by default:

- `**/*.pdf`
- vendor datasheets
- vendor app notes
- vendor reference manuals
- vendor board schematics
- copied CAD models
- copied vendor symbols or footprints
- copied 3D models

These files may be included only when redistribution permission is recorded in
`21_LICENSE_ATTRIBUTION/` and the public release checklist names the reviewer
and source evidence. Link-only metadata is preferred.

## Fabrication And Manufacturing Output Exclusions

Exclude by default:

- `**/*.gbr`
- `**/*.drl`
- `**/*.xln`
- `**/*.pos`
- `**/*CPL*`
- `**/*PNP*`
- `**/*pick*place*`
- `**/*gerber*`
- `**/*drill*`
- `**/*fabrication*`
- `**/*FAB_READY*`
- any folder named `fabrication`
- any folder named `gerbers`
- any folder named `production`
- any folder named `final`

`NOT_FINAL` evidence may be included only when it is small, explicitly useful
for a public demo, license-safe, and listed in `PAYLOAD_ALLOWLIST.md`.

No file marked `FAB_READY` may be included unless a separate human release
approval explicitly documents why it is public and licensed.

## Open KiCad Sample Project Exclusions

Always exclude:

| Path | Reason |
| --- | --- |
| `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/` | Raw imports are preservation evidence, not public payload content. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/` | Working copies are not public payload content. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/benchmark_candidates/` | Not public until promoted and reviewed. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/*_ERC_DRC_REPORT.md` | Include only if intentionally curated; may contain generated/local details. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/*_VISUAL_AUDIT.md` | Include only if intentionally curated. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/*_GATE_STATUS.md` | Include only if intentionally curated. |

Exclude every sample with status:

- `LINK_ONLY`
- `NEEDS_HUMAN_LICENSE_REVIEW`
- `DO_NOT_IMPORT`
- `LICENSE_BLOCKED`
- `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`

until the status is changed by human review to `PUBLIC_BUNDLE_ALLOWED`.

## Current Controlled Sample Exclusion

The controlled ATtiny85 sample fixture is useful documentation and gate-run
evidence, but it is not yet a clean passing public sample and its bundle status
is still `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`.

Therefore, exclude these paths by default:

- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/*.kicad_pro`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/*.kicad_sch`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/*.kicad_pcb`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/fp-lib-table`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/custom_footprints/`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/_verification/`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/.gate_runs/`
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/fabrication/`

Small markdown files under the sample may be included only when listed in
`PAYLOAD_ALLOWLIST.md`.

## Size And Format Exclusions

Exclude files larger than the current payload builder size limit unless a human
release review approves them. The installer payload builder currently uses a
5 MB default limit.

Exclude large binary media by default:

- `**/*.png`
- `**/*.jpg`
- `**/*.jpeg`
- `**/*.gif`
- `**/*.bmp`
- `**/*.tif`
- `**/*.tiff`
- `**/*.stl`
- `**/*.step`
- `**/*.stp`
- `**/*.wrl`
- `**/*.zip`
- `**/*.7z`
- `**/*.rar`
- `**/*.exe`
- `**/*.dll`
- `**/*.so`
- `**/*.dylib`

Small screenshots or SVGs may be included only as reviewed sample evidence.

## Builder Rule

A public payload builder must:

1. Start from `PAYLOAD_ALLOWLIST.md`.
2. Apply this exclusion file.
3. Apply `PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`.
4. Fail on secret-like content.
5. Fail on any sample source file whose public bundle status is not
   `PUBLIC_BUNDLE_ALLOWED`.
6. Produce a manifest with included and excluded paths.
7. Support a dry-run mode that writes no release artifact.
