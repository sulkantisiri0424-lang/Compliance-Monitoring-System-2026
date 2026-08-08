from datetime import datetime


class ReportAgent:
    """
    Generates compliance reports based on monitoring results.
    """

    def generate(self, data):
        report_title = data.get(
            "title",
            "Compliance Monitoring Report"
        )

        findings = data.get("findings", [])
        risk_level = data.get("risk_level", "LOW")

        report = {
            "title": report_title,
            "risk_level": risk_level,
            "findings": findings,
            "total_findings": len(findings),
            "generated_at": datetime.now().isoformat(),
            "recommendation": self.get_recommendation(risk_level)
        }

        return report

    def get_recommendation(self, risk_level):
        if risk_level == "HIGH":
            return "Immediate compliance investigation is recommended."

        if risk_level == "MEDIUM":
            return "Further review of the identified findings is recommended."

        return "No immediate compliance action is required."
