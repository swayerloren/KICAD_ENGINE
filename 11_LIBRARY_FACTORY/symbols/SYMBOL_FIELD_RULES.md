# Symbol Field Rules

Status: `MANDATORY_FOR_CUSTOM_AND_VERIFIED_SYMBOLS`

## Purpose

KiCad symbol fields are how schematic data flows into BOMs, review reports, datasheet links, and footprint verification. Empty or vague fields make it easy for an AI agent to lose source evidence or approve a wrong part.

## Required Fields

| Field | Required For | Allowed Placeholder |
| --- | --- | --- |
| `Reference` | All symbols | No. Must annotate before PCB gate. |
| `Value` | All symbols | Only if intentionally generic and marked. |
| `Footprint` | PCB-bound symbols | Candidate allowed until footprint audit. |
| `Datasheet` | Exact parts | `TODO_SOURCE_REQUIRED` if missing. |
| `MPN` | Exact parts | `generic_placeholder` only for true generic parts. |
| `Manufacturer` | Exact parts | `Unknown - requires source verification`. |
| `Package` | PCB-bound symbols | `Unknown - requires source verification`. |
| `VerificationStatus` | All non-trivial symbols | `UNVERIFIED`, `SOURCE_LINK_ONLY`, `PINOUT_VERIFIED`, or `NEEDS_HUMAN_REVIEW`. |
| `SourceDocument` | Exact parts | Source URL, local private path, or source record path. |
| `HumanReviewRequired` | High-risk parts | `true` for connectors, PMOS, ESD arrays, regulators, RF, modules, and polarity-sensitive parts until reviewed. |

## Useful Optional Fields

- `Lifecycle`
- `SupplierSKU`
- `KiCadLibrarySource`
- `FootprintStatus`
- `PinoutStatus`
- `DoNotPopulate`
- `DesignNotes`
- `ErrataNotes`

## Field Status Rules

- `Datasheet` must point to the exact source used for the symbol claim, not a generic family page unless the symbol is still `SOURCE_LINK_ONLY`.
- `Footprint` field presence does not prove footprint correctness.
- `VerificationStatus` cannot be promoted past `UNVERIFIED` unless the evidence is saved in a component record, verification record, or project report.
- `HumanReviewRequired` must remain true for high-risk mechanical and orientation decisions until the review is explicitly recorded.

## Prohibited Field Content

- Secrets, API keys, supplier credentials, cookies, or private tokens.
- Unsupported claims such as "verified" without evidence path.
- Absolute user-specific paths when a repo-relative, project-relative, or KiCad environment-variable path is available.

## Review Gate

A symbol may be used as a planning candidate with incomplete fields. It must not be approved for schematic-to-PCB gate unless source, pinout, value, package, and review status are complete or explicitly blocked.
