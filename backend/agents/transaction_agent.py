class TransactionMonitor:
    """
    Monitors financial transactions and identifies
    potentially suspicious activities.
    """

    def analyze(self, transaction):
        amount = float(transaction.get("amount", 0))
        transaction_type = transaction.get("type", "unknown")
        
        if amount >= 100000:
            risk_level = "HIGH"
            status = "Suspicious transaction"
        elif amount >= 50000:
            risk_level = "MEDIUM"
            status = "Transaction requires review"
        else:
            risk_level = "LOW"
            status = "Transaction appears normal"

        return {
            "transaction_type": transaction_type,
            "amount": amount,
            "risk_level": risk_level,
            "status": status,
            "recommendation": self.get_recommendation(risk_level)
        }

    def get_recommendation(self, risk_level):
        if risk_level == "HIGH":
            return "Conduct immediate compliance investigation."
        elif risk_level == "MEDIUM":
            return "Review the transaction and supporting documents."
        else:
            return "No immediate action required."
