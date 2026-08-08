from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.transaction_agent import TransactionMonitor
from agents.communication_agent import CommunicationScanner
from agents.regulation_agent import RegulationAgent
from agents.audit_agent import AuditAgent
from agents.report_agent import ReportAgent

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
    audit_agent.record("Transaction Monitoring", result)
    return result


@app.post("/monitor/communication")
def monitor_communication(data: dict):
    result = communication_agent.scan(data)
    audit_agent.record("Communication Monitoring", result)
    return result


@app.post("/report")
def generate_report(data: dict):
    report = report_agent.generate(data)
    audit_agent.record("Report Generation", report)
    return report


@app.get("/audit")
def get_audit_logs():
    return audit_agent.get_logs()
