# GitHub Push Plan

Generated: `2026-05-12`

## Intent

Commit and push safe non-design `KICAD_ENGINE` repo changes only.

KiCad design files are explicitly not approved in this prompt and must remain
unstaged.

## Preconditions Met

- repo-integrity rerun classification:
  `REPO_READY_TO_COMMIT_AND_PUSH_EXCLUDING_DIRTY_KICAD_FILES`
- branch expected: `main`
- remote expected: `https://github.com/swayerloren/KICAD_ENGINE.git`
- `.sfdx/` removed and ignored
- no high-confidence secrets found

## Staging Strategy

Use explicit safe staging only.

Include only non-design repo/documentation/tooling changes from approved areas
such as:

- `.github/`
- `.prompts/`
- `00_CODEX_START/`
- `01_MEMORY/`
- `02_HISTORY/`
- `03_TOOLS/` safe docs/scripts/calculators/integrations only
- `05_OUTPUTS/release_readiness/`
- `06_DATASHEETS/` indexes/docs only
- `07_REFERENCE_DESIGNS/`
- `08_COMPONENT_DATABASE/`
- `09_ACCURACY_ENGINE/`
- `10_KNOWLEDGE_BASE/`
- `11_LIBRARY_FACTORY/`
- `17_RELEASE_BUILD/`
- `20_CI_CD/`
- `21_LICENSE_ATTRIBUTION/` docs only
- `24_FAB_PROFILES/`
- `25_VENDOR_DATABASE/`
- `26_AGENT_QUALITY/`
- `29_FOOTPRINT_GAP_ANALYSIS/`
- `30_SUPPLIER_FOOTPRINT_MATCHES/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/`
- `33_KICAD_GUI_AUTOMATION/`
- `33_PCB_PRELAYOUT_ENGINE/`
- `34_SCHEMATIC_QUALITY_ENGINE/`
- `35_FOOTPRINT_PACKAGE_ENGINE/`
- root docs such as `README.md`, `README_GPT.md`, `AGENTS.md`, `START_HERE_FOR_AI_AGENTS.md`, `THIRD_PARTY_TOOLS_ATTRIBUTION.md`, `.gitignore`

Exclude:

- all `04_KICAD_PROJECTS/`
- all KiCad design files
- backups
- local envs
- tool caches
- vendor repo copies
- quarantine/raw copied payloads
- large binaries

## Commit / Push

Commit message:

`Update KiCad Engine knowledge base and migration indexes`

Push command:

`git push -u origin main`

## Required Final Checks Before Commit

1. staged KiCad design files = `0`
2. staged file count = `1009`
3. staged files over `50 MB` = `0`
4. staged `.sfdx/` paths = `0`
5. staged ignored/local-generated folders = `0`
6. staged raw extraction captures = `0`
7. post-push report/log placeholders excluded from commit = `YES`
