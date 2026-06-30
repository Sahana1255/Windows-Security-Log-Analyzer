"""
Dashboard KPI Cards

Professional KPI cards for the dashboard.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st


def _card(title, value, icon, color):

    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:0 6px 16px rgba(0,0,0,.30);
            min-height:140px;
        ">
            <div style="font-size:40px;">{icon}</div>

            <div style="
                font-size:16px;
                color:#d1d5db;
                margin-top:10px;
            ">
                {title}
            </div>

            <div style="
                font-size:34px;
                font-weight:bold;
                color:white;
                margin-top:10px;
            ">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
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
            "📄",
            "#1e293b"
        )

    with c2:
        _card(
            "Successful Logins",
            stats["successful_logins"],
            "🟢",
            "#065f46"
        )

    with c3:
        _card(
            "Failed Logins",
            stats["failed_logins"],
            "🔴",
            "#7f1d1d"
        )

    with c4:
        _card(
            "Account Creations",
            stats["account_creations"],
            "👤",
            "#78350f"
        )

    with c5:
        _card(
            "Privilege Escalations",
            stats["privilege_escalations"],
            "⚠️",
            "#7c2d12"
        )