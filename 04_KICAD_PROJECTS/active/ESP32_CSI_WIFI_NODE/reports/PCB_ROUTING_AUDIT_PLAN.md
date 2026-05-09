# PCB Routing Audit Plan

Date: `2026-05-09`
Task type: `AUDIT_ONLY`
Active project: `ESP32_CSI_WIFI_NODE`
Target PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
Live PCB hash: `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`
PCB modified in this session: `NO`

## Read-Only Validation

- `python health_check.py --no-write`
  - Result: `PASS=18 WARN=2 FAIL=0`
  - Notable warning: normal Python cannot import `pcbnew`; board-aware work should re-enter through KiCad Python.
- `python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py`
  - Result: `WARN`
  - Current Python `pcbnew`: `False`
  - KiCad Python `pcbnew`: `True`
  - Recommended context: `KICAD_PYTHON`
- `python 03_TOOLS/scripts/kicad_api/kicad_python_context.py`
  - Result: `pcbnew` is available only in KiCad Python.
  - Current Python: `3.12.10`
  - KiCad Python: `3.11.5` at `C:\Program Files\KiCad\9.0\bin\python.exe`
- `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8`
  - Result: `BLOCKED`
  - Live blockers: `0` DRC violations, `17` unconnected items, `4` unrouted nets.

## Live Routing Facts

- Unrouted nets: `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`
- Geometry hard-fail counts:
  - `RIGHT_ANGLE_FOUND`: `22`
  - `ACUTE_JOG_FOUND`: `5`
  - `UNNECESSARY_ZIGZAG_FOUND`: `5`
- Hard-fail nets from the live geometry audit:
  - `+3V3`
  - `/+5V_IN`
  - `/+5V_PROTECTED`
  - `/BOOT0`
  - `/CC1`
  - `/CC2`
  - `/ESP_EN`
  - `/SHIELD`
  - `/STATUS_LED`
  - `/U0RXD`
  - `/U0TXD`
  - `unconnected-(J2-VBUS-PadA4)`
- The extracted routing plan reports `0.2 mm` current widths on the routed power nets that exist on the board today, including `/+5V_IN`, `/+5V_FUSED`, `/+5V_PROTECTED`, `/BUCK_SW`, and `+3V3`.

## Routing Defects By Audited Area

### 1. `J2 / U3` USB header area

Live board note:

- The current PCB and schematic do not contain `R50`, `R51`, or `R52`.
- The live USB data resistors in this area are `R8` and `R9`.

Defects found:

- USB data routing is incomplete:
  - `/DM_C`: `J2 A7/B7`, `U3 pad 2`, and `R8 pad 1` are not connected together.
  - `/DM_E`: `U2 pad 13`, `R8 pad 2`, and `TP9` are not connected together.
  - `/DP_C`: `J2 A6/B6`, `U3 pad 1`, and `R9 pad 1` are not connected together.
  - `/DP_E`: `U2 pad 14`, `R9 pad 2`, and `TP8` are not connected together.
- `J2` control/power side geometry is also poor:
  - `/CC1` has an acute jog (`58.688` degree non-45 transition).
  - `/CC2` has a right-angle turn.
  - `unconnected-(J2-VBUS-PadA4)` has a right-angle turn at the connector breakout.
  - `/SHIELD` has a right-angle, an acute jog, and an unnecessary zigzag.
- The USB area is the single biggest electrical blocker because it contains all four explicitly unrouted nets.

Likely nets involved:

- `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`, `/CC1`, `/CC2`, `/SHIELD`, `unconnected-(J2-VBUS-PadA4)`

### 2. `SW1 / D3 / F1 / Q1 / J1` power input area

Defects found:

- `/+5V_IN` contains a right-angle turn near the input path.
- `/+5V_PROTECTED` contains multiple right-angle turns plus an unnecessary zigzag.
  - Measured trace length: `24.823 mm`
  - Direct distance: `6.537 mm`
  - Length ratio: about `3.8x`
- `TP1` is still electrically open from `/+5V_PROTECTED`.
- The local 5 V protection path is routed with narrow `0.2 mm` conductors even though this is part of the incoming power chain.
- The visual crop shows avoidable doglegs between `J1`, `F1`, `Q1`, `D3`, and the upstream regulator input.

Likely nets involved:

- `/+5V_IN`, `/+5V_FUSED`, `/+5V_PROTECTED`, `GND`

### 3. `U1 / L1 / C6 / C7` buck converter area

Defects found:

- `/BUCK_BST` and `/BUCK_SW` do not show geometry hard fails in the live audit.
- The buck output distribution still fails quality once it leaves the regulator area:
  - `+3V3` has multiple right-angle turns, acute jogs, and an unnecessary zigzag.
  - Measured trace length: `158.543 mm`
  - Direct distance: `28.129 mm`
  - Length ratio: about `5.6x`
- The `+3V3` trunk uses long orthogonal detours instead of a compact 45-degree distribution path.
- The present extracted width for the routed `+3V3` net is only `0.2 mm`.

Likely nets involved:

- `+3V3`, `/+5V_PROTECTED`, `/BUCK_SW`, `/BUCK_BST`, `GND`

### 4. `U2` ESP module escape routing

Defects found:

- `U2` escape routing is electrically incomplete on the following nets:
  - `/ESP_EN`: open between the local track and `U2 pad 3`, and open between `TP2` and `U2 pad 3`
  - `/BOOT0`: open between `R2 pad 1` and `U2 pad 27`, and open between `TP4` and `U2 pad 27`
  - `/DM_E`: open between `U2 pad 13` and `R8 pad 2`
  - `/DP_E`: open between `U2 pad 14` and `R9 pad 2`
- The existing routed escapes also show poor geometry:
  - `/ESP_EN`: right-angle plus unnecessary zigzag, length ratio about `4.27x`
  - `/BOOT0`: right-angle turns
  - `/U0RXD`: right-angle turn on the long right-edge run
  - `/U0TXD`: right-angle turn on the long right-edge run
- ESP antenna keepout appears respected in the current board image and the keepout audit did not detect a crossing.

Likely nets involved:

- `/ESP_EN`, `/BOOT0`, `/DM_E`, `/DP_E`, `/U0RXD`, `/U0TXD`, `+3V3`, `GND`

### 5. `TP1` through `TP9` test point routing

Defects found:

- Test point connectivity is incomplete on:
  - `TP1` on `/+5V_PROTECTED`
  - `TP2` on `/ESP_EN`
  - `TP4` on `/BOOT0`
  - `TP8` on `/DP_E`
  - `TP9` on `/DM_E`
- The right-edge test-point distribution uses long rectangular spines and 90-degree corners:
  - `TP3` ties into the overlong `+3V3` trunk
  - `TP6` is on `/U0TXD`, which has a right-angle long edge route
  - `TP7` is on `/U0RXD`, which has a right-angle long edge route
- The current geometry does not meet the "keep test point stubs short" rule for the long right-edge routed branches.

Likely nets involved:

- `/+5V_PROTECTED`, `/ESP_EN`, `+3V3`, `/BOOT0`, `GND`, `/U0TXD`, `/U0RXD`, `/DP_E`, `/DM_E`

### 6. `D1 / D2 / R3 / R4` routing

Defects found:

- `D1` and `R3` (`/PLED`) do not show geometry hard fails in the live routing audit.
- `D2` to `R4` to `U2` is where the problem begins:
  - `/STATUS_LED` has a right-angle turn and an unnecessary zigzag.
  - Measured trace length: `43.167 mm`
  - Direct distance: `34.668 mm`
- The long route from `R4` back toward `U2` participates in the same right-edge rectangular routing style seen on other nets.

Likely nets involved:

- `/PLED`, `/SLED`, `/STATUS_LED`, `+3V3`, `GND`

### 7. `SW1 / SW2` button area routing

Defects found:

- `/BOOT0` at `SW1` has two right-angle turns in the local left-edge dogleg.
- `/ESP_EN` at `SW2` has a right-angle turn plus an unnecessary zigzag.
- DRC still reports incomplete control-net connectivity:
  - `SW1 pad 1` is open to the local `/BOOT0` track
  - `SW2` still reports an open between its duplicated pad-1 shapes
  - `TP2` and `TP4` are not tied through to `U2`
- The button area looks repairable by rerouting; the evidence does not currently prove that switch movement is required.

Likely nets involved:

- `/BOOT0`, `/ESP_EN`, `GND`, `+3V3`

### 8. Right-side board-edge long rectangular routes

Defects found:

- The long right-edge spine is the main source of the board's "boxy" routing style.
- Nets currently affected by this pattern include:
  - `+3V3`
  - `/U0TXD`
  - `/U0RXD`
  - `/STATUS_LED`
  - portions of the test-point fanout
- These runs create unnecessary vertical-horizontal-vertical path changes instead of direct 45-degree routing.
- The `+3V3` route is the clearest example of excessive detour and repeated reversals.

Likely nets involved:

- `+3V3`, `/U0TXD`, `/U0RXD`, `/STATUS_LED`, `/BOOT0`, `/ESP_EN`

### 9. Ground pours, return paths, and via stitching under/near `U2`

Verified facts:

- The board has `2` `GND` zones.
- The keepout audit did not detect a trace crossing in the ESP antenna keepout.
- Read-only `pcbnew` inspection found only a small number of explicit `GND` vias near the `U2` region, including visible stitching points near:
  - `(21.250, 22.740) mm`
  - `(38.750, 22.740) mm`
  - `(21.500, 44.950) mm`
  - `(26.500, 44.775) mm`
  - plus larger vias at `(10, 30)`, `(50, 30)`, `(10, 50)`, and `(50, 50)` mm

Risk assessment:

- The ground pours exist, but the current stitching pattern around `U2` does not yet look deliberate or dense.
- The long right-edge signal spines likely squeeze or fragment simple return paths more than necessary.
- This is a medium-confidence layout risk based on zone presence plus visual topology, not a solved return-current proof.

Likely nets involved:

- `GND`, `+3V3`, `/U0TXD`, `/U0RXD`, `/DP_E`, `/DM_E`

## Proposed Repair Order

1. Repair the USB data chain first.
   - Complete `/DM_C`, `/DM_E`, `/DP_C`, and `/DP_E` between `J2`, `U3`, `R8`, `R9`, `U2`, `TP8`, and `TP9`.
   - Replace the current `J2` breakout right angles with clean 45-degree exits.
2. Repair the ESP control nets second.
   - Complete `/ESP_EN` and `/BOOT0` from `SW2` and `SW1` through `U2`, `TP2`, `TP4`, and `R2`.
   - Remove the existing left-edge doglegs and zigzags.
3. Clean the 5 V power-entry path third.
   - Rebuild `/+5V_IN`, `/+5V_FUSED`, and `/+5V_PROTECTED` with shorter 45-degree paths.
   - Add the missing `TP1` connection.
   - Re-evaluate width on the incoming 5 V path.
4. Rebuild the `+3V3` trunk fourth.
   - Collapse the large rectangular detour into a shorter path from the buck area toward `U2` and the test-point spine.
   - Re-evaluate width on the `+3V3` distribution path.
5. Clean the right-edge test-point spine fifth.
   - Shorten the `TP3`, `TP6`, and `TP7` branches.
   - Route the data test points only after the USB nets are fully connected.
6. Clean the LED and miscellaneous long runs sixth.
   - Simplify `/STATUS_LED`, `/U0RXD`, `/U0TXD`, `/CC1`, `/CC2`, and `/SHIELD`.
7. Re-pour and review `GND` last.
   - After routing is stable, refill pours and check for narrow neck-downs or isolated return regions near `U2` and the right-edge spine.
   - Add via stitching only after the final signal/power paths are known.

## Movement And Schematic Assessment

- Component movement appears required right now: `NO` from current evidence.
  - Read-only audit outcome: reroute-first.
  - Escalate to local movement only if the USB data pair or button/test-point cleanup cannot be completed with compliant 45-degree geometry.
- Schematic changes appear required right now: `NO` from current evidence.
  - The live blockers are routing and PCB connectivity problems, not a demonstrated schematic-netlist mismatch.

## Audit Conclusion

- The board is not ready for further routing claims or release work.
- The dominant blockers are incomplete USB routing, incomplete control-net routing, overly indirect power/test-point geometry, and weak ground-return confidence around the ESP region.
- This session intentionally stopped at a read-only repair plan. No KiCad design files were edited.
