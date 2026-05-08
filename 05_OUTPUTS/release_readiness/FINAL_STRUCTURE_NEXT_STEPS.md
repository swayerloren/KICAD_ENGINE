# Final Structure Next Steps

Date: 2026-05-03

## Next Practical Steps

1. Create `.gitignore` and release exclusion rules for dependency folders, local environments, build outputs, backups, generated outputs, and private/reference artifacts.
2. Run a Git-aware release audit from a real Git worktree.
3. Build a clean public payload using `installer/payload/build_payload.py`, then inspect the manifest for excluded folders and PDFs.
4. Create a redistribution decision table for every PDF and copied reference artifact.
5. Scrub or exclude historical command logs that contain placeholder token/API-key strings from third-party documentation.
6. Run installer smoke tests again after payload cleanup.
7. Add automated CI checks for:
   - Required folders.
   - README/INDEX presence.
   - No forbidden secrets.
   - No PDFs unless allowlisted.
   - No final fab outputs without NOT_FINAL/human-review labels.
   - Python script syntax.
8. Add JSON schema checks for component records, datasheet source lists, package profiles, fab profiles, and vendor records.
9. Add a public alpha release note that clearly states:
   - Local-first KiCad support.
   - Not official KiCad.
   - Not fabrication approval.
   - Data and installer maturity limitations.
10. Start converting placeholder component records into verified records with source links and explicit symbol/footprint evidence.

## Recommended Classification Path

- Current: INTERNAL_ALPHA_READY.
- To reach PUBLIC_ALPHA_READY: clean release branch/payload, legal exclusions, no secret-pattern findings, no bundled uncertain PDFs, and at least one documented installer/payload smoke test.
- To reach PUBLIC_BETA_READY: repeated Windows/macOS/Linux installer builds, sample project workflow tests, schema validation, and a curated verified component subset.
- To reach PUBLIC_RELEASE_READY: legal review, signed/notarized release artifacts where applicable, reproducible CI, release checksums, mature docs, and verified benchmark evidence.

