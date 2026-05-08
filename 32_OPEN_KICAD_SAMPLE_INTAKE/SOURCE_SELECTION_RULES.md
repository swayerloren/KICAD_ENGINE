# Source Selection Rules

Status: `MANDATORY_BEFORE_CANDIDATE_IMPORT`

## Preferred Sources

Use sources in this order:

1. Official vendor open hardware repositories with explicit license.
2. Public GitHub/GitLab/Codeberg repositories with explicit open-source hardware/software license.
3. KiCad official demo/example projects with compatible licensing.
4. Open hardware community projects with clear authorship, license, and KiCad source files.
5. User-provided local archives only when the user confirms origin and license status.

## Source Requirements

Every candidate must record:

- project name,
- source URL,
- source host,
- project owner/author,
- license file or license statement path,
- whether KiCad source files are visible,
- candidate import status,
- attribution requirements,
- public bundle status.

## Reject Or Block Sources

Do not import sources that:

- have no license,
- say "all rights reserved",
- prohibit redistribution,
- are commercial/proprietary client work,
- are copied from forums without author/license context,
- contain private credentials or personal data,
- require login, paywall, CAPTCHA bypass, or scraping to access,
- are Gerber-only or PDF-only without KiCad source files,
- appear to include third-party vendor PDFs or CAD files without redistribution review.

## Search Rules

This intake system is not a scraper. `find_candidate_projects.py` may create target/search plans and candidate records from user-provided URLs or local CSV/JSON lists. It must not crawl the web, clone repositories, or download archives by default.

## Candidate Statuses

| Status | Meaning |
| --- | --- |
| `CANDIDATE_LINK_ONLY` | Source link recorded; no import. |
| `SOURCE_SCREENED` | Basic source and KiCad-file presence reviewed. |
| `LICENSE_NEEDS_REVIEW` | License unclear or not yet human-reviewed. |
| `IMPORT_ALLOWED_DRY_RUN` | Import appears allowable but has not been copied. |
| `REJECTED_SOURCE` | Source should not be imported. |
