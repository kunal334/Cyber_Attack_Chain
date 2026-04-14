def respond(alerts):
    actions = []

    for alert in alerts:
        if alert["type"] == "Privilege Escalation":
            actions.append(f"BLOCK IP: {alert['ip']}")

    return actions