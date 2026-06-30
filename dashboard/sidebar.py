"""
Sidebar Module

Creates the Streamlit sidebar.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st


def create_sidebar():
    """
    Build the application sidebar.

    Returns
    -------
    uploaded_file
        Uploaded EVTX file.

    max_events
        Maximum events to analyze.

    analyze
        Analyze button state.
    """

    with st.sidebar:

        st.title("🛡 Security Log Analyzer")

        st.divider()

        uploaded_file = st.file_uploader(
            "Upload Security.evtx",
            type=["evtx"]
        )

        st.divider()

        max_events = st.selectbox(
            "Maximum Events",
            [1000, 5000, 10000, "All"],
            index=2
        )

        st.divider()

        analyze = st.button(
            "▶ Analyze",
            use_container_width=True
        )

        st.divider()

        st.success("Ready")

    return uploaded_file, max_events, analyze