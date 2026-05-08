# Global Memory

Durable workspace-wide rules for AI-assisted KiCad engineering.

## Workspace Purpose
- This workspace is for AI-assisted KiCad design, review, verification, and fabrication prep.
- Codex should operate from `KICAD_ENGINE` unless working inside a specific project.
- Preserve clean separation between tools, projects, memory, history, outputs, datasheets, and backups.

## Trust And Verification
- Never trust AI-only review for fabrication.
- Always verify with KiCad ERC/DRC and visual review.
- Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.
- Treat missing or blocked verification as a release blocker, not a minor note.

## Workspace Separation
- Tools and tool repositories belong in `03_TOOLS/`.
- Active projects belong in `04_KICAD_PROJECTS/active/`.
- Durable decisions belong in `01_MEMORY/`.
- Session notes, command logs, reviews, and reports belong in `02_HISTORY/`.
- Generated outputs belong in `05_OUTPUTS/` or approved project output folders.
- Datasheets belong in `06_DATASHEETS/` or approved project datasheet folders.
- Backups before edits belong in `99_BACKUPS/pre_codex_edits/`.

## Current Durable State
- Workspace bootstrapped.
- No active project selected unless `00_CODEX_START/CURRENT_PROJECT.md` says otherwise.
- No external repositories installed by bootstrap.
- No MCP tools configured by bootstrap.
- Do not install tools, clone repositories, or configure MCP unless explicitly requested.
- Private GitHub publication must use explicit ignore rules for local configs, env files, backups, copied-board rehearsal copies, raw imported originals, lock files, tool caches, and large local build artifacts before the first commit.
- A successful private GitHub push is not evidence of public-release readiness; public publication stays blocked until the release checklist, license audit, and repo-hygiene review all pass.
- After GitHub publication exists, the repo must maintain a GitHub-facing navigation layer that stays consistent with live project truth: `README.md`, `START_HERE.md`, `REPO_INDEX.md`, `FOLDER_MAP.md`, `PROJECTS_INDEX.md`, `TOOLS_INDEX.md`, `WORKFLOWS_INDEX.md`, `CURRENT_STATUS.md`, `PUBLIC_RELEASE_STATUS.md`, and the `.github/` templates.
- GitHub-facing root indexes should include concrete command examples, safety boundaries, and current blocker summaries when those details are central to understanding the repo; pointer-only summaries are not enough once the repo is already published.
- The root `README.md` must act as the public-facing front door for the repo, not just a metadata index. It should explicitly explain the AI-assisted KiCad workflow, what the repo is and is not, current board warnings, routing-quality expectations, manufacturing/export guardrails, and how Codex or Claude should be prompted from VS Code.
- GitHub dev infrastructure for this repo is intentionally read-only with respect to engineering artifacts: devcontainers, Codespaces, and GitHub Actions should support docs, scripts, validation, and repo hygiene, but they must not assume KiCad GUI availability or act as fabrication authority.
- Meaningful runs must declare exactly one execution-contract task type. `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, and `PCB_EDIT_REQUIRED` are not complete unless the run proves real engineering artifact change or closes explicitly with the required failure status.
- `LIVE_PROJECT_STATE.json` is the top authority for project gates, routing-start decisions, placement-start decisions, and closeout status claims. Reports without source hashes are weak, and stale `NO_PCB`, `0 footprints`, or `no routing` markdown must never override live KiCad file evidence.
- Routing acceptance now hard-fails visible geometry defects. A routing pass is not acceptable when the audit or scorecard reports `RIGHT_ANGLE_FOUND`, `ACUTE_JOG_FOUND`, `PAD_ENTRY_GEOMETRY_POOR`, `UNNECESSARY_ZIGZAG_FOUND`, `CRITICAL_LOOP_DETOUR_FOUND`, `KEEP_OUT_CROSSING_FOUND`, `UNJUSTIFIED_VIA_FOUND`, or `TRACE_WIDTH_MISMATCH_FOUND`, even if a DRC snapshot is otherwise clean.
- Routing start now also requires explicit placement-readiness proof. Before a routing task is treated as eligible, a fresh placement-readiness scorecard must report exact status `PLACEMENT_READY_FOR_ROUTING`; generic placement PASS claims are not enough.
- Broad routing now also requires stage admission through `14_LAYOUT_AUTOMATION/scripts/staged_routing_runner.py`. If `detect_no_progress.py` reports `BLOCKED_REPAIR_MODE`, only the recommended targeted repair stage may continue; broad routing and report-only retries must stop.
