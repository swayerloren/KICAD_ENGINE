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
- The GitHub-facing docs must make local use obvious. Root `README.md`, root `START_HERE.md`, and `00_CODEX_START/START_HERE.md` should clearly support `Download ZIP` or normal local clone workflows in VS Code, while `.github/README.md` must explicitly say it only documents the `.github/` folder and is not the main project documentation.
- GitHub dev infrastructure for this repo is intentionally read-only with respect to engineering artifacts: devcontainers, Codespaces, and GitHub Actions should support docs, scripts, validation, and repo hygiene, but they must not assume KiCad GUI availability or act as fabrication authority.
- Public-facing prompts, starter docs, and passive helper scripts should use repo-relative paths by default. If a machine-local Windows path must be shown, mark it clearly as a local example or historical audit artifact.
- The preferred baseline onboarding path is now: ZIP or clone -> open repo in VS Code -> run `python health_check.py --no-write` -> paste the starter prompt from `ONE_PROMPT_START.md`. Future doc changes should preserve that one-prompt local workflow.
- The GitHub-facing front page and key root indexes should present `KiCad Engine` as the general AI-assisted KiCad workflow engine. Active projects, including `ESP32_CSI_WIFI_NODE`, are examples or current workspaces inside that engine, not the identity of the whole repo.
- Local-only helper folders such as `03_TOOLS/node_envs`, `03_TOOLS/python_envs`, `03_TOOLS/repos`, `03_TOOLS/tool_logs`, `99_BACKUPS`, and future routing scratch folders should be documented with tracked placeholder docs instead of requiring users to inherit private local contents.
- Project-local `routing_work` folders are local generated routing scratch space. Future timestamped route-trial or copied-board payloads should stay ignored, and Git should keep only the placeholder `routing_work/README.md` unless a small sanitized evidence subset is intentionally promoted.
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES` is local generated library inventory, not portable repo truth. Keep only `GENERATED_INDEXES/README.md` tracked; regenerate symbol, footprint, 3D model, and candidate outputs on the current machine when needed.
- `00_CODEX_START/TOOL_INDEX.md` is machine-specific local inventory, not portable tool truth. Portable tool truth for normal repo use lives in root `TOOLS_INDEX.md`, `03_TOOLS/TOOLS_INDEX.md`, `EXTERNAL_DEPENDENCIES.md`, `LOCAL_SETUP_REQUIREMENTS.md`, `docs/HEALTH_CHECK.md`, and live results from `python health_check.py --no-write`.
- On a private personal GitHub repo, rulesets may not enforce until the repo is moved to a GitHub Team or organization context. When that limitation exists, use manual PR discipline plus Actions checks targeting `main` instead of assuming the UI ruleset is active.
- When GitHub-hosted CI runs on standard Linux runners, any KiCad-`pcbnew`-dependent validation must degrade to an explicit read-only skip instead of failing the whole workflow. Hosted CI may validate syntax, fixtures, contracts, docs, and repo hygiene, but it must not require local KiCad Python availability unless the runner image deliberately provides it.
- Current owner workflow for this private repo allows direct-owner updates to `main` after local validation and file review. PR branches remain useful for large hardening batches, but they are not required for routine private-repo maintenance right now.
- Private/internal GitHub releases are allowed even while public-release blockers remain, provided the release notes explicitly warn that active boards are not fabrication-ready and that human KiCad review is still required before ordering boards.
- Meaningful runs must declare exactly one execution-contract task type. `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, and `PCB_EDIT_REQUIRED` are not complete unless the run proves real engineering artifact change or closes explicitly with the required failure status.
- `LIVE_PROJECT_STATE.json` is the top authority for project gates, routing-start decisions, placement-start decisions, and closeout status claims. Reports without source hashes are weak, and stale `NO_PCB`, `0 footprints`, or `no routing` markdown must never override live KiCad file evidence.
- Routing acceptance now hard-fails visible geometry defects. A routing pass is not acceptable when the audit or scorecard reports `RIGHT_ANGLE_FOUND`, `ACUTE_JOG_FOUND`, `PAD_ENTRY_GEOMETRY_POOR`, `UNNECESSARY_ZIGZAG_FOUND`, `CRITICAL_LOOP_DETOUR_FOUND`, `KEEP_OUT_CROSSING_FOUND`, `UNJUSTIFIED_VIA_FOUND`, or `TRACE_WIDTH_MISMATCH_FOUND`, even if a DRC snapshot is otherwise clean.
- Routing start now also requires explicit placement-readiness proof. Before a routing task is treated as eligible, a fresh placement-readiness scorecard must report exact status `PLACEMENT_READY_FOR_ROUTING`; generic placement PASS claims are not enough.
- Broad routing now also requires stage admission through `14_LAYOUT_AUTOMATION/scripts/staged_routing_runner.py`. If `detect_no_progress.py` reports `BLOCKED_REPAIR_MODE`, only the recommended targeted repair stage may continue; broad routing and report-only retries must stop.
