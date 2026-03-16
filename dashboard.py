import streamlit as st
import pandas as pd

st.title("Security Log Analyzer Dashboard")

df = pd.read_csv("sample_logs.csv")

st.subheader("Log Summary")

total_logs = len(df)
failed_logs = len(df[df["status"] == "failed"])
successful_logs = len(df[df["status"] == "success"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Logs", total_logs)
col2.metric("Failed Logins", failed_logs)
col3.metric("Successful Logins", successful_logs)

st.subheader("Failed Login Attempts by IP")

failed = df[df["status"] == "failed"]
failed_by_ip = failed.groupby("ip").size().reset_index(name="Attempts")

st.dataframe(failed_by_ip)

st.bar_chart(failed_by_ip.set_index("ip"))

st.subheader("User Login Activity")

user_activity = df.groupby("user").size().reset_index(name="Log Events")

st.bar_chart(user_activity.set_index("user"))

st.subheader("Raw Logs")

st.dataframe(df)
