# Tool Index

This file tracks intended and available KiCad-related tools. `CLONED_NOT_INSTALLED` means the source repository is present locally, but dependencies have not been installed and setup scripts have not been run.

Portability note: when this file includes absolute Windows paths, treat them as one-machine inventory notes from a prior local audit. New docs, prompts, and day-to-day repo use should prefer repo-relative paths plus local tool discovery on the current machine.

## Startup Tooling Rule
- Do not install tools unless explicitly requested.
- Do not clone additional repositories unless explicitly requested.
- Do not configure MCP unless explicitly requested.
- Before using any tool, confirm it exists locally and record important command results in `02_HISTORY/`.
- Do not give an MCP server write or manufacturing authority until tested on non-critical sample files.
- Last inspection: 2026-04-30 final setup audit. Tool repositories remain under `03_TOOLS\repos`; selected tools have been installed only in isolated workspace environments and project-scoped configuration remains analysis/safe by default.
- Install plan: `03_TOOLS\tool_logs\INSTALL_PLAN.md`.
- Local environment check: `03_TOOLS\tool_logs\LOCAL_ENVIRONMENT_CHECK.md`.
- PATH readiness report: `03_TOOLS\tool_logs\PATH_READINESS_REPORT.md`.
- Visual review tools usage: `03_TOOLS\tool_logs\VISUAL_REVIEW_TOOLS_USAGE.md`.
- Platform strategy: `03_TOOLS\TOOL_PLATFORM_STRATEGY.md`.
- Platform migration plan: `03_TOOLS\tool_logs\TOOL_MIGRATION_PLAN.md`.
- Health check: `03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md` reports PASS=72, WARN=5, FAIL=0 as of the 2026-04-30 PATH readiness update.
- Final setup audit: `02_HISTORY\design_reviews\KICAD_ENGINE_FINAL_SETUP_AUDIT.md` reports readiness score 88/100 as of 2026-04-30.
- Current local blockers: No hard PATH blocker remains for `kicad`, `kicad-cli`, or `python` after the 2026-04-30 user PATH update. `pip.exe` is not present in the confirmed Python Scripts folder, so use `python -m pip` for pip operations. Node `v22.15.0`, npm `10.9.2`, Git `2.52.0.windows.1`, PowerShell `5.1.26100.8115`, and Codex CLI `0.80.0` are available.

## Platform-Aware Tool Roots

Created on 2026-04-30. These roots are available for future organization, but legacy paths remain valid until a migration is explicitly approved.

- Common OS-neutral KiCad tooling: `03_TOOLS\common`
- Common future repos: `03_TOOLS\common\repos`
- Common future scripts: `03_TOOLS\common\scripts`
- Common docs: `03_TOOLS\common\docs`
- Windows GUI automation tooling: `03_TOOLS\windows`
- Windows future repos: `03_TOOLS\windows\repos`
- Windows future scripts: `03_TOOLS\windows\scripts`
- Windows GUI automation environment: `03_TOOLS\python_envs\windows_gui`
- Linux/headless automation tooling: `03_TOOLS\linux`
- Linux future repos: `03_TOOLS\linux\repos`
- Linux future scripts: `03_TOOLS\linux\scripts`

Legacy paths that must keep working:

- `03_TOOLS\repos`
- `03_TOOLS\scripts`
- `03_TOOLS\python_envs`
- `03_TOOLS\node_envs`
- `03_TOOLS\tool_logs`

Migration status: STRUCTURE_CREATED_NO_REPOS_MOVED. Current repos remain in `03_TOOLS\repos`; current scripts remain in `03_TOOLS\scripts`; current Python and Node environments remain in their original folders.

## Legacy Tool Paths

These paths remain valid and must not be moved unless a separate migration prompt explicitly approves it:

- `03_TOOLS\repos`: current cloned KiCad/Codex support repos.
- `03_TOOLS\scripts`: current PowerShell verification, export, backup, health-check, and project-creation scripts.
- `03_TOOLS\python_envs`: current Python virtual environments, including `windows_gui`.
- `03_TOOLS\node_envs`: current Node workspaces/build sandboxes.
- `03_TOOLS\tool_logs`: current tool reports, install plans, usage guides, health checks, and migration plans.

## Common Tool Root

- Root: `03_TOOLS\common`
- Status: STRUCTURE_EXISTS_NO_REPOS_MOVED
- Purpose: OS-neutral KiCad project intelligence and deterministic automation.
- Use for: `kicad-cli`, KiBot, `pcbnew` scripts, MCP analysis tools, BOM/Gerber/PNP parsers, file validators, InteractiveHtmlBom, PcbDraw, and KiCanvas.
- Current repo placement: common repos are still in the legacy root `03_TOOLS\repos` until migration is approved.
- Current common repo candidates in legacy root: `kicad-mcp-pro`, `kicad-happy`, `KiCAD-MCP-Server`, `KiBot`, `InteractiveHtmlBom`, `PcbDraw`, and `kicanvas`.

## Windows GUI Automation Root

- Root: `03_TOOLS\windows`
- Status: STRUCTURE_EXISTS_PASSIVE_DISCOVERY_ONLY
- Purpose: Windows desktop GUI hands/eyes for KiCad when common tools are insufficient.
- Use for: pywinauto, PyAutoGUI, OpenCV image matching, screenshots, window discovery, UIA/Win32 inspection, FlaUI/FlaUInspect, AutoHotkey, and SikuliX.
- Logs: `03_TOOLS\windows\logs`
- Screenshots: `03_TOOLS\windows\logs\screenshots`
- Safety: discovery first; no random clicks, typing, hotkeys, GUI saves, or coordinate automation without explicit approval and screenshot/window verification.

## Installed Windows GUI Packages

- Environment: `03_TOOLS\python_envs\windows_gui`
- Status: INSTALLED_IMPORT_CHECKED_PASSIVE_ONLY
- Packages present: `pywinauto 0.6.9`, `PyAutoGUI 0.9.54`, `PyGetWindow 0.0.9`, `pyperclip 1.11.0`, `pillow 12.2.0`, `opencv-python 4.13.0.92`, and `psutil 7.2.2`.
- Known issue: the first KiCad GUI discovery run on 2026-04-30 matched VS Code because its title contained `KICAD_ENGINE`; future discovery must prefer confirmed KiCad process names.

## Windows GUI Helper Repos

- Root: `03_TOOLS\windows\repos`
- Status: CLONED_REFERENCE_ONLY_NOT_INSTALLED_NOT_BUILT
- Repos present: `FlaUI`, `FlaUInspect`, `AutoHotkey`, and `SikuliX1`.
- Rule: do not build, install, or use these repos to control KiCad without a future explicit gated task.

## Linux/Headless Automation Root

- Root: `03_TOOLS\linux`
- Status: PLANNED_DOCS_AND_STARTER_SCRIPTS_CREATED_NOT_INSTALLED
- Purpose: Linux/headless/CI automation and repeatable validation.
- Use for: Linux `kicad-cli`, KiBot, Xvfb, xdotool, wmctrl, ydotool, dogtail, Docker/headless validation.
- Logs: `03_TOOLS\linux\logs`
- Safety: read-only by default; no `sudo` inside scripts; no delete commands; no final manufacturing output unless verify-before-fab is explicitly approved.

## Linux Docs/Scripts

- Docs present:
  - `03_TOOLS\linux\docs\LINUX_AUTOMATION_README.md`
  - `03_TOOLS\linux\docs\LINUX_KICAD_HEADLESS_PLAN.md`
  - `03_TOOLS\linux\docs\WSL_SETUP_NOTES.md`
  - `03_TOOLS\linux\docs\LINUX_TOOL_INSTALL_COMMANDS_DRAFT.md`
- Starter scripts present:
  - `03_TOOLS\linux\scripts\check_linux_kicad_env.sh`
  - `03_TOOLS\linux\scripts\xvfb\run_kicad_headless_check.sh`
  - `03_TOOLS\linux\scripts\xdotool\list_windows.sh`
  - `03_TOOLS\linux\scripts\wmctrl\list_windows.sh`
- Installation status: Linux tools were not installed from Windows; WSL is not assumed configured.

## MCP Status

- Active workspace-local server: `kicad_mcp_pro_analysis`
- Config path: `.codex\config.toml`
- Authority: analysis/safe mode only.
- Rule: do not enable write, destructive, parallel shared-state, or manufacturing/export authority unless explicitly approved for a specific active project after backup and verification gates.

## Verification Script Status

- Root: `03_TOOLS\scripts`
- Status: SAMPLE_SUCCESS_PATH_VALIDATED_NOT_PRODUCTION_TESTED
- PowerShell parse status: all verification/export/backup/health/project scripts parsed cleanly during the 2026-04-30 platform control-layer audit.
- Rule: generated manufacturing-style outputs remain `NOT_FINAL` until the full verification gate passes.

## Startup And Closeout Indexing Scripts

- Status: CREATED_SAFE_NON_DESTRUCTIVE
- Root: `03_TOOLS\scripts\indexing`
- Purpose: rebuild repo, memory, history, and known-problem indexes for startup and closeout.
- Safety posture: scan Markdown and directory metadata, write only generated index files, do not delete records, do not edit KiCad design files, and do not modify installed KiCad folders.
- Scripts:
  - `build_repo_index.py`: writes `00_CODEX_START\REPO_INDEX.generated.md` and `.json`.
  - `build_memory_index.py`: writes `01_MEMORY\MASTER_MEMORY_INDEX.md`, `00_CODEX_START\MEMORY_INDEX.generated.md`, and `.json`.
  - `build_history_index.py`: writes `02_HISTORY\MASTER_HISTORY_INDEX.md`, `00_CODEX_START\HISTORY_INDEX.generated.md`, and `.json`.
  - `build_known_problems.py`: writes `00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md` and `CURRENT_KNOWN_PROBLEMS.generated.json`.

## Datasheet Research Pipeline Scripts

- Status: CREATED_METADATA_ONLY_NO_DOWNLOADS
- Created: 2026-05-02.
- Script root: `03_TOOLS\scripts\datasheets`
- Policy docs: `06_DATASHEETS\00_INDEX\RESEARCH_PIPELINE.md`, `PUBLIC_RELEASE_DATASHEET_POLICY.md`, `SOURCE_PRIORITY_RULES.md`, `VENDOR_DOWNLOAD_RULES.md`, and `LINK_ONLY_VS_BUNDLED_POLICY.md`.
- Source lists: `06_DATASHEETS\00_INDEX\source_lists\*.csv`
- Default output root: `05_OUTPUTS\datasheet_research`
- Safety posture: read CSV/JSON source lists, create markdown reports and summary stubs, validate URLs where possible, do not download documents, do not scrape aggressively, and do not bundle restricted PDFs in a public release.
- `--download` status: present for future CLI compatibility but intentionally disabled. It exits non-zero until license confirmation, redistribution policy, rate limits, and user approval are implemented.
- `validate_datasheet_links.py`: validates source URLs with conservative HTTP checks and writes `link_validation_report.md`.
- `build_datasheet_index.py`: builds `datasheet_source_index.md` from CSV/JSON source metadata.
- `create_missing_datasheet_report.py`: writes `missing_datasheet_report.md` covering missing metadata, weak source URLs, redistribution uncertainty, and direct-PDF/license risks.
- `generate_component_summary_stub.py`: creates AI-readable summary stub markdown files without inventing electrical specs.
- Smoke-test outputs: `05_OUTPUTS\datasheet_research\datasheet_source_index.md`, `missing_datasheet_report.md`, `link_validation_report.md`, and `summary_stubs`.

## Microcontroller Family Content Generator

- Status: CREATED_AND_USED_SAFE_STUB_GENERATOR
- Created: 2026-05-03.
- Script root: `03_TOOLS\scripts\datasheet_tree`
- Generator: `create_microcontroller_family_content.py`
- Schema: `family_content_schema.json`
- Templates: `03_TOOLS\scripts\datasheet_tree\templates\*_TEMPLATE.md`
- Purpose: create useful AI-readable microcontroller family folders from conservative templates instead of empty `README.md`, `INDEX.md`, `MISSING.md`, and `SOURCES.md` placeholders.
- Safety posture: offline only, no PDF downloads, no web scraping, no KiCad project edits, no overwrite of substantive existing files unless `--force` is explicitly passed. `--overwrite-weak` may replace only obvious placeholder boilerplate.
- Supported inputs: `--vendor`, `--family`, `--representative-part`, optional `--output-folder`, optional JSON config, and optional link-only `--source-link` seed metadata.
- Generated content includes family overviews, common part-number stubs, part records, schematic notes, PCB layout notes, boot/debug notes, power/clock notes, package/footprint notes, dev-board notes, common mistakes, KiCad symbol/footprint notes, source-link stubs, and needs-review backlogs.
- Batch use status: On 2026-05-03, the generator upgraded 48 MCU family/vendor folders under `06_DATASHEETS\01_MICROCONTROLLERS`; it created 612 new files and replaced 141 obvious weak placeholder files without using `--force`.
- Evidence: `05_OUTPUTS\datasheet_tree\MCU_TREE_COMPLETION_SUMMARY.md` and `02_HISTORY\design_reviews\MCU_DATASHEET_TREE_UPGRADE_REPORT.md`.
- Validation status: Python syntax validation, JSON schema parse, dry-run planning, batch coverage check, and no-KiCad-design-file-modification check passed on 2026-05-03.

## Tool Records

### KiCad
- Status: INSTALLED_ON_USER_PATH
- Location: `C:\Program Files\KiCad\9.0\bin\kicad.exe`
- Version: 9.0.7 from Windows file metadata.
- Purpose: KiCad schematic, PCB, library, and fabrication workflow.
- Notes: `C:\Program Files\KiCad\9.0\bin` was added to the user PATH on 2026-04-30. `kicad.exe --version` exits successfully but does not print version text in this environment.

### kicad-cli
- Status: INSTALLED_ON_USER_PATH
- Location: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
- Version: 9.0.7 from `kicad-cli version`.
- Purpose: Command-line ERC, DRC, exports, and automation.
- Notes: `kicad-cli version` is callable from a refreshed PATH and reports 9.0.7.

### Codex CLI/App
- Status: INSTALLED
- Location: `C:\Users\LJ\AppData\Roaming\npm\codex.cmd`; VS Code extension binary also present at `c:\Users\LJ\.vscode\extensions\openai.chatgpt-26.422.71525-win32-x64\bin\windows-x86_64\codex.exe`
- Version: `codex-cli 0.80.0`
- Purpose: AI-assisted workspace operations and documentation.
- Notes: Follow `AGENTS.md` and startup instructions.

## Local Runtime Tools
- PowerShell: `5.1.26100.8115` at `C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe`.
- Python launcher: `py` at `C:\Users\LJ\AppData\Local\Microsoft\WindowsApps\py.exe`; `py --version` reports Python 3.12.10.
- Python command: `python` is on the refreshed user PATH at `C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe`; `python --version` reports Python 3.12.10.
- pip command: `pip.exe` is not present in `C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\Scripts`; use `python -m pip`, which reports pip 25.0.1 for Python 3.12.
- Node: `v22.15.0` at `C:\Program Files\nodejs\node.exe`.
- npm: `10.9.2` at `C:\Program Files\nodejs\npm.cmd`.
- Git: `git version 2.52.0.windows.1` at `C:\Program Files\Git\cmd\git.exe`.

## Workspace PowerShell Automation Scripts
- Status: SAMPLE_SUCCESS_PATH_VALIDATED_NOT_PRODUCTION_TESTED.
- Location: `03_TOOLS\scripts`.
- Created: 2026-04-30.
- Last revalidated: 2026-04-30 17:43:29 -04:00.
- Session log: `02_HISTORY\sessions\KICAD_VERIFICATION_SCRIPTS_CREATED.md`.
- Safety posture: scripts accept `-ProjectPath`, fail when the project path is missing, resolve or require `kicad-cli`, create timestamped folders, write logs, do not delete source files, and mark generated manufacturing-style exports as not final.
- Test status: PowerShell parser checks passed for all scripts. Scripts were rerun only against the disposable sample project; no real KiCad projects were modified.
- Sample pipeline status: Rerun on `04_KICAD_PROJECTS\archive\SAMPLE_KICAD_TEST_PROJECT` on 2026-04-30. Inventory and backup passed. ERC and DRC ran and failed with KiCad CLI exit code 5 due sample-project violations. BOM export passed. `full_verify_project.ps1` now skips Gerber, drill, and STEP exports by default after failed ERC/DRC and returned incomplete/failed as expected. No new fabrication folders were created during the fix rerun.
- Sample pipeline reports: `02_HISTORY\design_reviews\SAMPLE_KICAD_TEST_PROJECT_REVIEW.md`, `02_HISTORY\erc_drc_reports\SAMPLE_KICAD_TEST_PROJECT_VERIFICATION.md`, `02_HISTORY\sessions\SAMPLE_PIPELINE_TEST_SESSION.md`, `03_TOOLS\tool_logs\PIPELINE_FIX_REPORT.md`, and `02_HISTORY\sessions\SAMPLE_PIPELINE_FIX_SESSION.md`.
- Clean success-path sample: `04_KICAD_PROJECTS\archive\CLEAN_KICAD_PASSING_SAMPLE` uses the installed KiCad demo `test_pads_inside_pads`. Inventory, backup, ERC, DRC, BOM export, Gerber export, drill export, and STEP export all returned exit code 0. Full verification status was `COMPLETE_REQUIRES_HUMAN_REVIEW`; generated fabrication-style outputs are in `NOT_FINAL` folders.
- Clean success-path reports: `02_HISTORY\design_reviews\CLEAN_KICAD_PASSING_SAMPLE_REVIEW.md`, `02_HISTORY\erc_drc_reports\CLEAN_KICAD_PASSING_SAMPLE_VERIFICATION.md`, `02_HISTORY\sessions\CLEAN_SAMPLE_SUCCESS_PATH_SESSION.md`, and `02_HISTORY\command_logs\CLEAN_SAMPLE_SUCCESS_PATH_COMMANDS.md`.
- Script fixes from sample test: `new_kicad_project_workspace.ps1` now allows blank markdown lines in generated files; `kicad_automation_common.ps1` no longer emits log lines through function return pipelines, allows blank markdown lines in summaries, quotes all logged command arguments, and excludes project review/output folders such as `review_outputs`, `reference_original_inventory`, `learning`, and `notes` from KiCad source-file discovery; `run_erc.ps1` and `run_drc.ps1` write failure summaries when they fail before normal completion; `full_verify_project.ps1` logs child commands clearly and gates Gerber/drill/STEP exports behind passing ERC and DRC unless `-AllowExportsAfterFailedChecks` is explicitly supplied.
- Reference review script note: the `review_outputs` exclusion was added during the 2026-04-30 `COMMAND_LINK_VERIFIED_REFERENCE` read-only review after an in-project backup copy caused duplicate `.kicad_pro` detection.
- Direct finished-folder review note: on 2026-04-30, `kicad_automation_common.ps1` was extended to exclude `Codex Review Outputs`, `original_fiverr_outputs_snapshot`, and `*-backups` folders after the approved direct `COMMAND LINK` work placed review outputs inside the approved project folder.
- KiCad CLI note: scripts first try PATH, then search `C:\Program Files\KiCad` for `kicad-cli.exe`, and also accept explicit `-KiCadCliPath`.

## KiCad Installed App Intelligence

- Status: KICAD_9_WINDOWS_DEEP_AUDIT_CREATED_READ_ONLY
- Created: 2026-05-02.
- Scope: read-only audit of the installed KiCad app under `C:\Program Files\KiCad\9.0\bin`, `etc`, `lib`, and `share`.
- KiCad CLI version checked: `9.0.7` using only `kicad-cli version`.
- Main audit report: `02_HISTORY\design_reviews\KICAD_INSTALLED_APP_DEEP_AUDIT.md`.
- Intelligence docs:
  - `03_TOOLS\kicad_app_intelligence\KICAD_9_WINDOWS_PATH_MAP.md`
  - `03_TOOLS\kicad_app_intelligence\KICAD_CLI_COMMANDS_REFERENCE.md`
  - `03_TOOLS\kicad_app_intelligence\KICAD_LIBRARY_DISCOVERY_GUIDE.md`
  - `03_TOOLS\kicad_app_intelligence\KICAD_DO_NOT_TOUCH_RULES.md`
  - `03_TOOLS\kicad_app_intelligence\KICAD_AGENT_TASK_MAP.md`
- Agent operating docs:
  - `00_CODEX_START\KICAD_AGENT_OPERATING_MANUAL.md`
  - `00_CODEX_START\KICAD_SAFE_AUTOMATION_RULES.md`
- Read-only audit scripts:
  - `03_TOOLS\scripts\kicad_app_audit\audit_kicad_windows.ps1`
  - `03_TOOLS\scripts\kicad_app_audit\check_kicad_cli.ps1`
  - `03_TOOLS\scripts\kicad_app_audit\inventory_kicad_libraries.ps1`
- Generated read-only audit outputs:
  - `05_OUTPUTS\kicad_app_audit\KICAD_WINDOWS_APP_AUDIT_20260502_160057.md`
  - `05_OUTPUTS\kicad_app_audit\KICAD_WINDOWS_APP_AUDIT_20260502_160057.json`
  - `05_OUTPUTS\kicad_app_audit\KICAD_LIBRARY_INVENTORY_20260502_160145.md`
  - `05_OUTPUTS\kicad_app_audit\KICAD_SYMBOL_LIBRARIES_20260502_160145.csv`
  - `05_OUTPUTS\kicad_app_audit\KICAD_FOOTPRINT_LIBRARIES_20260502_160145.csv`
  - `05_OUTPUTS\kicad_app_audit\KICAD_3DMODEL_FOLDERS_20260502_160145.csv`
  - `05_OUTPUTS\kicad_app_audit\KICAD_LIBRARY_TABLES_20260502_160145.csv`
- Installed app summary: `bin`, `etc`, `lib`, and `share` exist; stock libraries include 224 symbol files, 155 footprint libraries with 15,415 footprints, and 105 3D model folders with 14,043 files.
- Safety: do not write into `C:\Program Files\KiCad`; use installed app folders as read-only evidence only. User-global KiCad tables under `%APPDATA%\kicad\9.0` are user state and must not be edited without explicit approval and backup.

### Verification Script Entries
- `run_erc.ps1`: runs KiCad schematic ERC and writes a timestamped report folder.
- `run_drc.ps1`: runs KiCad PCB DRC and writes a timestamped report folder.
- `export_gerbers.ps1`: exports Gerbers into a timestamped not-final output folder.
- `export_drill.ps1`: exports drill files into a timestamped not-final output folder.
- `export_step.ps1`: exports STEP into a timestamped not-final output folder.
- `export_bom.ps1`: exports BOM into a timestamped BOM/output folder for review.
- `full_verify_project.ps1`: locates project files, runs backup, ERC, DRC, BOM, Gerber, drill, and STEP child scripts, and writes a verification summary.
- `backup_kicad_project.ps1`: copies KiCad project source files and local libraries into `99_BACKUPS\pre_codex_edits\<project-id>_<timestamp>`.
- `find_kicad_project_files.ps1`: inventories KiCad project, schematic, PCB, symbol, and footprint files.
- `kicad_automation_common.ps1`: shared helper used by the entry scripts.
- `kicad_engine_health_check.ps1`: checks workspace structure, startup files, prompts, memory/history, repos, tool statuses, runtime tools, and verification scripts; writes `03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md`.

## Windows GUI Automation

### windows_gui Python environment
- Status: INSTALLED_IMPORT_CHECKED_PASSIVE_ONLY
- Environment: `03_TOOLS\python_envs\windows_gui`
- Python: 3.12.10
- Purpose: Windows desktop GUI discovery, screenshots, and future carefully gated KiCad GUI automation experiments.
- Installed packages: `pywinauto 0.6.9`, `PyAutoGUI 0.9.54`, `PyGetWindow 0.0.9`, `pyperclip 1.11.0`, `pillow 12.2.0`, `opencv-python 4.13.0.92`, `psutil 7.2.2`.
- Supporting packages installed by dependency resolution: `comtypes 1.4.16`, `MouseInfo 0.1.3`, `numpy 2.4.4`, `PyMsgBox 2.0.1`, `PyRect 0.2.0`, `PyScreeze 1.0.1`, `pytweening 1.2.0`, `pywin32 311`, `six 1.17.0`.
- Safe checks run: import-only check for `pywinauto`, `pyautogui`, `pygetwindow`, `pyperclip`, `PIL`, `cv2`, and `psutil`; Python syntax checks for passive scripts.
- Documentation: `03_TOOLS\windows\docs\WINDOWS_GUI_AUTOMATION_README.md` and `03_TOOLS\windows\docs\KICAD_GUI_CONTROL_LIMITS.md`.
- Passive scripts: `03_TOOLS\windows\scripts\window_discovery\discover_windows.py` and `03_TOOLS\windows\scripts\screenshots\take_screenshot.py`.
- Safety posture: do not control KiCad, click, type, move windows, save files, or modify projects unless a future task explicitly authorizes a gated GUI control experiment. Discover windows and take screenshots before any future control attempt.
- Command log: `02_HISTORY\command_logs\WINDOWS_GUI_AUTOMATION_INSTALL_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\WINDOWS_GUI_AUTOMATION_INSTALL_SESSION.md`.

### KiCad GUI discovery workflow
- Status: FILTER_FIXED_CONFIRMED_READ_ONLY_KICAD_DETECTION
- Purpose: Read-only discovery of running KiCad windows, process info, UIA tree, Win32 tree, and visible-window screenshots.
- README: `03_TOOLS\windows\scripts\KICAD_GUI_DISCOVERY_README.md`
- Shared classifier: `03_TOOLS\windows\scripts\kicad_window_filter.py`
- Window discovery script: `03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py`
- UIA inspection script: `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py`
- Win32 inspection script: `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py`
- KiCad window screenshot script: `03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py`
- Report output: `03_TOOLS\windows\logs`
- Screenshot output: `03_TOOLS\windows\logs\screenshots`
- Candidate fields: `process_name`, `pid`, `window_title`, `confidence`, `reason`, `eligible_for_inspection`, `eligible_for_screenshot`, and `eligible_for_control`.
- High-confidence rule: process name must be `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
- Low-confidence rule: title-only matches are `LOW_CONFIDENCE_TITLE_ONLY` and are not eligible for UIA inspection, Win32 inspection, screenshots, or control.
- Optional args: `--allow-title-only-review`, `--target-pid <PID>`, and `--output-dir <PATH>`.
- Safe checks run: Python compile checks for the shared classifier and all four scripts; import/runtime checks for `pywinauto`, `psutil`, `PIL`, and `PIL.ImageGrab` through passive scripts.
- Runtime discovery run: 2026-04-30, read-only. The scripts safely ran but matched VS Code as a false positive because the title contained `KICAD_ENGINE`; direct checks found no `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
- Filter fix run: 2026-04-30, read-only. Discovery found 0 high-confidence KiCad windows. VS Code and Chrome title matches were classified as `LOW_CONFIDENCE_TITLE_ONLY` with `inspect=false`, `screenshot=false`, and `control=false`; UIA and Win32 inspection inspected 0 windows.
- Confirmed run: 2026-04-30, read-only. Discovery found 1 high-confidence KiCad window: `kicad.exe` PID `19576`, title `COMMAND LINK DRAFT â€” KiCad 9.0`, with `inspect=true`, `screenshot=true`, and `control=false`.
- Confirmed run reports: discovery `03_TOOLS\windows\logs\kicad_window_discovery_20260430_192803.md`; UIA `03_TOOLS\windows\logs\kicad_uia_inspection_20260430_192817.md`; Win32 `03_TOOLS\windows\logs\kicad_win32_inspection_20260430_192816.md`; screenshot report `03_TOOLS\windows\logs\kicad_window_screenshot_20260430_192827.md`.
- Confirmed run screenshot: `03_TOOLS\windows\logs\screenshots\kicad_window_20260430_192827_COMMAND_LINK_DRAFT_KiCad_9_0_19576.png`.
- Confirmed run inspection scope: UIA recorded 65 controls; Win32 recorded 241 controls. Low-confidence VS Code and Chrome candidates were not inspected or captured.
- Runtime gate: do not run against KiCad unless KiCad is already open and LJ clearly intends read-only discovery. Discovery must not click, type, send hotkeys, close windows, move windows, open projects, save files, or modify KiCad projects.
- Session log: `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_WORKFLOW_CREATED.md`.
- First run session log: `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_RUN_SESSION.md`.
- Filter fix report: `03_TOOLS\windows\logs\KICAD_GUI_DISCOVERY_FILTER_FIX_REPORT.md`.
- Filter fix session log: `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_FILTER_FIX_SESSION.md`.
- Confirmed run session log: `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_CONFIRMED_RUN_SESSION.md`.

### Windows GUI helper repos
- Status: CLONED_NOT_INSTALLED_NOT_BUILT_REFERENCE_ONLY
- Location: `03_TOOLS\windows\repos`
- Repo index: `03_TOOLS\windows\docs\WINDOWS_GUI_REPO_INDEX.md`
- Local repo status: `03_TOOLS\tool_logs\LOCAL_TOOL_REPO_STATUS.md`
- Command log: `02_HISTORY\command_logs\WINDOWS_GUI_REPOS_CLONED_COMMANDS.md`
- Session log: `02_HISTORY\sessions\WINDOWS_GUI_REPOS_CLONED_SESSION.md`
- Safety posture: do not install, build, run setup scripts, or use these repos to control KiCad unless a future task explicitly approves a gated experiment.

#### FlaUI
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\windows\repos\FlaUI`
- Source URL: `https://github.com/FlaUI/FlaUI.git`
- Branch: `main`
- Commit: `7d600d5240ff2b8227cfcc829230cefe8116970a`
- Purpose: .NET UI Automation library reference for structured Windows desktop automation.

#### FlaUInspect
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\windows\repos\FlaUInspect`
- Source URL: `https://github.com/FlaUI/FlaUInspect.git`
- Branch: `main`
- Commit: `c554b6fac19d3486c4fa3cbf6f37bb6d98eed1d9`
- Purpose: UI Automation inspection tool reference for Windows control-tree exploration.

#### AutoHotkey
- Status: CLONED_NOT_BUILT
- Location: `03_TOOLS\windows\repos\AutoHotkey`
- Source URL: `https://github.com/AutoHotkey/AutoHotkey.git`
- Branch: `alpha`
- Commit: `7320bfffebf2eb5257990c3c24015499faaab6c8`
- Purpose: Windows hotkey and scripting engine source reference.

#### SikuliX1
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\windows\repos\SikuliX1`
- Source URL: `https://github.com/RaiMan/SikuliX1.git`
- Branch: `master`
- Commit: `17b2f48f5fc38cdea81e6aa0fb336503c5dc0e79`
- Purpose: Image-driven GUI automation reference for future visual workflow experiments.

## Linux/Headless Automation

### Linux automation plan
- Status: PLANNED_DOCS_AND_STARTER_SCRIPTS_CREATED_NOT_INSTALLED
- Location: `03_TOOLS\linux`
- Purpose: Linux/headless KiCad automation planning, CI/headless checks, X11 window listing, and virtual-display readiness notes.
- Documentation:
  - `03_TOOLS\linux\docs\LINUX_AUTOMATION_README.md`
  - `03_TOOLS\linux\docs\LINUX_KICAD_HEADLESS_PLAN.md`
  - `03_TOOLS\linux\docs\WSL_SETUP_NOTES.md`
  - `03_TOOLS\linux\docs\LINUX_TOOL_INSTALL_COMMANDS_DRAFT.md`
- Starter scripts:
  - `03_TOOLS\linux\scripts\check_linux_kicad_env.sh`
  - `03_TOOLS\linux\scripts\xvfb\run_kicad_headless_check.sh`
  - `03_TOOLS\linux\scripts\xdotool\list_windows.sh`
  - `03_TOOLS\linux\scripts\wmctrl\list_windows.sh`
- Safety posture: docs/scripts only; no Linux tools installed from Windows; WSL is not assumed configured; scripts contain no `sudo`, install commands, delete commands, or project modification commands.
- Runtime gate: run only inside an explicitly selected Linux/WSL/VM/container environment. Test on disposable samples before production projects.
- Session log: `02_HISTORY\sessions\LINUX_AUTOMATION_PLAN_CREATED.md`.

### kicad-mcp-pro
- Status: INSTALLED_PROJECT_SCOPED_CODEX_CONFIGURED_ANALYSIS_ONLY
- Location: `03_TOOLS\repos\kicad-mcp-pro`
- Environment: `03_TOOLS\python_envs\kicad-mcp-pro`
- CLI: `C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe`
- Source URL: `https://github.com/oaslananka/kicad-mcp-pro.git`
- Branch: `main`
- Commit: `9991061561d1e3551dee03a525c06bf2e2cbaf02`
- Purpose: MCP-assisted KiCad automation support.
- Installed version: 3.1.8.
- Install method used: local clone installed into dedicated Python 3.12 venv with `python -m pip install 03_TOOLS\repos\kicad-mcp-pro`.
- Runtime requirements: Python >=3.12; `uv`/`uvx` recommended; KiCad/`kicad-cli` for real workflows. Repo dev scripts require Node >=24.11.0 and npm >=11.6.1.
- Safe tests run: `--help`, `version`, `health --json`, and `doctor --json` with `KICAD_MCP_PROFILE=analysis`.
- Test result: installed and healthy; `doctor --json` reported `status: degraded` only because no active KiCad board/project was open. KiCad CLI was found through explicit path `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` and reported version 9.0.7.
- MCP startup command: run `03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe` with args `serve --transport stdio --profile analysis` from the current checkout.
- Draft Codex config: `03_TOOLS\tool_logs\KICAD_MCP_PRO_CODEX_CONFIG_SNIPPET.toml`.
- Active project-scoped Codex config: `.codex\config.toml`.
- MCP server name: `kicad_mcp_pro_analysis`.
- Project-scoped env: `KICAD_MCP_PROFILE=analysis`, `KICAD_MCP_TRANSPORT=stdio`, `KICAD_MCP_WORKSPACE_ROOT=C:\Users\LJ\GitHub\KICAD_ENGINE`, `KICAD_MCP_PROJECT_DIR=C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active`, `KICAD_MCP_OUTPUT_DIR=C:\Users\LJ\GitHub\KICAD_ENGINE\05_OUTPUTS\kicad-mcp-pro-analysis`, `KICAD_MCP_KICAD_CLI=C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`, `KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS=false`.
- Project-scoped config backup: `99_BACKUPS\pre_codex_edits\codex_config_20260430_154315.toml`.
- Command log: `02_HISTORY\command_logs\KICAD_MCP_PRO_INSTALL_COMMANDS.md`.
- Config command log: `02_HISTORY\command_logs\CODEX_MCP_CONFIG_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\KICAD_MCP_PRO_INSTALL_SESSION.md`.
- Config session log: `02_HISTORY\sessions\CODEX_MCP_CONFIG_SESSION.md`.
- Initial authority: analysis-only; no write or manufacturing authority.
- Notes: MCP config was applied only to the workspace-local `.codex\config.toml`; global `C:\Users\LJ\.codex\config.toml` was not modified. Manufacturing/export authority and experimental tools remain disabled. Write/destructive tools still require manual approval and active project backup gates.

### kicad-happy
- Status: INSTALLED_ANALYSIS_ONLY
- Location: `03_TOOLS\repos\kicad-happy`
- Environment: `03_TOOLS\python_envs\kicad-happy`
- Runner: `C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\kicad-happy\Scripts\python.exe`
- Source URL: `https://github.com/aklofas/kicad-happy.git`
- Branch: `main`
- Commit: `2a7dc4147a8edbbe3694498ff1ba9f06e37244cb`
- Purpose: AI-assisted KiCad design review using skill guidance and deterministic Python analyzers for schematics, PCB layout, cross-domain checks, EMC, thermal review, Gerber review, and fabrication release gating.
- Install method used: dedicated Python 3.12 venv created with the Windows Python launcher. No pip dependencies were installed because core analyzers are documented as Python stdlib-only.
- Runtime requirements: Python 3.10+ for core analyzers. KiCad install is not required for saved-file analysis. Optional KiDoc rendering, SPICE, distributor, and datasheet workflows have additional requirements and were not installed or configured.
- Safe tests run: analyzer `--help` checks for schematic, PCB, Gerber, cross-analysis, thermal, EMC, and fab release gate scripts; one `analyze_schematic.py --schema` smoke test.
- Exact analysis runner pattern: `C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\kicad-happy\Scripts\python.exe C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\repos\kicad-happy\skills\kicad\scripts\analyze_schematic.py <copied-or-approved-project-file.kicad_sch> --output <05_OUTPUTS\kicad-happy\PROJECT_TIMESTAMP\schematic.json>`.
- Usage guide: `03_TOOLS\tool_logs\KICAD_HAPPY_USAGE_GUIDE.md`.
- Command log: `02_HISTORY\command_logs\KICAD_HAPPY_INSTALL_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\KICAD_HAPPY_INSTALL_SESSION.md`.
- Initial authority: read-only, analysis-only.
- Notes: Do not run against production/current projects until explicitly approved. Do not globally install Codex skills, configure GitHub Actions, run optional KiDoc dependency installs, or use distributor/API-key flows unless requested.

### KiCAD-MCP-Server
- Status: CLONED_NOT_INSTALLED
- Location: `03_TOOLS\repos\KiCAD-MCP-Server`
- Source URL: `https://github.com/mixelpixx/KiCAD-MCP-Server.git`
- Branch: `main`
- Commit: `d3c01e20bd3af96eaaebcdb84baa7ec9908b31e4`
- Purpose: MCP server for KiCad integration experiments.
- Install method: staged manual install after approval; do not run `setup-windows.ps1` until approved.
- Runtime requirements: KiCad 9.0+ with Python/`pcbnew`; Node.js 18+; Python >=3.9/3.10+ depending on path; npm dependencies and Python requirements.
- Safe first test: KiCad bundled Python `pcbnew` import check, then `npm run build` after dependency install.
- Initial authority: analysis-only/read-only; write-capable only after disposable-project validation.
- Notes: Dependencies are not installed. MCP is not configured.

### KiBot
- Status: INSTALLED_OUTPUT_AUTOMATION_NOT_PROJECT_TESTED
- Location: `03_TOOLS\repos\KiBot`
- Environment: `03_TOOLS\python_envs\kibot`
- CLI: `C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\kibot\Scripts\kibot.exe`
- Source URL: `https://github.com/INTI-CMNB/KiBot.git`
- Branch: `master`
- Commit: `367a2e04122aa46413a30e61cb213bfe7223c8c8`
- Purpose: Deterministic KiCad ERC/DRC, fabrication export, documentation, BOM, and release-output automation.
- Installed version: 1.8.5.
- Install method used: KiCad 9.0 bundled Python 3.11 created the dedicated venv at `03_TOOLS\python_envs\kibot`; KiBot and Python dependencies were installed into that venv.
- Runtime requirements: KiCad 9.0.7 is available at `C:\Program Files\KiCad\9.0\bin`; KiBot commands must run with KiCad `bin` on `PATH` and KiCad `site-packages`/`bin` on `PYTHONPATH` so `pcbnew` is available.
- Installed Python packages: `kibot`, `kiauto`, `pyyaml`, `xlsxwriter`, `colorama`, `requests`, `qrcodegen`, `markdown2`, `lark`, `psutil`, `xvfbwrapper`, and `lxml`.
- Safe tests run: Python import of KiBot and KiCad `pcbnew`, `kibot --version`, `kibot --help`, `kibot --help-list-outputs`, `kibot --help-preflights`, and template output listing.
- Exact command pattern:
  `powershell -NoProfile -Command "$env:PATH='C:\Program Files\KiCad\9.0\bin;' + $env:PATH; $env:PYTHONPATH='C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin'; & 'C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\kibot\Scripts\kibot.exe' -c '<project.kibot.yaml>' -b '<board.kicad_pcb>' -e '<schematic.kicad_sch>' -d '<output_dir>' -A"`
- Starter config template: `04_KICAD_PROJECTS\templates\kibot_default.kibot.yaml`.
- Command log: `02_HISTORY\command_logs\KIBOT_INSTALL_COMMANDS.md`.
- Session log: `02_HISTORY\sessions\KIBOT_INSTALL_SESSION.md`.
- Initial authority: output-only automation into approved output folders.
- Notes: Windows support is documented as experimental by KiBot. Do not run on real projects until an active project is selected, backups are confirmed, and outputs are directed to `05_OUTPUTS` or project `reports`/`fabrication` folders. Do not treat generated outputs as final until full workspace fabrication checks pass.

### InteractiveHtmlBom
- Status: INSTALLED_HELP_TESTED_NOT_PROJECT_TESTED
- Location: `03_TOOLS\repos\InteractiveHtmlBom`
- Environment: `03_TOOLS\python_envs\InteractiveHtmlBom`
- CLI: `C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\InteractiveHtmlBom\Scripts\generate_interactive_bom.exe`
- Source URL: `https://github.com/openscopeproject/InteractiveHtmlBom.git`
- Branch: `master`
- Commit: `8c13013fc5233cfa31698a777813e87502bdb625`
- Purpose: Interactive HTML BOM generation.
- Install method used: KiCad 9.0 bundled Python created a dedicated venv; local clone installed into that venv.
- Runtime requirements: Python >=3.8; `wxpython>=4.0`; `jsonschema>=4.1`; KiCad/Pcbnew context for real board extraction.
- Safe tests run: `generate_interactive_bom --help` with KiCad `bin` and KiCad Python paths set, plus `INTERACTIVE_HTML_BOM_NO_DISPLAY=1`.
- Initial authority: read-only analysis with generated output only.
- Notes: Installed packages include InteractiveHtmlBom, wxPython, jsonschema, numpy, and related dependencies. Not run against any real KiCad board.

### PcbDraw
- Status: INSTALLED_HELP_TESTED_NOT_PROJECT_TESTED
- Location: `03_TOOLS\repos\PcbDraw`
- Environment: `03_TOOLS\python_envs\PcbDraw`
- CLI: `C:\Users\LJ\GitHub\KICAD_ENGINE\03_TOOLS\python_envs\PcbDraw\Scripts\pcbdraw.exe`
- Source URL: `https://github.com/yaqwsx/PcbDraw.git`
- Branch: `master`
- Commit: `9f6bfe8bc0aa398a6b6e91993b19ce1271fe312f`
- Purpose: PCB rendering for documentation and visual review.
- Install method used: KiCad 9.0 bundled Python created a dedicated venv; local git clone installed by `pip` from a temporary local-git build so the source checkout stayed clean.
- Runtime requirements: Python >=3.9; KiCad 9+; Inkscape 1.x or librsvg; Python packages from `setup.py`.
- Safe tests run: `pcbdraw --help`, `pcbdraw --version`, and `pcbdraw plot --help` with KiCad `bin` and KiCad Python paths set.
- Initial authority: read-only rendering with output only.
- Notes: Installed extra Windows dependency `LnkParse3` after first help test exposed it as missing. Inkscape exists at `C:\Program Files\Inkscape\bin\inkscape.exe` with file metadata version 1.4.2, but Inkscape is not on PATH. `rsvg-convert` is not installed. Not run against any real KiCad board.

### KiCanvas
- Status: ISOLATED_NPM_BUILD_TESTED_NOT_PROJECT_TESTED
- Location: `03_TOOLS\repos\kicanvas`
- Isolated workspace: `03_TOOLS\node_envs\kicanvas\workspace_20260430_161903`
- Source URL: `https://github.com/theacodes/kicanvas.git`
- Branch: `main`
- Commit: `b031159eb74aaa7eef2b026fd85d35bc05ff2095`
- Purpose: Browser-based KiCad visualization.
- Install method used: copied the repo to an isolated timestamped workspace under `03_TOOLS\node_envs\kicanvas`, then ran npm install/build tests there. The source checkout remained clean.
- Runtime requirements: Node/npm for local build; docs require Python packages only for documentation build. KiCad 6+ file formats; KiCad 5 unsupported.
- Safe tests run: `npm ci --ignore-scripts`, `npm run lint:types`, and `npm run build:no-check` in the isolated workspace.
- Initial authority: read-only visualization.
- Notes: npm reported deprecated packages and 10 audit findings in dev dependencies. Build artifacts exist only in the isolated workspace. Not run against real KiCad files.

