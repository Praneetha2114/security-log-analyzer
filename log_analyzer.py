import pandas as pd


def analyze_logs():

    df = pd.read_csv("sample_logs.csv")
    threat_db = pd.read_csv("threat_intel.csv")

    print("\nSECURITY LOG ANALYSIS\n")

    failed = df[df["status"] == "failed"]

    failed_by_ip = failed.groupby("ip").size()

    incidents = []

    for ip, count in failed_by_ip.items():

        if count >= 5:
            severity = "HIGH"

        elif count >= 3:
            severity = "MEDIUM"

        else:
            severity = "LOW"

        if count >= 3:

            threat_match = threat_db[threat_db["ip"] == ip]

            threat_level = "Unknown"

            if not threat_match.empty:
                threat_level = threat_match.iloc[0]["threat_level"]

            print(
                f"\nSuspicious IP Detected\n"
                f"IP Address: {ip}\n"
                f"Failed Attempts: {count}\n"
                f"Severity: {severity}\n"
                f"Threat Intelligence: {threat_level}"
            )

            incidents.append({
                "IP Address": ip,
                "Failed Attempts": count,
                "Severity": severity,
                "Threat Level": threat_level
            })

    if incidents:

        report = pd.DataFrame(incidents)

        report.to_excel("security_incident_report.xlsx", index=False)

        print("\nSecurity incident report generated.")

    else:

        print("No incidents detected.")


if __name__ == "__main__":
    analyze_logs()
