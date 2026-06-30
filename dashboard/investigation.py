"""
Investigation Module

Displays detailed information about a selected event.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st

from dashboard.severity import get_severity
from dashboard.descriptions import get_description


def show_event_details(events):
    """
    Display detailed information for a selected event.
    """

    if not events:
        return

    st.subheader("🔍 Event Investigation")

    options = [

        f"{event['timestamp']} | Event {event['event_id']} | {event['username']}"

        for event in events

    ]

    selected = st.selectbox(

        "Select an Event",

        range(len(options)),

        format_func=lambda i: options[i]

    )

    event = events[selected]

    left, right = st.columns(2)

    with left:

        st.markdown("### 📋 General Information")

        st.write(f"**Timestamp:** {event['timestamp']}")

        st.write(f"**Event ID:** {event['event_id']}")

        st.write(
            f"**Severity:** {get_severity(event['event_id'])}"
        )

        st.write(
            f"**Description:** {get_description(event['event_id'])}"
        )

    with right:

        st.markdown("### 👤 System Information")

        st.write(f"**Username:** {event['username']}")

        st.write(f"**Computer:** {event['computer']}")

    st.markdown("---")

    with st.expander("📄 View Raw XML", expanded=False):

        st.code(

            event["raw_xml"],

            language="xml"

        )