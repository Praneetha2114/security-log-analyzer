Security Log Analyzer

A Python-based cybersecurity project that analyzes authentication logs to detect suspicious activities such as brute-force login attempts and potential attacks.

The project simulates basic Security Operations Center (SOC) monitoring by analyzing logs, generating incident reports, and visualizing attack patterns.

Project Overview

This tool demonstrates how security teams can automate log monitoring and incident detection.

The system performs the following tasks:

Authentication log analysis

Detection of suspicious login attempts

Brute-force attack identification

Threat intelligence correlation

Security incident report generation

Real-time monitoring of login activity

Attack visualization using dashboards

Geographic mapping of attack sources

Key Features
Log Analysis

Authentication logs are stored in:

sample_logs.csv

Each log entry contains:

Field	Description
timestamp	Time of login attempt
user	Username attempting login
ip	Source IP address
status	Login result

Example:

timestamp	user	ip	status
2026-03-16 10:00	admin	8.8.8.8	failed
Brute Force Detection

The analyzer groups failed login attempts by IP address.

Severity is determined based on the number of attempts.

Attempts	Severity
1–2	Low
3–4	Medium
5+	High

Example detection output:

Suspicious IP Detected
IP Address: 8.8.8.8
Failed Attempts: 3
Severity: MEDIUM
Threat Intelligence Correlation

Suspicious IPs are compared with a threat intelligence database.

File used:

threat_intel.csv

Example dataset:

ip	threat_level
192.168.1.10	High
10.0.0.5	Medium

Matching IPs are flagged as higher risk.

Security Incident Report

Detected incidents are exported to an Excel report.

Generated file:

security_incident_report.xlsx

Example report:

IP Address	Failed Attempts	Severity	Threat Level
8.8.8.8	3	Medium	High
Real-Time Log Monitoring

The tool includes a real-time monitoring script.

realtime_monitor.py

This continuously scans log updates and prints alerts when suspicious activity occurs.

Example alert:

FAILED LOGIN DETECTED
User: admin
IP: 8.8.8.8
Time: 2026-03-16 10:01
Security Dashboard

The project includes a Streamlit-based dashboard.

Run:

streamlit run dashboard.py

The dashboard displays:

Security metrics

Failed login statistics

Suspicious IP activity

User login analysis

Raw log data

Attack Geo-Location Map

The dashboard visualizes attack sources on a world map.

Severity levels are represented by colors:

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

git clone https://github.com/Praneetha2114/security-log-analyzer.git

Navigate to the project folder:

cd security-log-analyzer

Install dependencies:

pip install pandas streamlit requests pydeck openpyxl
Usage

Run log analysis:

python log_analyzer.py

Run real-time monitoring:

python realtime_monitor.py

Launch dashboard:

streamlit run dashboard.py
Technologies Used
Technology	Purpose
Python	Core programming
Pandas	Data analysis
Streamlit	Dashboard
PyDeck	Map visualization
Requests	IP geolocation
OpenPyXL	Excel reporting
Author

Praneetha

GitHub
https://github.com/Praneetha2114

License

Educational and portfolio project.
