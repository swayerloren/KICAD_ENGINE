# Board Shape And Mechanical Rules

## Purpose

Force board-shape choice to come from real mechanical and usability reasoning.

## Core Rules

- Do not assume the PCB is rectangular.
- Choose board shape from:
  - enclosure or mounting constraints
  - connector edge access
  - cable usability
  - antenna clearance
  - routing feasibility
  - board handling and serviceability
- Record outline dimensions and why they were chosen.
- If a board needs curved, pill, notched, or asymmetric geometry, treat that as a valid design option rather than a failure to fit a rectangle.
- If a chosen outline creates dead zones, blocked connectors, or impossible routing channels, reject the variant.

## Required Questions

- Which edges need connectors?
- Which areas must stay clear for cable insertion or fingers/tools?
- Where do mounting holes belong, and do they still leave room for routing?
- Does the outline support the RF keepout?
- Does the shape reduce or worsen routing complexity?

