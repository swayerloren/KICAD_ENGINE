# Hallucination Risk Log: KiCad GUI Automation Layer

Date: `2026-05-06`

Risk level: `MEDIUM`

## Risk

The main hallucination risk is overstating the new GUI layer as capable of complete native annotation/ERC automation. The current layer supports read-only detection, safety gating, screenshot capability, and manual fallback. Live GUI action execution is deliberately blocked until selector-level behavior is verified.

## Controls

- Docs and scripts mark live annotation/save/ERC as not production-approved.
- `AGENTS.md` now requires KiCad-native annotation or manual LJ action for annotation tasks.
- `CURRENT_KNOWN_PROBLEMS.md` records that live GUI automation is not yet approved.
- Final reporting must state that annotation can not yet be fully automated by this layer.
