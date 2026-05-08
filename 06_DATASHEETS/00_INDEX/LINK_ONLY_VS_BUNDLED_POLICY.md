# Link-Only Vs Bundled Policy

Date: 2026-05-02

Status: policy for deciding whether to store local documents.

## Link-Only

Use link-only when:

- Redistribution permission is unknown.
- The document is a vendor datasheet, app note, reference manual, package drawing, or schematic with unclear copyright.
- The source is behind a license, account, export-control, or click-through gate.
- The repo is intended for public GitHub release.
- The document changes frequently.

Recommended status:

```text
LINK_ONLY_RECOMMENDED
```

## Private Local Copy

Use private local copy when:

- The user explicitly wants a local engineering copy.
- The copy is not intended for public release.
- Source URL, access date, and copyright uncertainty are recorded.

Recommended status:

```text
PRIVATE_LOCAL_COPY_ONLY
```

## Bundled In Public Repo

Bundle only when:

- License clearly allows redistribution.
- The document is intentionally part of open documentation.
- Source URL, license, access date, and revision are recorded.
- A release audit confirms the decision.

Recommended status:

```text
PUBLIC_REDISTRIBUTION_PERMITTED
```

## AI Summary Stubs

Summary stubs may be committed if:

- They contain original wording.
- They do not copy long passages from restricted documents.
- They clearly mark unknown values.
- They point back to source URLs for user verification.
