# Compliance Monitoring System 2026

## 📌 Project Overview

The Compliance Monitoring System is an AI-powered application designed to help organizations monitor compliance activities, identify potential risks, analyze transactions and communications, maintain audit records, and generate compliance reports.

The system uses multiple specialized monitoring agents to perform different compliance-related tasks.

---

## 🎯 Objectives

The main objectives of this project are:

- Monitor financial transactions.
- Detect potentially suspicious transactions.
- Analyze communications for compliance-related keywords.
- Manage applicable compliance regulations.
- Maintain audit logs.
- Generate compliance reports.
- Provide a centralized monitoring dashboard.
- Reduce manual compliance monitoring effort.

---

## 🚀 Features

### 1. Transaction Monitoring

The Transaction Monitoring Agent analyzes transactions based on their amount and identifies different risk levels.

Risk levels:

- LOW
- MEDIUM
- HIGH

### 2. Communication Monitoring

The Communication Monitoring Agent scans messages for potentially risky compliance-related keywords such as:

- Fraud
- Bribery
- Money laundering
- Insider trading
- Kickback
- Confidential information

### 3. Regulation Management

The Regulation Agent manages compliance regulations stored in a JSON dataset.

Example regulations include:

- Anti-Money Laundering
- Data Privacy
- Fraud Prevention
- Insider Trading
- Record Keeping

### 4. Audit Monitoring

The Audit Agent records important compliance activities and maintains an audit trail.

### 5. Report Generation

The Report Agent generates compliance reports containing:

- Risk level
- Findings
- Recommendations
- Report generation time

### 6. Database

SQLite is used to store:

- Transactions
- Audit logs
- Reports

### 7. Web Dashboard

The frontend provides a simple dashboard for:

- System status
- Regulation count
- Audit log count
- Transaction analysis
- Communication scanning
- Report generation

---

## 🏗️ System Architecture

```text
                    User
                     |
                     v
              Web Dashboard
                     |
                     v
                FastAPI
                     |
        +------------+-------------+
        |            |             |
        v            v             v
 Transaction    Communication   Regulation
    Agent           Agent          Agent
        |            |             |
        +------------+-------------+
                     |
                     v
                 Audit Agent
                     |
                     v
                Report Agent
                     |
                     v
                SQLite DB
