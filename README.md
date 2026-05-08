# KiCad Engine

KiCad Engine is a local-first workspace for AI-assisted KiCad engineering, review, verification, and release preparation. It is designed to help humans plus agents such as Codex or Claude work inside a structured repo with explicit safety gates, memory, history, validation tools, and review artifacts.

## Current Status

- Repository status: `EXPERIMENTAL_INTERNAL_ALPHA`
- GitHub visibility: `PRIVATE`
- Public release status: `NOT_READY`
- Fabrication status: `NOT_FABRICATION_READY`
- Active project: [ESP32_CSI_WIFI_NODE](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/README.md)
- Exact PCB warning: `ESP32_CSI_WIFI_NODE is not fabrication-ready.`

## What Is Complete

- The GitHub repo exists and was pushed successfully.
- The active project exists under `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`.
- A real KiCad PCB file exists for the active project.
- PCB placement exists.
- Partial routing exists.
- Current DRC state is `0` rule violations, but unconnected items remain.

## What Is Not Complete

- USB data nets remain unresolved.
- Some control and power connectivity still needs review.
- Unconnected items remain on the live PCB.
- Final fabrication outputs are not approved.
- The repository is not ready for public release.

## Start Here

### Humans

1. Read [START_HERE.md](START_HERE.md).
2. Read [CURRENT_STATUS.md](CURRENT_STATUS.md).
3. Read [PROJECTS_INDEX.md](PROJECTS_INDEX.md).
4. If you are reviewing the live board, open [FINAL_PCB_VISUAL_REVIEW_PACKET.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_PCB_VISUAL_REVIEW_PACKET.md).

### Codex Or Claude

1. Read [AGENTS.md](AGENTS.md).
2. Read [README_GPT.md](README_GPT.md).
3. Read [FOR CHAT GPT.MD](FOR%20CHAT%20GPT.MD).
4. Read [00_CODEX_START/START_HERE.md](00_CODEX_START/START_HERE.md).
5. Read [00_CODEX_START/GITHUB_NAVIGATION.md](00_CODEX_START/GITHUB_NAVIGATION.md).
6. Read [00_CODEX_START/CURRENT_PROJECT.md](00_CODEX_START/CURRENT_PROJECT.md).

## Folder Map

The full map is in [FOLDER_MAP.md](FOLDER_MAP.md). The shortest useful summary is:

- `00_CODEX_START/`: startup rules, workflow gates, repo navigation, current status
- `01_MEMORY/`: durable reusable memory
- `02_HISTORY/`: sessions, command logs, failed attempts, issue logs, AI-quality evidence
- `03_TOOLS/`: scripts and automation support
- `04_KICAD_PROJECTS/`: active, archive, and template KiCad projects
- `05_OUTPUTS/`: release-readiness and generated output summaries
- `09_ACCURACY_ENGINE/`: verification and anti-hallucination rules
- `14_LAYOUT_AUTOMATION/`: real-board routing and placement planning rules
- `34_PCB_LAYOUT_SANDBOX/`: pre-PCB-edit layout-variant planning and gating
- `99_BACKUPS/`: local-only pre-edit backups, intentionally excluded from Git

## Active Project Snapshot

Latest known live board state for `ESP32_CSI_WIFI_NODE`:

- PCB hash: `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`
- Board outline: `60.0 mm x 95.0 mm`
- Footprints: `43`
- Tracks: `74`
- Vias: `32`
- Zones: `2`
- DRC: `0` violations, `17` unconnected items
- Detectable unrouted nets: `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`

See:

- [CURRENT_STATUS.md](CURRENT_STATUS.md)
- [PROJECTS_INDEX.md](PROJECTS_INDEX.md)
- [CURRENT_PROJECT_STATE.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md)
- [CURRENT_BLOCKERS.md](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md)

## Safety Rules

- Do not treat any AI output as fabrication approval.
- Do not edit KiCad design files without active-project confirmation, backup, rollback plan, and verification plan.
- Do not treat DRC `0` violations as proof of completion when unconnected items or unrouted nets remain.
- Do not commit secrets, `.env` files, lock files, caches, or local-only rehearsal artifacts.
- Do not make the repository public until the public-release blockers are closed.

## GitHub Release Status

- Private GitHub push: `YES`
- Public GitHub release ready: `NO`
- Large local-only artifacts are intentionally excluded from Git.
- Backups, copied-board rehearsals, raw imports, caches, and env/config files remain excluded by `.gitignore`.

See:

- [PUBLIC_RELEASE_STATUS.md](PUBLIC_RELEASE_STATUS.md)
- [05_OUTPUTS/release_readiness/GITHUB_PUSH_REPORT.md](05_OUTPUTS/release_readiness/GITHUB_PUSH_REPORT.md)
- [05_OUTPUTS/release_readiness/GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md](05_OUTPUTS/release_readiness/GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md)

## Repo Navigation

- High-level repo index: [REPO_INDEX.md](REPO_INDEX.md)
- Tool catalog: [TOOLS_INDEX.md](TOOLS_INDEX.md)
- Workflow catalog: [WORKFLOWS_INDEX.md](WORKFLOWS_INDEX.md)
- Project catalog: [PROJECTS_INDEX.md](PROJECTS_INDEX.md)
- GitHub navigation for agents: [00_CODEX_START/GITHUB_NAVIGATION.md](00_CODEX_START/GITHUB_NAVIGATION.md)

## Public Release Blockers

Current blockers before making the repo public are tracked in:

- [PUBLIC_RELEASE_STATUS.md](PUBLIC_RELEASE_STATUS.md)
- [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md)
- [21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md](21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md)

## License

The repository is under the MIT License. Third-party assets, vendor documents, and linked sources may have their own redistribution terms.
