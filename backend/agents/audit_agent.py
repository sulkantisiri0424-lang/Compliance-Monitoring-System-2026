from datetime import datetime


class AuditAgent:
    """
    Records compliance activities and maintains
    an audit trail.
    """

    def __init__(self):
        self.logs = []

    def record(self, activity, result):
        log_entry = {
            "activity": activity,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

        self.logs.append(log_entry)

        return log_entry

    def get_logs(self):
        return {
            "total_logs": len(self.logs),
            "logs": self.logs
        }

    def clear_logs(self):
        self.logs.clear()

        return {
            "message": "Audit logs cleared successfully"
        }
