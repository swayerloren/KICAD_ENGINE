# Public Payload Manifest

Status: `DRY_RUN_BUILDER_AVAILABLE_NO_PUBLIC_PAYLOAD_BUILT`

Last updated: `2026-05-06`

## Purpose

This manifest describes the intended public payload contents. It is not a build
result and does not prove that a public archive is ready. A real payload build
must produce a generated manifest with file paths, sizes, hashes, exclusions,
and validation results.

## Current Classification

Current public payload status: `BLOCKED_PENDING_HUMAN_RELEASE_REVIEW`

Reasons:

- The repository-level license audit is still `REQUIRES_HUMAN_REVIEW`.
- The controlled ATtiny85 sample has MIT license evidence, but its public bundle
  status is still `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`.
- `17_RELEASE_BUILD/build_public_payload.py` now exists and defaults to dry-run.
- A real public release artifact has not been built or approved.

## Intended Public Payload Groups

| Group | Include status | Notes |
| --- | --- | --- |
| Root public docs | `ALLOW` | README, quickstarts, license, disclaimer, security, contributing, roadmap. |
| AI startup rules | `ALLOW` | `00_CODEX_START/` with no private project state. |
| Prompt packs | `ALLOW` | `.prompts/` public prompts. |
| Accuracy and quality systems | `ALLOW` | `09_ACCURACY_ENGINE/`, `26_AGENT_QUALITY/`. |
| Datasheet indexes | `ALLOW_METADATA_ONLY` | No PDFs unless redistribution is approved. |
| Component database | `ALLOW_METADATA_ONLY` | Records must keep verification flags. |
| Public docs | `ALLOW` | `18_PUBLIC_DOCS/` and root user docs. |
| Sample project docs | `ALLOW` | Sample index and how-to docs. |
| Controlled ATtiny85 sample source | `BLOCKED_PENDING_HUMAN_REVIEW` | Do not include KiCad source files until public bundle status is exactly `PUBLIC_BUNDLE_ALLOWED`. |
| Controlled ATtiny85 sample markdown status/attribution | `ALLOW` | May include sample README, attribution, license, and blocked status docs. |
| Raw open-sample imports | `EXCLUDE` | Never include `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`. |
| Normalized open-sample copies | `EXCLUDE` | Never include `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/` by default. |
| Generated outputs | `EXCLUDE_BY_DEFAULT` | Only small reviewed `NOT_FINAL` evidence can be included. |
| Backups and personal history | `EXCLUDE` | Exclude `99_BACKUPS/`, most `02_HISTORY/`, and uncurated `05_OUTPUTS/`. |

## Current Sample Payload Decision

| Sample | Current gate result | License evidence | Public bundle status | Payload decision |
| --- | --- | --- | --- | --- |
| `tomasr8_attiny85_dev_board` | `BLOCKED_UNTIL_HUMAN_REVIEW` | MIT license preserved | `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW` | `LINK_ONLY_PLUS_DOCS`; source files excluded pending final human release review. |

## Required Generated Manifest Fields

The future public payload builder must output a generated manifest containing:

- build timestamp
- builder version
- source repo path omitted or sanitized
- release candidate name
- included file path
- file size
- SHA-256
- license status
- sample/public-bundle status where relevant
- exclusion reason for skipped files
- total file count
- total byte count
- secret scan result
- license review result
- dry-run/apply mode

## Current Builder Status

`17_RELEASE_BUILD/build_public_payload.py` is present. It is conservative and
dry-run-first:

- default mode writes a report and JSON manifest only;
- raw imports, normalized samples, backups, generated outputs, PDFs,
  fabrication outputs, local environments, third-party repos, and secret-like
  files are excluded;
- controlled ATtiny85 sample KiCad source files remain excluded until human
  public-bundle review records status exactly `PUBLIC_BUNDLE_ALLOWED`;
- output is written under
  `05_OUTPUTS/release_readiness/public_payload_dry_runs/<timestamp>/`.

The existing installer payload builder lives at
`installer/payload/build_payload.py`; it remains separate from this public
release payload builder.
