# STM32WL PCB Layout Checklist

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Layout Checklist

- Footprint matches exact package drawing.
- Pin-1 orientation visible and checked.
- Power decoupling close to relevant pins.
- Analog rails/reference kept quiet and routed intentionally.
- Clock crystals follow AN2867 placement, guard, trace length, and load-cap review.
- USB/CAN/RF/high-speed routes follow interface-specific rules when present.
- SWD connector/test pads remain physically accessible.
- BOOT0/reset access remains physically accessible.
- Courtyards, silkscreen, assembly text, exposed pad, and 3D model reviewed.
- DRC run and report stored before claiming layout readiness.

## Family-Specific Layout Focus

- regional RF compliance
- matching network
- antenna/feedline layout
- reference design fidelity

## Review Gate

PCB placement/routing must remain `NEEDS_REVIEW` until footprint drawing comparison, connector orientation, polarity, ERC/DRC evidence, and close-up visual review are complete.
