from datetime import datetime

incident = input("Incident Name: ")

report = f"""
Incident Report
===============

Incident: {incident}
Date: {datetime.now()}
Status: Open
"""

with open("incident_report.txt", "w", encoding="utf-8") as file:
file.write(report)

print("Incident report generated successfully.")
