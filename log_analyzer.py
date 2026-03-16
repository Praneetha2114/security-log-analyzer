import pandas as pd

def analyze_logs():

    df = pd.read_csv("sample_logs.csv")

    print("\nSecurity Log Analysis\n")

    # total log events
    print("Total log events:", len(df))

    # failed logins
    failed = df[df["status"] == "failed"]
    print("Failed login attempts:", len(failed))

    # group by IP
    failed_by_ip = failed.groupby("ip").size()

    print("\nFailed Login Attempts by IP")

    print(failed_by_ip)

    # detect brute force
    print("\nPossible Brute Force Attacks")

    for ip, count in failed_by_ip.items():

        if count >= 3:

            print(f"ALERT: Suspicious activity from {ip} ({count} failed attempts)")

if __name__ == "__main__":

    analyze_logs()
