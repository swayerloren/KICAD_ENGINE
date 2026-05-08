# KiCad Symbol Footprint Linking Rules

Date: 2026-05-02

Status: rules for connecting component records to KiCad symbols, footprints, and 3D models.

## Purpose

Component records may contain KiCad symbol, footprint, and 3D model candidates. A candidate is not verified until it is checked against source evidence.

## Candidate Levels

| Level | Meaning |
| --- | --- |
| `UNKNOWN` | No KiCad candidate has been identified. |
| `CANDIDATE_FROM_NAME` | A candidate was found by name search only. |
| `VERIFIED_FROM_KICAD_LIBRARY` | The KiCad symbol, footprint, or 3D model file was inspected locally. |
| `VERIFIED_FROM_DATASHEET` | Pinout or land pattern was checked against the datasheet/package drawing. |
| `USER_CONFIRMED` | User explicitly confirmed the mapping for a stated project. |

## Required Link Fields

Every record must include:

- `kicad_symbol_candidates`
- `kicad_footprint_candidates`
- `kicad_3d_model_candidates`
- `pinout_status`
- `footprint_status`
- `package_drawing_status`
- `human_review_required`

## Required Candidate Record Fields

When a candidate is listed, include enough detail for the next agent to verify or reject it without repeating discovery:

| Field | Required | Guidance |
| --- | --- | --- |
| `candidate_name` | Yes | KiCad library item name or project-local item. |
| `candidate_source` | Yes | Installed KiCad, project-local library, user global library, supplier record, or manual entry. |
| `discovery_method` | Yes | Name search, library inspection, package drawing match, user confirmation, etc. |
| `evidence_path` | Yes if beyond name search | Report, source URL, command output, or verification record. |
| `status` | Yes | `UNKNOWN`, `CANDIDATE_FROM_NAME`, `REJECTED`, `PARTIALLY_VERIFIED`, or verified status. |
| `risk_notes` | Yes | Pinout, pad numbering, orientation, package, model, or portability concerns. |

## Verification Workflow

1. Resolve project-local libraries first.
2. Resolve user global libraries second.
3. Resolve installed KiCad stock libraries last.
4. Inspect the symbol pins, pin numbers, pin names, hidden pins, and electrical types.
5. Inspect the footprint pads, pad numbers, pad sizes, drills, courtyard, fab outline, silkscreen, and pin-1 mark.
6. Compare symbol and footprint to datasheet/package drawing.
7. Inspect 3D model path only as a mechanical/visual candidate, not as electrical proof.
8. Record evidence and update only the verified fields.

## Hard Warnings

- Do not use a footprint just because the name is similar.
- Do not use a symbol just because it appears in the KiCad stock library.
- Do not assume generic connectors have correct orientation.
- Do not assume RF connectors or USB-C connectors are interchangeable.
- Do not silently depend on user global libraries for portable projects.

## Cannot-Promote Rules

These conditions must keep the mapping blocked:

| Condition | Required Status |
| --- | --- |
| Package drawing missing | `NEEDS_HUMAN_REVIEW` |
| Connector orientation not reviewed | `BLOCKED_UNTIL_HUMAN_REVIEW` |
| PMOS source/gate/drain mapping unresolved | `BLOCKED_UNTIL_HUMAN_REVIEW` |
| ESD array flow-through orientation unresolved | `NEEDS_HUMAN_REVIEW` |
| Symbol pin numbers not compared to source | `UNVERIFIED` |
| Supplier package text is the only evidence | `MATCHED_BY_PACKAGE_NAME_ONLY` |
| 3D model exists but pad geometry not reviewed | `CANDIDATE_ONLY` |

## Required Verification Records

When a symbol, footprint, or 3D model candidate is promoted beyond placeholder status, create or update a supporting record under:

- `08_COMPONENT_DATABASE/12_KICAD_SYMBOL_FOOTPRINT_MATCHES/`
- `08_COMPONENT_DATABASE/15_PACKAGE_FOOTPRINT_DATABASE/`
- `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/`

The supporting record must identify the exact part number, package/orderable suffix, KiCad library item, source document, verification date, unresolved risks, and human-review status.

## Connector And Module Rule

Connectors and modules are high-risk even when a KiCad footprint candidate exists. Keep `human_review_required` set to `true` until exact manufacturer drawing, orientation, mating connector, keepout, and mechanical fit are reviewed.

## Supplier-To-Footprint Match Rule

Supplier records from Mouser, Digi-Key, JLCPCB, LCSC, or manual CSV/source-link workflows must not promote a footprint candidate by package name alone.

Use `30_SUPPLIER_FOOTPRINT_MATCHES/` when a supplier SKU, JLC/LCSC part number, supplier package name, or supplier datasheet link is being connected to a KiCad symbol, footprint, or 3D model candidate.

Required rule:

- Supplier package text is candidate metadata only.
- `MATCHED_BY_PACKAGE_NAME_ONLY` and `MATCHED_BY_GENERIC_FOOTPRINT` are not approval statuses.
- Connector, PMOS, ESD array, MCU module, and regulator matches require exact package or connector drawing evidence and human review before verification.
- Verified supplier-to-footprint records should still link back to `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/` for durable package/footprint evidence.
