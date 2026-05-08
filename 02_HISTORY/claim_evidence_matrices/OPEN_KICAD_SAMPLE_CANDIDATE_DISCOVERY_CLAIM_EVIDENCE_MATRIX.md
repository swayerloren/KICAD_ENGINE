# Claim Evidence Matrix - Open KiCad Sample Candidate Discovery

Date: 2026-05-03

| Claim | Status | Evidence | Notes |
|---|---|---|---|
| Candidate records were created under `32_OPEN_KICAD_SAMPLE_INTAKE/candidates/`. | VERIFIED_BY_FILE | Local file inventory listed candidate markdown files. | Direct filesystem evidence. |
| No repositories were cloned, downloaded, or imported. | VERIFIED_BY_COMMAND | Command log contains only web search, GitHub metadata checks, local file writes, and validation. | No import folders contain project files. |
| Candidate file presence counts came from GitHub file-tree metadata. | VERIFIED_BY_COMMAND | GitHub API tree commands returned counts for `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, BOM-like files, Gerber-like files, and STEP files. | Metadata only; not a local checkout audit. |
| Public bundle status is final legal approval. | CONTRADICTED | Candidate records say pending attribution preservation and final human license review. | Do not treat as legal approval. |
| `devnithw/stm32-devboard` was omitted because no license metadata/file was found. | VERIFIED_BY_COMMAND | GitHub metadata check showed `NO_LICENSE_METADATA` and zero license files. | Could be link-only later if user wants a no-license cautionary record. |
| Top 5 ranking is objective proof of engineering quality. | UNVERIFIED | Ranking is based on candidate fit, completeness, license clarity, and expected review value. | Treat as recommendation, not benchmark result. |
| All candidates are complete enough to open in KiCad. | PARTIALLY_VERIFIED | Metadata shows `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb` presence. | Opening in KiCad and resolving libraries were not tested. |
