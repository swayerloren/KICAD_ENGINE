# USB C Rules

- Start in `../07_usb_c_high_speed_esd/` and `../00_source_of_truth/fabricator_rules/`.
- Prefer official connector datasheets, USB-IF documents, and vendor ESD app notes before peer review.
- Use the original PDF, not extracted Markdown, for connector pin numbering, shell tabs, keepouts, and differential-pair figures.
- Cross-check CC behavior, role assumptions, and protection topology with official sources.
- Treat `../12_forums_peer_review/` as secondary confirmation only.
- Use `../11_calculators_ipc_reference/` for impedance and trace-width starting points, then verify against the board house.
- Cite local file paths and `url_index_id` for connector footprint, ESD placement, and routing decisions.
