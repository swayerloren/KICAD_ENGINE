# JLCPCB Source Profile

Source confidence level: `ASSEMBLY_SUPPLIER`

## Source Purpose

JLCPCB/LCSC assembly availability notes, part references, public assembly library metadata, and footprint-orientation risk flags.

## Preferred Access Method

Official/approved API or data-feed access first. User-provided exports second. Manual source links third.

## Login/API Key Required

May require account or approved access for reliable data. Do not automate logged-in pages.

## Playwright Allowed

Public-page evidence only when allowed. Live browser access is blocked if login, CAPTCHA, or unclear terms appear.

## Fields May Be Captured

- public part page URL
- public part number or assembly library ID
- manufacturer and MPN
- package text
- public availability text
- datasheet/source link

## Must Not Be Captured

- logged-in assembly library pages
- carts, quotes, order pages
- account-specific pricing
- cookies
- scraped catalogs

## Rate Limit Guidance

Use very low volume; prefer manual/user exports.

## Redistribution Guidance

Store links and normalized metadata only. Do not copy package drawings or PDFs.

## Notes For Codex/Claude

JLC/LCSC package names and assembly orientation are not KiCad footprint verification.

