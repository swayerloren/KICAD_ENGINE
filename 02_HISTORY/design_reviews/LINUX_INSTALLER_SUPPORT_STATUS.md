# Linux Installer Support Status

Local time: 2026-05-02 20:55 -04:00

## Summary

Status: Linux installer source support added. Linux artifacts were not built locally because this session ran on Windows.

No KiCad project files were modified. No tools were installed. No writes were made to system KiCad folders, global KiCad libraries, or user-global KiCad library tables.

## Created Or Updated

- `setup/linux/check_linux_requirements.sh`
- `setup/linux/install_missing_linux_tools.sh`
- `setup/linux/open_vscode_workspace.sh`
- `setup/linux/detect_linux_package_manager.sh`
- `setup/linux/README.md`
- `QUICKSTART_LINUX.md`
- `installer/docs/LINUX_INSTALLER_BUILD.md`
- `installer/docs/LINUX_PACKAGE_MANAGER_MATRIX.md`
- `installer/payload/manifests/dependencies.linux.json`
- `installer/payload/scripts/linux/check_environment.sh`
- `installer/payload/scripts/linux/README.md`
- `.github/workflows/build-linux-installer.yml`
- `installer/README.md`

The clean installer payload was rebuilt after the source changes.

## Supported Distro Strategy

First Linux release strategy:

- AppImage: broad-compatibility package target.
- DEB: Ubuntu/Debian package target.
- RPM: documented Fedora/RHEL strategy, not enabled as a first package target until tested.
- tar.gz/manual fallback: extract/copy clean workspace template and run Linux setup scripts.

Package-manager detection covers:

- `apt-get`: Ubuntu, Debian, Linux Mint, Pop!_OS.
- `dnf`: Fedora and modern RHEL-family systems.
- `yum`: older RHEL/CentOS-family systems.
- `pacman`: Arch and Manjaro.
- `flatpak`: cross-distro desktop package fallback.
- `snap`: snap-enabled distros.

## Linux Dependency Detection Added

Detection now covers:

- `kicad`.
- `kicad-cli`.
- Git.
- Python as `python3` or `python`.
- Node.
- npm.
- VS Code as `code` plus common Flatpak/snap paths in the installer manifest.
- Package managers: `apt-get`, `dnf`, `yum`, `pacman`, `flatpak`, and `snap`.
- Distro metadata from `/etc/os-release` in setup scripts.

## Tested Commands

Tested locally on Windows using available tooling:

- Git Bash `bash -n` syntax check for Linux setup scripts and packaged-payload Linux script: PASS.
- `dependencies.linux.json` JSON parse: PASS.
- `package.json` JSON parse: PASS.
- `electron-builder.yml` Linux `AppImage` and `deb` targets confirmed for `x64`.
- Clean payload rebuild: PASS.
- Payload health check: `PASS=97 WARN=0 FAIL=0`.
- Full repo health check: `PASS=97 WARN=0 FAIL=0`.
- Payload secret/private marker scan: no matches.
- Forbidden payload artifact scan: no PDFs, ZIPs, Gerbers, drill files, STEP/STL files, KiCad design files, or `.pyc` files found.
- Recent KiCad design-file modification scan: no recently modified KiCad design files found.

## Untested Areas

These require a Linux runner, VM, or real Linux machine:

- `npm run build:linux`.
- AppImage generation.
- DEB generation.
- AppImage launch behavior.
- DEB install/uninstall behavior.
- VS Code opening behavior under desktop Linux.
- `apt`, `dnf`, `yum`, `pacman`, `flatpak`, and `snap` install prompts on real distros.
- WSL behavior.
- FUSE/AppImage behavior on distros with different FUSE defaults.
- RPM packaging and signing.

## AppImage Notes

AppImage is the first broad-compatibility target. It should be tested on:

- Ubuntu LTS.
- Debian stable.
- Fedora current.
- One Arch-family distro if practical.

Do not assume AppImage desktop integration or FUSE availability until tested.

## DEB Notes

DEB is the first package-manager-native target for Ubuntu/Debian. It must be tested for:

- Install path.
- User-writable workspace behavior.
- Uninstall behavior.
- Dependency metadata.
- No writes to global KiCad libraries.

## RPM Notes

RPM is documented but not enabled as a first build target. Before enabling RPM artifacts:

- Test on Fedora.
- Test on one RHEL-compatible distro if possible.
- Review package metadata and dependencies.
- Validate install/uninstall behavior.
- Decide signing and repository distribution strategy.

## Manual tar.gz Fallback

Manual fallback should:

1. Provide a clean repo-template or release source archive.
2. Let the user extract to `~/KICAD_ENGINE`.
3. Run `bash setup/linux/check_linux_requirements.sh`.
4. Run `bash setup/linux/setup_linux.sh`.
5. Open the workspace in VS Code.

Fallback archives must not contain restricted PDFs, generated final fab outputs, credentials, package caches, build outputs, or user-specific KiCad projects.

## Safety Notes

- Linux setup scripts ask before install attempts.
- For root-required package managers, the install helper prints exact commands unless it is already running with root privileges.
- No silent credential collection exists.
- No global KiCad library writes are performed.
- No one-distro assumption is made.

## Next Steps

1. Run `.github/workflows/build-linux-installer.yml` on GitHub.
2. Review any Linux-specific electron-builder failures.
3. Smoke test AppImage on Ubuntu/Debian and one non-apt distro.
4. Smoke test DEB on Ubuntu/Debian.
5. Validate package-manager prompts on apt, dnf, pacman, Flatpak, and snap systems.
6. Add icon resources before public release.
7. Decide whether and when to enable RPM artifact generation.
8. Record clean-machine smoke test results before claiming Linux installer readiness.
