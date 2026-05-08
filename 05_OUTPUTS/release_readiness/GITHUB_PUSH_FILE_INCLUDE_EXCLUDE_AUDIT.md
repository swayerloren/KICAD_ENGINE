# GitHub Push File Include Exclude Audit

Status: `ACTIVE_AUDIT`

Date: `2026-05-08`

## Scope Decision

The user requested the current KiCad Engine workspace be committed and pushed to a private GitHub repository. The working assumption for staging is:

- include the safe current workspace
- exclude secrets, local configs, lock files, caches, backups, copied-board rehearsal copies, and raw import/source preservation folders

## Included By Default

- Root repo documentation and policy files
- `00_CODEX_START/`
- `01_MEMORY/`
- `02_HISTORY/`
- `03_TOOLS/` except ignored envs, third-party repo clones, caches, and logs
- `04_KICAD_PROJECTS/` except ignored copied rehearsal and lock/temp artifacts
- `05_OUTPUTS/release_readiness/`
- `06_DATASHEETS/` link/metadata structure that is not excluded by current ignore rules
- `07_REFERENCE_DESIGNS/` through `34_PCB_LAYOUT_SANDBOX/` except ignored paths and ignored artifact extensions
- `.github/`, `.prompts/`, `.vscode/`, and safe `.codex/` prompt/docs files

## Excluded By .gitignore

Required credential/temp exclusions added or confirmed:

- `.env`
- `.env.*`
- `*.key`
- `*.token`
- `secrets.*`
- `api_keys.*`
- `local_credentials.*`
- `private_config.*`
- `*.tmp`
- `*.temp`
- `*.log.tmp`
- `*.lck`
- `~*.lck`
- `__pycache__/`
- `*.pyc`
- `node_modules/`
- `.DS_Store`
- `Thumbs.db`
- `fp-info-cache`
- `*.bak`
- `*.old`

Repo-local safe-publication exclusions added or confirmed:

- `99_BACKUPS/`
- `04_KICAD_PROJECTS/active/*/routing_work/*/copied*/`
- `04_KICAD_PROJECTS/active/*/routing_rehearsals/`
- `14_LAYOUT_AUTOMATION/real_board_tests/sample_inputs/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`
- `.codex/config.toml`
- `T_E_M_P/`
- `03_TOOLS/repos/`
- `03_TOOLS/windows/repos/`
- `03_TOOLS/linux/repos/`
- `03_TOOLS/python_envs/`
- `03_TOOLS/node_envs/`
- `05_OUTPUTS/*` except the allowlisted release-readiness files

Existing ignored binary/manufacturing/document artifact extensions:

- `*.pdf`
- `*.zip`
- `*.7z`
- `*.rar`
- `*.gbr`
- `*.drl`
- `*.xln`
- `*.step`
- `*.stp`

## Decision Notes

- `routing_work` is included in general because its markdown logs are part of the project history, but copied-board rehearsal directories under that tree are excluded.
- `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/` is excluded because it is raw preservation evidence, not safe first-push content.
- `14_LAYOUT_AUTOMATION/real_board_tests/sample_inputs/` is excluded because it is copied-board sample input material, not core workspace logic.
- `.codex/config.toml` is excluded as a local machine config file, while `.codex/prompts/` and docs remain included.
- `T_E_M_P/` is excluded as a temp workspace folder.

## Pre-Stage Working Tree Snapshot

- Untracked entries before staging: `272`
- Ignored entries before staging: `199`

## Public Release Note

This audit is for a private GitHub push. It does not mean the repo is safe for public release as-is.
