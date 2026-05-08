# GitHub Actions Release Builder

Status: source workflows created. They must be run on GitHub-hosted platform runners before release artifacts are trusted.

## Purpose

The release-builder workflows create KiCad Engine installer artifacts from the clean payload template. They are designed for transparent, manual release preparation and do not publish public releases automatically.

## Workflows

| Workflow | Runner | Purpose |
| --- | --- | --- |
| `.github/workflows/build-installer-windows.yml` | `windows-latest` | Build Windows NSIS EXE. |
| `.github/workflows/build-installer-macos.yml` | `macos-latest` | Build unsigned macOS universal DMG. |
| `.github/workflows/build-installer-linux.yml` | `ubuntu-latest` | Build Linux AppImage and DEB. |
| `.github/workflows/build-all-installers.yml` | all platform runners | Build all installers and upload one combined artifact set. |
| `.github/workflows/release-draft.yml` | all platform runners plus Ubuntu collector | Build all installers and create a draft GitHub release. |

## Build Order

Each platform workflow:

1. Checks out the repo.
2. Sets up Python.
3. Sets up Node.js.
4. Builds `installer/payload/repo-template`.
5. Runs `health_check.py` against the clean payload.
6. Runs an optional `rg` secret scan when ripgrep is available.
7. Installs local npm dependencies with `npm ci`.
8. Builds the platform installer.
9. Normalizes artifact names.
10. Generates `SHA256SUMS.txt`.
11. Uploads artifacts and build logs.

## Artifact Names

The release-builder layer normalizes electron-builder output to:

- `KiCad-Engine-Setup-Windows-x64.exe`
- `KiCad-Engine-Setup-macOS-universal.dmg`
- `KiCad-Engine-Setup-Linux-x64.AppImage`
- `KiCad-Engine-Setup-Linux-amd64.deb`
- `KICAD_ENGINE_PAYLOAD.zip`
- `SHA256SUMS.txt`

Platform build logs and `PAYLOAD_BUILD_REPORT-*.md` are included with artifacts.

## Draft Release Behavior

`release-draft.yml` is manual-only through `workflow_dispatch`.

It:

- Requires an existing tag.
- Refuses missing tags.
- Creates a draft release.
- Marks the draft as prerelease.
- Uploads normalized artifacts, checksums, payload, logs, and payload build reports.

It does not:

- Publish the release.
- Create secrets.
- Require paid services.
- Sign or notarize artifacts.
- Claim production readiness.

## Signing And Trust Limits

Current workflows build unsigned or developer-test artifacts unless future signing secrets are explicitly added.

Before public release:

- Windows should be signed or unsigned status must be clearly documented.
- macOS must be signed, notarized, stapled, and Gatekeeper tested.
- Linux artifacts should have checksums and clean-machine smoke-test logs.
- Release notes must include limitations and verification requirements.

## Secret Handling

No workflow file contains credentials. Do not commit:

- Apple certificates or notarization credentials.
- Windows signing keys.
- API keys.
- AI service credentials.
- GitHub personal tokens.

Use GitHub encrypted secrets only when a future signed release workflow is intentionally designed and reviewed.

## Smoke Testing

The workflows only build artifacts. Human release validation still needs:

- Windows EXE install/uninstall smoke test.
- macOS DMG launch, install, Gatekeeper, and notarization validation.
- Linux AppImage launch test.
- Linux DEB install/uninstall test.
- Payload content audit.
- Verification that installers do not modify installed KiCad app folders or global KiCad libraries.
