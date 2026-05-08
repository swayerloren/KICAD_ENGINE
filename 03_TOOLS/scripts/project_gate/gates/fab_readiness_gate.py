"""FAB_READINESS_GATE."""

from __future__ import annotations

from .base_gate import BLOCKED, FAIL, INCOMPLETE, PASS, BaseGate, GateBlocker


class FabReadinessGate(BaseGate):
    gate_id = "FAB_READINESS_GATE"
    gate_name = "Fabrication Readiness Gate"
    stage = 9

    def evaluate(self):
        final_verification = self.first_existing("reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md")
        fab_audit = self.first_existing("reports/NOT_FINAL_FAB_PACKAGE_AUDIT.md")
        golden_gate = self.first_existing("reports/GOLDEN_PATH_GATE_REPORT.md")
        golden_final = self.first_existing("reports/GOLDEN_PATH_FINAL_AUDIT.md")
        fabrication_dir = self.project_file("fabrication")
        unsafe_fab_outputs = self._find_unsafe_fab_outputs(fabrication_dir)
        evidence = [
            self.evidence_path("final_pcb_verification_before_fab", final_verification),
            self.evidence_path("not_final_fab_package_audit", fab_audit),
            self.evidence_path("golden_path_gate_report", golden_gate),
            self.evidence_path("golden_path_final_audit", golden_final),
            self.evidence_path("fabrication_dir", fabrication_dir, kind="directory"),
        ]

        if unsafe_fab_outputs:
            return self.make_result(
                FAIL,
                "Fabrication directory contains outputs that are not clearly NOT_FINAL.",
                blockers=[
                    GateBlocker(
                        id="UNSAFE_FAB_OUTPUT_LABEL",
                        severity="CRITICAL",
                        message=f"Fabrication-style output is not clearly NOT_FINAL: {self.rel(path)}",
                        evidence_path=self.rel(path),
                        remediation="Move, relabel, or audit generated manufacturing-style outputs before public use.",
                    )
                    for path in unsafe_fab_outputs[:25]
                ],
                evidence=evidence,
                details={"unsafe_fab_output_count": len(unsafe_fab_outputs)},
            )

        final_text = self.read_text(final_verification)
        if final_verification:
            if "READY_FOR_NOT_FINAL_FAB_EXPORT" in final_text:
                return self.make_result(
                    PASS,
                    "Final PCB verification says the project is ready for NOT_FINAL fabrication export.",
                    evidence=evidence,
                    details={"ready_for_not_final_export": True},
                )
            return self.make_result(
                BLOCKED,
                "Final PCB verification exists but does not allow NOT_FINAL fabrication export.",
                blockers=[
                    GateBlocker(
                        id="FAB_EXPORT_NOT_AUTHORIZED",
                        severity="HIGH",
                        message="FINAL_PCB_VERIFICATION_BEFORE_FAB.md does not say READY_FOR_NOT_FINAL_FAB_EXPORT.",
                        evidence_path=self.rel(final_verification),
                        remediation="Complete final PCB verification before generating any fabrication package.",
                    )
                ],
                evidence=evidence,
            )

        prior_text = "\n".join([self.read_text(golden_gate), self.read_text(golden_final)])
        if any(token in prior_text for token in ("BLOCKED_UNTIL_HUMAN_REVIEW", "GOLDEN_PATH_PARTIAL", "ERC | `FAIL`", "DRC | `FAIL`", "Fabrication output | `NOT_GENERATED`")):
            return self.make_result(
                BLOCKED,
                "Fabrication readiness is blocked by prior ERC/DRC/footprint/human-review results.",
                blockers=[
                    GateBlocker(
                        id="FAB_READINESS_BLOCKED_BY_PRIOR_GATES",
                        severity="HIGH",
                        message="Existing golden-path reports show ERC/DRC/footprint or human-review blockers; no fabrication package may be generated.",
                        evidence_path=self.rel(golden_final or golden_gate),
                        remediation="Resolve upstream gate blockers, then create FINAL_PCB_VERIFICATION_BEFORE_FAB.md before export.",
                    )
                ],
                evidence=evidence,
                details={"ready_for_not_final_export": False},
            )

        return self.make_result(
            INCOMPLETE,
            "No final PCB verification report or prior gate decision was found.",
            [self.missing_evidence_blocker("final PCB verification", "reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md")],
            evidence=evidence,
        )

    def _find_unsafe_fab_outputs(self, fabrication_dir):
        if not fabrication_dir.exists():
            return []
        extensions = {".gbr", ".ger", ".drl", ".xln", ".pos", ".step", ".stp"}
        unsafe = []
        for path in fabrication_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in extensions and "NOT_FINAL" not in str(path):
                unsafe.append(path)
        return unsafe
