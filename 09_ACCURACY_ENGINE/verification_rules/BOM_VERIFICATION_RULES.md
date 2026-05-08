# BOM Verification Rules

Status: `MANDATORY_BEFORE_SOURCING_OR_FAB_REVIEW`

## Purpose

Prevent AI-generated BOMs from becoming accidental sourcing, assembly, or fabrication approval. A KiCad BOM export is only a raw design artifact until each line is checked against the schematic, component database, datasheet/source records, supplier records, and footprint/package evidence.

## Required BOM Line Fields

| Field | Required | Blocks Release If Missing |
| --- | --- | --- |
| `references` | Yes | Yes. Every designator must be annotated and unique. |
| `quantity` | Yes | Yes. Quantity must match references and DNP policy. |
| `value` | Yes | Yes. Vague values block exact-part sourcing. |
| `manufacturer` | Required for exact parts | Yes for exact parts; optional for true generics. |
| `manufacturer_part_number` | Required for exact parts | Yes for exact parts. |
| `package` | Yes | Yes when package affects footprint, assembly, voltage, current, or thermal limits. |
| `kicad_symbol` | Yes | Yes for schematic approval. |
| `kicad_footprint` | Yes | Yes for PCB update and fab review. |
| `datasheet_or_source_url` | Yes | Yes unless intentionally generic and human-approved. |
| `verification_status` | Yes | Yes if not `PARTIALLY_VERIFIED` or better for exact parts. |
| `footprint_status` | Yes | Yes unless still in planning-only mode. |
| `lifecycle_status` | Desired | Blocks only when required by project or source evidence indicates risk. |
| `supplier_sku` | Optional | Does not block design, but blocks turnkey sourcing if required. |
| `dnp_status` | Yes | Ambiguous DNP blocks BOM lock. |
| `human_review_required` | Yes | If true, fab/sourcing remains blocked until reviewed. |

## Required Checks

1. Confirm every schematic reference appears in the BOM and every BOM reference appears in the schematic.
2. Confirm no references end in `?` and no duplicate references exist.
3. Confirm value, MPN, package, and footprint align with the BOM lock or are explicitly marked `NEEDS_REVIEW`.
4. Confirm each exact part has a source record under `06_DATASHEETS` or `08_COMPONENT_DATABASE`.
5. Confirm package and footprint status for high-risk parts: connectors, PMOS, ESD arrays, regulators, MCU modules, crystals, RF parts, and polarity-sensitive parts.
6. Confirm DNP, substitute, and generic placeholder status is explicit.
7. Confirm no supplier price, stock, or lifecycle claim is made without current source data.
8. Confirm the BOM report path is saved in project `reports/` or `history/verification_runs/`.

## Status Labels

| Status | Use |
| --- | --- |
| `BOM_LOCK_PASS` | All required lines match schematic, source evidence, and footprint status. |
| `BOM_LOCK_WARN` | Non-blocking issues remain; report must list why they do not block. |
| `BOM_LOCK_FAIL` | Required line, value, source, quantity, DNP, or footprint evidence is missing. |
| `NEEDS_HUMAN_REVIEW` | Human must approve a substitution, generic part, sourcing choice, or high-risk package. |

## Hard Rules

- Generic parts must be marked generic and must not be silently converted to exact MPNs.
- Exact parts must have source evidence.
- BOM export is not procurement approval.
- BOM lock does not verify footprint geometry by itself.
- A `NOT_FINAL` fab package may include a BOM for review, but it must not imply purchasing or assembly approval.
