# FAQ

## Is KiCad Engine a PCB CAD program?

No. KiCad Engine does not replace KiCad. It is a local workspace that helps AI agents understand and use your installed KiCad app more safely.

## Is this official KiCad?

No. KiCad Engine is not official KiCad and is not affiliated with KiCad unless a future relationship is explicitly documented.

## Does it require cloud PCB design?

No. The repo is designed around local files, local KiCad, VS Code, Git, and local verification reports. Your AI tool may have its own service model, but KiCad Engine itself is local-first.

## Does it require paid APIs?

No. It does not require paid APIs. You use your own Codex, Claude, or other AI tool account if you choose to use one.

## Does it store my AI credentials?

No. Do not store API keys, tokens, or login credentials in this repo.

## Can it make a board for me?

It can help plan, inspect, validate, document, and sometimes automate carefully scoped tasks. It cannot replace engineering review, datasheet verification, footprint verification, or final manufacturing approval.

## Can it run ERC and DRC?

Yes, when `kicad-cli` is installed and the project files are available. ERC and DRC are important checks, but they are not complete design approval.

## Are the datasheets included?

The datasheet library is primarily metadata, source links, summaries, and policy scaffolding. PDFs may be link-only unless redistribution rights are confirmed.

## Are component records verified?

Some records may be researched; many are placeholders. Always check verification status, source links, datasheets, and package drawings before relying on a record.

## Can I use it with Claude instead of Codex?

Yes. Prompt packs exist for both Codex and Claude. Similar VS Code-based agents can use the shared standards.

## Why are outputs called NOT_FINAL?

Because generated fabrication-style outputs are only review artifacts until ERC, DRC, BOM, footprint, datasheet, connector, polarity, mechanical, and visual checks are complete and approved by a human.

## Can I contribute?

Yes. Read `CONTRIBUTING.md`, `SECURITY.md`, `DISCLAIMER.md`, and `PUBLIC_RELEASE_CHECKLIST.md` first.
