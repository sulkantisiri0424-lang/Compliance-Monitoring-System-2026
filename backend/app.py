from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.transaction_agent import TransactionMonitor
from agents.communication_agent import CommunicationScanner
from agents.regulation_agent import RegulationAgent
from agents.audit_agent import AuditAgent
from agents.report_agent import ReportAgent

from database import (
    initialize_database,
    save_transaction,
    add_audit_log,
    get_audit_logs,
    save_report
)


app = FastAPI(
    title="Compliance Monitoring System 2026",
    description="AI-powered compliance monitoring and reporting system",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Initialize database
initialize_database()


# Initialize agents
transaction_agent = TransactionMonitor()
communication_agent = CommunicationScanner()
regulation_agent = RegulationAgent()
audit_agent = AuditAgent()
report_agent = ReportAgent()


@app.get("/")
def home():
    return {
        "message": "Compliance Monitoring System is running",
        "status": "active"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Compliance Monitoring System"
    }


@app.get("/regulations")
def get_regulations():
    return regulation_agent.get_regulations()


@app.post("/monitor/transaction")
def monitor_transaction(transaction: dict):

    result = transaction_agent.analyze(transaction)

    transaction_id = transaction.get(
        "transaction_id",
        "UNKNOWN"
    )

    amount = float(
        transaction.get("amount", 0)
    )

    save_transaction(
        transaction_id,
        amount,
        result["status"],
        result["risk_level"]
    )

    add_audit_log(
        "Transaction Monitoring",
        str(result),
        result["risk_level"]
    )

    return result


@app.post("/monitor/communication")
def monitor_communication(data: dict):

    result = communication_agent.scan(data)

    add_audit_log(
        "Communication Monitoring",
        str(result),
        result["risk_level"]
    )

    return result


@app.post("/report")
def generate_report(data: dict):

    report = report_agent.generate(data)

    save_report(
        report["title"],
        str(report)
    )

    add_audit_log(
        "Report Generation",
        str(report),
        report["risk_level"]
    )

    return report


@app.get("/audit")
def get_audit():

    return {
        "audit_logs": get_audit_logs()
    }
