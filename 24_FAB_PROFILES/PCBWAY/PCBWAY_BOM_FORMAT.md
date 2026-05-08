# PCBWay BOM Format

Status: `ACTIVE_RULES`

## Required Columns

```csv
Line #,Quantity Per Part Number,Reference Designator,Part Number,Part Description,Package,Type,Manufacturer Name,Manufacturer Part Number,Distributor Part Number,Notes
```

## Rules

- `Quantity Per Part Number` must match the comma-separated reference designator count.
- `Reference Designator`, `Part Number`, `Part Description`, `Package`, and `Type` are required for upload review.
- Manufacturer and distributor fields are required for turn-key or partial turn-key confidence.
- Through-hole parts may remain in the BOM even if not listed in centroid.

