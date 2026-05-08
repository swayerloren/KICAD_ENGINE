# Linux Installer Plan

Status: `MULTI_DISTRO_PLAN`

## Target

Support Linux users with AppImage, DEB, RPM planning, and manual tar.gz fallback.

## Default Path

`~/KICAD_ENGINE`

## Dependency Checks

- `kicad`
- `kicad-cli`
- `git`
- `python3`
- `node`
- `npm`
- `code`
- package managers: `apt`, `dnf`, `yum`, `pacman`, `flatpak`, `snap`

## Install Strategy

- Detect distro and available package managers.
- Ask before installing anything.
- Prefer official package-manager paths.
- Provide manual instructions when package manager support is unclear.
- Do not modify global KiCad libraries.

## Planned Artifacts

- `KiCad-Engine-Setup-Linux-x64.AppImage`
- `KiCad-Engine-Setup-Linux-amd64.deb`
- Future RPM package after Fedora/RHEL testing.
- Manual tar.gz fallback after payload review.

## Limitations

Linux support must not assume one distro. AppImage is the broad first target; DEB is the Ubuntu/Debian target; RPM requires separate validation.

