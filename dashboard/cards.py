"""
Dashboard KPI Cards

Professional KPI cards for the dashboard.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st


def _card(title, value, icon):

    st.metric(
        label=f"{icon} {title}",
        value=value,
        border=True
    )


def show_kpi_cards(stats):
    """
    Display dashboard KPI cards.
    """

    st.subheader("📊 Security Overview")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        _card(
            "Total Events",
            stats["total_events"],
            "📄"
        )

    with c2:
        _card(
            "Successful Logins",
            stats["successful_logins"],
            "🟢"
        )

    with c3:
        _card(
            "Failed Logins",
            stats["failed_logins"],
            "🔴"
        )

    with c4:
        _card(
            "Account Creations",
            stats["account_creations"],
            "👤"
        )

    with c5:
        _card(
            "Privilege Escalations",
            stats["privilege_escalations"],
            "⚠️"
        )