# Supplier Source Policy

## Source Priority

1. Official supplier APIs and approved feeds.
2. User-provided CSV exports from supplier portals.
3. Manual source-link records with source date and human review.

## Forbidden Collection Methods

- Blind scraping of supplier websites.
- Bypassing rate limits, robots, login protections, CAPTCHAs, or anti-automation controls.
- Storing private account pages or restricted responses without permission.
- Mass-downloading datasheets unless redistribution is clearly allowed.
- Treating supplier package text as verified footprint evidence.

## Time-Sensitive Fields

These fields must include source date and source URL or import file:

- Stock quantity.
- Price breaks.
- Lifecycle status.
- Availability or lead time.
- Minimum order quantity.
- Packaging availability.
- Supplier SKU status.

## Verification Status

Use these labels:

- `VERIFIED_FROM_OFFICIAL_API`
- `VERIFIED_FROM_USER_CSV`
- `VERIFIED_FROM_MANUAL_SOURCE_LINK`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `CONTRADICTED`
- `REQUIRES_HUMAN_REVIEW`

## Datasheet Handling

Store datasheet URLs, titles, document types, source dates, and redistribution status. Do not download or commit PDFs by default.
