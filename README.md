# Intelligent Attack Analysis & Prediction System

>  A real-time cybersecurity dashboard that detects threats, predicts attack chains, visualizes attack graphs, and generates automated responses.

---

##  Overview

This project is an advanced **cybersecurity analytics platform** designed to:

-  Analyze uploaded log files (.txt / .json)
-  Detect malicious activities
-  Identify anomalies
-  Predict next possible attack steps
-  Visualize attack chains using graphs
-  Trigger automated responses
-  Calculate risk score & severity
-  Generate downloadable incident reports

---

##  Key Features

### Threat Detection
- Rule-based detection for:
  - Port Scanning
  - Brute Force Attacks
  - Privilege Escalation

### Anomaly Detection
- Identifies suspicious patterns in logs

###  Attack Chain Prediction
- Predicts next attacker move based on behavior sequence

###  Graph Visualization
- Interactive attack graph using D3.js
- Shows relationship between IPs and attack stages

### Auto Response System
- Suggests actions like:
  - IP Blocking
  - Alert escalation

###  Risk Scoring Engine
- Calculates:
  - Risk Score (numeric)
  - Risk Level (Low / Medium / High)

### Report Generation
- Generates downloadable **PDF incident reports**

### File Upload Support
- Accepts:
  - `.txt` logs
  - `.json` logs



---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt

python app.py

Input Format

TXT File Example
192.168.1.10,port_scan
192.168.1.10,failed_login
192.168.1.20,privilege_escalation


JSON Format
[
  {"ip": "192.168.1.10", "event": "port_scan"},
  {"ip": "192.168.1.20", "event": "failed_login"}
]
