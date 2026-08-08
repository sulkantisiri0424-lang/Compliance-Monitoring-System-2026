class CommunicationScanner:
    """
    Scans communications for potential compliance violations.
    """

    KEYWORDS = [
        "bribe",
        "bribery",
        "fraud",
        "money laundering",
        "insider trading",
        "illegal",
        "kickback",
        "confidential"
    ]

    def scan(self, data):
        message = data.get("message", "")

        message_lower = message.lower()

        detected_keywords = [
            keyword
            for keyword in self.KEYWORDS
            if keyword in message_lower
        ]

        if detected_keywords:
            risk_level = "HIGH"
            status = "Potential compliance violation detected"
        else:
            risk_level = "LOW"
            status = "No obvious compliance violation detected"

        return {
            "message": message,
            "detected_keywords": detected_keywords,
            "risk_level": risk_level,
            "status": status,
            "recommendation": self.get_recommendation(risk_level)
        }

    def get_recommendation(self, risk_level):
        if risk_level == "HIGH":
            return "Escalate the communication for compliance review."

        return "No immediate action required."
