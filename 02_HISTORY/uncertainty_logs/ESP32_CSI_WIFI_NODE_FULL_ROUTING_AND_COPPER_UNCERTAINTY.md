# Uncertainty Log - ESP32_CSI_WIFI_NODE Full Routing And Copper

Date: 2026-05-07

## Uncertainties

- RF keepout check was performed against route endpoints/vias and the project-intelligence rectangle. It was not a full computational segment-polygon clearance proof.
- J1 3D proof remains missing; current acceptance is based on prior 2D footprint/orientation proof.
- The U2 0.20 mm drill issue needs LJ/fab/footprint decision before DRC-clean status is possible.
- Further routing likely requires manual/local placement-aware routing, especially around Q1/F1 and USB.

