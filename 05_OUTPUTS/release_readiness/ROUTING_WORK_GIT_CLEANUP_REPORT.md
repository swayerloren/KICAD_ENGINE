# Routing Work Git Cleanup Report

Date: `2026-05-09`
Task type: `AUDIT_ONLY`
Active project: `ESP32_CSI_WIFI_NODE`
Active project path: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Goal

Remove the large tracked routing scratch payload from the portable GitHub repo while keeping `routing_work` visible by a tracked placeholder `README.md`.

## Tracked State Before Cleanup

- `git ls-files 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` reported `3300` tracked paths.
- `3299` tracked paths lived under `routing_work/20260508_091428/`.
- The timestamped payload size on disk was `291,520,597` bytes (`278.02 MiB`) for the tracked files and `291,520,635` bytes (`278.02 MiB`) including the ignored lock file.
- The payload was dominated by copied trial boards and generated routing outputs:
  - `.kicad_pcb`: `820` files, `260,981,474` bytes
  - `.kicad_pro`: `820` files, `12,029,837` bytes
  - `.kicad_prl`: `817` files, `1,710,599` bytes
  - `.json`: `830` files, `16,738,927` bytes
  - small supporting `.md`, `.csv`, and `.txt` logs

## Classification

- `routing_work/20260508_091428/` is local generated routing scratch and rehearsal payload.
- It is not required for ZIP users or first-time repo use.
- It does not contain reusable source scripts or required engine logic.
- It should remain on local disk when useful, but it should not be tracked in Git.

## Actions Applied

1. Updated `.gitignore` so `04_KICAD_PROJECTS/active/*/routing_work/*` is ignored while `routing_work/README.md` remains tracked.
2. Rewrote `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/README.md` as the durable placeholder policy.
3. Removed `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428/` from Git tracking with:

```powershell
git rm -r --cached -- "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428"
```

## Validation

- The timestamped folder still exists on local disk after cleanup: `YES`
- Staged Git removals from the timestamped folder: `3299`
- Placeholder kept and tracked: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/README.md`
- Useful source scripts removed: `NO`
- Live project `.kicad_sch` changed: `NO`
- Live project `.kicad_pcb` changed: `NO`
- Cleanup scope: tracked scratch payload only

## Result

After commit, GitHub should show `routing_work` only by its placeholder `README.md`, and the portable ZIP should no longer include the large historical scratch payload.

## Repo ZIP Size Impact Estimate

- Removed from Git tracking: about `278.02 MiB`
- Expected GitHub ZIP reduction from this gap alone: about `278 MiB`, subject to GitHub archive compression
