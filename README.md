Security Log Analyzer

A Python-based security monitoring tool that analyzes authentication logs to detect suspicious activities such as brute-force login attempts and potential attacks.

The tool simulates a Security Operations Center (SOC) monitoring workflow by analyzing logs, detecting threats, generating reports, and visualizing attack patterns.

Project Features
1. Log Analysis

The system reads authentication logs stored in:

sample_logs.csv

Each log entry contains the following fields:

timestamp

user

ip

status

Example log entry:

timestamp	user	ip	status
2026-03-16 10:00	admin	8.8.8.8	failed
2. Brute Force Detection

The analyzer groups failed login attempts by IP address.

Attack severity is determined based on the number of failed attempts.

Attempts	Severity
1–2	Low
3–4	Medium
5+	High

If an IP exceeds the threshold, the system generates a security alert.

Example output:

Suspicious IP Detected
IP Address: 8.8.8.8
Failed Attempts: 3
Severity: MEDIUM
3. Threat Intelligence Correlation

The system compares suspicious IP addresses with a threat intelligence database.

File used:

threat_intel.csv

Example dataset:

ip	threat_level
192.168.1.10	High
10.0.0.5	Medium

If a match is found, the threat level is included in the incident report.

4. Security Incident Report

Detected incidents are exported into an Excel report.

Generated file:

security_incident_report.xlsx

Example report:

IP Address	Failed Attempts	Severity	Threat Level
8.8.8.8	3	Medium	High

This simulates incident reporting used in security monitoring environments.

5. Real-Time Log Monitoring

The tool includes a real-time monitoring module.

Script used:

realtime_monitor.py

This continuously monitors logs and prints alerts when suspicious activity appears.

Example alert:

FAILED LOGIN DETECTED
User: admin
IP: 8.8.8.8
Time: 2026-03-16 10:01
6. Security Dashboard

The project includes a visualization dashboard built with Streamlit.

Run the dashboard using:

streamlit run dashboard.py

The dashboard displays:

security metrics

failed login statistics

suspicious IP activity

user login analysis

raw log data

7. Attack Geo-Location Map

The dashboard also visualizes attack sources on a world map.

IP addresses are converted into geographic coordinates.

Severity levels are represented by colors:

Color	Severity
Yellow	Low
Orange	Medium
Red	High

This helps analysts identify geographic attack patterns.

Technologies Used

The project uses the following technologies:

Python

Pandas

Streamlit

PyDeck

Requests

OpenPyXL

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
1. Clone the Repository
git clone https://github.com/yourusername/security-log-analyzer.git
2. Navigate to the Project Folder
cd security-log-analyzer
3. Install Dependencies
pip install pandas streamlit requests pydeck openpyxl
How to Use the Tool
Step 1 — Analyze Security Logs

Run the log analyzer script:

python log_analyzer.py

This detects suspicious login attempts and generates an incident report.

Step 2 — Start Real-Time Monitoring

Run:

python realtime_monitor.py

The system will continuously monitor logs and display alerts.

Step 3 — Launch the Dashboard

Run:

streamlit run dashboard.py

Upload or load the log data to visualize attack activity.

Example Use Cases

This project demonstrates concepts used in:

Security Operations Centers (SOC)

SIEM log analysis

Brute-force attack detection

Threat intelligence correlation

Security analytics dashboards

Author

Praneetha

GitHub Profile
https://github.com/Praneetha2114

License

This project is created for educational and portfolio purposes.
