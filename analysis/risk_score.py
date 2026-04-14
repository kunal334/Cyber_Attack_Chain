def calculate_risk(alerts):
    score = 0

    weights = {
        "Reconnaissance": 1,
        "Brute Force Attempt": 3,
        "Privilege Escalation": 5
    }

    for alert in alerts:
        score += weights.get(alert["type"], 0)

    if score < 5:
        level = "LOW"
    elif score < 10:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return score, level