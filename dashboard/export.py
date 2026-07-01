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
    Display CSV export button.

    Parameters
    ----------
    events : list
        Filtered security events.
    """

    st.subheader("📥 Export Investigation")

    st.caption(
        "Download the filtered investigation results as a CSV report."
    )

    if not events:

        st.info("No security events available for export.")

        return

    # ---------------------------------------------------
    # Prepare CSV
    # ---------------------------------------------------

    with st.spinner(
        "📥 Preparing investigation CSV report..."
    ):

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

        csv = df.to_csv(index=False)

    st.success(
        "✅ CSV report is ready for download."
    )

    # ---------------------------------------------------
    # Download Button
    # ---------------------------------------------------

    st.download_button(

        label="⬇ Download Investigation CSV",

        data=csv,

        file_name="investigation_report.csv",

        mime="text/csv",

        use_container_width=True

    )