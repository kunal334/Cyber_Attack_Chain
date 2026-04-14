from flask import Flask, render_template, request, redirect, send_file, session
import json
import os

from detection.rules import detect_threats
from predictor.attack_chain import predict_next, predict_next_sequence
from graph.graph_builder import build_graph
from response.auto_response import respond
from detection.anomaly import detect_anomalies
from analysis.risk_score import calculate_risk
from report.report_generator import generate_report
from utils.parser import parse_txt_logs

app = Flask(__name__)
app.secret_key = "supersecretkey"   

# HOME ROUTE

@app.route("/")
def index():
    data = session.get("data")

    if data:
        return render_template("index.html", **data)

    # Default empty dashboard
    return render_template("index.html",
        alerts=[],
        predictions=[],
        responses=[],
        graph_data={"nodes": [], "links": []},
        anomalies=[],
        risk_score=0,
        risk_level="LOW",
        next_attack="N/A"
    )


# UPLOAD ROUTE

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file or file.filename == "":
        return "No file selected ❌"

    os.makedirs("data", exist_ok=True)

    filepath = os.path.join("data", file.filename)
    file.save(filepath)

    # PARSE FILE
    try:
        if file.filename.endswith(".txt"):
            logs = parse_txt_logs(filepath)

        elif file.filename.endswith(".json"):
            with open(filepath) as f:
                logs = json.load(f)

        else:
            return "Unsupported file type"

    except Exception as e:
        return f"Parsing error  {str(e)}"

    # PROCESS PIPELINE
    try:
        alerts = detect_threats(logs)
        predictions = predict_next(alerts)
        graph_data = build_graph(alerts)
        responses = respond(alerts)
        anomalies = detect_anomalies(logs)

        risk_score, risk_level = calculate_risk(alerts)
        next_attack = predict_next_sequence(alerts)

    except Exception as e:
        return f"Processing error  {str(e)}"

    # STORE RESULTS IN SESSION (IMPORTANT FIX)
    session["data"] = {
        "alerts": alerts,
        "predictions": predictions,
        "responses": responses,
        "graph_data": graph_data,
        "anomalies": anomalies,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "next_attack": next_attack
    }

    return redirect("/")

# =========================
# REPORT ROUTE
# =========================
@app.route("/report")
def report():
    data = session.get("data")

    if not data:
        return "No data available. Upload logs first ❌"

    file_path = "incident_report.pdf"

    generate_report(
        data["alerts"],
        data["predictions"],
        data["risk_level"]
    )

    return send_file(file_path, as_attachment=True)

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)