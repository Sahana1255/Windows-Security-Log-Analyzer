"""
Windows Security Log Analyzer
Main Dashboard

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st

from parser.evtx_parser import read_evtx
from parser.xml_extractor import extract_events

from dashboard.statistics import get_statistics
from dashboard.sidebar import create_sidebar
from dashboard.uploader import save_uploaded_file
from dashboard.charts import (
    show_event_distribution,
    show_event_timeline
)


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Windows Security Log Analyzer",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

uploaded_file, max_events, analyze = create_sidebar()

# ---------------------------------------------------
# Default Values
# ---------------------------------------------------

structured_events = []

stats = {
    "total_events": 0,
    "successful_logins": 0,
    "failed_logins": 0,
    "account_creations": 0,
    "privilege_escalations": 0
}

# ---------------------------------------------------
# Load EVTX File
# ---------------------------------------------------

if max_events == "All":
    max_events = None

# Default file
file_path = "data/sample_logs/Security.evtx"

# ---------------------------------------------------
# Analyze Uploaded or Sample Log
# ---------------------------------------------------

if analyze:

    # Save uploaded file only when Analyze is clicked
    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)

    with st.spinner("Analyzing Windows Security Log..."):

        xml_events = read_evtx(
            file_path,
            max_events=max_events
        )

        structured_events = extract_events(xml_events)

        stats = get_statistics(structured_events)

    st.success("Analysis Complete")

# ---------------------------------------------------
# First Page Load
# ---------------------------------------------------

else:

    xml_events = read_evtx(
        file_path,
        max_events=max_events
    )

    structured_events = extract_events(xml_events)

    stats = get_statistics(structured_events)

# ---------------------------------------------------
# Dashboard Header
# ---------------------------------------------------

st.title("🛡️ Windows Security Log Analyzer")

st.caption(
    "Python-based Windows Security Event Monitoring Dashboard"
)

st.divider()

# ---------------------------------------------------
# Statistics Cards
# ---------------------------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Events", stats["total_events"])

with col2:
    st.metric("Successful Logins", stats["successful_logins"])

with col3:
    st.metric("Failed Logins", stats["failed_logins"])

with col4:
    st.metric("Account Creations", stats["account_creations"])

with col5:
    st.metric("Privilege Escalations", stats["privilege_escalations"])

# ---------------------------------------------------
# Charts
# ---------------------------------------------------

st.divider()

left, right = st.columns(2)

with left:
    show_event_distribution(structured_events)

with right:
    show_event_timeline(structured_events)

st.divider()

# ---------------------------------------------------
# Recent Security Events
# ---------------------------------------------------

st.subheader("Recent Security Events")

if structured_events:

    preview = []

    for event in structured_events[:10]:

        preview.append({

            "Timestamp": event["timestamp"],
            "Event ID": event["event_id"],
            "Username": event["username"],
            "Computer": event["computer"]

        })

    st.dataframe(
        preview,
        width="stretch"
    )

else:

    st.info("No events found.")