# Mouser Field Mapping

Status: `DRY_RUN_MAPPING`

## Normalized Field Mapping

| Normalized field | Mouser/sample field candidates | Verification |
| --- | --- | --- |
| `source.supplier` | fixed `Mouser` | `UNVERIFIED` until connector tested |
| `source.source_type` | `source_type` or `dry_run_sample` | `UNVERIFIED` |
| `source.source_url` | `--source-url` | `UNVERIFIED` |
| `source.retrieved_at` | connector timestamp | time-sensitive |
| `manufacturer.name` | `manufacturer`, `Manufacturer` | `UNVERIFIED` |
| `manufacturer.manufacturer_part_number` | `manufacturer_part_number`, `ManufacturerPartNumber`, `mpn`, `part_number`, `--query` | `UNVERIFIED` |
| `manufacturer.lifecycle_status` | `lifecycle_status` | `UNVERIFIED` |
| `supplier_part.supplier_sku` | `supplier_sku`, `MouserPartNumber`, `mouser_part_number`, `sku` | `UNVERIFIED` |
| `supplier_part.supplier_part_url` | `supplier_part_url`, `ProductDetailUrl`, `product_url`, `url` | `UNVERIFIED` |
| `supplier_part.description` | `description`, `Description` | `UNVERIFIED` |
| `supplier_part.category` | `category`, `Category` | `UNVERIFIED` |
| `package.supplier_package` | `supplier_package`, `PackageType`, `package` | `UNVERIFIED` |
| `inventory_price.stock_quantity` | `stock_quantity`, `AvailabilityInStock` | time-sensitive |
| `inventory_price.minimum_order_quantity` | `minimum_order_quantity`, `Min` | time-sensitive |
| `inventory_price.price_breaks` | `price_breaks`, `PriceBreaks`, `pricing` | time-sensitive |
| `datasheets[]` | `datasheet_url`, `DataSheetUrl`, `datasheet` | link-only |
| `footprint_risk.*` | connector-generated warning notes | human review required |

## Rule

Package text is not package drawing verification. Footprint matches remain `UNVERIFIED` until checked against manufacturer package drawings.
