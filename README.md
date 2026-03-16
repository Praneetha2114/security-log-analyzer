Security Log Analyzer

A Python-based cybersecurity project that analyzes authentication logs to detect suspicious activities such as brute-force login attempts and potential attacks.

The tool simulates a Security Operations Center (SOC) monitoring workflow by analyzing logs, detecting threats, generating reports, and visualizing attack patterns.

Project Overview

This project demonstrates how security analysts can automate log monitoring and incident detection using Python.

The system performs the following tasks:

Log analysis for authentication events

Detection of suspicious login attempts

Brute-force attack identification

Threat intelligence correlation

Security incident report generation

Real-time monitoring of log activity

Visualization of attack data through a dashboard

Geographic mapping of attack sources

Key Features
Log Analysis

The system reads authentication logs stored in:

sample_logs.csv

Each log entry contains the following fields:

Field	Description
timestamp	Time of login attempt
user	Username attempting authentication
ip	Source IP address
status	Login result (success / failed)

Example:

timestamp	user	ip	status
2026-03-16 10:00	admin	8.8.8.8	failed
Brute Force Detection

The analyzer groups failed login attempts by IP address.

Severity levels are determined using the following logic:

Attempts	Severity
1–2	Low
3–4	Medium
5+	High

Example output:

Suspicious IP Detected
IP Address: 8.8.8.8
Failed Attempts: 3
Severity: MEDIUM
Threat Intelligence Correlation

Suspicious IP addresses are checked against a threat intelligence database.

File used:

threat_intel.csv

Example dataset:

ip	threat_level
192.168.1.10	High
10.0.0.5	Medium

If an IP appears in the threat database, its risk level is included in the incident report.

Security Incident Report

Detected incidents are exported to an Excel report.

Generated file:

security_incident_report.xlsx

Example report:

IP Address	Failed Attempts	Severity	Threat Level
8.8.8.8	3	Medium	High
Real-Time Log Monitoring

The system includes a real-time monitoring module.

Script used:

realtime_monitor.py

This continuously monitors logs and prints alerts when suspicious activity is detected.

Example alert:

FAILED LOGIN DETECTED
User: admin
IP: 8.8.8.8
Time: 2026-03-16 10:01
Security Dashboard

The project includes a visualization dashboard built with Streamlit.

Run the dashboard using:

streamlit run dashboard.py

The dashboard displays:

Security metrics

Failed login statistics

Suspicious IP activity

User login analysis

Raw log data

Attack Geo-Location Map

The dashboard visualizes attack sources on a world map.

Severity levels are represented using colors:

Color	Severity
Yellow	Low
Orange	Medium
Red	High

This helps analysts identify geographic attack patterns.

Project Structure
security-log-analyzer
│
├── log_analyzer.py
├── realtime_monitor.py
├── dashboard.py
├── threat_intel.csv
├── sample_logs.csv
├── security_incident_report.xlsx
└── README.md
Installation

Clone the repository:

git clone https://github.com/yourusername/security-log-analyzer.git

Navigate to the project folder:

cd security-log-analyzer

Install required dependencies:

pip install pandas streamlit requests pydeck openpyxl
Usage

Run the log analyzer:

python log_analyzer.py

Run the real-time monitoring script:

python realtime_monitor.py

Launch the dashboard:

streamlit run dashboard.py
Example Use Cases

This project demonstrates concepts used in:

Security Operations Centers (SOC)

SIEM log analysis

Brute-force attack detection

Threat intelligence analysis

Security monitoring dashboards

Technologies Used
Technology	Purpose
Python	Core programming
Pandas	Log analysis
Streamlit	Dashboard
PyDeck	Map visualization
Requests	IP geolocation
OpenPyXL	Excel report generation
Author

Praneetha

GitHub:
https://github.com/Praneetha2114

License

This project is created for educational and portfolio purposes.
