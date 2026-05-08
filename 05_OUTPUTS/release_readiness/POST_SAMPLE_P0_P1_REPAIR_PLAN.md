# Post Sample P0/P1 Repair Plan

Date: `2026-05-06`

Status: `ACTIVE_REPAIR_PLAN`

Scope: repair only P0/P1 blockers from the post-sample production audit.

## Inputs Reviewed

- `02_HISTORY/design_reviews/POST_SAMPLE_PROJECT_PRODUCTION_AUDIT.md`
- `05_OUTPUTS/release_readiness/POST_SAMPLE_PROJECT_BLOCKERS.md`
- `05_OUTPUTS/release_readiness/POST_SAMPLE_PROJECT_NEXT_STEPS.md`
- `05_OUTPUTS/release_readiness/POST_SAMPLE_PROJECT_SCORECARD.md`
- `17_RELEASE_BUILD/PAYLOAD_ALLOWLIST.md`
- `17_RELEASE_BUILD/PAYLOAD_EXCLUDE_RULES.md`
- `17_RELEASE_BUILD/SAMPLE_PROJECT_PAYLOAD_POLICY.md`
- `17_RELEASE_BUILD/PUBLIC_PAYLOAD_MANIFEST.md`
- `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`

## P0/P1 Findings

| Priority | Finding | Decision |
| --- | --- | --- |
| P0 | False public-release readiness would be unsafe. | Keep public status `INTERNAL_ALPHA`; do not claim sample or repo is public-release ready. |
| P0 | Unsafe payload inclusion must be blocked. | Add a dry-run-first public payload builder that excludes raw imports, normalized samples, backups, history, generated outputs, PDFs, secrets, `FAB_READY`, and sample KiCad source while human review is pending. |
| P1 | `17_RELEASE_BUILD/build_public_payload.py` is missing. | Create the script and validate syntax plus dry-run behavior. |
| P1 | Public payload manifest still says the builder is missing. | Update release docs to reflect the new dry-run builder and current blocked sample-source status. |

## Explicit Non-Fixes

These are not repaired in this P0/P1 pass because they require KiCad design edits
or human engineering/legal review:

- ATtiny85 ERC failure on `J1` shield.
- ATtiny85 DRC violations.
- ATtiny85 schematic/footprint parity issues.
- Human footprint/orientation review for `J1`, `J2`, and `U2`.
- Human visual review.
- Final PCB verification and NOT_FINAL fab audit.
- Final public-bundle license approval for sample source files.

## Repair Steps

1. Create `17_RELEASE_BUILD/build_public_payload.py`.
2. Update release docs to reference the builder and keep status honest.
3. Run Python syntax validation on the new script.
4. Run the dry-run payload builder.
5. Run the one-command project gate runner to confirm the sample remains blocked.
6. Run available safe reference/secret validation or document missing dedicated scripts.
7. Record repair audit, command log, session log, remaining backlog, and AI quality closeout records.

## Expected Outcome

P0/P1 infrastructure status should improve from `RULES_READY_BUILDER_MISSING` to
`DRY_RUN_BUILDER_AVAILABLE`. Public release remains blocked until engineering
and human release-review blockers are resolved or explicitly scoped out.
