"""
Filters Module

Provides event filtering functionality.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st


def filter_events(events):
    """
    Filter events based on analyst selections.

    Parameters
    ----------
    events : list
        Structured event list.

    Returns
    -------
    list
        Filtered events.
    """

    if not events:
        return events

    st.subheader("🔍 Investigation Filters")

    col1, col2, col3 = st.columns(3)

    # -------------------------
    # Event IDs
    # -------------------------

    event_ids = sorted(
        set(event["event_id"] for event in events)
    )

    selected_event = col1.selectbox(
        "Event ID",
        ["All"] + event_ids
    )

    # -------------------------
    # Usernames
    # -------------------------

    usernames = sorted(
        set(
            event["username"]
            for event in events
            if event["username"]
        )
    )

    selected_user = col2.selectbox(
        "Username",
        ["All"] + usernames
    )

    # -------------------------
    # Computer Names
    # -------------------------

    computers = sorted(
        set(
            event["computer"]
            for event in events
            if event["computer"]
        )
    )

    selected_computer = col3.selectbox(
        "Computer",
        ["All"] + computers
    )

    filtered = events

    if selected_event != "All":
        filtered = [
            event
            for event in filtered
            if event["event_id"] == selected_event
        ]

    if selected_user != "All":
        filtered = [
            event
            for event in filtered
            if event["username"] == selected_user
        ]

    if selected_computer != "All":
        filtered = [
            event
            for event in filtered
            if event["computer"] == selected_computer
        ]

    return filtered