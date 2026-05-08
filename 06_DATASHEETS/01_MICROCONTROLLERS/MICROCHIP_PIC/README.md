# Microchip PIC, PIC24, PIC32, And dsPIC Reference Library

Date: 2026-05-02

Path: `06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_PIC`

## Purpose

This folder stores link-first source records, summaries, and future local reference documents for Microchip PIC10, PIC12, PIC16, PIC18, PIC24, PIC32, dsPIC30, and dsPIC33 design work.

## Current Status

This library is not complete and is not a design authority by itself. It is a curated index that tells AI agents where to look before selecting symbols, footprints, packages, programming headers, oscillator circuits, reset circuits, and voltage domains.

No datasheet PDFs were downloaded during this research pass. Official Microchip product pages and document links are recorded in `MICROCHIP_PIC_MASTER_INDEX.md`.

## Agent Rules

- Prefer official Microchip product pages, datasheets, errata, programming specifications, application notes, and board schematics.
- Do not bundle Microchip PDFs in a public repo unless redistribution rights are confirmed.
- Treat KiCad symbol and footprint names as candidates until pad count, pin numbering, package code, and land pattern are checked against the exact datasheet.
- Never assume PICkit, ICSP, MCLR, PGC, PGD, PGM, oscillator, USB, CAN, or analog pins are interchangeable across PIC families.
- Record missing documents in `MISSING.md` and known source URLs in `SOURCES.md`.

## Key Local Indexes

- `MICROCHIP_PIC_MASTER_INDEX.md`
- `PIC10/`
- `PIC12/`
- `PIC16/`
- `PIC18/`
- `PIC24/`
- `PIC32/`
- `dsPIC30/`
- `dsPIC33/`
- `PROGRAMMING_DEBUG_PICKIT/`
- `DEVELOPMENT_BOARDS/`
