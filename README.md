# Security Log Analyzer

A Python-based cybersecurity project that analyzes authentication logs to detect suspicious login attempts and potential brute-force attacks.

---

## Project Overview

This project simulates a **Security Operations Center (SOC)** monitoring workflow.

### Main capabilities:

- **Log analysis**
- **Suspicious login detection**
- **Brute-force attack detection**
- **Threat intelligence correlation**
- **Incident report generation**
- **Real-time monitoring**
- **Security dashboard visualization**
- **Geographic attack mapping**

---

## Log Analysis

Authentication logs are stored in: **sample_logs.csv**

### Example structure:

| timestamp | user | ip | status |
|-----------|------|----|----|
| 2026-03-16 10:00 | admin | 8.8.8.8 | failed |

---

## Brute Force Detection

Failed login attempts are grouped by **IP address**.

| Attempts | Severity |
|----------|----------|
| 1–2 | Low |
| 3–4 | Medium |
| 5+ | High |

### Example detection output:

```
Suspicious IP Detected
IP Address: 8.8.8.8
Failed Attempts: 3
Severity: MEDIUM
```

---

## Threat Intelligence

Suspicious IPs are checked against a **threat intelligence dataset**.

File: **threat_intel.csv**

### Example dataset:

| ip | threat_level |
|----|--------------|
| 192.168.1.10 | High |
| 10.0.0.5 | Medium |

---

## Security Incident Report

Detected incidents are exported to: **security_incident_report.xlsx**

### Example report:

| IP Address | Failed Attempts | Severity | Threat Level |
|-----------|-----------------|----------|--------------|
| 8.8.8.8 | 3 | Medium | High |

---

## Real-Time Monitoring

The system includes a monitoring script: **realtime_monitor.py**

### Example alert:

```
FAILED LOGIN DETECTED
User: admin
IP: 8.8.8.8
Time: 2026-03-16 10:01
```

---

## Security Dashboard

Launch the dashboard with:

```bash
streamlit run dashboard.py
```

### The dashboard shows:

- **Security metrics**
- **Failed login statistics**
- **Suspicious IP activity**
- **User activity analysis**
- **Attack geo-location map**

---

## Project Structure

```
security-log-analyzer
│
├── log_analyzer.py
├── realtime_monitor.py
├── dashboard.py
├── threat_intel.csv
├── sample_logs.csv
├── security_incident_report.xlsx
└── README.md
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Praneetha2114/security-log-analyzer.git
   ```

2. **Navigate to the project folder**
   ```bash
   cd security-log-analyzer
   ```

3. **Install dependencies**
   ```bash
   pip install pandas streamlit requests pydeck openpyxl
   ```

---

## Usage

- **Run log analysis**
  ```bash
  python log_analyzer.py
  ```

- **Run real-time monitoring**
  ```bash
  python realtime_monitor.py
  ```

- **Launch dashboard**
  ```bash
  streamlit run dashboard.py
  ```

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming |
| **Pandas** | Log analysis |
| **Streamlit** | Dashboard |
| **PyDeck** | Geo visualization |
| **Requests** | IP lookup |
| **OpenPyXL** | Excel reporting |

---

## Author

**Praneetha**

- **GitHub:** https://github.com/Praneetha2114