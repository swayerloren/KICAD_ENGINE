# PCB Engineering Rules Index

This is a topic index for routing an AI agent to the right knowledge folders. These are not self-proving rules by themselves. For final recommendations, trace back to local source files and `url_index_id`.

## Layout And Routing

| Topic | Why It Matters | Start Here |
| --- | --- | --- |
| No acute trace angles | Reduces fabrication and field-concentration problems | `09_pcb_layout_grounding_emi_si/`, `10_dfm_fabrication_assembly/` |
| Prefer 45-degree routing or curves | Cleaner return path and easier fabrication | `09_pcb_layout_grounding_emi_si/` |
| Avoid 90-degree bends when practical | Helps routing quality and avoids bad style in sensitive paths | `09_pcb_layout_grounding_emi_si/` |
| Continuous return path | Critical for signal integrity and EMI control | `09_pcb_layout_grounding_emi_si/` |
| Avoid split planes under high-speed traces | Prevents disrupted return current and emissions | `09_pcb_layout_grounding_emi_si/`, `07_usb_c_high_speed_esd/` |
| USB differential pair routing | Controls impedance, skew, and return continuity | `07_usb_c_high_speed_esd/`, `11_calculators_ipc_reference/` |

## Power And Decoupling

| Topic | Why It Matters | Start Here |
| --- | --- | --- |
| Short high-current switching loops | Dominant buck-converter EMI and stability risk | `08_power_buck_regulators/`, `09_pcb_layout_grounding_emi_si/` |
| Decoupling capacitors close to power pins | Lowers loop inductance and transient noise | `09_pcb_layout_grounding_emi_si/`, `05_esp32_espressif/`, `06_microcontrollers/` |
| Buck converter layout | Placement and loop control are often more critical than schematic correctness | `08_power_buck_regulators/` |

## Interfaces, Protection, And RF

| Topic | Why It Matters | Start Here |
| --- | --- | --- |
| ESD diodes near connector | Protection effectiveness depends strongly on placement | `07_usb_c_high_speed_esd/`, `10_dfm_fabrication_assembly/` |
| ESP32 antenna keepout | Radio performance depends on clearance, ground, and placement discipline | `05_esp32_espressif/`, `09_pcb_layout_grounding_emi_si/` |

## Library, DFM, And Mechanical

| Topic | Why It Matters | Start Here |
| --- | --- | --- |
| Manufacturer footprint verification | Library parts are starting points, not proof | `04_kicad_libraries_symbols_footprints/`, `14_datasheets_pdf_markdown/` |
| Pin 1 and orientation verification | Prevents assembly and bring-up failures | `04_kicad_libraries_symbols_footprints/`, vendor datasheet PDFs |
| DFM clearances | Actual shop capability limits what is manufacturable | `10_dfm_fabrication_assembly/` |
| Annular rings and via constraints | Impacts yield, drill breakout, and reliability | `10_dfm_fabrication_assembly/`, `11_calculators_ipc_reference/` |
| Silkscreen and reference readability | Affects inspection, assembly, and debug usability | `10_dfm_fabrication_assembly/` |
| Test points | Needed for debug, programming, and production test | `10_dfm_fabrication_assembly/`, `09_pcb_layout_grounding_emi_si/` |
| Mounting holes and mechanical constraints | Prevents enclosure and assembly conflicts | `10_dfm_fabrication_assembly/`, part datasheets |

## Mandatory Cross-Checks

- USB-C topics: cross-check against official controller, connector, and protection sources.
- Buck layout topics: cross-check against regulator datasheet and app note.
- RF and ESP32 antenna topics: cross-check against official hardware design guidance.
- Footprints and pin 1 orientation: cross-check against the original package drawing in the PDF.
