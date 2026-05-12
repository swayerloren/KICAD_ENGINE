# Knowledge Map

Use this file to decide which numbered folder to search first. The goal is fast routing, not exhaustive summary.

## Folder Map

| Folder | Purpose | Use When |
| --- | --- | --- |
| `00_ai_entrypoints/` | Navigation and rules for AI agents | You are entering the knowledge base or deciding trust, routing, or registry workflow |
| `00_source_of_truth/` | Official-source routing layer | You need to choose the highest-trust source class before using topic folders |
| `00_engineering_rules/` | Compact engineering decision rules | You need a short ruleset for layout, USB-C, ESP32, buck, automation, or footprint verification |
| `00_retrieval_indexes/` | Quick retrieval maps and recovery routing | You need fast folder routing, official-source routing, or rejected recovery context |
| `01_kicad_core/` | KiCad manuals, core features, editors, CLI, workflow docs | The question is about KiCad behavior, PCB Editor, Schematic Editor, GerbView, or official KiCad usage |
| `02_kicad_python_api/` | KiCad Python API, bindings, scripting, SWIG, IPC API | You need automation, scripting, board inspection, scripted edits, or API behavior |
| `03_kicad_file_formats/` | KiCad file formats and S-expression structure | You need to read, diff, generate, or validate `.kicad_pcb`, `.kicad_sch`, or related formats |
| `04_kicad_libraries_symbols_footprints/` | KLC rules, symbols, footprints, 3D packages, library conventions | You need footprint policy, symbol naming, library rules, or package reference material |
| `05_esp32_espressif/` | Espressif datasheets, TRMs, hardware design guidance | The board uses ESP32-family devices or Espressif reference guidance |
| `06_microcontrollers/` | Other MCU families and vendor device references | The question is about STM32, Microchip, RP2040, RP2350, Nordic, Renesas, Infineon, WCH, GD32, or similar |
| `07_usb_c_high_speed_esd/` | USB, USB-C, high-speed routing, ESD protection | The design includes USB connectors, differential pairs, ESD arrays, or connector-side protection |
| `08_power_buck_regulators/` | Buck regulators, power-stage guidance, switch-mode layout | The question is about power topology, regulator selection, layout loops, or compensation-related references |
| `09_pcb_layout_grounding_emi_si/` | Grounding, EMI, EMC, SI, decoupling, return paths | The issue is layout quality, crosstalk, antenna performance, return current, or EMI risk |
| `10_dfm_fabrication_assembly/` | Board house and assembly guidance | You need stackup, annular ring, solder mask, drill, panel, assembly, or manufacturing constraints |
| `11_calculators_ipc_reference/` | Trace calculators, impedance calculators, IPC-style references | You need quick sizing, spacing, or calculator-based starting points |
| `12_forums_peer_review/` | Peer-review and discussion material | You want secondary opinions, troubleshooting hints, or examples after checking higher-trust sources |
| `13_vendor_parts_cad_models/` | Parts portals, CAD model sources, vendor libraries | You need vendor footprints, CAD downloads, or part-library lookup paths |
| `14_datasheets_pdf_markdown/` | Original PDFs, extracted Markdown, extraction logs | You need the original datasheet PDF or searchable extracted text |
| `15_video_reference_index/` | Video indexes and media references | You want a video pointer, not a source of truth |
| `90_unsorted_review/` | Temporary holding area for unclear classification | A file exists but category fit is still uncertain |
| `91_rejected_low_value/` | Captchas, search pages, generic indexes, low-value scrape output | You are debugging coverage gaps or scrape quality, not looking for authority |
| `99_source_logs/` | Scrape and build-support log material | You are debugging ingestion, registry generation, or extraction behavior |

## Routing Rules

- Start with the smallest high-trust folder that matches the question.
- Route through `00_source_of_truth/` when the decision affects footprints, pinouts, layout, or fabrication.
- If the topic is part, package, pinout, or layout critical, also check `14_datasheets_pdf_markdown/`.
- Use `12_forums_peer_review/` only after official or vendor sources.
- Use `91_rejected_low_value/` only when investigating why a topic is missing or degraded.

## Common Task Routes

- KiCad scripting: `02_kicad_python_api/` -> `03_kicad_file_formats/` -> `01_kicad_core/`
- Footprints and symbols: `04_kicad_libraries_symbols_footprints/` -> `14_datasheets_pdf_markdown/`
- ESP32 board design: `05_esp32_espressif/` -> `09_pcb_layout_grounding_emi_si/` -> `07_usb_c_high_speed_esd/`
- MCU power and routing: `06_microcontrollers/` -> `08_power_buck_regulators/` -> `09_pcb_layout_grounding_emi_si/`
- USB-C port design: `07_usb_c_high_speed_esd/` -> `10_dfm_fabrication_assembly/` -> `14_datasheets_pdf_markdown/`
- Manufacturing review: `10_dfm_fabrication_assembly/` -> `11_calculators_ipc_reference/` -> vendor datasheet PDFs
