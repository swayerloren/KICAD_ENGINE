# EMC Precompliance Review Rules

## Purpose

Define the internal precompliance review gate before any export or final-board
acceptance claim references EMC or safety readiness.

## Rules

- EMC precompliance review is a risk screen, not certification.
- Review switching regions, return-path continuity, connector locations, RF
  keepouts, and noisy cable-entry paths.
- Harsh-environment or reliability context may increase review depth but does
  not override core PCB quality gates.
- If evidence is incomplete, mark the result `NEEDS_HUMAN_REVIEW`.
