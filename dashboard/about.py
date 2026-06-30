"""
About Module
"""

import streamlit as st


def show_about():

    with st.expander("ℹ About this Project"):

        st.markdown(
            """
### Windows Security Log Analyzer

A SOC analyst dashboard for Windows EVTX logs.

Features

- EVTX Parsing
- Login Detection
- Account Monitoring
- Investigation Panel
- Charts
- CSV Export
- PDF Report

Built using

- Python
- Streamlit
- Pandas
- ReportLab
            """
        )