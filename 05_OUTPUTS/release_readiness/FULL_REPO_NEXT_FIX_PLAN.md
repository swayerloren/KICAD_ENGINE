# Full Repo Next Fix Plan

Audit date: `2026-05-03`

Goal: move from internal alpha toward public alpha without hiding engineering risk.

1. Public payload cleanup: exclude envs, vendored repos, backups, generated smoke outputs, old logs not useful to end users, and unreviewed PDFs.
2. Path normalization: replace stale `C:\Users\LJ\KICAD_ENGINE` references with repo-relative paths or clearly marked historical examples.
3. Scaffold triage: work through `FULL_REPO_WEAK_FILES.csv` and `FULL_REPO_EMPTY_OR_PLACEHOLDER_FILES.csv` by subsystem.
4. Script hardening: review safety flags, add dry-run/help/log behavior where needed, and run Bash syntax checks in Linux/macOS CI.
5. Legal/security cleanup: review PDFs, third-party repos, vendor docs, generated outputs, and secret-like hits.
6. Verified component pilot: source-backed records for STM32F103C8T6, ESP32-S3-WROOM-1U, AP63203, AO3401A, TPD2EUSB30, and one exact USB-C connector.
7. Verified footprint pilot: exact package drawings, KiCad footprint pad mapping, symbol mapping, and orientation notes for the same pilot parts.
8. Active project decision: either repair `ESP32_CSI_WIFI_NODE` until the schematic-to-PCB gate passes or archive it as a blocked safety example.
9. Installer hardening: rebuild clean payload, smoke-test clean machines, sign/notarize/package per platform.
10. Public-alpha release-candidate audit: rerun quality, legal, security, script, payload, and sample-project checks before drafting release.

Do not mass-rewrite the repo. Each fix should be a small scoped task with exact files, verification output, and updated history.
