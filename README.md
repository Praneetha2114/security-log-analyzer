Security Log Analyzer

A Python-based security monitoring tool that analyzes authentication logs to detect suspicious activities such as brute-force login attempts and potential attacks.

The project demonstrates how security teams can analyze logs, generate incident reports, and visualize attack patterns using dashboards.

Project Overview

This project simulates a Security Operations Center (SOC) monitoring workflow.

It performs the following tasks:

Log analysis

Suspicious login detection

Brute-force attack detection

Threat intelligence correlation

Security incident report generation

Real-time log monitoring

Attack visualization dashboard

Geographic attack source mapping

Key Features
Log Analysis

The system reads authentication logs from:

sample_logs.csv

Each log entry contains:

Field	Description
timestamp	Time of login event
user	Username attempting login
ip	Source IP address
status	Login result (success / failed)

Example log entry:

timestamp	user	ip	status
2026-03-16 10:00	admin	8.8.8.8	failed
Brute Force Detection

The analyzer detects suspicious login attempts by grouping failed logins by IP address.

Severity is determined based on number of attempts:

Attempts	Severity
1–2	Low
3–4	Medium
5+	High
Threat Intelligence Correlation

The system checks IP addresses against a threat intelligence dataset.

File used:

threat_intel.csv

Example:

ip	threat_level
192.168.1.10	High
10.0.0.5	Medium

If a suspicious IP matches the database, the incident severity increases.

Security Incident Report

Detected incidents are exported to an Excel report:

security_incident_report.xlsx

Example report:

IP Address	Failed Attempts	Severity	Threat Level
8.8.8.8	3	Medium	High

This simulates incident reporting used by SOC teams.

Real-Time Log Monitoring

The tool includes a real-time monitoring script:

realtime_monitor.py

This continuously checks for new login events and prints alerts for suspicious activity.

Example alert:

FAILED LOGIN DETECTED
User: admin
IP: 8.8.8.8
Time: 2026-03-16 10:01
Security Dashboard

The project includes a visualization dashboard built with Streamlit.

Run using:

streamlit run dashboard.py

The dashboard provides:

Security metrics

Login activity analysis

Failed login charts

User activity charts

Attack source tables

Raw log viewing

Attack Geo-Location Map

The dashboard visualizes attack sources on a world map.

Each attack is represented with severity-based colors:

Color	Meaning
Yellow	Low severity
Orange	Medium severity
Red	High severity

This allows analysts to identify geographic attack patterns.

Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Data analysis
Streamlit	Dashboard visualization
PyDeck	Map visualization
OpenPyXL	Excel report generation
Requests	IP geolocation lookup
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

Navigate to the project directory:

cd security-log-analyzer

Install dependencies:

pip install pandas streamlit requests pydeck openpyxl
How to Run
Run Log Analysis
python log_analyzer.py
Run Real-Time Monitoring
python realtime_monitor.py
Launch Dashboard
streamlit run dashboard.py
Example Use Cases

This project demonstrates concepts used in:

Security Operations Centers (SOC)

SIEM log analysis

Incident detection

Threat intelligence correlation

Security analytics dashboards

Author

Praneetha

GitHub Profile:
https://github.com/Praneetha2114

License

This project is created for educational and portfolio purposes.
