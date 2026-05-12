# Engineering Rules Knowledge Move Session

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Scope

Drain the engineering-rule and PCB/schematic-layout knowledge folders listed in
Prompt 4 into canonical repo rule/checklist locations, migration history, and
license quarantine.

## What Changed

- Created canonical PCB rule docs for USB-C, USB ESD, buck layout, decoupling,
  return paths, ESP32 RF keepout, test points, mounting holes, and
  thermal/mechanical review.
- Created canonical schematic rule docs for buck readability, ESP32 boot/reset,
  and decoupling readability.
- Created placement/routing/final-review checklists and a schematic visual
  readability checklist.
- Added normalized summary areas under `10_KNOWLEDGE_BASE/`.
- Updated the migration controller config and destination map so these folders
  no longer route into `knowledge_scrape_import` trees.
- Moved `149` target source files out of `knowledge_scrape/`.

## Move Result

- Files moved from target folders: `149`
- Quarantine moves: `131`
- History/archive moves: `18`
- Target source folders removed: `10`
- `knowledge_scrape` file count before phase: `1854`
- `knowledge_scrape` file count after phase: `1705`

## Validation

- Target folders removed: `PASS`
- Rule docs contain source-registry references: `PASS`
- Checklists link to canonical rules: `PASS`
- Task contract validation: `PASS`
- No KiCad design-file state changed during this task: `PASS`

## Result

This phase succeeded. The targeted engineering-rule source folders are drained,
canonical rule/checklist surfaces now exist under `09_ACCURACY_ENGINE/`, and
raw scraped captures were archived or quarantined instead of being left in
`knowledge_scrape/` or promoted into a parallel rule tree.
