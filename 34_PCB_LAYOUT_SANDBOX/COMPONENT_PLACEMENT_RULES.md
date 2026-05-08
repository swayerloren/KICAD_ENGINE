# Component Placement Rules

## Fixed-First Order

Place or reason about these first in every variant:

1. board outline
2. mounting holes and hard mechanical keepouts
3. edge connectors and cable-entry connectors
4. RF modules and antenna keepouts
5. power-input path and switching regulator cluster
6. USB or other high-risk data-path cluster
7. remaining support circuitry

## Core Rules

- Do not scatter components before thinking through routing flow.
- Place power parts in source-to-load order.
- Keep switching loops compact during the planning stage, not after the board is already crowded.
- Keep USB/ESD/series components aligned to a credible path between connector and destination.
- Keep test and debug features out of connector bodies, antenna zones, and dense power clusters.
- Do not force component placement that obviously creates future routing contortions.
- If the board is too small for a clean cluster arrangement, that is a variant failure signal, not a reason to keep a bad placement.

## Mechanical Review Rule

Any footprint that defines the board edge, cable insertion, plug clearance, or large body overhang must be treated as mechanically sensitive and reviewed before the variant can be selected.

## Specialized Rule Packs

- `ESP32_STYLE_BOARD_PLACEMENT_RULES.md`
- `DEV_BOARD_SHAPE_REASONING_RULES.md`
