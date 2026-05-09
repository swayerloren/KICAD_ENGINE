# Final Portability Verification Report

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

## Clean Portable Status

- Portable baseline status: `YES`
- Git working tree fully clean: `NO`

The portability fixes are holding. A ZIP or clone user can start from the portable docs, run the read-only health check, detect local KiCad live, and avoid machine-local scratch payloads and generated inventories.

The working tree is not fully clean because unrelated local active-project files remain unstaged under `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/`. Those files are not portability blockers and were not changed by this task.

## Health Check Result

- `python health_check.py --no-write`
  - result: `PASS=18 WARN=2 FAIL=0`
- `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite`
  - result: `PASS=18 WARN=2 FAIL=0`
- expected user action note:
  - board-aware scripts should re-enter through KiCad Python when normal Python cannot import `pcbnew` directly

## Verification Results

| Check | Result | Evidence |
| --- | --- | --- |
| `routing_work` tracked scratch payload removed | `PASS` | `git ls-files 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` returned only `README.md` |
| Generated KiCad library local indexes not tracked | `PASS` | `git ls-files 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES` returned only `README.md` |
| `00_CODEX_START/TOOL_INDEX.md` marked machine-specific | `PASS` | file begins with `WARNING: MACHINE-SPECIFIC INVENTORY` and points to portable tool truth files |
| Historical local paths documented as evidence only | `PASS` | `README.md`, `ONE_PROMPT_START.md`, `docs/PATH_PORTABILITY.md`, and `00_CODEX_START/PATH_PORTABILITY_RULES.md` all warn against using old absolute paths as current config |
| `pcbnew` normal-Python issue downgraded to onboarding warning | `PASS` | `health_check.py` reports `WARN` unless `--require-pcbnew` is supplied |
| ZIP -> VS Code -> one prompt onboarding retained | `PASS` | `README.md` and `ONE_PROMPT_START.md` both still present that flow |
| Extra cloned GitHub repos not required for baseline | `PASS` | `EXTERNAL_DEPENDENCIES.md` and `03_TOOLS/README.md` say extra repos are optional/local-only |
| Advanced external tools classified clearly | `PASS` | `EXTERNAL_DEPENDENCIES.md` distinguishes `REQUIRED`, `OPTIONAL`, `LOCAL_ONLY`, and `NOT_INCLUDED` |

## Portable Source Of Truth

Use these files for current-machine setup truth:

- `README.md`
- `ONE_PROMPT_START.md`
- `TOOLS_INDEX.md`
- `03_TOOLS/TOOLS_INDEX.md`
- `EXTERNAL_DEPENDENCIES.md`
- `LOCAL_SETUP_REQUIREMENTS.md`
- `docs/HEALTH_CHECK.md`
- `python health_check.py --no-write`
- `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`
- `python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`

## Remaining Gaps

- The repo portability layer is clean, but the local working tree still contains unrelated unstaged active-project files:
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_prl`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/NEXT_ALLOWED_PHASE.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROMPT_COUNTER.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/GATE_RECONCILIATION_REPORT.*`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/STALE_REPORTS_AUDIT.*`
- Historical reports still contain old absolute local paths by design. They are preserved as evidence and no longer treated as onboarding truth.
- Direct `pcbnew` import from the repo's normal Python remains a truthful warning on this machine. Board-aware workflows should use the KiCad-compatible Python context.

## Design File Safety

- `.kicad_sch` changed: `NO`
- `.kicad_pcb` changed: `NO`
- `.kicad_pro` changed: `NO`

## Conclusion

The five portability gap fixes remain effective. The tracked repo state no longer depends on routing scratch payloads, generated local KiCad index JSON, machine-specific tool inventory as portable truth, or historical absolute paths as setup instructions. Baseline startup does not require extra cloned GitHub repos.
