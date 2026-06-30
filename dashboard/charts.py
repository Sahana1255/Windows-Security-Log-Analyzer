"""
Charts Module

Creates dashboard charts.

Author: Your Name
Project: Windows Security Log Analyzer
"""

from collections import Counter

import pandas as pd
import streamlit as st


def show_event_distribution(events):
    """
    Display Event ID distribution.
    """

    if not events:
        st.info("No events available.")
        return

    counter = Counter(event["event_id"] for event in events)

    chart_data = (
        pd.DataFrame(
            {
                "Event ID": list(counter.keys()),
                "Count": list(counter.values())
            }
        )
        .sort_values("Count", ascending=False)
        .head(10)
        .set_index("Event ID")
    )

    st.subheader("📊 Event ID Distribution")

    st.bar_chart(chart_data)


def show_event_timeline(events):
    """
    Display events over time.
    """

    if not events:
        st.info("No events available.")
        return

    timestamps = []

    for event in events:

        if event["timestamp"]:

            timestamps.append(
                pd.to_datetime(event["timestamp"])
            )

    if not timestamps:
        st.info("No timestamps found.")
        return

    timeline = (
        pd.DataFrame({"Timestamp": timestamps})
        .assign(Count=1)
        .set_index("Timestamp")
        .resample("1h")
        .sum()
    )

    st.subheader("📈 Events Over Time")

    st.line_chart(timeline)