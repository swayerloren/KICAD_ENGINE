# Dirty KiCad File Requires Commit-Scope Decision

Date: `2026-05-12`

Status: `OPEN`

## Issue

The repo-push hygiene blocker repair did not touch KiCad design files, but the
working tree still contains a preexisting modified schematic:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

## Required Decision

Before any later commit/push task, decide whether this file is intentionally in
scope or must remain unstaged.

