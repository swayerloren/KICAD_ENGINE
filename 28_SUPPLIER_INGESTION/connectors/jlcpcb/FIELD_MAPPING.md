# JLCPCB Field Mapping

Status: `DRY_RUN_MAPPING`

## Normalized Field Mapping

| Normalized field | JLCPCB/export field candidates | Verification |
| --- | --- | --- |
| `source.supplier` | fixed `JLCPCB` | `UNVERIFIED` until connector tested |
| `source.source_type` | `source_type` or `dry_run_sample_or_user_export` | `UNVERIFIED` |
| `source.source_url` | `--source-url` | `UNVERIFIED` |
| `source.retrieved_at` | connector timestamp | time-sensitive |
| `manufacturer.name` | `manufacturer`, `manufacturer_name` | `UNVERIFIED` |
| `manufacturer.manufacturer_part_number` | `manufacturer_part_number`, `mpn`, `part_number`, `--query` | `UNVERIFIED` |
| `manufacturer.lifecycle_status` | `lifecycle_status` | `UNVERIFIED` |
| `supplier_part.supplier_sku` | `supplier_sku`, `jlcpcb_part_number`, `jlc_part_number`, `part_number` | `UNVERIFIED` |
| `supplier_part.jlc_lcsc_part_number` | `lcsc_part_number`, `LCSC Part`, `lcsc` | `UNVERIFIED` |
| `supplier_part.supplier_part_url` | `supplier_part_url`, `product_url`, `url` | `UNVERIFIED` |
| `supplier_part.description` | `description` | `UNVERIFIED` |
| `supplier_part.category` | `category` | `UNVERIFIED` |
| `package.supplier_package` | `supplier_package`, `package` | `UNVERIFIED` |
| `inventory_price.stock_quantity` | `stock_quantity` | time-sensitive |
| `inventory_price.minimum_order_quantity` | `minimum_order_quantity` | time-sensitive |
| `inventory_price.price_breaks` | `price_breaks`, `pricing` | time-sensitive |
| `datasheets[]` | `datasheet_url`, `datasheet` | link-only |
| `footprint_risk.*` | connector-generated warning notes | human review required |

## Rule

JLCPCB package or assembly text is not package drawing verification. Footprint and PNP orientation matches remain `UNVERIFIED` until checked against exact manufacturer drawings and assembly orientation evidence.
