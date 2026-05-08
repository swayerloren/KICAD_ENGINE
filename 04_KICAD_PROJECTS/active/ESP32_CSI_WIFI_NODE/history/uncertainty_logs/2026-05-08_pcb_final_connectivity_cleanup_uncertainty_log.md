# Uncertainty Log: PCB Final Connectivity Cleanup

Generated: `2026-05-08T12:34:25-04:00`

- The remaining `SW1` and `SW2` duplicate-pad opens are classified as expected footprint behavior based on typical tactile-switch construction and the copied-board safety tradeoff, but that classification is still weaker than a direct footprint-datasheet confirmation.
- No additional safe route for `TP1`, `TP2`, `TP4`, or the USB data spines was proven in this pass.
