import pandas as pd
import time

def monitor_logs():

    print("Starting Real-Time Security Log Monitoring...\n")

    processed = 0

    while True:

        df = pd.read_csv("sample_logs.csv")

        new_logs = df.iloc[processed:]

        for index, row in new_logs.iterrows():

            if row["status"] == "failed":

                print(
                    f"FAILED LOGIN DETECTED | "
                    f"User: {row['user']} | "
                    f"IP: {row['ip']} | "
                    f"Time: {row['timestamp']}"
                )

        processed = len(df)

        time.sleep(5)


if __name__ == "__main__":
    monitor_logs()
