# AI Self Review - Tool Index Portability Fix

- Kept the fix narrow: startup docs and tool-index docs only.
- Preserved the existing startup architecture instead of moving `TOOL_INDEX.md` and risking broken references.
- Strengthened both ends of the workflow: the machine-specific warning and the portable startup prompts.
- Avoided touching any KiCad design files.
