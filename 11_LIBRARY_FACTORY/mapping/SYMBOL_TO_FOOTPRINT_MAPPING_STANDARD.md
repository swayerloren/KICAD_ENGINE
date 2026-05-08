# Symbol To Footprint Mapping Standard

## Purpose

Prevent agents from pairing a correct symbol with the wrong footprint.

## Required Inputs

- Exact part number.
- Exact package or module variant.
- Verified symbol pinout.
- Footprint candidate.
- Package drawing or connector drawing.
- Pin 1 orientation for symbol and footprint.

## Mapping Rules

- The symbol pin numbers must match the footprint pad numbers.
- The symbol value/MPN must match the package variant used for footprint selection.
- Do not map by pin count alone.
- Do not map by package family name alone.
- Do not map by supplier package name alone.
- Do not map by Mouser, Digi-Key, JLCPCB, or LCSC part number alone.
- Do not approve a connector mapping without exact manufacturer drawing.
- Record mapping status separately from symbol and footprint status.

## Status Labels

- `MAPPING_VERIFIED`: symbol pins and footprint pads match exact source evidence.
- `MAPPING_CANDIDATE`: plausible but source evidence incomplete.
- `MAPPING_REJECTED`: mismatch found.

## Review Gate

A design cannot treat a component as ready for PCB layout until symbol, footprint, and mapping statuses are all verified or explicitly accepted as risk by the human.

## Supplier Match Records

When supplier metadata is involved, create or update a record under `30_SUPPLIER_FOOTPRINT_MATCHES/`.

The supplier match record must identify:

- Manufacturer and MPN.
- Supplier and supplier SKU.
- JLC/LCSC part number when applicable.
- Supplier package name.
- Datasheet URL.
- Package drawing source.
- KiCad symbol, footprint, and 3D model candidates.
- Confidence level.
- Human-review status.

Supplier package names can support candidate search, but they cannot verify high-risk footprints.
