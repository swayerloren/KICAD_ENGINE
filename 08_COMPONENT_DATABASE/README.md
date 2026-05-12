# Component Database

Status: `LINK_FIRST_COMPONENT_EVIDENCE_SURFACE`

## Purpose

Store structured part intelligence for AI-assisted KiCad design beyond raw PDFs
or copied vendor pages.

## Canonical Files

- [COMPONENT_SOURCE_INDEX.md](COMPONENT_SOURCE_INDEX.md)
- [COMPONENT_EVIDENCE_RULES.md](COMPONENT_EVIDENCE_RULES.md)
- [HIGH_RISK_COMPONENTS_INDEX.md](HIGH_RISK_COMPONENTS_INDEX.md)
- [component_index.json](component_index.json)

## What Belongs Here

- component family records in Markdown and JSON
- evidence rules and review-state notes
- high-risk part guidance
- source-registry backed summaries
- footprint/package/orientation proof requirements

## What Does Not Belong Here

- raw scraped datasheet PDFs
- copied vendor pages as public source-of-truth
- active KiCad project source files
- fabricated electrical claims
- secrets or distributor credentials

## Rules

- Component records are link-first unless redistribution rights are confirmed.
- Vendor part numbers are identifiers, not footprint proof.
- Connector, RF, PMOS, regulator, ESD, TVS, and module records remain high risk
  until mechanical, package, and pin-mapping proof exists.
- If source license is unclear, keep the raw file in quarantine and store only
  normalized evidence notes here.

## Public Release Notes

Public release records must avoid unsupported claims and must not bundle
restricted datasheets or copied vendor content.
