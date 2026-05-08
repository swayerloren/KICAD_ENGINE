# Datasheet Library README

This directory is the local datasheet and electronics reference library for KICAD_ENGINE.

It is designed for AI-assisted KiCad work from VS Code. The goal is to make component evidence easy to find, cite, compare, and audit while keeping copyright and source provenance clear.

## What Belongs Here

- Component datasheets.
- Package drawings and land pattern documents.
- Errata.
- Application notes.
- Reference designs.
- Module and development board documentation.
- Board-house fabrication and assembly references.
- Vendor source URL indexes.

## What Does Not Belong Here

- Secrets, private credentials, API tokens, or license keys.
- KiCad project source files.
- Generated Gerbers, drills, pick-and-place files, or manufacturing packages.
- Unlabeled downloads with unknown origin.
- Claims that a component is verified without source evidence.

## Status

This library is a scaffold with useful source-link and metadata rules. It is not complete. Folder presence does not prove datasheet coverage, source verification, pinout correctness, footprint correctness, sourcing availability, or fabrication readiness.

## Required Record Types

| Record Type | Purpose | Minimum Evidence |
| --- | --- | --- |
| Part datasheet record | Links a component to its authoritative datasheet/source page. | Vendor, part number, document type, source URL, retrieval date, redistribution status, verification status. |
| Package drawing record | Supports footprint and mechanical review. | Exact MPN/package suffix, drawing URL or document title, package dimensions status, pin/pad numbering status. |
| Errata record | Warns agents about silicon/module issues. | Part/family affected, source URL, revision/date, affected design area, human-review flag. |
| Reference manual record | Supports MCU/peripheral and boot/debug claims. | Family, document title, source URL, revision/date, claim scope. |
| Dev board record | Links official board schematics/user guides. | Board name, source URL, schematic status, license/redistribution status. |
| Application note record | Captures layout or circuit guidance. | Source URL, applicable parts, extracted guidance, verification limits. |

## Agent Workflow

1. Search `MASTER_DATASHEET_INDEX.md` first.
2. Search the relevant category `INDEX.md` next.
3. Check family `SOURCE_LINKS.md`, `SOURCES.md`, and `NEEDS_RESEARCH.md`.
4. Check `MISSING_DATASHEETS.md` before assuming no document is needed.
5. Use datasheets as evidence for symbol, footprint, BOM, and review work only after the relevant claim is extracted and cited.
6. Record uncertainty explicitly in the component record and AI closeout logs.

## Verification Rules

- A URL alone is `SOURCE_LINK_ONLY`.
- A local file without provenance is `LOCAL_PRIVATE_ONLY` or `UNKNOWN_REQUIRES_REVIEW`.
- A copied vendor document is not public-release safe unless redistribution is confirmed.
- Direct PDF links are useful, but source landing pages are preferred when revision, family, and terms are clearer.
- Exact values must include source document and section/page reference when available.
- Package and footprint approval requires the package drawing, not just the part datasheet title.

## Downstream Use

Datasheet records feed:

- `08_COMPONENT_DATABASE` part records,
- `11_LIBRARY_FACTORY` symbol/footprint verification,
- `29_FOOTPRINT_GAP_ANALYSIS` package-drawing gaps,
- `30_SUPPLIER_FOOTPRINT_MATCHES` supplier-to-footprint evidence,
- project BOM locks and schematic-to-PCB gates.

If a downstream record uses this library, it must preserve the verification status and not promote `SOURCE_LINK_ONLY` to `VERIFIED` without new evidence.
