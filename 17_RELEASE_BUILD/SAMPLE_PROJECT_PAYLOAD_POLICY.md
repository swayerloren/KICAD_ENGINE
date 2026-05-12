# Sample Project Payload Policy

Status: `ACTIVE_RELEASE_POLICY`

Last updated: `2026-05-06`

## Purpose

This policy controls when open KiCad sample projects may be included in a public
KiCad Engine release payload. It exists to prevent accidental redistribution of
raw imports, unclear-license projects, generated manufacturing outputs, or
sample files that look more verified than they are.

## Default Rule

Sample projects are excluded from public payloads by default.

Include only after the sample has:

1. Source URL recorded.
2. Imported commit or timestamp recorded.
3. License file recorded.
4. Attribution preserved.
5. Public bundle status exactly `PUBLIC_BUNDLE_ALLOWED`.
6. Engineering gate status recorded.
7. Generated outputs marked `NOT_FINAL` if included.
8. Human release review recorded.

## Folder Boundaries

| Folder | Payload rule |
| --- | --- |
| `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/` | Always exclude. This is preservation evidence only. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/` | Always exclude by default. These are working copies. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/candidates/` | Allow source-link records and license screening notes. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/attribution/` | Allow attribution records if no copied restricted content is embedded. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/` | Allow curated markdown summaries only when useful and reviewed. |
| `07_REFERENCE_DESIGNS/` | Allow link-first notes, style summaries, and generated metric indexes that do not embed restricted sample source. |
| `19_TEST_PROJECTS/sample_kicad_projects/` | Allow only controlled samples listed in `PAYLOAD_ALLOWLIST.md` and approved by human release review. |

## Required Sample Payload Fields

Every included sample must have a payload record containing:

| Field | Required value |
| --- | --- |
| sample name | exact local sample name |
| source URL | public source link |
| source owner | original owner/project |
| imported commit/timestamp | immutable source evidence |
| license | license name |
| license confidence | `HIGH_SOURCE_FILE_PRESENT`, `MEDIUM`, or `LOW` |
| public bundle status | must be `PUBLIC_BUNDLE_ALLOWED` |
| attribution path | local attribution file |
| included files | exact list or generated manifest reference |
| excluded files | exact list or rule reference |
| gate status | `PASS`, `PARTIAL`, `FAIL`, or `BLOCKED_UNTIL_HUMAN_REVIEW` |
| manufacturing status | must not be `FAB_READY` unless separately approved |
| human reviewer | name/initials or release-review record ID |

## Current Controlled Fixture

Sample: `tomasr8_attiny85_dev_board`

Decision: `LINK_ONLY_PLUS_DOCS`

Reason:

- License evidence is present and appears to be MIT.
- Public bundle status is still
  `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`.
- Gate result is `BLOCKED_UNTIL_HUMAN_REVIEW`.
- ERC, DRC, footprint/package, PCB sync, visual review, and fab-readiness gates
  still have blockers.

Allowed now:

- sample README/status docs
- attribution record
- license evidence reference
- markdown reports that preserve blocked status

Excluded now:

- `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`
- project-local footprint libraries
- generated visuals and gate-run outputs unless separately curated
- any upstream or generated fabrication output
- any file or folder marked `FAB_READY`

## Builder Enforcement

`17_RELEASE_BUILD/build_public_payload.py` enforces this policy in dry-run mode
by default. It may include the controlled fixture's small markdown status,
attribution, license, and report files, but it excludes KiCad source files,
project-local footprints, `_verification`, `.gate_runs`, fabrication folders,
and raw/normalized imported samples while the public bundle status remains
pending human review.

## NOT_FINAL Evidence Rule

`NOT_FINAL` evidence can be included only when all of these are true:

1. It is small.
2. It is useful to explain a public demo.
3. It does not include restricted third-party content.
4. It is listed in the allowlist or generated manifest.
5. It cannot be mistaken for a manufacturing-ready package.

Reference-style indexes and sample metric summaries are safer public payload
candidates than copied sample source files, but they still require attribution,
license-aware wording, and clear warning that comparison evidence is not
engineering approval.

## FAB_READY Block

No sample payload may include a file marked `FAB_READY` unless a separate
release approval states:

- why the file is included
- who reviewed it
- what license permits it
- why it is safe for public distribution
- how users are warned that AI review is not fabrication approval

## Required Public Warning

Every public sample description must state:

> Sample projects are workflow fixtures and learning material. They are not
> fabrication approval. Outputs remain `NOT_FINAL` unless independently
> reviewed by a qualified human.
