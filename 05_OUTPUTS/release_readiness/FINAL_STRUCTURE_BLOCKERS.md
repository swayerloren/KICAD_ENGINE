# Final Structure Blockers

Date: 2026-05-03
Classification: INTERNAL_ALPHA_READY

## Blocking Before Public GitHub Release

1. Create a clean public branch or payload that excludes local dependency folders:
   - `installer/node_modules`
   - `03_TOOLS/python_envs`
   - `03_TOOLS/node_envs`
   - `03_TOOLS/repos`
   - `03_TOOLS/windows/repos`
2. Decide policy for generated outputs and backups:
   - Exclude most of `05_OUTPUTS/`
   - Exclude private `99_BACKUPS/`
   - Exclude installer build output unless publishing as release artifacts with checksums.
3. Resolve PDF redistribution:
   - Review legacy datasheet PDFs under `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444`.
   - Review reference project PDFs and installed demo PDFs.
   - Prefer link-only records unless redistribution rights are confirmed.
4. Scrub or exclude old command logs containing placeholder token/API-key strings copied from third-party docs.
5. Confirm Git worktree status before release:
   - Branch.
   - Diff.
   - Tracked/untracked files.
   - `.gitignore` coverage.
6. Rebuild installer payload from clean source and re-run smoke tests.
7. Complete platform build validation:
   - Windows installer build and install smoke test.
   - macOS DMG/PKG build on macOS runner, signing/notarization notes.
   - Linux AppImage/DEB build on Linux runner.
8. Verify third-party licenses and attribution for tools, docs, workflows, and installer dependencies.
9. Keep benchmark/comparison claims evidence-gated. Do not claim Flux-level parity or superiority without documented benchmark runs.
10. Expand verified component records before claiming serious design-database maturity.

## Not Blocking Internal Alpha

- Placeholder component/datasheet records are acceptable when marked clearly.
- Installer source can remain experimental if docs do not claim production readiness.
- Reference fabrication artifacts can remain locally if excluded from public release.

