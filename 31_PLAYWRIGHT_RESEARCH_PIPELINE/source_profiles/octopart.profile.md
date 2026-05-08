# Octopart Source Profile

Source confidence level: `AGGREGATOR`

## Source Purpose

Part discovery, supplier cross-reference, datasheet links, lifecycle hints, and sourcing metadata across distributors.

## Preferred Access Method

Official API or approved access first. Manual source-link records second.

## Login/API Key Required

API access may require credentials or approval. Do not hardcode keys.

## Playwright Allowed

Only public pages when terms allow and `--live` is explicit. Do not use Playwright to avoid API access requirements.

## Fields May Be Captured

- product URL
- manufacturer and MPN
- supplier links
- datasheet link
- package text
- lifecycle/source hints

## Must Not Be Captured

- API keys
- account pages
- private/commercial data
- bulk copied results
- cached HTML

## Rate Limit Guidance

Follow API terms. Public-page capture should be low volume.

## Redistribution Guidance

Store source links and summaries only.

## Notes For Codex/Claude

Aggregator data is useful for discovery, but official manufacturer/distributor sources should verify claims.

