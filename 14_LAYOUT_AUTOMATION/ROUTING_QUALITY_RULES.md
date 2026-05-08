# Routing Quality Rules

## Purpose

Layout automation assistance, scripted routing, and agent-guided routing must target professional routing quality rather than minimum DRC legality.

## Hard Rules

- Follow `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`.
- Follow `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`.
- Do not accept crude 90-degree or acute-angle traces as a finished result.
- Do not accept bad routing just because DRC passes.
- Prefer local placement repair over ugly copper.
- Avoid unnecessary vias, long detours, and long diagonals through unrelated areas.

## Critical-Net Expectations

- Keep `BUCK_SW` and switching loops short, compact, and away from USB and RF areas.
- Keep USB data routing short, clean, parallel where practical, and low-stub.
- Keep wide power paths clean at pad transitions and branch points.

## Automation Review Gate

- Any automated or partially automated routing result requires visual review.
- If the first-pass result looks scripted, awkward, or non-professional, rip it up and reroute.
- A routing flow is incomplete until both DRC and routing-quality review pass.

