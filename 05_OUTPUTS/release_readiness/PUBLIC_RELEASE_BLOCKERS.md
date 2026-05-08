# Public Release Blockers

Date: 2026-05-03

## Hard Blockers

1. Source workspace is not a Git repository and has no `.gitignore`.
   - `git status --short` returned: not a git repository.
   - Public release process cannot be verified through normal Git review yet.

2. Source tree contains local development artifacts that should not be public release content.
   - `03_TOOLS/repos`: third-party cloned repos.
   - `03_TOOLS/windows/repos`: third-party Windows GUI helper repos.
   - `03_TOOLS/python_envs`: local Python environments.
   - `03_TOOLS/node_envs`: local Node environments.
   - `installer/build`: generated Electron build output.
   - `05_OUTPUTS`: generated reports, copied demos, and review outputs.

3. Vendor PDFs remain in `06_DATASHEETS`.
   - `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/ESP32-S3-WROOM-1U-N16R8.pdf`
   - `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf`
   - Redistribution status: unclear. Use link-only metadata unless permission is confirmed.

4. Private/reference KiCad projects remain in the source tree.
   - `04_KICAD_PROJECTS/active/COMMAND_LINK_VERIFIED_REFERENCE`
   - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - These should be excluded unless explicitly approved and sanitized as public samples.

5. Manufacturing-style outputs are present and not uniformly labeled `NOT_FINAL`.
   - Audit scan found 116 manufacturing-like files outside excluded tool paths.
   - 90 did not contain `NOT_FINAL` in the path.
   - Most are old reference files, backups, copied demo outputs, or generated samples. They should not be part of public release content.

6. Legal/license review is incomplete for bundled third-party repos and copied/generated examples.
   - Existing risk register already marks `KiBot` AGPL, `AutoHotkey` GPL, mixed nested licenses, generated demos, and private projects as requiring review/exclusion.

7. Installer release artifacts are not production-ready.
   - Windows EXE is unsigned and not clean-machine GUI smoke-tested.
   - macOS artifacts are not built, signed, notarized, stapled, or Gatekeeper-tested.
   - Linux AppImage/DEB artifacts are not smoke-tested.

## Medium Blockers

1. Old command logs contain placeholder token examples.
   - No active secret was found in the clean payload.
   - Old logs should still be excluded or scrubbed before public source release.

2. Datasheet and component databases are scaffolding-heavy.
   - This is acceptable if clearly documented.
   - Do not claim completeness.

3. Benchmarks exist but have no actual results.
   - This is acceptable for methodology.
   - Do not use benchmarks for public comparison claims yet.

4. macOS/Linux support is documentation/source-level only.
   - Public docs should label these as untested until CI and clean-machine runs are complete.

## Not Blockers

- README claims are conservative and do not claim KiCad replacement or fabrication approval.
- Flux/cloud PCB AI comparison docs avoid unsupported superiority claims.
- Setup scripts ask before installing tools.
- Installer source blocks unsafe install paths including KiCad install folders.
- Clean payload health check passes.
