"""
Windows Security Log Analyzer
Main Dashboard

Author: Your Name
Project: Windows Security Log Analyzer
"""

from datetime import datetime

import streamlit as st

from parser.evtx_parser import read_evtx
from parser.xml_extractor import extract_events

from dashboard.statistics import get_statistics
from dashboard.sidebar import create_sidebar
from dashboard.uploader import save_uploaded_file
from dashboard.theme import load_theme

from dashboard.filters import filter_events
from dashboard.search import search_events

from dashboard.cards import show_kpi_cards
from dashboard.charts import (
    show_event_distribution,
    show_event_timeline
)
from dashboard.alerts import show_alerts
from dashboard.summary import show_summary
from dashboard.table import show_event_table
from dashboard.investigation import show_event_details

from dashboard.export import show_export
from dashboard.pdf_button import show_pdf_button

from dashboard.about import show_about
from dashboard.footer import show_footer


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Windows Security Log Analyzer",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------
# Load Theme
# ---------------------------------------------------

load_theme()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

uploaded_file, max_events, analyze = create_sidebar()

# ---------------------------------------------------
# Default Values
# ---------------------------------------------------

structured_events = []
stats = {}

if max_events == "All":
    max_events = None

file_path = "data/sample_logs/Security.evtx"

# ---------------------------------------------------
# Load Uploaded File
# ---------------------------------------------------

if analyze and uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)

# ---------------------------------------------------
# Read EVTX
# ---------------------------------------------------

# ---------------------------------------------------
# Read EVTX
# ---------------------------------------------------

if analyze:

    with st.spinner(
        "🔍 Parsing EVTX file and analyzing security events..."
    ):

        xml_events = read_evtx(
            file_path,
            max_events=max_events
        )

        with st.spinner(
            "📊 Loading dashboard and calculating statistics..."
        ):

            structured_events = extract_events(xml_events)

            structured_events = search_events(
                filter_events(structured_events)
            )

            stats = get_statistics(structured_events)

    st.success("✅ Analysis Complete")

else:

    xml_events = read_evtx(
        file_path,
        max_events=max_events
    )

    structured_events = extract_events(xml_events)

    structured_events = search_events(
        filter_events(structured_events)
    )

    stats = get_statistics(structured_events)

# ---------------------------------------------------
# Dashboard Header
# ---------------------------------------------------

st.title("🛡 Windows Security Log Analyzer")

st.caption(
    f"SOC Investigation Dashboard • "
    f"Last Analysis: "
    f"{datetime.now():%d %B %Y %H:%M:%S}"
)

st.divider()

# ---------------------------------------------------
# Security Overview
# ---------------------------------------------------

show_kpi_cards(stats)

# ---------------------------------------------------
# Alerts
# ---------------------------------------------------

st.divider()

show_alerts(
    stats,
    structured_events
)

# ---------------------------------------------------
# Investigation Summary
# ---------------------------------------------------

show_summary(
    structured_events,
    stats
)

# ---------------------------------------------------
# Charts
# ---------------------------------------------------

st.divider()

st.subheader("📈 Security Analytics")

col1, col2 = st.columns(2)

with col1:
    show_event_distribution(structured_events)

with col2:
    show_event_timeline(structured_events)

# ---------------------------------------------------
# Security Events
# ---------------------------------------------------

st.divider()

show_event_table(structured_events)

# ---------------------------------------------------
# Investigation Panel
# ---------------------------------------------------

st.divider()

with st.spinner(
    "📑 Loading investigation details..."
):
    show_event_details(structured_events)
# ---------------------------------------------------
# Reports
# ---------------------------------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:
    show_export(structured_events)

with col2:
    show_pdf_button(
        stats,
        structured_events
    )

# ---------------------------------------------------
# About
# ---------------------------------------------------

st.divider()

show_about()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

show_footer()