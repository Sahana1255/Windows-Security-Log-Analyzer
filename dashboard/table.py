"""
Event Table Module

Displays security events in a professional table.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import pandas as pd
import streamlit as st

from dashboard.severity import get_severity
from dashboard.descriptions import get_description


def show_event_table(events):
    """
    Display recent security events.
    """

    st.subheader("📑 Security Events")

    if not events:

        st.info("No events available.")

        return

    rows = []

    for event in events:

        rows.append({

            "Severity": get_severity(event["event_id"]),

            "Event ID": event["event_id"],

            "Description": get_description(event["event_id"]),

            "Username": event["username"],

            "Computer": event["computer"],

            "Timestamp": event["timestamp"]

        })

    df = pd.DataFrame(rows)

    st.dataframe(

        df,

        width="stretch",

        hide_index=True

    )