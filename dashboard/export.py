"""
Export Module

Exports filtered investigation results.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import pandas as pd
import streamlit as st

from dashboard.severity import get_severity


def show_export(events):
    """
    CSV Export Button.
    """

    if not events:

        return

    rows = []

    for event in events:

        rows.append({

            "Timestamp": event["timestamp"],
            "Event ID": event["event_id"],
            "Severity": get_severity(
                event["event_id"]
            ),
            "Username": event["username"],
            "Computer": event["computer"]

        })

    df = pd.DataFrame(rows)

    st.download_button(

        "⬇ Download Investigation CSV",

        data=df.to_csv(index=False),

        file_name="investigation_report.csv",

        mime="text/csv"
    )