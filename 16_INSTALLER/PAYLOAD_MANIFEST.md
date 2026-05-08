# Installer Payload Manifest

Status: `MANIFEST_RULES`

## Purpose

Define what the installer is allowed to copy into a new KiCad Engine workspace.

## Approved Payload Source

Use `installer/payload/repo-template/` after running the payload build process.

## Required Payload Areas

- `AGENTS.md`
- `README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `START_HERE_FOR_USERS.md`
- `START_HERE_FOR_AI_AGENTS.md`
- `.vscode/`
- `.codex/`
- `.claude/`
- `.prompts/`
- `00_CODEX_START/`
- `01_MEMORY/`
- `02_HISTORY/`
- `03_TOOLS/`
- `04_KICAD_PROJECTS/`
- `05_OUTPUTS/`
- `06_DATASHEETS/`
- `08_COMPONENT_DATABASE/`
- `09_ACCURACY_ENGINE/`
- `10_KNOWLEDGE_BASE/`
- `11_LIBRARY_FACTORY/`
- `12_REFERENCE_DESIGN_LIBRARY/`
- `13_PART_INGESTION/`
- `14_LAYOUT_AUTOMATION/`
- `15_BENCHMARKS/`
- `setup/`
- `health_check.py`
- `health_check.ps1`
- `LICENSE`
- `DISCLAIMER.md`
- `SECURITY.md`

## Exclusions

- Secrets, API keys, tokens, private keys, certificates.
- Local personal logs not useful to end users.
- Third-party tool repos unless explicitly reviewed.
- Python/Node environments and dependency caches.
- Final fab packages.
- Large generated outputs.
- Copyrighted PDFs or design files unless redistribution is confirmed.
- User-specific KiCad projects unless explicitly safe samples.

## Manifest Requirement

Every payload build must generate:

- `payload.manifest.json`
- file count and size summary
- `PAYLOAD_BUILD_REPORT.md`

