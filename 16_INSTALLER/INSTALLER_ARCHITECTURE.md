# Installer Architecture

Status: `PLANNED_NOT_BUILT`

## Purpose

Define the production installer architecture for KiCad Engine without creating binaries in this planning step.

## Product Rule

The installer creates a local KiCad Engine workspace. It does not replace KiCad, bundle KiCad, modify installed KiCad folders, or store AI credentials.

## Architecture Layers

1. Installer UI: lets the user choose an install path and review dependency status.
2. Dependency detection: checks KiCad, `kicad-cli`, Git, Python, Node/npm, VS Code, and platform package managers.
3. Optional install helpers: ask before installing anything and use official package managers where possible.
4. Payload copy: copies only the approved clean workspace template.
5. VS Code setup: opens the installed workspace and points users to prompts and quickstarts.
6. Health check: runs read-only checks and writes a local setup report.
7. Logging: writes setup logs without secrets.

## Current Implementation Roots

- Planning and release coordination: `16_INSTALLER/`
- Electron/source installer implementation: `installer/`
- Clean payload builder: `installer/payload/`
- Setup scripts: `setup/`

Do not migrate or delete implementation roots without a separate migration task.

## Required Safety Properties

- Never write to Program Files KiCad folders or KiCad app bundles.
- Never modify user-global KiCad symbol or footprint library tables.
- Never collect, request, or store Codex, Claude, ChatGPT, OpenAI, Anthropic, GitHub, distributor, or fab-house credentials.
- Ask before installing dependencies.
- Produce logs and health reports that are safe to share publicly.

## Production Exit Criteria

- Payload manifest reviewed.
- Windows, macOS, and Linux builds run on native runners.
- Smoke tests install into disposable folders.
- Checksums generated.
- Signing/notarization status documented.
- Security and license audits complete.

