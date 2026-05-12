# Release Build

## PURPOSE

Stage release-build plans, manifests, checklists, and artifact review records.

## WHAT_BELONGS_HERE

- Release build plans.
- Artifact naming rules.
- Checksum/checklist templates.
- Release candidate manifests.

## Production Planning Files

- `RELEASE_BUILD_PLAN.md`
- `PAYLOAD_BUILD_RULES.md`
- `PAYLOAD_ALLOWLIST.md`
- `PAYLOAD_EXCLUDE_RULES.md`
- `PUBLIC_PAYLOAD_MANIFEST.md`
- `SAMPLE_PROJECT_PAYLOAD_POLICY.md`
- `GITHUB_RELEASE_CHECKLIST.md`
- `ARTIFACT_NAMING.md`
- `CHECKSUM_RULES.md`
- `PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`

## WHAT_DOES_NOT_BELONG_HERE

- Unreviewed final fabrication packages.
- Secrets, tokens, signing keys, certificates.
- Large generated builds unless intentionally staged and documented.
- Active KiCad source files.

## AI_AGENT_RULES

- Do not publish releases automatically.
- Do not label artifacts final without verification evidence.
- Keep generated manufacturing-style outputs `NOT_FINAL`.
- Do not place copied IPC/UL/paid-standards text into public release payloads
  unless redistribution rights are explicitly documented.

## SAFE_EDIT_RULES

- Add release docs and manifests.
- Preserve existing artifacts.
- Do not delete build outputs.

## PUBLIC_RELEASE_NOTES

Public release candidates require secret scan, license review, checksums, and smoke-test notes.

Do not auto-publish public releases from this folder.

Before any payload or release artifact is built, apply `PUBLIC_RELEASE_EXCLUSION_MANIFEST.md` and block unreviewed PDFs, generated outputs, local environments, backups, third-party repos, secrets, and unfinished fabrication packages.

For public payloads that mention or include sample projects, also apply
`PAYLOAD_ALLOWLIST.md`, `PAYLOAD_EXCLUDE_RULES.md`, and
`SAMPLE_PROJECT_PAYLOAD_POLICY.md`. Raw imports under
`32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`, normalized sample working
copies, unclear-license samples, generated fab outputs, backups, and files
marked `FAB_READY` are excluded by default.

## Public Payload Builder

Use `build_public_payload.py` from the repository root to create a dry-run
public payload report:

```powershell
python 17_RELEASE_BUILD\build_public_payload.py --repo-root .
```

The script does not create a release archive in default mode. It writes a
timestamped report and JSON manifest under
`05_OUTPUTS\release_readiness\public_payload_dry_runs\`. The current ATtiny85
sample fixture remains `LINK_ONLY_PLUS_DOCS`; KiCad source files and generated
sample outputs are excluded until human public-bundle review records status
exactly `PUBLIC_BUNDLE_ALLOWED`.
