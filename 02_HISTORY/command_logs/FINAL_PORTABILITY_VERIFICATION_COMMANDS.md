# Final Portability Verification Commands

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

## Commands And Results

1. `git status`
   - result: branch `main` matched `origin/main`; unrelated local unstaged active-project files were present
2. `python health_check.py --no-write`
   - result: `PASS=18 WARN=2 FAIL=0`
3. `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite`
   - result: `PASS=18 WARN=2 FAIL=0`
4. `git ls-files 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work`
   - result: only `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/README.md` is tracked
5. `git ls-files 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES`
   - result: only `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/README.md` is tracked
6. `rg -n "MACHINE-SPECIFIC INVENTORY|C:\\Users\\LJ|historical|ZIP|VS Code|one prompt|extra GitHub repos|not required|OPTIONAL|WARN|pcbnew" README.md ONE_PROMPT_START.md EXTERNAL_DEPENDENCIES.md 00_CODEX_START/TOOL_INDEX.md docs/PATH_PORTABILITY.md 00_CODEX_START/PATH_PORTABILITY_RULES.md docs/HEALTH_CHECK.md`
   - result: confirmed machine-specific warning, historical-path warning, ZIP/VS Code onboarding flow, optional dependency classification, and health-check `pcbnew` warning guidance
7. `Get-Content 00_CODEX_START\TOOL_INDEX.md -TotalCount 40`
   - result: file starts with `WARNING: MACHINE-SPECIFIC INVENTORY` and points to portable tool truth files
8. `Get-Content README.md -TotalCount 200`
   - result: README still presents `ZIP -> VS Code -> One Prompt`
9. `Get-Content ONE_PROMPT_START.md -TotalCount 160`
   - result: one-prompt startup still points agents to portable docs and live discovery
10. `Get-Content EXTERNAL_DEPENDENCIES.md -TotalCount 220`
    - result: extra cloned repos remain classified as `NOT_INCLUDED` and not required for baseline use
11. `Get-Content docs\PATH_PORTABILITY.md -TotalCount 200`
    - result: historical absolute paths are explicitly classified as evidence only
12. `rg -n "require-pcbnew|pcbnew.*WARN|WARN.*pcbnew|BOARD_AWARE|current Python interpreter can import pcbnew|recommended context" health_check.py health_check.ps1 docs/HEALTH_CHECK.md 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py 03_TOOLS/scripts/kicad_api/kicad_python_context.py`
    - result: confirmed `pcbnew` is warning-only for onboarding and promoted to failure only when `--require-pcbnew` is requested
13. `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
    - result: no KiCad design file diffs
14. `rg -n "Extra cloned GitHub repos|not required for first use|not required for the repo's basic workflow|03_TOOLS/repos" README.md ONE_PROMPT_START.md EXTERNAL_DEPENDENCIES.md LOCAL_SETUP_REQUIREMENTS.md START_HERE.md 03_TOOLS/README.md 03_TOOLS/TOOLS_INDEX.md`
    - result: baseline startup does not require extra cloned repos
15. `git rev-parse HEAD`
    - result: `2a49bbc8c941f65397dcdf012050aa59142a040d` before this verification commit
16. `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 05_OUTPUTS/release_readiness/FINAL_PORTABILITY_VERIFICATION_TASK_CONTRACT.json`
    - result: task contract valid; recommended final status `VALID_TASK_CONTRACT`
17. `python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .`
    - result: repo index rebuilt
18. `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .`
    - result: memory index rebuilt
19. `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .`
    - result: history index rebuilt
20. `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .`
    - result: `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` rebuilt
21. `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`
    - result: `00_CODEX_START/AI_QUALITY_INDEX.generated.*` rebuilt
