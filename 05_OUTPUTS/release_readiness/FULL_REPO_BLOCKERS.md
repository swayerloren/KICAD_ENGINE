# Full Repo Blockers

Audit date: `2026-05-03`

Public release status: `NOT_READY`

| Priority | Blocker | Affected files | Fix prompt needed |
|---|---|---|---|
| 1 | Public release payload is not clean. | `03_TOOLS/python_envs`, `03_TOOLS/node_envs`, `03_TOOLS/repos`, installer payload/build folders | Build clean manifest and exclude generated/vendor/tool material. |
| 2 | Current workspace is not a git repo. | root `.git` missing | Initialize or clone as a real Git checkout before release validation. |
| 3 | Old absolute paths remain. | `README_GPT.md`, `FOR CHAT GPT.MD`, `00_CODEX_START/TOOL_INDEX.md` | Normalize or mark as historical examples. |
| 4 | Too much scaffold remains. | weak/placeholder CSVs | Replace generic scaffold with useful content or mark reserved. |
| 5 | Datasheet redistribution review is open. | two PDFs under `06_DATASHEETS/99_UNSORTED_INBOX` | Confirm rights or convert to link-only. |
| 6 | Component records are mostly unverified. | `08_COMPONENT_DATABASE` | Create verified source-backed pilot records. |
| 7 | Footprint verification is not production-grade. | `29_FOOTPRINT_GAP_ANALYSIS`, `30_SUPPLIER_FOOTPRINT_MATCHES` | Verify exact package drawings and footprint matches. |
| 8 | Active ESP32 project is blocked. | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` | Resolve BOM, footprint, connector, PMOS, USB, and regulator blockers. |
| 9 | Installer is prototype-grade. | `installer/build/windows`, installer docs | Sign, test clean-machine installs, and build macOS/Linux artifacts. |
| 10 | Script safety needs triage. | `FULL_REPO_SCRIPT_AUDIT.csv` | Review install/network/destructive patterns and run Bash checks in CI. |
| 11 | Legal/security review is incomplete. | legal docs, third-party repos, history logs | Review third-party content, PDFs, and secret-like hits. |
| 12 | No full pipeline sample passes. | `15_BENCHMARKS`, `19_TEST_PROJECTS`, active project | Build one safe passing public sample. |
