# Vendor Download Rules

Date: 2026-05-02

Status: download safety rules for future pipeline work.

## Default

Downloads are disabled by default.

Scripts may expose a future `--download` flag for planned workflows, but current policy treats automatic download as unsafe for public redistribution unless license and source review are complete.

## Never Do

- Do not bulk mirror a vendor site.
- Do not bypass rate limits, robots rules, login gates, paywalls, export-control gates, or license prompts.
- Do not download from unofficial mirrors when an official source exists.
- Do not commit downloaded PDFs to a public repo unless redistribution is clearly permitted.
- Do not rename downloaded documents as verified unless revision and source are checked.

## Allowed With Explicit Approval

- Download one specific document from an official product page for private local engineering use.
- Store a private local copy when the user requests it and public redistribution is not implied.
- Generate summaries from local documents when copyright constraints are respected.

## Required Metadata For Any Download

- Vendor.
- Part number or topic.
- Document type.
- Title.
- Source URL.
- Download/access date.
- Local path.
- Revision/date if visible.
- Redistribution status.
- Notes about license uncertainty.

## Future Download Gate

A future download-capable script must require:

- `--download`
- `--confirm-license-reviewed`
- explicit output folder
- source list row with non-empty source URL
- redistribution status not equal to `UNKNOWN`
- command log and report output
