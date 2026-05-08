# Batch 004 USB-C Connectors Report

Classification: `SOURCE_LINKS_CAPTURED`

Human review state: `NEEDS_HUMAN_REVIEW`

## Run Summary

- Scope: USB-C connector source-link and exact-manufacturer-part discovery.
- Target CSV: `31_PLAYWRIGHT_RESEARCH_PIPELINE/research_targets/batch_004_usb_c_connectors_targets.csv`
- Dry-run output: `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/20260503_122259_batch_expansion/batch_004_usb_c_connectors/research_plan.json`
- Normalized output: `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/20260503_122259_batch_expansion/batch_004_usb_c_connectors/normalized_records.json`
- Records: 7
- Live capture: `BLOCKED_PLAYWRIGHT_NOT_AVAILABLE`
- PDFs downloaded: `false`
- Verification status: `UNVERIFIED`

## Notes

USB-C connectors remain high risk. Generic USB-C connector rows are not footprint candidates for production. Exact manufacturer part number, drawing, pin numbering, shell/tab geometry, board-edge relationship, 3D/mechanical review, and human orientation review are required.

## Required Next Step

Select exact manufacturer parts first, then verify the KiCad footprint against the drawing and orientation. Do not use package-name or connector-family text as verification.

