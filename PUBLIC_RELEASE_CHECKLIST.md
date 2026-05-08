# Public Release Checklist

Use this checklist before publishing KiCad Engine or an installer release.

## Required

- [ ] `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md` was reviewed.
- [ ] Public payload excludes `03_TOOLS/python_envs`, `03_TOOLS/node_envs`, third-party cloned repos, generated outputs, backups, installer build folders, smoke-test installs, and unreviewed PDFs.
- [ ] Old local paths such as `C:\Users\LJ\KICAD_ENGINE` are absent from public-facing startup docs or clearly marked as historical examples.
- [ ] No secrets, API keys, passwords, private tokens, SSH private keys, or license keys are present.
- [ ] No `.env` files with real values are present.
- [ ] No copyrighted datasheet PDFs are included unless redistribution rights are confirmed.
- [ ] Datasheets without confirmed redistribution rights are link-only or metadata-only.
- [ ] No final fabrication outputs are mislabeled as final.
- [ ] All generated manufacturing-style outputs are marked `NOT_FINAL` unless fully verified and intentionally released.
- [ ] Setup scripts were tested.
- [ ] Health check passes.
- [ ] Windows quickstart was tested.
- [ ] Sample project workflow was tested.
- [ ] License was reviewed.
- [ ] Attribution was reviewed.
- [ ] Third-party tool licenses were reviewed.

## Documentation

- [ ] `README.md` explains what KiCad Engine is and is not.
- [ ] `DISCLAIMER.md` is present and clear.
- [ ] `SECURITY.md` is present and clear.
- [ ] `CONTRIBUTING.md` is present.
- [ ] `CODE_OF_CONDUCT.md` is present.
- [ ] `CHANGELOG.md` is updated.
- [ ] `ROADMAP.md` is updated.
- [ ] Public docs do not claim the datasheet or component database is complete.

## KiCad Safety

- [ ] KiCad Engine is described as using the user's installed KiCad app.
- [ ] Public docs do not claim official KiCad affiliation.
- [ ] Scripts do not write into installed KiCad folders.
- [ ] User-global KiCad library tables are not modified by setup.
- [ ] KiCad project edits require backup and verification gates.

## AI Safety

- [ ] Docs explain that AI review is not fabrication approval.
- [ ] Docs require ERC, DRC, BOM, footprint, symbol, pinout, datasheet, connector orientation, mechanical, and fab-output verification.
- [ ] Prompt packs require no fake datasheet claims.
- [ ] Prompt packs require no unverified footprint approval.
- [ ] Prompt packs require history logs and verification reports.

## Setup And Installer

- [ ] Setup scripts ask before installing anything.
- [ ] Installer plan says KiCad is not bundled in v1.
- [ ] Installer plan says no AI credentials are stored.
- [ ] Installer plan says no paid APIs are required.
- [ ] Installer plan says installed KiCad folders are not modified.
- [ ] Installer binaries are not published until signing/checksum process is ready.

## Release Artifacts

- [ ] Release notes are written.
- [ ] Checksums are generated for release artifacts.
- [ ] Signing/notarization status is documented.
- [ ] Payload manifest is reviewed.
- [ ] Restricted files and local machine paths are removed or documented as examples only.
