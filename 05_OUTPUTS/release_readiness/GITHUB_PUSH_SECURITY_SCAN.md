# GitHub Push Security Scan

Status: `NO_LIVE_SECRET_BLOCKER_FOUND`

Date: `2026-05-08`

## Commands Run

- `gh auth status`
- `git status --short --branch --ignored`
- exact-token scans for:
  - `ghp_...`
  - `github_pat_...`
  - `sk-...`
- assignment-style credential scan for:
  - `API_KEY`
  - `SECRET`
  - `TOKEN`
  - `PASSWORD`
- `.env` file discovery
- `*.lck` discovery
- large-file scan for files over `50 MB`

## Secret Scan Result

- Exact GitHub/OpenAI-style token matches: `0`
- Assignment-style credential matches: `0`
- Real `.env` files found: `0`
- `.env.example` files found: `1`

Observed `.env.example` path:

- `03_TOOLS/repos/kicad-mcp-pro/.env.example`

This `.env.example` is inside an ignored third-party repo copy and does not block the push.

## Placeholder / Reference Token Noise

The broader text scan found placeholder or workflow-reference strings, not live credentials. Examples:

- `.github/workflows/release-draft.yml`
  - `GH_TOKEN: ${{ github.token }}`
- `02_HISTORY/command_logs/KICAD_MCP_PRO_INSTALL_COMMANDS.md`
  - placeholder strings such as `replace-with-your-kicad-ipc-token`
- `02_HISTORY/command_logs/KICAD_HAPPY_INSTALL_COMMANDS.md`
  - workflow-secret references such as `${{ secrets.OPENAI_API_KEY }}`
- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/.github/workflows/issue_handler.yml`
  - `github-token: ${{ secrets.PAT }}`

These strings are not evidence of a live credential in the workspace, but they remain public-release hygiene concerns.

## KiCad Lock File Result

- Lock files found: `8`

Representative paths:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/~ESP32_CSI_WIFI_NODE.kicad_pro.lck`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428/.../~ESP32_CSI_WIFI_NODE.kicad_pro.lck`
- additional lock files inside `99_BACKUPS/`

Current disposition:

- ignored by `.gitignore`
- do not stage
- do not push

## Large File Result

- Files over `50 MB` found: `7`
- All current over-limit files are ignored by `.gitignore`

Ignored large-file examples:

- `installer/build/windows/win-unpacked/KiCad Engine Installer.exe` — `212.79 MB`
- `installer/node_modules/electron/dist/electron.exe` — `212.79 MB`
- `03_TOOLS/windows/repos/SikuliX1/.git/objects/pack/...` — `171.50 MB`
- `installer/build/windows/KiCad-Engine-Installer-0.1.0-win-x64.exe` — `95.59 MB`
- `03_TOOLS/repos/KiBot/.git/objects/pack/...` — `75.61 MB`
- `03_TOOLS/python_envs/windows_gui/Lib/site-packages/cv2/cv2.pyd` — `71.35 MB`
- `05_OUTPUTS/clean_sample_candidate_tests/installed_demos_20260430_173955/.../vme-wren.kicad_pcb` — `68.24 MB`

## Security Decision

- Push blocked by live secrets: `NO`
- Push blocked by `.env` files: `NO`
- Push blocked by lock files: `NO`, because they are ignored
- Push blocked by large files: `NO`, because they are ignored

## Remaining Caution

Private GitHub push may continue.

Public release is still not safe without separate cleanup of:

- placeholder-token historical logs
- license/redistribution review items
- excluded binary/sample payload content
