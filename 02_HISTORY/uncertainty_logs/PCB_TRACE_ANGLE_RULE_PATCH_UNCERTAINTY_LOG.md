# PCB Trace Angle Rule Patch Uncertainty Log

Date: `2026-05-07`

## Uncertainties

1. The user requested `.prompts/kicad_pipeline/11_route_critical_nets.md` and `12_route_remaining_nets.md`, but those filenames do not exist in this repo.
   - Handling: the active routing prompts `14_route_critical_nets.md` and `15_route_remaining_nets.md` were updated instead, and the absence of `11/12` was recorded explicitly.

2. The maintenance run rewrote `ESP32_CSI_WIFI_NODE` current-state memory back to stale blocked-routing wording.
   - Handling: project memory was corrected from the latest Stage 1/2 routing evidence rather than trusting the stale compiled summary.

3. The no-design-file-change statement is based on the pre-edit hash capture already taken in this session, the post-edit hash recheck, and the fact that only markdown files were patched in this task.
   - Handling: final audit language stays at the level of "no KiCad design files changed in this task" and does not overclaim broader repo cleanliness.

4. A final `git diff` check could not be used because this checkout is not a git working tree.
   - Handling: the final confirmation uses the pre-edit hash capture, the post-edit hash recheck, and the task's markdown-only edit scope.
