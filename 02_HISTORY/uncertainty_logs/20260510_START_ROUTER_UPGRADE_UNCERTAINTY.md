# Start Router Upgrade Uncertainty Log

Date: `2026-05-10`

## Low-Risk Uncertainties

- The repo still contains some older prompt-pack stage prompts that may embed
  route-specific manual read lists. The new front-door router and start prompts
  are now authoritative, but not every historical prompt file was rewritten in
  this task.
- The historical `03_TOOLS/scripts/pcb_quality` path no longer exists. The new
  router maps that request to `03_TOOLS/scripts/pcb_geometry/` based on the
  current local filesystem.
