# Hallucination Risk Log: Supplier Datasheet Footprint Final Audit

Date: 2026-05-03

## Risks Controlled

- No exact datasheet specifications were inferred.
- No footprint candidates were marked verified.
- No supplier stock, price, lifecycle, or SKU data was claimed current.
- No fabrication readiness was claimed.
- No live API behavior was claimed.

## Residual Risk

| Risk | Severity | Mitigation |
| --- | --- | --- |
| AI agent may overread AI-readable STM32/MCU stubs as verified datasheet facts | `HIGH` | Keep files labeled `SCAFFOLDED_WITH_AI_SUMMARIES` or `UNKNOWN_REQUIRES_SOURCE`; require source section review. |
| AI agent may treat installed KiCad footprint candidates as approvals | `HIGH` | Use `29_FOOTPRINT_GAP_ANALYSIS` and `30_SUPPLIER_FOOTPRINT_MATCHES` rules; require package drawing and human review. |
| AI agent may overlook bundled PDF redistribution risk | `HIGH` | Block public release until PDFs are reviewed or excluded. |
| AI agent may assume supplier connector live API support exists | `MEDIUM` | Audit reports and `README_GPT.md` state live calls are not implemented or tested. |

