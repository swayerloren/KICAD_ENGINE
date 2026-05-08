# KiCad Engine Installer

Status: first real cross-platform Electron installer project. Installer binaries are not production-ready until platform builds and smoke tests pass.

The installer creates a local KiCad Engine workspace from a clean payload template, checks dependencies, optionally offers package-manager installs after confirmation, runs the workspace health check, and opens VS Code.

It does not replace KiCad. It uses the KiCad app already installed on the user's machine. If KiCad is missing, it offers official package-manager or manual install paths.

## Goals

- Create a local `KICAD_ENGINE` repo/workspace for the user.
- Check the user's installed KiCad app.
- Use the user's installed KiCad app; do not bundle KiCad in v1.
- Optionally install missing free requirements after explicit user confirmation.
- Configure the VS Code workspace files already present in the repo.
- Install prompt packs by copying or unpacking repo files into `.prompts`.
- Create datasheet and component database scaffolding.
- Run the repo health check.
- Open VS Code at the installed workspace.

## Non-Goals

- Do not claim production readiness until builds and smoke tests pass.
- Do not bundle KiCad in v1.
- Do not modify `C:\Program Files\KiCad`, `/Applications/KiCad`, `/usr/share/kicad`, or other installed KiCad app folders.
- Do not modify installed KiCad folders.
- Do not store Codex, Claude, OpenAI, Anthropic, GitHub, distributor, or fab-house credentials.
- Do not require paid APIs.
- Do not silently install paid tools.
- Do not make fabrication outputs or label anything final.

## Project Layout

- `package.json`: npm scripts and Electron dependencies.
- `electron-builder.yml`: Windows, macOS, and Linux packaging targets.
- `src/main.js`: Electron main process and IPC handlers.
- `src/preload.js`: safe renderer bridge.
- `src/renderer/`: installer GUI.
- `src/installer-core/`: OS detection, dependency checks, workspace copy, health check, command runner, and log writer.
- `payload/repo-template/`: clean KiCad Engine workspace template copied to the user's machine.
- `payload/manifests/`: dependency and payload manifests.
- `payload/scripts/`: transparent platform fallback scripts.
- `build/`: platform output folders.
- `docs/`: build, security, and user-flow docs.

## npm Scripts

Run from `installer/` after installing npm dependencies:

```bash
npm run dev
npm run build:win
npm run build:mac
npm run build:linux
npm run package
```

This repo does not run `npm install` automatically.

## Versioned Milestone Plan

| Version | Milestone | Exit Criteria |
| --- | --- | --- |
| v0.1 | Repo template | Startup docs, repo layout, memory/history rules, safe output folders, and initial README are present. |
| v0.2 | Windows setup scripts | Windows setup/check/install wrapper scripts exist, ask before installs, and write setup reports. |
| v0.3 | KiCad app audit | Installed KiCad app audit scripts and docs can inventory local KiCad read-only. |
| v0.4 | Datasheet/component database | Datasheet scaffolding, source policies, component schemas, and placeholder records exist. |
| v0.5 | VS Code prompt packs | VS Code workspace files, Codex prompts, Claude prompts, and shared standards exist. |
| v0.6 | Windows installer | Signed Windows installer creates workspace, checks KiCad, runs health check, and opens VS Code. |
| v0.7 | macOS/Linux setup | macOS and Linux setup flows are tested, with package-manager detection and health checks. |
| v1.0 | Public GitHub release | Public docs, license, release notes, signed artifacts/checksums, clean payload, and demo workflow are ready. |

Current status: source project created. Packaging dependencies are declared but not installed in this session.

## Document Set

- `INSTALLER_ARCHITECTURE.md`
- `WINDOWS_EXE_PLAN.md`
- `MACOS_DMG_PLAN.md`
- `LINUX_APPIMAGE_DEB_RPM_PLAN.md`
- `PAYLOAD_MANIFEST.md`
- `SECURITY_MODEL.md`
- `SIGNING_AND_RELEASE_NOTES.md`
- `UPDATE_MODEL.md`
- `USER_FLOW.md`
- `docs/WINDOWS_INSTALLER_BUILD.md`
- `docs/MACOS_INSTALLER_BUILD.md`
- `docs/MACOS_NOTARIZATION_NOTES.md`
- `docs/LINUX_INSTALLER_BUILD.md`
- `docs/LINUX_PACKAGE_MANAGER_MATRIX.md`
- `docs/GITHUB_ACTIONS_RELEASE_BUILDER.md`
- `docs/INSTALLER_SECURITY_MODEL.md`
- `docs/INSTALLER_USER_FLOW.md`

## Clean Payload Template

The installer payload is generated under:

- `payload/repo-template/`
- `payload/payload.manifest.json`
- `payload/PAYLOAD_BUILD_REPORT.md`

Build it from the repo root:

```powershell
.\installer\payload\build_payload.ps1
```

or:

```bash
python installer/payload/build_payload.py
```

Payload rules are documented in `payload/PAYLOAD_CONTENT_RULES.md` and `payload/PAYLOAD_BUILD_SCRIPT.md`.

The builder excludes third-party cloned repos, Python/Node environments, generated outputs, backups, screenshots/logs, active projects, downloaded PDFs, and machine-local Codex config. It generates clean replacements for stateful files such as `README_GPT.md`, `FOR CHAT GPT.MD`, `00_CODEX_START/CURRENT_PROJECT.md`, memory, history, empty project folders, and output scaffolding.

## macOS Build Support

macOS installer artifacts must be built on macOS. This repo includes `.github/workflows/build-macos-installer.yml` for unsigned CI builds on a macOS runner. Public macOS releases still require Apple Developer ID signing, notarization, Gatekeeper validation, checksums, and clean-machine smoke testing.

## Linux Build Support

Linux installer artifacts should be built on Linux. This repo includes `.github/workflows/build-linux-installer.yml` for AppImage and DEB builds on an Ubuntu runner. RPM is documented as a future Fedora/RHEL strategy, and manual `tar.gz` extraction remains the fallback for distros that do not fit the first package targets.

## GitHub Actions Release Builder

Canonical release-builder workflows live under `.github/workflows`:

- `build-installer-windows.yml`
- `build-installer-macos.yml`
- `build-installer-linux.yml`
- `build-all-installers.yml`
- `release-draft.yml`

They build the clean payload first, run health checks, run an optional ripgrep secret scan, normalize artifact names, generate `SHA256SUMS.txt`, and upload logs. The draft release workflow is manual-only and creates a draft release, not a published release.
