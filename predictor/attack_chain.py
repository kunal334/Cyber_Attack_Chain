attack_map = {
    "Reconnaissance": "Brute Force Attempt",
    "Brute Force Attempt": "Privilege Escalation",
    "Privilege Escalation": "Data Exfiltration"
}

def predict_next(alerts):
    predictions = []

    for alert in alerts:
        current = alert["type"]
        next_step = attack_map.get(current, "Unknown")

        predictions.append({
            "ip": alert["ip"],
            "current": current,
            "predicted_next": next_step
        })

    return predictions
def predict_next_sequence(alerts):
    sequence = [a["type"] for a in alerts]

    if "Reconnaissance" in sequence and "Brute Force Attempt" not in sequence:
        return "Brute Force Attempt"

    if "Brute Force Attempt" in sequence and "Privilege Escalation" not in sequence:
        return "Privilege Escalation"

    if "Privilege Escalation" in sequence:
        return "Data Exfiltration"

    return "Unknown"