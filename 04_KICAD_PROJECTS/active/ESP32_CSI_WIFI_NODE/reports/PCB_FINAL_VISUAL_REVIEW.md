# PCB Final Visual Review

Date: `2026-05-09`

Active PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Visual verdict: `FAIL`

Scope: Final visual and routing-quality review of the live PCB. This pass was limited to obvious safe cleanup only. No live PCB edits were applied because the remaining problems are tied to incomplete routing corridors rather than isolated cosmetic corners.

Live DRC result:
- `0` rule violations
- `13` unconnected items
- DRC evidence: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_FINAL_VISUAL_REVIEW_LIVE_DRC.json`

Safe fixes made in this review:
- None

Why no live fix was applied:
- The board still has multiple incomplete nets and several long orthogonal route spines.
- A cosmetic-only corner cleanup would not materially improve routing quality without reopening the remaining escape and test-point routing decisions.
- No zero-risk board-edge or zone-refill-only fix stood out during this pass.

## Findings

Remaining 90-degree bends:
- `+3V3` still has many right-angle corners on both `F.Cu` and `B.Cu`, especially around the right-side distribution spine and the lower-left to upper-right trunk.
- `/+5V_PROTECTED` still has right-angle geometry near the `TP1` branch and power-entry corridor.
- `/BOOT0` and `/ESP_EN` still have right-angle doglegs in the switch-to-U2/test-point paths.
- `/DM_E` still has a large orthogonal rectangular path with right-angle corners between `U2`, `R8`, and `TP9`.
- `/U0RXD` and `/U0TXD` still use boxy right-side escape routing.
- `/STATUS_LED`, `/SHIELD`, and `/CC2` still contain visible right-angle corners.

Acute or non-45 geometry:
- No major acute-angle cluster dominates the board now.
- Non-45 geometry still exists on `/SHIELD` and `/CC1`, and there is a near-horizontal off-grid `+3V3` segment near the U2 area.
- The larger visual problem is still orthogonal boxiness rather than acute-angle damage.

Long diagonal or ratsnest-style traces:
- No giant random diagonal trace dominates the board.
- `/SHIELD` still has a long non-45 diagonal sweep that looks improvised rather than intentional.
- `/CC1` still has a non-45 diagonal segment in the USB connector area.

Giant rectangular loops:
- `+3V3` still forms the largest boxy route network on the board and remains the clearest routing-style defect.
- `/DM_E` still has a large rectangular loop-like route from the U2 area to the upper-right test-point corridor.
- `/U0RXD` still has a long right-side rectangular route.
- `/U0TXD` and `/STATUS_LED` remain visually boxy even where the loop detector threshold did not flag them as the top offenders.

Test-point routing quality:
- `TP1`, `TP2`, `TP4`, and `TP8` are still open because their nets remain unrouted.
- `TP3` is connected, but it still sits on the same long `+3V3` route spine that needs cleanup.
- `TP6`, `TP7`, and `TP9` are connected through long right-edge orthogonal paths rather than short clean stubs.
- The test-point row is physically accessible, but the routing feeding it still looks interim rather than final.

Buck converter and power routing:
- The local buck converter cell around `U1`, `L1`, `C6`, `C7`, and `C8` is materially better than before and does not look like the main visual blocker now.
- The remaining power-routing concern is the long boxy downstream `+3V3` distribution spine, not the local buck switch loop.
- No new obviously skinny high-current segment in the repaired buck cell stood out in this review.

Board-edge routing:
- The right-side board-edge corridor still looks visually poor because of the long orthogonal `+3V3`, `/U0RXD`, `/U0TXD`, and test-point feed routes.
- No board-edge clearance violation was reported by live DRC, so the issue is routing quality rather than rule failure.

Ground zones and return paths:
- The current pours appear broadly continuous after earlier refill work.
- No glaring fragmented `GND` island or missed refill issue was obvious in this visual pass.
- The board still needs a post-reroute pour review after the remaining open nets are finished.

Ground via stitching:
- U2 already has several nearby `GND` vias and the antenna keepout remains clear.
- The buck area already has existing return vias from earlier repair work.
- More stitching may be justified after the final reroute, but no obvious zero-risk via addition was identified in this pass.

Antenna keepout:
- No obvious ESP antenna keepout violation was visible.
- No new copper or via concern near the antenna zone was identified in this review.

Component placement:
- No obvious placement collision or immediate move-required issue was identified.
- The right-side test-point corridor remains routing-congested, but this still looks like a routing problem first, not a forced placement failure.

## Remaining Open Nets

Open nets visible in live DRC:
- `/+5V_PROTECTED` to `TP1`
- `/BOOT0` from `U2` to `R2` and `TP4`
- `/DM_C` from `J2` through `U3` to `R8`
- `/DP_C` from `J2` through `U3` to `R9`
- `/DP_E` from `U2` to `R9` and `TP8`
- `/ESP_EN` from `U2` to the control network and `TP2`

## Recommendation

Board readiness:
- Ready for user screenshot review: `YES`
- Ready for fabrication or release: `NO`
- Ready to claim routing-quality pass: `NO`

Recommended next manual visual checks:
- Review `F.Cu` and `B.Cu` separately at `400%` to `800%` zoom in KiCad.
- Focus on `J2/U3/R8/R9`, the full `U2` right-side test-point corridor, the `+3V3` trunk, and the `SW1/SW2` control nets.
- Highlight nets `+3V3`, `/DM_E`, `/U0RXD`, `/U0TXD`, `/BOOT0`, `/ESP_EN`, and `/+5V_PROTECTED`.
- Confirm whether the right-side TP row should stay in its current routing corridor before any final cleanup pass.

Change status for this review:
- Schematic changed: `NO`
- PCB changed in this review: `NO`
