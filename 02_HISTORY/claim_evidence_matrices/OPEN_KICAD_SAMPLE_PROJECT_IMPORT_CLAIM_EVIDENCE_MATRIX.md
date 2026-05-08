# Claim/Evidence Matrix - Open KiCad Sample Project Import

Date: `2026-05-03`

| Claim | Status | Evidence | Notes |
| --- | --- | --- | --- |
| Three approved candidates were imported. | `VERIFIED_BY_FILE` | `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/` and `normalized_samples/` contain the three sample folders. | Candidate approval comes from candidate index and user import prompt. |
| Each imported sample has a local license file. | `VERIFIED_BY_FILE` | Local `LICENSE` or `LICENSE-CERN-OHL` files in each imported original. | Human legal review still required before public bundle. |
| Attribution records were created. | `VERIFIED_BY_FILE` | `32_OPEN_KICAD_SAMPLE_INTAKE/attribution/*_ATTRIBUTION.md`. | Records preserve source URL and commit. |
| Normalized copies were created. | `VERIFIED_BY_FILE` | `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/<sample>/`. | No review/repair edits were made to normalized copies. |
| No active KiCad project was modified. | `VERIFIED_BY_COMMAND` | Commands targeted `32_OPEN_KICAD_SAMPLE_INTAKE` and `05_OUTPUTS` staging, not `04_KICAD_PROJECTS/active`. | Full git metadata was not relied on. |
| No KiCad Engine manufacturing outputs were generated. | `VERIFIED_BY_COMMAND` | No KiCad export commands were run; import reports identify upstream outputs as source artifacts. | Imported source repos contain upstream Gerbers/BOM/placement/STEP for some samples. |
| Samples are ready for benchmark scoring. | `CONTRADICTED` | Import reports and benchmark candidate file mark all as `IMPORTED_NEEDS_REVIEW` / `CANDIDATE_ONLY_NOT_RUN`. | Benchmark scoring is blocked until review artifacts exist. |
| Samples are public-release payload ready. | `PARTIALLY_VERIFIED` | License files exist and candidate status allows possible public bundle, but final human review is required. | Keep public payload blocked until legal/release review. |
