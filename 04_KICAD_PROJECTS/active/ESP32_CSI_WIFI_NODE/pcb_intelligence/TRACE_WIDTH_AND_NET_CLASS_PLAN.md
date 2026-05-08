# Trace Width And Net Class Plan

These are first-pass layout planning values, not manufacturing capability claims.

- `POWER_5V_INPUT`: nets `/+5V_IN`, `/+5V_FUSED`, `/+5V_PROTECTED`; width `0.75` mm; clearance `0.2` mm. Use wider than signal where space allows.
- `POWER_3V3`: nets `+3V3`; width `0.5` mm; clearance `0.2` mm. Wider than low-speed signals; distribute after output caps.
- `USB_FS`: nets `/DP_C`, `/DM_C`, `/DP_E`, `/DM_E`; width `0.25` mm; clearance `0.2` mm. Short and parallel as practical; not an impedance-verified claim.
- `BUCK_LOCAL`: nets `/BUCK_SW`, `/BUCK_BST`; width `0.5` mm; clearance `0.2` mm. Shortest possible local routing; avoid USB/RF.
- `SIGNAL`: nets `/BOOT0`, `/ESP_EN`, `/STATUS_LED`, `/PLED`, `/SLED`, `/U0RXD`, `/U0TXD`, `/CC1`, `/CC2`; width `0.2` mm; clearance `0.2` mm. Low-speed/control/debug/CC routing.
- `GND`: nets `GND`; width `None` mm; clearance `0.2` mm. Use zones and low-impedance returns.
