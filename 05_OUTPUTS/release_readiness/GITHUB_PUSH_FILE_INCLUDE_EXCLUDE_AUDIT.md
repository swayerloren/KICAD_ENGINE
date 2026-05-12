# GitHub Push File Include / Exclude Audit

Generated: `2026-05-12`

Status: `SAFE_STAGE_SCOPE_DEFINED`

## Branch / Remote

- branch: `main`
- remote: `https://github.com/swayerloren/KICAD_ENGINE.git`

## Hard Exclusions

These must not be staged:

- `*.kicad_sch`
- `*.kicad_pcb`
- `*.kicad_pro`
- `.sfdx/`
- `99_BACKUPS/`
- `knowledge_scrape/`
- `node_modules/`
- `.venv/`
- `venv/`
- `__pycache__/`
- `installer/build/`
- `installer/node_modules/`
- `03_TOOLS/python_envs/`
- `03_TOOLS/node_envs/`
- `03_TOOLS/repos/`
- `21_LICENSE_ATTRIBUTION/license_risk_reviews/`
- files over `50 MB`

## Explicit Safe Scope

The safe push scope for this task is limited to non-design repo content such as:

- startup/router docs and indexes
- memory/history docs and audit records
- tooling scripts and script READMEs
- release-readiness reports
- knowledge-base and accuracy-engine docs
- canonical source-registry/index files
- non-design documentation and workflow files

## Working-Tree Exclusions Applied

Explicitly excluded from staging in this task:

- all `04_KICAD_PROJECTS/` paths
- the preexisting dirty schematic file
- project reports, project memory, project verification assets, and project templates
- quarantine/raw copied payload trees
- `02_HISTORY/knowledge_scrape_migration/datasheet_extraction_logs/`
- `*.body.txt`
- `*.raw.txt`
- post-push-only files:
  `05_OUTPUTS/release_readiness/GITHUB_PUSH_REPORT.md`,
  `02_HISTORY/sessions/GITHUB_POST_KNOWLEDGE_MIGRATION_PUSH_SESSION.md`,
  `02_HISTORY/command_logs/GITHUB_POST_KNOWLEDGE_MIGRATION_PUSH_COMMANDS.md`
- local environments and generated installers

## Final Safe Stage Set

- candidate selected files during first filtering pass: `695`
- final staged files after direct staging cleanup: `1009`
- staged raw extraction captures after cleanup: `0`
- staged post-push placeholder/report files after cleanup: `0`

Representative rejected reasons:

- `EXCLUDE_PREFIX`: project paths, local envs, repos, quarantine, backups
- `EXCLUDE_EXT`: KiCad design files and heavy binary extensions
- `NOT_IN_SAFE_SCOPE`: root/workspace items outside the approved push scope

## KiCad Design File Protection

Required result for this task:

- staged `.kicad_sch`: `0`
- staged `.kicad_pcb`: `0`
- staged `.kicad_pro`: `0`

The preexisting dirty design file remains out of scope:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

## Conclusion

The include/exclude rules are tight enough for a safe non-design push, provided
the final staged set is checked again before commit.
