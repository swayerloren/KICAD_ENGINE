# Payload Content Rules

Status: active rules for building `installer/payload/repo-template`.

The installer payload is a clean KiCad Engine workspace template. It is not a copy of the developer's working tree.

## Include

The payload must include these user-facing workspace areas:

- `AGENTS.md`
- `README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `START_HERE_FOR_USERS.md`
- `START_HERE_FOR_AI_AGENTS.md`
- `QUICKSTART_WINDOWS.md`
- `QUICKSTART_MACOS.md`
- `QUICKSTART_LINUX.md`
- `INSTALLER_USER_GUIDE.md`
- `USER_MANUAL.md`
- `FAQ.md`
- `TROUBLESHOOTING.md`
- `docs/`
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

The payload may also include small supporting public docs and templates when they are first-party, useful to users, and pass the exclusion rules.

## Exclude

The payload must not include:

- Personal local paths specific to one developer, except examples clearly marked as examples.
- Secrets, tokens, passwords, API keys, license keys, private keys, SSH keys, or `.env` files.
- Old development command logs and session logs not useful to end users.
- Private project memory or private project history.
- Large generated outputs.
- Final fabrication packages.
- `NOT_FINAL` generated outputs unless an intentionally public sample output is explicitly approved.
- Copyrighted PDFs or vendor documents unless redistribution has been confirmed.
- User-specific KiCad project files unless they are approved safe samples.
- Third-party cloned repositories.
- Python virtual environments, Node environments, package caches, build caches, and `__pycache__`.
- Screenshots, GUI logs, installer build artifacts, and local backup folders.

## P0 Public-Release Exclusion Gate

The full repo production-quality audit found that public release safety depends on excluding local/generated material. The payload builder and any manual release process must exclude these paths by default:

- `03_TOOLS/python_envs/`
- `03_TOOLS/node_envs/`
- `03_TOOLS/repos/`
- `03_TOOLS/windows/repos/`
- `03_TOOLS/linux/repos/`
- `03_TOOLS/tool_logs/`
- `03_TOOLS/windows/logs/`
- `03_TOOLS/linux/logs/`
- `05_OUTPUTS/`
- `99_BACKUPS/`
- `installer/build/`
- `installer/dist/`
- `installer/node_modules/`
- `installer/payload/repo-template/`
- `installer/payload/payload.manifest.json`
- `installer/payload/PAYLOAD_BUILD_REPORT.md`
- `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_*/`

The current local Espressif PDFs under `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/` are blocked from public payloads until redistribution rights are confirmed or they are converted to link-only records.

## Clean Template Replacements

Some source files are intentionally replaced in the payload instead of copied:

- `.codex/config.toml` is not copied. The payload gets `.codex/config.example.toml`.
- `.claude/` is created even when the source workspace has no Claude-specific local folder.
- `00_CODEX_START/CURRENT_PROJECT.md` is reset to `NONE`.
- `00_CODEX_START/PROJECT_INDEX.md`, `TOOL_INDEX.md`, and `REPO_MAP.md` are reset to fresh-install template state.
- `01_MEMORY/` is generated with generic placeholder memory and no private project memory.
- `02_HISTORY/` is generated as empty history scaffolding.
- `04_KICAD_PROJECTS/active/` and `04_KICAD_PROJECTS/archive/` are empty.
- `05_OUTPUTS/` is empty except for README/scaffold folders.
- `README_GPT.md` and `FOR CHAT GPT.MD` are generated as fresh-install handoff files instead of copying development history.

## Datasheet Rules

- Copy datasheet scaffolding, source lists, metadata, indexes, and policy docs.
- Do not copy PDFs by default.
- Do not copy migrated legacy datasheet folders by default.
- Keep `99_UNSORTED_INBOX/` as an empty user inbox with guidance.
- Use link-only metadata unless redistribution is confirmed.

## Tool Rules

- Copy first-party tool scripts and docs.
- Do not copy `03_TOOLS/repos/`.
- Do not copy `03_TOOLS/python_envs/`.
- Do not copy `03_TOOLS/node_envs/`.
- Do not copy `03_TOOLS/tool_logs/`.
- Do not copy `03_TOOLS/windows/repos/`, `03_TOOLS/windows/logs/`, or `03_TOOLS/linux/logs/`.
- Do not copy generated KiCad library indexes; users should regenerate them locally.

## Manifest Rules

Each payload build must create:

- `installer/payload/payload.manifest.json`
- `installer/payload/PAYLOAD_BUILD_REPORT.md`

The manifest must contain file paths relative to `repo-template`, file sizes, SHA-256 hashes, total file count, total byte count, generated-file list, and exclusion summary. It must not record developer-specific absolute paths.
