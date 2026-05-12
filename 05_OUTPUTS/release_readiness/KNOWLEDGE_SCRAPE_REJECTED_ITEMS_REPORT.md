# Knowledge Scrape Rejected Items Report

Status: `FINAL_REJECTED_FOLDER_DRAIN_APPLIED`

Date: `2026-05-11`

## Scope

- `knowledge_scrape/91_rejected_low_value`

## Outcome

- Source folder removed: `YES`
- Total rows drained: `782`
- Metadata/history-only moves: `2`
- Raw capture quarantine moves: `780`
- Public rejected-history raw payload moves: `0`

## Why Public Rejected-History Payload Moves Were Zero

The remaining rejected content was almost entirely raw copied webpage text. That
made license quarantine the safer destination than preserving the payload inside
a public history tree.

## Result

Rejected low-value content no longer remains in `knowledge_scrape/`.

