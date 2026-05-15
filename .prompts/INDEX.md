# Prompt Pack Index

## PURPOSE
AI-readable index for Codex, Claude, and shared prompt packs.

## WHAT_BELONGS_HERE
- `.prompts/codex/`
- `.prompts/claude/`
- `.prompts/shared/`
- `.prompts/kicad_pipeline/`

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- KiCad project source files.
- Generated outputs.

## AI_AGENT_RULES
- Prompts must require startup reads, backups before KiCad edits, history logs, and verification reports.
- Prompts must forbid fake datasheet claims and unverified footprint approval.
- KiCad pipeline prompts must preserve gate order unless the user explicitly approves and logs an exception.
- Schematic create, review, repair, visual-cleanup, and readiness prompts must
  force `HUMAN_DRAFTING_MODE`: orient symbols before labels, wire local nets
  before labels when cleanly possible, physically wire local MCU support
  circuits when close enough, verify emphasized rails as real wires, sanity-check
  reset/boot topology, enforce visible text ownership, and treat screenshot
  evidence as stronger than ERC-only success language.
- Those schematic prompts must also require reporting of symbol moves, labels
  replaced with wires, labels kept and why, rail verification, topology sanity,
  and ERC/text/unresolved results.

## SAFE_EDIT_RULES
- Keep prompts tool-agnostic where possible.
- Keep manufacturing outputs labeled `NOT_FINAL`.

## PUBLIC_RELEASE_NOTES
- Prompt files are public-facing guidance and must not contain personal credentials.
