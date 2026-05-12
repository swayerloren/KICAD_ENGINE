# Hallucination Risk Log

- Risk checked: assuming a nonblank footprint is automatically correct.
  - Mitigation: re-ran live extraction, built a lock file, and used official vendor pages plus local KiCad library defaults.
- Risk checked: guessing exact passive MPNs from package size.
  - Mitigation: left unknown MPN fields blank and marked review-required rows explicitly.
- Risk checked: silently replacing `U2` and `U3` footprints without a dedicated schematic-edit contract path.
  - Mitigation: recorded them as human-review blockers instead of claiming a verified live fix.
