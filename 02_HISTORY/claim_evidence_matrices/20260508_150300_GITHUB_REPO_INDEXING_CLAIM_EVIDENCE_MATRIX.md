# Claim Evidence Matrix

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| The repo already existed on GitHub before this task | user-provided repo URL plus local `origin` push success |
| The active project is `ESP32_CSI_WIFI_NODE` | `00_CODEX_START/CURRENT_PROJECT.md` and active-project memory/status files |
| The active PCB is not fabrication-ready | `FINAL_PCB_VISUAL_REVIEW_PACKET.md`, `CURRENT_PROJECT_STATE.md`, and `CURRENT_BLOCKERS.md` |
| Live PCB state includes a real board with partial routing | `CURRENT_PROJECT_STATE.md` and project review reports |
| Public release is still blocked | `README.md`, `PUBLIC_RELEASE_CHECKLIST.md`, `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md`, and `GITHUB_PUSH_REPORT.md` |
| The staged indexing update excluded lock files, `.env` files, and local-only artifacts | staged-path regex checks and `git status` review |
| `05_OUTPUTS/OUTPUTS_INDEX.md` required explicit inclusion because of ignore policy | `git add` refusal followed by `git add -f 05_OUTPUTS\\OUTPUTS_INDEX.md` |
| Base indexing commit was pushed successfully | `git push -u origin main` output and local `git rev-parse HEAD` |
