# Supplier Datasheet Footprint Blockers

Date: 2026-05-03
Classification impact: blocks `PUBLIC_BETA` and `PUBLIC_RELEASE_READY`

## Critical Blockers

1. `06_DATASHEETS` contains two legacy Espressif PDFs:
   - `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/ESP32-S3-WROOM-1U-N16R8.pdf`
   - `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf`
   Redistribution status is not confirmed in this audit. Public release must either prove redistribution rights or exclude/link-only these files.

2. Supplier connectors are dry-run only.
   Digi-Key, Mouser, JLCPCB, and LCSC stubs are safe, but no live official API connector has been implemented or tested.

3. Supplier-footprint matching has no production verified records.
   The current match index has 6 records, all `EXAMPLE_ONLY` and human-review-required.

4. Footprint gap candidates are not package-drawing verified.
   The footprint gap report checks 125 records and leaves all 125 requiring verification or missing candidates.

5. STM32 and MCU family data remains scaffolded.
   The content is useful AI guidance, but exact electrical values, datasheet section references, pinout checks, package drawings, and footprint approvals are still unresolved.

## Major Blockers

- MCU support folders remain weak, including design guides, errata, module folders, Nucleo/Discovery/Eval board folders, and programming/debug folders.
- No CI job currently proves supplier connector dry-run tests, footprint gap scripts, and supplier-footprint match scripts on every release.
- No release packaging guard was run here to exclude restricted PDFs from payloads.
- `git status --short` failed because this working folder is not currently recognized as a Git repository. GitHub release readiness cannot be fully assessed from Git metadata in this checkout.

## Non-Blocker Warnings

- No obvious API key/token/password patterns were found in audited supplier/footprint folders.
- No recent installed KiCad `share`, `lib`, or `etc` modifications were found.
- No recent KiCad design/library file modifications were found during this audit window.

