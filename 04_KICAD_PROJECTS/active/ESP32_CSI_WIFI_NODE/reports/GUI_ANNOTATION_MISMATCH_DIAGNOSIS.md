# GUI Annotation Mismatch Diagnosis

Generated: `2026-05-06 18:55:00 -04:00`

Active project: `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`

Target schematic requested by LJ:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

## Task Boundary

This was a forensic diagnosis only. No schematic text repair, visual layout cleanup, value edits, footprint edits, PCB edits, routing, or manufacturing outputs were performed.

## Exact GUI Process Evidence

Windows process inspection found an open KiCad schematic editor process:

```text
ProcessId: 3232
Name: eeschema.exe
CommandLine: "C:\Program Files\KiCad\9.0\bin\eeschema.exe" "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"
MainWindowTitle: *ESP32_CSI_WIFI_NODE [ESP32_CSI_WIFI_NODE] - Schematic Editor
```

Diagnosis:

- The GUI is opened on the exact active schematic path.
- The leading `*` in the KiCad schematic editor title indicates the GUI document is modified/unsaved in memory.
- That means the GUI can be showing unsaved in-memory state that differs from the saved file on disk.
- Because LJ reports the GUI still shows `R?`, `D?`, `SW?`, `C?`, and `MH?`, the safest conclusion is: the active GUI state is not equivalent to the current saved disk file.

## Exact Disk File Evidence

Current active saved schematic:

```text
Path: C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
Length: 141082 bytes
LastWriteTime: 2026-05-06 18:34:24
SHA256: D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C
```

Structured parse of actual placed-symbol blocks in that saved file found:

| Check | Result |
| --- | --- |
| Placed symbols parsed | `79` |
| Bad placed-symbol references ending in `?` | `0` |
| Duplicate placed-symbol references | `0` |
| Missing instance references | `0` in previous final table |
| Instance/reference mismatches | `0` in previous final table |

Bad placed-symbol references found in the saved file before any GUI-native repair:

| Ref shown | Lib ID | Value | UUID | X/Y location |
| --- | --- | --- | --- | --- |
| None found in saved disk file | N/A | N/A | N/A | N/A |

## Duplicate Schematic Files Found

The repo contains the active schematic plus backup copies with the same filename:

| Path | Last write | SHA256 | Role |
| --- | --- | --- | --- |
| `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 18:34:24` | `D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C` | Active target |
| `99_BACKUPS\pre_codex_edits\20260506_152549_ESP32_CSI_WIFI_NODE_schematic_safe_repair\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-03 07:36:00` | `0BD837841434F45EBBFA0B6D8BF788EEDF65784789872E6516A8A141DDD066F0` | Backup |
| `99_BACKUPS\pre_codex_edits\20260506_155934_ESP32_CSI_WIFI_NODE_emergency_truth_audit\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 15:33:00` | `A87C36095B9710B0596255A771921DFDAD4A5412F84DC61CD232D28FB4D444C9` | Backup |
| `99_BACKUPS\pre_codex_edits\20260506_162153_ESP32_CSI_WIFI_NODE_schematic_real_repair\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 15:33:00` | `A87C36095B9710B0596255A771921DFDAD4A5412F84DC61CD232D28FB4D444C9` | Backup |
| `99_BACKUPS\pre_codex_edits\20260506_170404_ESP32_CSI_WIFI_NODE_human_readable_schematic_relayout\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 16:32:37` | `F2C58AA09BDD601914A74C25785C09302C29FE77D5FF33E46C39440BF7260861` | Backup |
| `99_BACKUPS\pre_codex_edits\20260506_180514_ESP32_CSI_WIFI_NODE_emergency_annotation_repair\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 17:27:10` | `344B550EBFB36DE43B9E7AA5D395C7463F7E1E5CDA19A3BD9DA8ED134FF4D6EB` | Backup |
| `99_BACKUPS\pre_codex_edits\20260506_181726_ESP32_CSI_WIFI_NODE_final_human_readable_schematic_repair\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 18:07:44` | `E0AFE2AA295BE1D523652DE48396D3CF6EB95CC08F942B1AB8BCDA1BF2A18AC7` | Backup |
| `99_BACKUPS\pre_codex_edits\20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-06 18:07:44` | `E0AFE2AA295BE1D523652DE48396D3CF6EB95CC08F942B1AB8BCDA1BF2A18AC7` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_COPPER_ZONE_STRATEGY_BLOCKED_20260503_084828\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-03 07:36:00` | `0BD837841434F45EBBFA0B6D8BF788EEDF65784789872E6516A8A141DDD066F0` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_CRITICAL_ROUTING_BLOCKED_20260503_090215\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-03 07:36:00` | `0BD837841434F45EBBFA0B6D8BF788EEDF65784789872E6516A8A141DDD066F0` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_FULL_ROUTING_BLOCKED_20260503_090757\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-03 07:36:00` | `0BD837841434F45EBBFA0B6D8BF788EEDF65784789872E6516A8A141DDD066F0` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_HOLE_PAD_VIA_STRATEGY_BLOCKED_20260503_084327\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-03 07:36:00` | `0BD837841434F45EBBFA0B6D8BF788EEDF65784789872E6516A8A141DDD066F0` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_PCB_PLACEMENT_PASS_2_BLOCKED_20260503_083808\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-03 07:36:00` | `0BD837841434F45EBBFA0B6D8BF788EEDF65784789872E6516A8A141DDD066F0` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_20260503_073335\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-02 15:20:52` | `4B83AEFCC4C980CB3AAE5126A38DBD4943090228FFBCFF6D28662015703267EB` | Backup |
| `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_SCHEMATIC_ERC_FIX_20260502_150836\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` | `2026-05-02 15:04:28` | `646E5C2BDBF9079A0D731DC87CA992AF77194F5F53A23369E67098DD80AF9983` | Backup |

The GUI process command line points to the active target, not a backup path.

## ERC Results

`kicad-cli sch erc` was run against the exact active schematic path from repo root:

```text
ERC report (2026-05-06T18:46:38-0400, Encoding UTF8)

***** Sheet /

 ** ERC messages: 0  Errors 0  Warnings 0
```

`kicad-cli sch erc` was also run from the active project `kicad` directory using the active schematic filename:

```text
ERC report (2026-05-06T18:46:38-0400, Encoding UTF8)

***** Sheet /

 ** ERC messages: 0  Errors 0  Warnings 0
```

`kicad-cli sch erc --help` shows one `INPUT_FILE` argument for the schematic. A separate `.kicad_pro` ERC argument is not exposed by this CLI command; running from the project schematic directory was used to keep project context local.

## Comparison To Previous Reference Table

`reports/ANNOTATION_REFERENCE_TABLE_FINAL.md` matches the current saved disk parse:

- 79 placed symbols.
- 43 physical symbols.
- 33 `#PWR` symbols.
- 3 `#FLG` symbols.
- 0 unresolved question references.
- 0 duplicate physical references.
- 0 duplicate `#PWR` references.
- 0 duplicate `#FLG` references.

The difference is not between that table and the current saved disk file. The difference is between the current saved disk file and the currently open KiCad GUI in-memory document. The `*` in the Eeschema window title is the strongest local evidence of unsaved/modified GUI state.

## KiCad-Native Annotation Decision

KiCad-native annotation was not run by Codex.

Reason:

- local `kicad-cli` does not provide a schematic annotation command.
- GUI automation would have to act on an unsaved modified KiCad window.
- Saving or annotating that in-memory GUI state through automation could overwrite the current saved disk file with stale or unintended GUI data.
- The repo rules prohibit risky GUI control without a proven safe, screenshot-verified, gated automation workflow.

## Required Manual KiCad-Native Workflow For LJ

Codex must stop here.

LJ should run this manually in KiCad:

1. In the already-open schematic, decide whether the current unsaved GUI state should be kept.
2. If the visible GUI schematic is the desired current state, save a copy or confirm it should overwrite the disk file.
3. Run `Tools -> Annotate Schematic...`.
4. Choose `Re-annotate all symbols`.
5. Confirm annotation.
6. Save the schematic.
7. Run ERC in KiCad.
8. Confirm the GUI no longer shows `R?`, `D?`, `SW?`, `C?`, `MH?`, `#PWR?`, or `#FLG?`.
9. Tell Codex the manual annotation/save is complete.

After that, Codex can re-run a disk parse, KiCad CLI ERC, duplicate check, and final reference table export. Visual cleanup must not resume until the KiCad GUI itself shows no `?` references and ERC passes.

## Final Diagnosis

The command-line/regex reports were insufficient because they tested the saved disk file, while LJ is looking at the live KiCad GUI state. The live KiCad GUI is opened on the exact active schematic path but is modified/unsaved, so it may contain stale or divergent annotation state.

Current status: `BLOCKED_PENDING_MANUAL_KICAD_NATIVE_ANNOTATION`
