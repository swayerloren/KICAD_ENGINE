# Supplier Source Lists

Status: `INPUT_TEMPLATES_AND_USER_PROVIDED_SOURCE_LISTS`

CSV and JSON source lists belong here. These files define what supplier or vendor records should be researched, imported, or normalized. They should be small, reviewable, and safe to commit only when they contain no secrets and no private customer/account data.

## Allowed Inputs

- User-provided supplier CSV exports after secrets/private account fields are removed.
- Manually curated source-link lists.
- Official API result metadata only when redistribution and terms allow it.
- Dry-run target lists for future research.

## Required CSV Fields

| Field | Required | Notes |
| --- | --- | --- |
| `manufacturer` | Yes | Exact vendor/manufacturer when known. |
| `manufacturer_part_number` | Yes | MPN or `generic_placeholder`. |
| `supplier` | Yes | Digi-Key, Mouser, JLCPCB, LCSC, manual, etc. |
| `supplier_sku` | Optional | Use only if public/user-provided and non-secret. |
| `product_url` | Desired | Prefer source page over search result. |
| `datasheet_url` | Optional | Link-only; do not download by default. |
| `package` | Optional | Candidate metadata only. |
| `category` | Optional | Component database category. |
| `verification_status` | Yes | Default `UNVERIFIED`. |
| `notes` | Optional | Include source caveats. |

## Prohibited Inputs

- API keys, access tokens, session IDs, cookies, account numbers, private quotes, or order history.
- Bulk scraped HTML or restricted API payloads.
- Downloaded PDFs unless redistribution status is reviewed elsewhere.

## Agent Use

Agents should treat these lists as input intent, not verified data. Run normalization and gap reporting before updating downstream component or footprint records.
