# KiCad Official Libraries Source Profile

Source confidence level: `PUBLIC_LIBRARY_OFFICIAL`

## Source Purpose

Public KiCad symbol, footprint, and 3D model candidate discovery through official KiCad library repositories or installed KiCad library evidence.

## Preferred Access Method

Read installed KiCad libraries locally first. Use public KiCad library repositories second.

## Login/API Key Required

No login required for public repository viewing.

## Playwright Allowed

Allowed only for public repository page evidence if local installed library inspection is insufficient.

## Fields May Be Captured

- repository URL
- symbol library path/name
- footprint library path/name
- 3D model path/name
- commit/release/source context if visible

## Must Not Be Captured

- generated claims that a footprint is exact without package drawing review
- modified KiCad global libraries
- repository scraping at scale

## Rate Limit Guidance

Prefer local scripts. Keep public repository checks small.

## Redistribution Guidance

Follow KiCad library licensing and attribution. Candidate links are safer than copied assets.

## Notes For Codex/Claude

Official KiCad footprints are still candidates until matched to the exact manufacturer package drawing.

