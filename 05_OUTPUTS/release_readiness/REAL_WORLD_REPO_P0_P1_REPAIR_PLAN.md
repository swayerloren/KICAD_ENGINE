# Real World Repo P0 / P1 Repair Plan

Audit date: `2026-05-12`

This is the short release-readiness repair queue derived from `T_E_M_P/real_world_repo_audit/14_P0_P1_P2_REPAIR_PLAN.md`.

## P0

### `RWA-P0-001`
- Area: `Public release / license / attribution`
- Problem: public release is still blocked by unresolved license and attribution decisions
- Safe to auto-fix: `NO`
- Requires human decision: `YES`
- Validation: release checklist can be completed honestly for the shipped payload

### `RWA-P0-002`
- Area: `Public payload hygiene / retired migration residue`
- Problem: retired migration/public-risk payload still ships in the tracked baseline
- Safe to auto-fix: `NO`
- Requires human decision: `YES`
- Validation: every retained large/public-risk artifact has an explicit reason to ship

### `RWA-P0-003`
- Area: `AI startup safety / GitHub push routing`
- Problem: no first-class startup route for push/public-release safety
- Safe to auto-fix: `YES`
- Requires human decision: `NO`
- Validation: push/public-release prompts force release-status, license, attribution, security, and payload-review reads

## P1

### `RWA-P1-001`
- Area: `AI startup path consistency`
- Problem: `CLAUDE.md`, `README_GPT.md`, and `FOR CHAT GPT.MD` drift from the canonical route
- Safe to auto-fix: `YES`
- Requires human decision: `NO`
- Validation: companion startup docs agree with the canonical route

### `RWA-P1-002`
- Area: `Knowledge routing`
- Problem: knowledge-retrieval route is not explicit and retrieval mirrors drift from canonical maps
- Safe to auto-fix: `YES`
- Requires human decision: `NO`
- Validation: retrieval route is explicit and mirrors match canonical startup maps

### `RWA-P1-003`
- Area: `New-user project selection`
- Problem: default startup state points at a blocked live board
- Safe to auto-fix: `NO`
- Requires human decision: `YES`
- Validation: first-use startup is neutral or explicitly demo-scoped

### `RWA-P1-004`
- Area: `Path portability / workspace portability`
- Problem: active docs and workspace surfaces still contain maintainer-only path assumptions
- Safe to auto-fix: `YES`
- Requires human decision: `NO`
- Validation: no first-use active surface requires `C:\Users\LJ\...`

### `RWA-P1-005`
- Area: `Baseline ZIP payload size and hygiene`
- Problem: starter ZIP is too heavy and noisy
- Safe to auto-fix: `NO`
- Requires human decision: `YES`
- Validation: baseline ZIP profile is explicit and first-use focused

### `RWA-P1-006`
- Area: `Knowledge source registry contract`
- Problem: registry lacks direct confidence/license fields
- Safe to auto-fix: `NO`
- Requires human decision: `YES`
- Validation: high-trust, allowed-to-use sources can be filtered directly

### `RWA-P1-007`
- Area: `Schematic annotation proof`
- Problem: stale structured-text annotation narratives conflict with current native-annotation-only proof
- Safe to auto-fix: `YES`
- Requires human decision: `NO`
- Validation: active reports no longer imply raw text annotation is acceptable proof

### `RWA-P1-008`
- Area: `PCB live-state truth`
- Problem: stale PCB reports drift from current live-board truth
- Safe to auto-fix: `YES`
- Requires human decision: `NO`
- Validation: PCB prompts and reports visibly defer to live-state authority

### `RWA-P1-009`
- Area: `End-to-end demo path`
- Problem: no clean passing green-path demo ships today
- Safe to auto-fix: `NO`
- Requires human decision: `YES`
- Validation: a new user can follow a passing demo path without relying on the blocked example board

## First Safe Repair Slice

Run these first:

1. `RWA-P0-003`
2. `RWA-P1-001`
3. `RWA-P1-002`
4. `RWA-P1-004`
5. `RWA-P1-007`
6. `RWA-P1-008`
