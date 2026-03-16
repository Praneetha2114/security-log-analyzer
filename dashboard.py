import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

st.title("Security Log Analyzer Dashboard")

df = pd.read_csv("sample_logs.csv")

# Basic metrics
st.subheader("Log Summary")

total_logs = len(df)
failed_logs = len(df[df["status"] == "failed"])
success_logs = len(df[df["status"] == "success"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Logs", total_logs)
col2.metric("Failed Logins", failed_logs)
col3.metric("Successful Logins", success_logs)

# Failed login analysis
st.subheader("Failed Login Attempts by IP")

failed = df[df["status"] == "failed"]
failed_by_ip = failed.groupby("ip").size().reset_index(name="Attempts")

st.dataframe(failed_by_ip)

st.bar_chart(failed_by_ip.set_index("ip"))

# Geo location section
st.subheader("Attack Geo Location Map")

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


locations = []

for ip in failed_by_ip["ip"]:
    loc = get_location(ip)

    if loc and loc["lat"] is not None:
        locations.append(loc)

if locations:

    map_df = pd.DataFrame(locations)

    st.map(map_df.rename(columns={"lat":"latitude","lon":"longitude"}))

    st.write(map_df)

else:

    st.write("No location data available.")

# Raw logs
st.subheader("Raw Logs")

st.dataframe(df)