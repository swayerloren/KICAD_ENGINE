# BOM For Assembly Rules

Status: `NOT_FINAL_UNTIL_HUMAN_REVIEW`

## Required Fields

| Field | Required For Assembly Review | Notes |
| --- | --- | --- |
| `Reference` | Yes | Must match schematic and PCB. |
| `Quantity` | Yes | Must match grouped references and DNP status. |
| `Value` | Yes | Generic value is not enough for exact assembly unless intentionally generic. |
| `Footprint` | Yes | Candidate is not approval; footprint audit must exist. |
| `Manufacturer` | Exact parts | Required for assembly-specified parts. |
| `MPN` | Exact parts | Must include suffix/package/orderable variant when needed. |
| `SupplierSKU` | Optional unless turnkey build | Must come from authorized/API/manual source records. |
| `Package` | Yes | Must align with footprint and package drawing. |
| `DNP` | Yes | Every line must be fitted, not fitted, or variant-specific. |
| `DatasheetSource` | Yes for exact parts | Link-only is acceptable for public repo; claim stays unverified until reviewed. |
| `SubstitutionAllowed` | Yes | Human-approved substitutions only. |
| `HumanReviewRequired` | Yes | True for high-risk or unverified lines. |

## Review Steps

1. Check designator coverage against schematic and PCB.
2. Check quantities and grouped references.
3. Check exact MPNs, suffixes, voltage/tolerance/package ratings, and substitutions.
4. Check connector mating parts, cable assemblies, hardware, jumpers, and test points.
5. Check lifecycle, availability, and price only from current source data.
6. Check footprint/package status for all assembly-critical parts.
7. Save BOM review report with `NOT_FINAL` status unless human assembly approval exists.

## Common Mistakes

- Using generic values without MPNs for assembly.
- Missing DNP or variant status.
- Treating placeholder component records as approved.
- Forgetting connector mating parts or cable assemblies.
- Assuming supplier package text verifies a KiCad footprint.
- Exporting a BOM from KiCad and calling it production-ready without source and footprint review.

## Human Review Gate

Assembly BOMs require human approval of MPNs, substitutions, fitted status, connector mating system, package/footprint match, and sourcing. AI may prepare a `NOT_FINAL` review BOM but must not approve procurement or assembly.
