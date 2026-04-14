from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(alerts, predictions, risk_level):
    doc = SimpleDocTemplate("incident_report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Cybersecurity Incident Report", styles["Title"]))
    content.append(Paragraph(f"Risk Level: {risk_level}", styles["Normal"]))

    for alert in alerts:
        content.append(Paragraph(f"{alert['ip']} - {alert['type']}", styles["Normal"]))

    doc.build(content)