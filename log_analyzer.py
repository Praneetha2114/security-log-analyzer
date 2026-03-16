import pandas as pd


def analyze_logs():

    df = pd.read_csv("sample_logs.csv")

    print("\nSECURITY LOG ANALYSIS\n")

    # total events
    total_events = len(df)
    print("Total log events:", total_events)

    # failed logins
    failed = df[df["status"] == "failed"]
    failed_count = len(failed)

    print("Failed login attempts:", failed_count)

    # group failed attempts by IP
    failed_by_ip = failed.groupby("ip").size()

    print("\nFAILED LOGIN ATTEMPTS BY IP")
    print(failed_by_ip)

    print("\nATTACK DETECTION")

    for ip, count in failed_by_ip.items():

        if count >= 5:
            severity = "HIGH"

        elif count >= 3:
            severity = "MEDIUM"

        else:
            severity = "LOW"

        if count >= 3:

            print(
                f"ALERT: Suspicious activity detected\n"
                f"IP Address: {ip}\n"
                f"Failed Attempts: {count}\n"
                f"Severity Level: {severity}\n"
            )

    # suspicious users
    print("\nSUSPICIOUS USERS")

    failed_by_user = failed.groupby("user").size()

    for user, count in failed_by_user.items():

        if count >= 3:

            print(
                f"User: {user} may be under attack "
                f"({count} failed login attempts)"
            )


if __name__ == "__main__":
    analyze_logs()