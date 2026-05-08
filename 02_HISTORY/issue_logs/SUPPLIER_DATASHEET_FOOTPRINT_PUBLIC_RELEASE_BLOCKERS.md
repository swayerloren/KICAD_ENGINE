# Supplier Datasheet Footprint Public Release Blockers

Date opened: 2026-05-03
Status: `OPEN`
Severity: `HIGH`

## Issue

Supplier, datasheet, and footprint systems are useful for internal alpha work but are not public-release-ready.

## Blockers

- Two legacy Espressif PDFs under `06_DATASHEETS/99_UNSORTED_INBOX` need redistribution review or exclusion from public payloads.
- Supplier connectors are dry-run only; no live official API client is implemented or tested.
- Supplier-footprint matches are example-only and human-review-required.
- Footprint gap analysis produces candidates only; no exact package drawing verification is recorded.
- MCU and STM32 content is scaffolded with source links and unknown markers, not verified extracted datasheet data.
- Git metadata was unavailable in this checkout, so GitHub release state cannot be fully verified locally.

## Required Closure Criteria

- Public payload excludes or documents redistribution permission for all PDFs.
- At least one official supplier API connector is implemented, tested, and proven not to log secrets.
- A small supplier-footprint pilot set has real records, package drawing evidence, and human-review fields.
- CI runs dry-run and syntax tests for all three systems.
- Repo checkout is confirmed as a Git repository before release workflows are claimed ready.

