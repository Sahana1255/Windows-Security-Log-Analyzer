"""
Sidebar Module

Professional Sidebar

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

        # ---------------------------------------------------
        # Header
        # ---------------------------------------------------

        st.markdown("# 🛡 Security Log Analyzer")

        st.caption("SOC Investigation Dashboard")

        st.divider()

        # ---------------------------------------------------
        # Project Status
        # ---------------------------------------------------

        st.subheader("📌 Project Status")

        st.success("🟢 System Ready")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Version", "1.0.0")

        with col2:
            st.metric("Status", "Ready")

        st.divider()

        # ---------------------------------------------------
        # Upload Log
        # ---------------------------------------------------

        st.subheader("📂 Upload Security Log")

        uploaded_file = st.file_uploader(
            "Choose a Windows Security.evtx file",
            type=["evtx"]
        )

        st.divider()

        # ---------------------------------------------------
        # Analysis Settings
        # ---------------------------------------------------

        st.subheader("⚙ Analysis Settings")

        max_events = st.selectbox(
            "Maximum Events",
            [1000, 5000, 10000, "All"],
            index=2
        )

        analyze = st.button(
            "🚀 Analyze Security Log",
            use_container_width=True
        )

        st.divider()

        # ---------------------------------------------------
        # Dashboard Features
        # ---------------------------------------------------

        st.subheader("📊 Dashboard Features")

        st.markdown("""
✅ EVTX Parsing

✅ Detection Rules

✅ Security Alerts

✅ Interactive Charts

✅ Investigation Panel

✅ Event Search

✅ Event Filters

✅ CSV Export

✅ PDF Report
""")

        st.divider()

        # ---------------------------------------------------
        # About
        # ---------------------------------------------------

        st.subheader("ℹ About")

        st.caption(
            "Windows Security Log Analyzer is a SOC-focused "
            "dashboard for investigating Windows Security Event Logs."
        )

        st.divider()

        st.caption(
            "Built with ❤️ using Python • Streamlit"
        )

    return uploaded_file, max_events, analyze