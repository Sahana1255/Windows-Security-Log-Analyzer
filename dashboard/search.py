"""
Search Module

Provides global search across security events.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st


def search_events(events):
    """
    Search across all event fields.
    """

    if not events:
        return events

    query = st.text_input(
        "🔎 Global Search",
        placeholder="Search Event ID, Username, Computer..."
    )

    if not query:
        return events

    query = query.lower()

    filtered = []

    for event in events:

        values = [
            str(event["event_id"]),
            str(event["username"]),
            str(event["computer"]),
            str(event["timestamp"])
        ]

        searchable = " ".join(values).lower()

        if query in searchable:
            filtered.append(event)

    return filtered