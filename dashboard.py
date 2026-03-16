import streamlit as st
import pandas as pd
import requests
import ipaddress

st.title("Security Log Analyzer Dashboard")

# Load logs
df = pd.read_csv("sample_logs.csv")

# -------------------------
# Metrics Section
# -------------------------

st.subheader("Log Summary")

total_logs = len(df)
failed_logs = len(df[df["status"] == "failed"])
success_logs = len(df[df["status"] == "success"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Logs", total_logs)
col2.metric("Failed Logins", failed_logs)
col3.metric("Successful Logins", success_logs)

# -------------------------
# Failed login analysis
# -------------------------

st.subheader("Failed Login Attempts by IP")

failed = df[df["status"] == "failed"]

failed_by_ip = failed.groupby("ip").size().reset_index(name="Attempts")

st.dataframe(failed_by_ip)

st.bar_chart(failed_by_ip.set_index("ip"))

# -------------------------
# Helper functions
# -------------------------

def is_public_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_global
    except:
        return False


def get_location(ip):

    try:

        response = requests.get(f"http://ip-api.com/json/{ip}")

        data = response.json()

        return {
            "ip": ip,
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "country": data.get("country")
        }

    except:
        return None


# -------------------------
# Geo Location Map
# -------------------------

st.subheader("Attack Geo Location Map")

locations = []

for ip in failed_by_ip["ip"]:

    if not is_public_ip(ip):
        continue

    loc = get_location(ip)

    if loc and loc["lat"] is not None:

        locations.append(loc)

if locations:

    map_df = pd.DataFrame(locations)

    st.map(map_df.rename(columns={
        "lat": "latitude",
        "lon": "longitude"
    }))

    st.subheader("Attack Source Locations")

    st.dataframe(map_df)

else:

    st.warning("No public IP location data available.")

# -------------------------
# User Activity
# -------------------------

st.subheader("User Login Activity")

user_activity = df.groupby("user").size().reset_index(name="Log Events")

st.bar_chart(user_activity.set_index("user"))

# -------------------------
# Raw Logs
# -------------------------

st.subheader("Raw Logs")

st.dataframe(df)
