def detect_threats(logs):
    alerts = []

    for log in logs:
        if log["event"] == "port_scan":
            alerts.append({"ip": log["ip"], "type": "Reconnaissance"})

        elif log["event"] == "failed_login":
            alerts.append({"ip": log["ip"], "type": "Brute Force Attempt"})

        elif log["event"] == "privilege_escalation":
            alerts.append({"ip": log["ip"], "type": "Privilege Escalation"})

    return alerts