# Post Sample Remaining Backlog

Date: `2026-05-06`

Status: `OPEN_P2_P3_AND_HUMAN_REVIEW_BACKLOG`

## Still Blocking Public Release

These were not fixed in the P0/P1 repair pass because they require KiCad design
repair, human engineering review, or human legal/release approval.

| Priority | Backlog item | Current evidence | Required next action |
| --- | --- | --- | --- |
| P2 | ATtiny85 sample remains `BLOCKED_UNTIL_HUMAN_REVIEW`. | `05_OUTPUTS/gate_runs/20260506_151003/PROJECT_GATE_REPORT.md` | Resolve or formally accept all gate blockers. |
| P2 | ERC fails on `J1` shield pin. | Latest gate report parses ERC evidence. | Decide and document USB shield policy, then repair and rerun ERC. |
| P2 | DRC fails with 15 violations and 13 parity/footprint issues. | Latest gate report. | Repair promoted sample copy only, then rerun DRC and gate runner. |
| P2 | Footprint/package/orientation review remains open for `J1`, `J2`, and `U2`. | `FOOTPRINT_PACKAGE_AUDIT.md` and latest gate report. | Human review against exact package drawings and orientation evidence. |
| P2 | Schematic and PCB visual close-up reviews still need human review. | Latest gate report. | Complete review sections, then rerun gate runner. |
| P2 | Final PCB verification before fab is missing. | Latest gate report. | Create final verification only after upstream gates pass. |
| P2 | NOT_FINAL fab package audit is missing because export is blocked. | Latest gate report. | Do not export until final PCB verification permits NOT_FINAL export. |
| P2/Human | Sample public-bundle status remains pending. | `GOLDEN_PATH_DEMO_STATUS.md`, release docs. | Human release review must record exact `PUBLIC_BUNDLE_ALLOWED` before sample source files can be included. |
| P2/Human | Repository license audit still requires human review. | `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md`. | Complete license/attribution review before public release. |
| P3 | General broken-reference scan is not automated. | No generic checker found during this repair pass. | Add a dedicated public-doc/reference checker. |
| P3 | General secret scan is not a standalone script. | Payload builder scans candidates, but no repo-wide scanner exists. | Add a dedicated release secret scanner that prunes envs/tool repos safely. |

## P0/P1 Status After Repair

- `17_RELEASE_BUILD/build_public_payload.py` now exists.
- Dry-run payload output exists at
  `05_OUTPUTS/release_readiness/public_payload_dry_runs/20260506_post_sample_p0_p1_repair/`.
- The dry-run included set contains zero raw imports, normalized samples,
  backups, history, generated outputs, PDFs, sample KiCad source files,
  archives, or `FAB_READY` paths based on manifest inspection.
- Public release remains blocked.
