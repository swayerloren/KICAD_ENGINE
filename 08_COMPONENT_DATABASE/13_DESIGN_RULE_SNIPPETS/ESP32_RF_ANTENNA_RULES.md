# ESP32 RF And Antenna Rules

Date: 2026-05-02

Status: RF placement guidance for module-based KiCad design. Exact antenna and matching design require the selected module datasheet and hardware design guide.

Primary sources:

- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html
- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/
- https://documentation.espressif.com/esp32-s3-mini-1_mini-1u_datasheet_en.html
- https://documentation.espressif.com/esp32-c6-wroom-1_wroom-1u_datasheet_en.html

## PCB Antenna Modules

- Prefer placing the module so the antenna extends beyond the edge of the host PCB.
- If the antenna cannot extend past the board edge, maintain the clearance recommended by the selected hardware guide and document the compromise.
- Keep ground pours, traces, vias, copper fills, components, batteries, mounting holes, shields, flex cables, displays, and metal enclosure features out of the antenna keepout.
- Do not place high-current switching regulators near the antenna side of the module.
- Do not rely on visual 3D clearance alone; inspect copper and keepout layers.

## External Antenna Modules

- Treat `U` modules as external-antenna connector designs.
- Verify connector type, footprint, pad orientation, pin-1/mechanical origin, cable direction, and antenna mounting.
- Keep the RF connector mechanically protected from cable pull.
- Decide whether the antenna is user-accessible, internal, adhesive, panel-mounted, or cabled.
- Plan RF validation of the complete product, including enclosure and cable routing.

## Bare-Chip RF Warning

- Do not design a bare ESP32-family RF section from memory.
- Bare-chip designs need the hardware design guide, reference schematic, reference layout, RF matching network, crystal rules, controlled-impedance RF feed, antenna design, and test equipment.
- Matching values from Espressif modules are not automatically reusable on a different PCB.

## KiCad Review Checks

- Does the footprint include a visible and enforced antenna keepout?
- Does the board outline support the antenna placement?
- Are copper zones excluded from the antenna region on all layers where required?
- Are RF connector footprints verified against the exact connector datasheet?
- Are there mechanical features inside the RF clearance volume?
- Is there a test plan for throughput/range or RF verification?
