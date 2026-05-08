# Public Release Exclusion Manifest

Status: `ACTIVE_P0_RELEASE_GATE`

Last updated: `2026-05-06`

Purpose: define files and folders that must not be copied into a public GitHub release, installer payload, or release archive unless a human release review explicitly approves an exception.

## Always Exclude

- Secrets, API keys, tokens, passwords, license keys, SSH keys, private keys, `.env` files, and local credential files.
- `03_TOOLS/python_envs/`
- `03_TOOLS/node_envs/`
- `03_TOOLS/repos/`
- `03_TOOLS/windows/repos/`
- `03_TOOLS/linux/repos/`
- `03_TOOLS/tool_logs/`
- `03_TOOLS/windows/logs/`
- `03_TOOLS/linux/logs/`
- `05_OUTPUTS/` generated outputs unless a specific output is an approved public sample.
- `99_BACKUPS/`
- `installer/build/`
- `installer/dist/`
- `installer/node_modules/`
- `installer/payload/repo-template/`
- `installer/payload/payload.manifest.json`
- `installer/payload/PAYLOAD_BUILD_REPORT.md`
- Any generated smoke-test install tree.
- `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/benchmark_candidates/`
- Any generated Gerber, drill, STEP, PNP/CPL, BOM, fabrication package, or manufacturing-style output unless it is intentionally included as a `NOT_FINAL` sample and reviewed.
- Any downloaded datasheet PDF, vendor app note, vendor reference manual, vendor schematic, CAD model, symbol, footprint, or 3D model unless redistribution rights are recorded.
- Historical command logs that embed third-party installer output, `.env.example` contents, placeholder token strings, or copied third-party docs. Prefer curated summaries for public release.
- Any file marked `FAB_READY` unless a separate human release approval records source, license, reason for inclusion, and reviewer.

## Sample Project Payload Gate

Open KiCad samples are excluded unless every requirement below is met:

1. Source URL, imported commit/timestamp, license, and attribution are recorded.
2. Public bundle status is exactly `PUBLIC_BUNDLE_ALLOWED`.
3. The sample is included from a controlled public sample path, not from `imported_originals/` or `normalized_samples/`.
4. Any generated output is marked `NOT_FINAL`.
5. Any included evidence is small, useful, and explicitly listed in `PAYLOAD_ALLOWLIST.md`.
6. Human release review is recorded.

Apply these companion files before building any payload:

- `PAYLOAD_ALLOWLIST.md`
- `PAYLOAD_EXCLUDE_RULES.md`
- `SAMPLE_PROJECT_PAYLOAD_POLICY.md`
- `PUBLIC_PAYLOAD_MANIFEST.md`

## Current P0 Human Review Items

These files are present locally and must not be included in a public release until rights are reviewed or the files are converted to link-only records:

- `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/ESP32-S3-WROOM-1U-N16R8.pdf`
- `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf`
- `02_HISTORY/command_logs/KICAD_MCP_PRO_INSTALL_COMMANDS.md` contains copied third-party `.env.example` placeholder token strings and must be excluded or summarized before public release.
- `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/` is a controlled sample fixture with MIT license evidence but public bundle status remains `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`; exclude KiCad source files, project-local footprints, generated visuals, gate-run folders, and any fabrication-style outputs from installer payloads and curated public release bundles until final human license/release review approves inclusion. Small markdown status/attribution docs may be included only as allowed by `PAYLOAD_ALLOWLIST.md`.

## Release Gate

Before publishing, run a release payload audit that proves the excluded paths above are absent from:

- GitHub source archive, if intentionally controlled.
- Installer payload.
- Release ZIP/tarball.
- Draft release artifacts.

If an excluded item is intentionally included, the release notes must state the reason, source, license/redistribution evidence, and human reviewer.
