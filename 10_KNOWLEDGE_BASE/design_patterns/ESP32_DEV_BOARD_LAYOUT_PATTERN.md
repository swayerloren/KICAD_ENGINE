# ESP32 Dev Board Layout Pattern

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## Purpose

Capture the default placement logic for compact ESP32-style boards that use onboard Wi-Fi or Bluetooth modules with an antenna keepout.

## Default Pattern

- Put the ESP32 module so the antenna sits at the board edge or in a clear antenna zone.
- Keep USB-C, barrel jack, or other cable-entry connectors on the edge they physically serve.
- Keep switching regulators, inductors, and noisy power-input parts away from the antenna edge.
- Keep reset and boot buttons user-accessible.
- Keep status LEDs visible after cables are inserted.
- Keep test pads accessible after assembly and not under connectors.
- Place mounting holes early enough that they do not crowd the antenna, connectors, or buttons.

## Placement Rules

- Do not place copper, traces, mounting holes, connectors, or tall components under the antenna keepout unless the exact module documentation explicitly allows it.
- Keep the USB/data path credible from connector to ESD or series parts to the ESP32 or bridge IC.
- Keep the power-input path credible from connector to protection to regulator to load.
- Keep user-facing parts on edges or surfaces that remain reachable after enclosure or cable installation.
- If the board outline clips the antenna clearance or forces connector crowding, treat that as a variant failure signal.

## Shape Guidance

- A rectangle is acceptable only when it supports antenna clearance, connector access, mounting, and routing.
- A pill, stepped, or connector-biased outline is acceptable when it solves real mechanical or usability problems.
- Do not choose a smaller board if that forces blocked RF clearance, bad connector access, or impossible test access.

## Human Review Gate

Human review is required for antenna-edge relationship, connector orientation, mechanical clearance, and selected board shape.
