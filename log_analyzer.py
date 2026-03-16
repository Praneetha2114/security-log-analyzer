import pandas as pd


def analyze_logs():

    df = pd.read_csv("sample_logs.csv")

    print("\nSECURITY LOG ANALYSIS\n")

    failed = df[df["status"] == "failed"]

    failed_by_ip = failed.groupby("ip").size()

    incidents = []

    print("ATTACK DETECTION\n")

    for ip, count in failed_by_ip.items():

        if count >= 5:
            severity = "HIGH"

        elif count >= 3:
            severity = "MEDIUM"

        else:
            severity = "LOW"

        if count >= 3:

            print(f"Suspicious activity detected from {ip}")

            incidents.append({
                "IP Address": ip,
                "Failed Attempts": count,
                "Severity": severity
            })

    # suspicious users
    failed_by_user = failed.groupby("user").size()

    for user, count in failed_by_user.items():

        if count >= 3:

            print(f"User under attack: {user}")

            incidents.append({
                "IP Address": "N/A",
                "Failed Attempts": count,
                "Severity": "USER ATTACK"
            })

    # create report
    if incidents:

        report = pd.DataFrame(incidents)

        report.to_excel("security_incident_report.xlsx", index=False)

        print("\nIncident report generated: security_incident_report.xlsx")

    else:

        print("\nNo security incidents detected.")


if __name__ == "__main__":
    analyze_logs()