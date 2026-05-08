# Sample Payload Audit

Status: `POLICY_UPDATED_DRY_RUN_BUILDER_AVAILABLE`

Date: `2026-05-06`

## Scope

Updated public release payload rules for safe sample-project inclusion. This
was documentation and policy work only.

No KiCad design files were edited, no raw imports were moved, no files were
deleted, no datasheets were downloaded, and no manufacturing outputs were
generated.

## Required Inputs Reviewed

| File | Status |
| --- | --- |
| `17_RELEASE_BUILD/PAYLOAD_ALLOWLIST.md` | Created because it was missing. |
| `17_RELEASE_BUILD/PAYLOAD_EXCLUDE_RULES.md` | Created because it was missing. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/INDEX.md` | Reviewed. |
| `19_TEST_PROJECTS/SAMPLE_PROJECTS_INDEX.md` | Reviewed. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md` | Reviewed. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md` | Reviewed. |
| `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md` | Reviewed; current status is `REQUIRES_HUMAN_REVIEW`. |
| `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md` | Reviewed and updated. |

## Files Updated Or Created

| File | Result |
| --- | --- |
| `17_RELEASE_BUILD/PAYLOAD_ALLOWLIST.md` | Created public payload allowlist with sample-project rules. |
| `17_RELEASE_BUILD/PAYLOAD_EXCLUDE_RULES.md` | Created exclusion rules for secrets, raw imports, backups, generated outputs, PDFs, fab outputs, and unsafe samples. |
| `17_RELEASE_BUILD/PUBLIC_PAYLOAD_MANIFEST.md` | Created planned manifest and current blocked public payload status. |
| `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md` | Updated sample-project exclusion gate and companion policy references. |
| `17_RELEASE_BUILD/SAMPLE_PROJECT_PAYLOAD_POLICY.md` | Created sample project payload policy. |
| `17_RELEASE_BUILD/README.md` | Updated to point at sample payload rules. |
| `17_RELEASE_BUILD/INDEX.md` | Updated with new release payload policy files. |
| `FOR CHAT GPT.MD` | Updated with current payload/sample release rules. |

## Current Sample Payload Decision

Sample: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`

Decision: `LINK_ONLY_PLUS_DOCS`

Reason:

- License evidence exists and identifies MIT.
- Repository license audit still requires human review.
- The sample public bundle status remains
  `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`.
- Latest one-command gate result remains `BLOCKED_UNTIL_HUMAN_REVIEW`.
- ERC, DRC, footprint/package, PCB sync, visual review, and fab-readiness
  blockers remain unresolved.

Allowed now:

- sample README/status markdown
- attribution markdown
- local license evidence reference
- small markdown reports that preserve blocked status

Excluded now:

- `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`
- `fp-lib-table`
- project-local custom footprints
- `_verification/`
- `.gate_runs/`
- `fabrication/`
- any generated fabrication-style output
- any file marked `FAB_READY`

## Dry-Run Payload Build Result

Result: `DRY_RUN_BUILDER_AVAILABLE`

Current builder:

- `17_RELEASE_BUILD/build_public_payload.py`

Validation evidence from the P0/P1 repair pass:

- Syntax validation passed with `python -m py_compile`.
- Dry-run output was generated under
  `05_OUTPUTS/release_readiness/public_payload_dry_runs/20260506_post_sample_p0_p1_repair/`.
- Raw imports, normalized samples, backups, history, generated outputs, PDFs,
  KiCad sample source files, archives, and `FAB_READY` paths were absent from
  the dry-run included-file set.

The dry run is not a public release approval. The repository remains blocked
pending human release review and the ATtiny85 fixture remains blocked by
engineering gates.

## Validation Results

| Check | Result | Evidence |
| --- | --- | --- |
| Required release policy files exist | `PASS` | PowerShell `Test-Path` check. |
| `build_public_payload.py` exists | `PASS` | Added at `17_RELEASE_BUILD/build_public_payload.py`. |
| Targeted secret assignment scan on changed release docs | `PASS` | No matches found. |
| Required sample status/attribution docs exist | `PASS` | PowerShell `Test-Path` check. |
| KiCad sample design files edited | `NOT_EDITED_BY_THIS_TASK` | No write actions targeted `.kicad_*` or `.kicad_mod`; last-write inventory was read-only. |
| Dry-run public payload build | `PASS_WITH_WARNINGS` | Latest P0/P1 repair dry run produced a report and manifest; public release remains blocked pending human review. |

## Remaining Blockers

1. Human release review must decide whether the ATtiny85 fixture can move from
   `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW` to
   `PUBLIC_BUNDLE_ALLOWED`.
2. Public payload builder exists, but an approved public release artifact has
   not been built.
3. The license audit is still `REQUIRES_HUMAN_REVIEW`.
4. The ATtiny85 fixture is not a clean passing design and remains blocked by
   gate evidence.

## Final Status

`MEDIUM_RISK`

The release rules are stricter and the dry-run public payload builder now
exists, but no approved public payload was built and sample source inclusion
remains blocked until human review.
