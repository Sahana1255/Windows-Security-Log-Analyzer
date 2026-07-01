"""
IOC Summary Module

Displays an investigation summary.

Author: Your Name
Project: Windows Security Log Analyzer
"""

from collections import Counter

import streamlit as st

from dashboard.severity import get_severity


def show_summary(events, stats):
    """
    Display IOC investigation summary.

    Parameters
    ----------
    events : list
        Filtered security events.

    stats : dict
        Dashboard statistics.
    """

    st.subheader("📋 Investigation Summary")

    if not events:

        st.info("No events available.")

        return

    with st.spinner(
        "🧠 Generating investigation summary..."
    ):

        # ---------------------------------------------------
        # Most Common Event
        # ---------------------------------------------------

        event_counter = Counter(
            event["event_id"]
            for event in events
        )

        common_event = event_counter.most_common(1)[0][0]

        # ---------------------------------------------------
        # Most Active User
        # ---------------------------------------------------

        usernames = [
            event["username"]
            for event in events
            if event["username"]
        ]

        if usernames:

            top_user = Counter(
                usernames
            ).most_common(1)[0][0]

        else:

            top_user = "N/A"

        # ---------------------------------------------------
        # Overall Risk
        # ---------------------------------------------------

        risk = get_severity(common_event)

    # ---------------------------------------------------
    # Display Summary
    # ---------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Most Common Event",
            common_event
        )

        st.metric(
            "Most Active User",
            top_user
        )

    with col2:

        st.metric(
            "Total Events",
            stats["total_events"]
        )

        st.metric(
            "Failed Logins",
            stats["failed_logins"]
        )

    with col3:

        st.metric(
            "Privilege Escalations",
            stats["privilege_escalations"]
        )

        st.metric(
            "Overall Risk",
            risk
        )