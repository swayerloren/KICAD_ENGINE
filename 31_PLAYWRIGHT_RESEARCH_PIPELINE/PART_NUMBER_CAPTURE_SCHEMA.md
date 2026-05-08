# Part Number Capture Schema

Status: `SCHEMA_DRAFT`

| Field | Required | Notes |
| --- | --- | --- |
| `manufacturer` | Yes | Exact manufacturer name if available. |
| `manufacturer_part_number` | Yes | MPN or generic target label. |
| `supplier` | No | Distributor/source name. |
| `supplier_sku` | No | Distributor SKU when captured from allowed source. |
| `family` | No | Product family. |
| `category` | Yes | MCU, power, communication, connector, protection, passive, RF, etc. |
| `package` | No | Supplier/manufacturer package text; not footprint proof. |
| `lifecycle_status` | No | Time-sensitive; requires source date. |
| `stock_status` | No | Time-sensitive; requires source date and source URL. |
| `price_breaks_summary` | No | Summary only; no private quote data. |
| `verification_status` | Yes | Default `UNVERIFIED`. |
| `human_review_required` | Yes | Default `true`. |

