import json
import os


class RegulationAgent:
    """
    Loads and manages compliance regulations.
    """

    def __init__(self):
        self.regulations = self.load_regulations()

    def load_regulations(self):
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "regulations.json"
        )

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data.get("regulations", [])

        except FileNotFoundError:
            return []

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
