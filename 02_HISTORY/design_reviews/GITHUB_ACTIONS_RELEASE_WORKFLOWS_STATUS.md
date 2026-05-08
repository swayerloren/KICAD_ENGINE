# GitHub Actions Release Workflows Status

Local time: 2026-05-02 21:02 -04:00

## Summary

Status: canonical GitHub Actions release-builder workflows created.

No release was published. No secrets were added. No paid services are required. No KiCad project files were modified.

## Created Or Updated

- `.github/workflows/build-installer-windows.yml`
- `.github/workflows/build-installer-macos.yml`
- `.github/workflows/build-installer-linux.yml`
- `.github/workflows/build-all-installers.yml`
- `.github/workflows/release-draft.yml`
- `.github/RELEASE_WORKFLOW_README.md`
- `installer/docs/GITHUB_ACTIONS_RELEASE_BUILDER.md`
- `installer/README.md`
- `health_check.py`
- `installer/payload/repo-template`
- `installer/payload/payload.manifest.json`
- `installer/payload/manifests/payload.manifest.json`
- `installer/payload/PAYLOAD_BUILD_REPORT.md`

## Artifact Naming

The canonical workflows normalize release artifacts to:

- `KiCad-Engine-Setup-Windows-x64.exe`
- `KiCad-Engine-Setup-macOS-universal.dmg`
- `KiCad-Engine-Setup-Linux-x64.AppImage`
- `KiCad-Engine-Setup-Linux-amd64.deb`
- `KICAD_ENGINE_PAYLOAD.zip`
- `SHA256SUMS.txt`

Build logs and payload build reports are uploaded with artifacts.

## Workflow Behavior

Each platform workflow:

- Builds the clean payload first.
- Runs payload health check.
- Runs optional ripgrep secret scan when `rg` is available.
- Installs local npm dependencies with `npm ci`.
- Builds the platform installer.
- Stages normalized artifacts.
- Generates SHA-256 checksums.
- Uploads artifacts.

`build-all-installers.yml` calls the three platform builders and assembles a combined artifact set.

`release-draft.yml` is manual-only, requires an existing tag, and creates a draft prerelease. It does not publish the release.

## Validation Run

- Workflow YAML parsed successfully with local `js-yaml`.
- Full repo health check: `PASS=97 WARN=0 FAIL=0`.
- Clean payload rebuild: PASS.
- Payload health check: `PASS=97 WARN=0 FAIL=0`.
- Targeted workflow/doc secret scan: no matches.
- Payload secret/private marker scan: no matches.
- Forbidden payload artifact scan: no PDFs, ZIPs, Gerbers, drill files, STEP/STL files, KiCad design files, or `.pyc` files found.
- Recent KiCad design-file modification scan: no recently modified KiCad design files found.

## Remaining Untested Areas

- GitHub-hosted Windows workflow execution.
- GitHub-hosted macOS universal DMG build.
- GitHub-hosted Linux AppImage/DEB build.
- Draft release creation against an existing tag.
- Clean-machine installer smoke tests.
- Signing/notarization release process.

## Next Steps

1. Push the workflows to GitHub.
2. Run `Build All Installers` manually.
3. Inspect uploaded artifacts and `SHA256SUMS.txt`.
4. Create an explicit draft tag if testing `Create Draft Release`.
5. Run `Create Draft Release` manually.
6. Smoke test downloaded artifacts before publishing any release.
