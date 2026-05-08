# ESP32 Dev Board Layout Intelligence Self Review

Record kind: `ai_self_review`
Created: `2026-05-07T17:27:33`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `LOW_RISK`
Gate result: `PASS`
Human review required: `NO`

## Summary

Created reusable placement-intelligence docs for ESP32-style boards, STM32-style dev boards, connector edges, RF keepouts, buttons, LEDs, mounting holes, and test pads without touching KiCad design files.

## Details

The task stayed in knowledge-base, sandbox-rule, memory, and handoff scope. The new docs explicitly state that they are patterns rather than universal rules and that project requirements come first. No KiCad design files or manufacturing outputs were modified.

## Evidence

Created files under 10_KNOWLEDGE_BASE/design_patterns, 10_KNOWLEDGE_BASE/common_mistakes, and 34_PCB_LAYOUT_SANDBOX; updated sandbox discovery files, DESIGN_RULES_MEMORY.md, README_GPT.md, and FOR CHAT GPT.MD; validated file existence and key warning/rule phrases; final KiCad hash recheck confirmed no design-file changes.

## Issue

The new placement-intelligence docs still need a first live project-local sandbox adoption pass.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
