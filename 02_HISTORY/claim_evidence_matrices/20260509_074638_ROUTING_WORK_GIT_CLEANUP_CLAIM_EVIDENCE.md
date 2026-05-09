# Claim Evidence Matrix

Timestamp: `20260509_074638`
Status: `UNVERIFIED`
Task: `routing_work git cleanup`

| Claim | Evidence |
| --- | --- |
| The timestamped `routing_work` payload was tracked in Git before cleanup. | `git ls-files 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` |
| The tracked payload was scratch/rehearsal output, not reusable source scripts. | file-extension and content summary in `ROUTING_WORK_GIT_CLEANUP_REPORT.md` |
| The timestamped payload was removed from Git tracking but kept on disk. | `git rm -r --cached ...` plus `Test-Path` result in the cleanup report |
| Future `routing_work` contents are ignored while `README.md` remains tracked. | `.gitignore` diff and `git check-ignore -v --no-index` output |
| Live KiCad design files were not changed. | `git status --short` and cleanup validation summary |
