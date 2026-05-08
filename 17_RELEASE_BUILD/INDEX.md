# Release Build Index

Status: `ACTIVE_RELEASE_GATE_INDEX`

## Purpose

This folder records release-build planning, payload rules, artifact naming, checksum requirements, public-release checklists, and release exclusion rules.

## Current Contents

- `README.md`: release-build folder purpose and safety rules.
- `RELEASE_BUILD_PLAN.md`: planned release-build process.
- `PAYLOAD_BUILD_RULES.md`: payload build and dry-run requirements.
- `PAYLOAD_ALLOWLIST.md`: public payload allowlist, including conditional sample-project inclusion rules.
- `PAYLOAD_EXCLUDE_RULES.md`: public payload exclusion rules for secrets, raw imports, backups, generated outputs, PDFs, and unsafe sample files.
- `PUBLIC_PAYLOAD_MANIFEST.md`: planned public payload manifest and current blocked sample-source decision.
- `SAMPLE_PROJECT_PAYLOAD_POLICY.md`: rules for including open KiCad sample projects in public payloads.
- `GITHUB_RELEASE_CHECKLIST.md`: GitHub release gate checklist.
- `ARTIFACT_NAMING.md`: release artifact naming rules.
- `CHECKSUM_RULES.md`: checksum rules.
- `PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`: P0 exclusion rules for envs, repos, generated outputs, backups, build artifacts, unreviewed PDFs, and secrets.
- `build_public_payload.py`: dry-run-first public payload manifest builder.

## Required Before Public Release

- Clean payload build reviewed.
- Exclusion manifest applied.
- Sample-project payload policy applied.
- Raw imported samples excluded.
- Secret scan reviewed.
- Datasheet/PDF redistribution reviewed.
- Third-party attribution reviewed.
- Checksums generated.
- Installer/build smoke-test evidence recorded.
- Signing/notarization status documented.

## Agent Rules

- Do not publish releases automatically.
- Do not label artifacts production-ready unless build, smoke, checksum, license, security, and payload checks passed.
- Do not include generated manufacturing-style outputs unless they are reviewed and labeled `NOT_FINAL`.
- Do not store signing keys, certificates, credentials, or API tokens here.

## Builder Notes

Run the public payload builder from the repository root:

```powershell
python 17_RELEASE_BUILD\build_public_payload.py --repo-root .
```

Default mode is dry-run. The builder applies the release allowlist/exclusion
policy, excludes unsafe sample source while human review is pending, and writes
reports under `05_OUTPUTS/release_readiness/public_payload_dry_runs/`.
