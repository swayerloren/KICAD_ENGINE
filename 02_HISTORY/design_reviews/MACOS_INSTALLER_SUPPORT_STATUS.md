# macOS Installer Support Status

Local time: 2026-05-02 20:44 -04:00

## Summary

Status: macOS installer source support added. A macOS installer was not built locally because this session ran on Windows.

No KiCad project files were modified. No tools were installed. No writes were made to a KiCad app bundle or global KiCad libraries.

## Created Or Updated

- `setup/macos/check_macos_requirements.sh`
- `setup/macos/install_missing_macos_tools.sh`
- `setup/macos/open_vscode_workspace.sh`
- `setup/macos/README.md`
- `QUICKSTART_MACOS.md`
- `installer/docs/MACOS_INSTALLER_BUILD.md`
- `installer/docs/MACOS_NOTARIZATION_NOTES.md`
- `installer/payload/manifests/dependencies.macos.json`
- `installer/payload/scripts/macos/check_environment.sh`
- `installer/payload/scripts/macos/README.md`
- `.github/workflows/build-macos-installer.yml`
- `installer/README.md`
- `health_check.py`

The clean installer payload was rebuilt after the source changes.

`health_check.py` was updated to exclude local package/build directories such as `node_modules`, `build`, and `dist` from secret scanning so third-party dependency docs and generated build output do not create false positives in a development checkout. The payload still excludes these directories.

## macOS Dependency Detection Added

Detection now covers:

- KiCad app bundle at `/Applications/KiCad/KiCad.app`.
- Alternate KiCad app bundle at `/Applications/KiCad.app`.
- App-bundle `kicad-cli` at `/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli`.
- Alternate app-bundle `kicad-cli` at `/Applications/KiCad.app/Contents/MacOS/kicad-cli`.
- `kicad-cli` on `PATH`.
- Git.
- Python as `python3` or `python`.
- Node.
- npm.
- VS Code through `code`, `/Applications/Visual Studio Code.app`, or `~/Applications/Visual Studio Code.app`.
- Homebrew.

## What Can Be Built Locally

From this Windows machine:

- Source files and docs can be created and validated.
- The clean payload can be rebuilt.
- JSON manifests can be parsed.
- Shell scripts can be syntax-checked with Git Bash.
- Electron config can be inspected.
- Windows installer artifacts can be built.

macOS DMG/PKG artifacts cannot be built or smoke-tested locally from this Windows session.

## What Requires macOS Runner

The following require a macOS machine or GitHub Actions macOS runner:

- `npm run build:mac`.
- DMG generation.
- PKG generation.
- Gatekeeper assessment.
- `codesign` verification.
- `pkgutil --check-signature`.
- `xcrun stapler` validation.
- Real macOS installer smoke testing.

## GitHub Actions Workflow

Created:

`.github/workflows/build-macos-installer.yml`

The workflow:

- Runs on `macos-latest`.
- Builds the clean payload.
- Runs payload health check.
- Installs local npm dependencies with `npm ci`.
- Builds unsigned macOS artifacts with `CSC_IDENTITY_AUTO_DISCOVERY=false`.
- Uploads `installer/build/macos/**` as an artifact.

It does not install KiCad, modify KiCad, collect AI credentials, or write global KiCad libraries.

## Signing And Notarization Limitations

Current macOS CI workflow is unsigned. It is suitable for source validation and internal smoke testing only.

Public release still requires:

- Apple Developer ID Application certificate.
- Apple Developer ID Installer certificate for signed PKG artifacts.
- Secure CI keychain setup.
- Notarization credentials through GitHub secrets or a local secure keychain.
- Notarization submission.
- Stapling.
- Gatekeeper validation on a clean macOS machine.
- Published checksums.

No Apple credentials were added to the repo.

## Validation Run

- `dependencies.macos.json`: JSON parse PASS.
- `package.json`: JSON parse PASS.
- `electron-builder.yml`: macOS `dmg` and `pkg` targets confirmed for `x64` and `arm64`.
- Git Bash `bash -n` syntax check: PASS for macOS setup scripts and packaged-payload macOS script.
- Clean payload rebuild: PASS.
- Payload health check: `PASS=97 WARN=0 FAIL=0`.
- Full repo health check after excluding local package/build directories: `PASS=97 WARN=0 FAIL=0`.
- Payload secret/private marker scan: no matches.
- Forbidden payload artifact scan: no PDFs, ZIPs, Gerbers, drill files, STEP/STL files, KiCad design files, or `.pyc` files found.
- Recent KiCad design-file modification scan: no recently modified KiCad design files found.

## Next Steps

1. Run `.github/workflows/build-macos-installer.yml` on GitHub.
2. Review any macOS-specific build failures from electron-builder.
3. Smoke test the produced unsigned DMG/PKG on a disposable macOS account or VM.
4. Add icon resources before public release.
5. Design and test signing/notarization with repository secrets.
6. Validate that the installer refuses KiCad app-bundle paths as install targets.
7. Record clean-machine smoke test results before claiming macOS installer readiness.
