# Integration With 30_SUPPLIER_FOOTPRINT_MATCHES

Playwright research can supply evidence links for supplier-to-footprint match records, but cannot approve matches by itself.

## Allowed Outputs

- Source URLs.
- Supplier product page URLs.
- Candidate package text.
- Public KiCad library page links.
- Screenshot evidence from public pages.

## Required Status

Generated match proposals must keep:

- `footprint_match_status`: `UNVERIFIED`
- `pinout_status`: `UNVERIFIED`
- `human_review_required`: `true`

High-risk connectors, PMOS/MOSFETs, ESD arrays, MCU modules, and regulators must not be marked verified from package text or browser evidence alone.

