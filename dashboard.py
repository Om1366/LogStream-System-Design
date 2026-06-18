import streamlit as st
import pandas as pd

from database import get_logs


st.set_page_config(
    page_title="LogStream Dashboard",
    layout="wide"
)

st.title("📊 LogStream Dashboard")

logs = get_logs()

if len(logs) == 0:
    st.warning("No logs found")
    st.stop()

df = pd.DataFrame(logs)

if "_id" in df.columns:
    df["_id"] = df["_id"].astype(str)

# Metrics

total_logs = len(df)

error_logs = len(df[df["level"] == "ERROR"])

info_logs = len(df[df["level"] == "INFO"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Logs", total_logs)

col2.metric("Error Logs", error_logs)

error_percentage = round(
    (error_logs / total_logs) * 100,
    2
) if total_logs > 0 else 0

col3.metric(
    "Error %",
    f"{error_percentage}%"
)

st.divider()

# Analytics Chart

st.subheader("Log Level Distribution")

level_counts = df["level"].value_counts()

st.bar_chart(level_counts)

st.divider()

# Filter

levels = ["ALL"] + sorted(df["level"].unique().tolist())

selected_level = st.selectbox(
    "Filter by Level",
    levels
)

if selected_level != "ALL":
    df = df[df["level"] == selected_level]

# Search

search_term = st.text_input(
    "Search Message"
)

if search_term:
    df = df[
        df["message"].str.contains(
            search_term,
            case=False,
            na=False
        )
    ]


st.divider()

st.subheader("🕒 Recent Logs")

recent_logs = df.sort_values(
    by="timestamp",
    ascending=False
).head(5)

st.dataframe(
    recent_logs,
    use_container_width=True
)

st.divider()

st.subheader("📈 Top Log Sources")

source_counts = df["source"].value_counts()

st.bar_chart(source_counts)

st.divider()

st.subheader("Logs")

st.dataframe(
    df,
    use_container_width=True
)
