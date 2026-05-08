# Payload Build Rules

Status: `ACTIVE_RULES`

## Approved Builder

Use:

- `installer/payload/build_payload.py`
- `installer/payload/build_payload.ps1`

## Required Checks

- Exclude secrets.
- Exclude dependency caches.
- Exclude local active projects unless approved as samples.
- Exclude copyrighted PDFs unless redistribution is confirmed.
- Exclude final fab packages.
- Exclude huge files unless reviewed.

## Required Outputs

- `payload.manifest.json`
- `PAYLOAD_BUILD_REPORT.md`
- file count summary
- size summary

## Dry Run

Every release candidate must include a payload dry run into a disposable folder.

