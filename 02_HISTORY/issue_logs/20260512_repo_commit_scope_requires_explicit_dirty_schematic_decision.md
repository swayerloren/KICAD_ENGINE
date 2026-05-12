# Repo Commit Scope Requires Explicit Dirty Schematic Decision

Date: `2026-05-12`

Status: `OPEN`

## Issue

The repo integrity rerun is clean enough for a commit/push workflow only if the
later staging step explicitly excludes:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

unless LJ intentionally wants that schematic change in scope.

## Why It Matters

The file is a preexisting dirty KiCad design file. It was not changed in this
audit, and it must not be silently included in a docs/migration push.
