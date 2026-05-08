# Normalized Supplier Records

Status: `GENERATED_METADATA_NOT_SOURCING_APPROVAL`

Generated normalized supplier records belong here. These records are safe summaries produced from official APIs, user-provided CSV exports, or manual source-link records. They are not raw restricted API responses and they are not purchasing approval.

## Required Normalized Fields

| Field | Required | Guidance |
| --- | --- | --- |
| `manufacturer` | Yes | Exact manufacturer name if present; otherwise `Unknown - requires source verification`. |
| `manufacturer_part_number` | Yes | Exact MPN or `generic_placeholder`. |
| `supplier` | Yes | Source supplier or `manual_csv`. |
| `supplier_sku` | Desired | Leave blank only when the source does not provide it. |
| `product_url` | Yes | Source page or API source URL. |
| `datasheet_url` | Desired | Link-only by default; do not download PDFs. |
| `package` | Desired | Supplier package text is candidate metadata only. |
| `lifecycle_status` | Desired | Current-source claim only; mark stale/unknown explicitly. |
| `stock_status` | Optional | Snapshot only with retrieval timestamp. |
| `price_breaks_summary` | Optional | Snapshot only; do not treat as quote approval. |
| `retrieved_at` | Yes | ISO timestamp. |
| `verification_status` | Yes | Default `UNVERIFIED`. |
| `redistribution_status` | Yes | Usually `LINK_ONLY` or `METADATA_ONLY`. |
| `human_review_required` | Yes | True for high-risk parts and any exact sourcing use. |

## Rules

- Records are metadata snapshots, not sourcing approval.
- Mark unreviewed records `UNVERIFIED`.
- Do not store raw restricted API responses.
- Do not store credentials, API keys, cookies, tokens, or private account data.
- Do not store downloaded datasheets.
- Do not promote package text into footprint verification.
- Preserve source URL and retrieval timestamp so stale data can be identified.

## Agent Use

Agents may use normalized records to identify candidate MPNs, supplier SKUs, source URLs, lifecycle clues, and package text. Agents must not use these records as proof that a part is in stock, correctly priced, lifecycle-safe, or footprint-verified without current source review and human approval where required.
