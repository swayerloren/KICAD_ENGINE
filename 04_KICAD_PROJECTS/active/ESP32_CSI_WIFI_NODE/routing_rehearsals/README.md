# Routing Rehearsals

This placeholder marks a local-only scratch area for future routing rehearsal runs.

## Purpose

- copied-board route rehearsal
- temporary geometry trials
- local DRC scratch output

## Why Contents Stay Ignored

- rehearsal payloads can become large
- they may contain temporary copied-board KiCad files
- they are not required for a clean clone-or-ZIP onboarding workflow

## Recreate Locally

- create the folder only when a routing task explicitly needs isolated rehearsal output
- use repo-relative paths and keep the results local unless a specific sanitized evidence subset is intentionally promoted

## Never Commit Blindly

- copied `.kicad_pcb`, `.kicad_pro`, or `.kicad_prl` files
- caches, locks, screenshots, or temporary route search trees
