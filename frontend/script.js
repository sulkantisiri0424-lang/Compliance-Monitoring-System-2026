const API_URL = "http://127.0.0.1:8000";


async function checkSystemStatus() {
    try {
        const response = await fetch(`${API_URL}/health`);
        const data = await response.json();

        document.getElementById("systemStatus").textContent =
            data.status.toUpperCase();

    } catch (error) {
        document.getElementById("systemStatus").textContent =
            "OFFLINE";
    }
}


async function loadRegulations() {
    try {
        const response = await fetch(`${API_URL}/regulations`);
        const data = await response.json();

        document.getElementById("regulationCount").textContent =
            data.total;

    } catch (error) {
        document.getElementById("regulationCount").textContent =
            "0";
    }
}


async function loadAuditLogs() {
    try {
        const response = await fetch(`${API_URL}/audit`);
        const data = await response.json();

        document.getElementById("auditCount").textContent =
            data.audit_logs.length;

    } catch (error) {
        document.getElementById("auditCount").textContent =
            "0";
    }
}


async function monitorTransaction() {

    const transactionId =
        document.getElementById("transactionId").value;

    const amount =
        document.getElementById("amount").value;

    if (!transactionId || !amount) {
        alert("Please enter transaction ID and amount.");
        return;
    }

    const transaction = {
        transaction_id: transactionId,
        amount: Number(amount),
        type: "financial"
    };

    try {
        const response = await fetch(
            `${API_URL}/monitor/transaction`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(transaction)
            }
        );

        const data = await response.json();

        document.getElementById("transactionResult").textContent =
            JSON.stringify(data, null, 2);

        loadAuditLogs();

    } catch (error) {

        document.getElementById("transactionResult").textContent =
            "Unable to connect to the backend.";
    }
}


async function scanCommunication() {

    const message =
        document.getElementById("message").value;

    if (!message) {
        alert("Please enter a message.");
        return;
    }

    try {
        const response = await fetch(
            `${API_URL}/monitor/communication`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        document.getElementById("communicationResult").textContent =
            JSON.stringify(data, null, 2);

        loadAuditLogs();

    } catch (error) {

        document.getElementById("communicationResult").textContent =
            "Unable to connect to the backend.";
    }
}


async function generateReport() {

    const reportData = {
        title: "Compliance Monitoring Report",
        risk_level: "MEDIUM",
        findings: [
            "Transaction monitoring completed",
            "Communication monitoring completed"
        ]
    };

    try {
        const response = await fetch(
            `${API_URL}/report`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(reportData)
            }
        );

        const data = await response.json();

        document.getElementById("reportResult").textContent =
            JSON.stringify(data, null, 2);

        loadAuditLogs();

    } catch (error) {

        document.getElementById("reportResult").textContent =
            "Unable to connect to the backend.";
    }
}


window.onload = function () {
    checkSystemStatus();
    loadRegulations();
    loadAuditLogs();
};
