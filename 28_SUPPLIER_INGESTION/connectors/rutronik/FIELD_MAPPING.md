# Rutronik Field Mapping

Status: `DRAFT`

| Supplier Field | Normalized Field | Notes |
| --- | --- | --- |
| Manufacturer | manufacturer.name | Keep exact supplier text until reviewed. |
| ManufacturerPartNumber / MPN | manufacturer.manufacturer_part_number | Do not merge variants without evidence. |
| SupplierPartNumber / SKU | supplier_part.supplier_sku | Supplier-specific identifier. |
| Description | supplier_part.description | Not datasheet proof. |
| ProductUrl | supplier_part.supplier_part_url | Source link. |
| DatasheetUrl | datasheets[].source_url | Link-only unless redistribution reviewed. |
| Package | package.supplier_package | Candidate evidence only. |
| Stock | inventory_price.stock_quantity | Time-sensitive snapshot. |
| PriceBreaks | inventory_price.price_breaks | Time-sensitive snapshot. |
| LifecycleStatus | manufacturer.lifecycle_status | Requires source date. |

## Footprint Warning

Supplier package text can help find candidates, but exact footprint approval requires manufacturer package drawing verification and human review.
