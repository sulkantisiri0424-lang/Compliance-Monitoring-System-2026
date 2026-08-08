class RegulationAgent:
    """
    Manages compliance regulations and provides
    applicable regulatory information.
    """

    def __init__(self):
        self.regulations = [
            {
                "id": "REG001",
                "name": "Anti-Money Laundering",
                "description": "Prevents and detects money laundering activities.",
                "risk_area": "Financial Transactions"
            },
            {
                "id": "REG002",
                "name": "Data Privacy",
                "description": "Protects personal and sensitive customer information.",
                "risk_area": "Data Protection"
            },
            {
                "id": "REG003",
                "name": "Fraud Prevention",
                "description": "Helps organizations identify and prevent fraudulent activities.",
                "risk_area": "Fraud"
            },
            {
                "id": "REG004",
                "name": "Insider Trading",
                "description": "Prevents misuse of confidential financial information.",
                "risk_area": "Financial Markets"
            }
        ]

    def get_regulations(self):
        return {
            "total": len(self.regulations),
            "regulations": self.regulations
        }

    def check_regulation(self, risk_area):
        matches = [
            regulation
            for regulation in self.regulations
            if regulation["risk_area"].lower() == risk_area.lower()
        ]

        return {
            "risk_area": risk_area,
            "applicable_regulations": matches
        }
