from sklearn.ensemble import IsolationForest
import numpy as np

# Convert logs to numeric features
def extract_features(logs):
    features = []

    event_map = {
        "port_scan": 1,
        "failed_login": 2,
        "login_success": 3,
        "privilege_escalation": 4
    }

    for log in logs:
        features.append([event_map.get(log["event"], 0)])

    return np.array(features)

def detect_anomalies(logs):
    X = extract_features(logs)

    model = IsolationForest(contamination=0.3)
    model.fit(X)

    preds = model.predict(X)

    anomalies = []
    for i, p in enumerate(preds):
        if p == -1:
            anomalies.append(logs[i])

    return anomalies