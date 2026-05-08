# Supplier Ingestion Index

Status: `ACTIVE_SCAFFOLD`

## PURPOSE

AI-readable routing index for supplier and vendor ingestion assets.

## WHAT_BELONGS_HERE

| Path | Purpose |
| --- | --- |
| `SOURCE_POLICY.md` | Source priority, no-scraping rules, redistribution rules. |
| `API_KEY_HANDLING.md` | Credential handling without storing keys in the repo. |
| `SUPPLIER_CONNECTOR_STANDARD.md` | Requirements for every supplier connector. |
| `DATA_NORMALIZATION_SCHEMA.md` | Canonical normalized supplier record shape. |
| `SUPPLIER_PART_SCHEMA.md` | Supplier part and MPN fields. |
| `INVENTORY_PRICE_SCHEMA.md` | Stock and pricing metadata fields. |
| `DATASHEET_LINK_SCHEMA.md` | Datasheet link metadata and redistribution fields. |
| `FOOTPRINT_GAP_SCHEMA.md` | Package and footprint-risk fields. |
| `connectors/` | Connector-specific API notes, auth notes, rate limits, and field mappings. |
| `source_lists/` | User-maintained source lists and CSV manifests. |
| `normalized/` | Generated normalized JSON/Markdown records. |
| `reports/` | Generated supplier gap, index, and match reports. |
| `scripts/` | Safe local import, normalization, index, and matching scripts. |
| `templates/` | Example records and input templates. |

## WHAT_DOES_NOT_BELONG_HERE

- Secrets or credentials.
- Raw restricted API responses intended for private use only.
- Scraped HTML.
- Downloaded datasheet archives.
- KiCad source files.

## AI_AGENT_RULES

- Read `SOURCE_POLICY.md` before collecting supplier data.
- Read `API_KEY_HANDLING.md` before designing or running a connector.
- Read connector `AUTH_REQUIREMENTS.md` and `RATE_LIMIT_AND_TERMS_NOTES.md` before any live API call.
- Use `UNVERIFIED` status for unreviewed imports.
- Route curated component decisions back to `08_COMPONENT_DATABASE` only after a separate verification step.

## SAFE_EDIT_RULES

- Keep examples fake and marked as examples.
- Keep generated records timestamped or source-dated.
- Do not overwrite normalized records without explicit output path and user intent.

## PUBLIC_RELEASE_NOTES

Connector scaffolds are public-safe only if they contain no credentials, private commercial data, restricted API payloads, or unsupported claims.
