import streamlit as st
import pandas as pd
import requests
import ipaddress
import pydeck as pdk

st.title("Security Log Analyzer Dashboard")

df = pd.read_csv("sample_logs.csv")

# --------------------------
# Metrics
# --------------------------

st.subheader("Log Summary")

total_logs = len(df)
failed_logs = len(df[df["status"] == "failed"])
success_logs = len(df[df["status"] == "success"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Logs", total_logs)
col2.metric("Failed Logins", failed_logs)
col3.metric("Successful Logins", success_logs)

# --------------------------
# Failed Login Analysis
# --------------------------

st.subheader("Failed Login Attempts by IP")

failed = df[df["status"] == "failed"]

failed_by_ip = failed.groupby("ip").size().reset_index(name="Attempts")

st.dataframe(failed_by_ip)

st.bar_chart(failed_by_ip.set_index("ip"))

# --------------------------
# Helper Functions
# --------------------------

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


def get_severity_color(attempts):

    if attempts >= 5:
        return [255, 0, 0]      # red

    elif attempts >= 3:
        return [255, 140, 0]    # orange

    else:
        return [255, 215, 0]    # yellow


# --------------------------
# Attack Map
# --------------------------

st.subheader("Attack Geo Location Map")

locations = []

for _, row in failed_by_ip.iterrows():

    ip = row["ip"]
    attempts = row["Attempts"]

    if not is_public_ip(ip):
        continue

    loc = get_location(ip)

    if loc and loc["lat"] is not None:

        locations.append({
            "ip": ip,
            "latitude": loc["lat"],
            "longitude": loc["lon"],
            "attempts": attempts,
            "color": get_severity_color(attempts)
        })

if locations:

    map_df = pd.DataFrame(locations)

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_df,
        get_position="[longitude, latitude]",
        get_fill_color="color",
        get_radius=200000,
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=20,
        longitude=0,
        zoom=1
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "IP: {ip}\nAttempts: {attempts}"}
    )

    st.pydeck_chart(deck)

    st.subheader("Attack Sources")

    st.dataframe(map_df)

else:

    st.warning("No public attack IPs detected.")

# --------------------------
# User Activity
# --------------------------

st.subheader("User Login Activity")

user_activity = df.groupby("user").size().reset_index(name="Log Events")

st.bar_chart(user_activity.set_index("user"))

# --------------------------
# Raw Logs
# --------------------------

st.subheader("Raw Logs")

st.dataframe(df)
