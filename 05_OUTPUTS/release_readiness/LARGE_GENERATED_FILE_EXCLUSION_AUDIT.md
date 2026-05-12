# Large Generated File Exclusion Audit

Generated: `2026-05-12`

Status: `PASS_WITH_IGNORED_LOCAL_ARTIFACTS`

## Local / Generated Paths Reviewed

| Path | Exists | Approx size | Ignore status | Notes |
| --- | --- | ---: | --- | --- |
| `installer/build/` | `YES` | large | `IGNORED` | Build artifacts remain local-only. |
| `installer/node_modules/` | `YES` | large | `IGNORED` | Bundled runtime/toolchain payload. |
| `03_TOOLS/python_envs/` | `YES` | large | `IGNORED` | Local Python environments remain excluded. |
| `03_TOOLS/node_envs/` | `YES` | local envs | `IGNORED` | Local Node environments remain excluded. |
| `node_modules/` | `NO` or not relevant | `0` | `IGNORED_RULE_PRESENT` | Root-level rule exists. |
| `.tool_cache/` | `NO` or not relevant | `0` | `IGNORED_RULE_PRESENT` | Cache rule exists. |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals/` | `YES` | local rehearsal outputs | `IGNORED` | Already excluded before this task. |
| `99_BACKUPS/` | `YES` | local backups | `IGNORED` | Must never be pushed. |
| `05_OUTPUTS/clean_sample_candidate_tests/` | `YES` | large | `IGNORED` | Clean-sample test output remains excluded. |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups/` | `YES` | `1.22 MB` | `IGNORED` | Newly ignored in this task. |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/tmp_real_board_audit/` | `YES` | `0.35 MB` | `IGNORED` | Newly ignored in this task. |

## Files Over `50 MB`

Still present locally:

- `installer/build/windows/win-unpacked/KiCad Engine Installer.exe`
- `installer/node_modules/electron/dist/electron.exe`
- `installer/build/windows/KiCad-Engine-Installer-0.1.0-win-x64.exe`
- `03_TOOLS/python_envs/windows_gui/Lib/site-packages/cv2/cv2.pyd`
- `05_OUTPUTS/clean_sample_candidate_tests/...`

## Conclusion

Large local/generated files remain in the working tree, but the reviewed heavy
paths are ignored or otherwise documented as excluded from push scope.

