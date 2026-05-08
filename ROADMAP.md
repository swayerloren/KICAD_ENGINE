# Roadmap

This roadmap is realistic and subject to change. It does not claim that KiCad Engine is complete.

## v0.1 Repo Template

- Establish repo layout.
- Establish startup, memory, history, safety, and backup rules.
- Add baseline README and workflow docs.

## v0.2 Windows Setup Scripts

- Add safe Windows setup and requirement checks.
- Add opt-in `winget` installer wrapper.
- Add top-level health checks.

## v0.3 KiCad App Audit

- Audit installed KiCad app read-only.
- Map KiCad 9 Windows paths.
- Document `kicad-cli` usage and library discovery.

## v0.4 Datasheet And Component Database

- Build scalable datasheet library structure.
- Add source, copyright, and link-only policies.
- Add component database schemas and placeholders.
- Add verified records only where sources support them.

## v0.5 VS Code Prompt Packs

- Add VS Code workspace files.
- Add Codex prompts.
- Add Claude prompts.
- Add shared safety and verification standards.

## v0.6 Windows Installer

- Design and later build a Windows installer.
- Use installed KiCad; do not bundle KiCad.
- Run health checks.
- Open VS Code.

## v0.7 macOS/Linux Setup

- Test macOS and Linux setup scripts.
- Improve platform-specific KiCad discovery.
- Validate package-manager flows.

## v1.0 Public GitHub Release

- Complete release checklist.
- Verify license and attribution.
- Review third-party tool licenses.
- Remove or link-only restricted datasheets.
- Demonstrate a safe sample workflow.
- Publish release notes and checksums.

## Longer-Term Ideas

- Better KiCad library indexing.
- Safer project-diff tools.
- Stronger BOM and datasheet coverage checks.
- More verified component records.
- Better GUI screenshot review without unsafe automation.
- CI-friendly headless validation examples.
