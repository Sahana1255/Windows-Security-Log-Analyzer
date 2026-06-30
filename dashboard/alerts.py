"""
Alerts Module

Displays security alerts.

Author: Your Name
Project: Windows Security Log Analyzer
"""

import streamlit as st

from dashboard.severity import get_severity


def _latest_event(events, event_id):
    """
    Return the latest event matching the given Event ID.
    """

    matches = [

        event

        for event in events

        if event["event_id"] == event_id

    ]

    if not matches:
        return None

    return matches[-1]


def show_alerts(stats, events):
    """
    Display security alerts.
    """

    st.subheader("🚨 Security Alerts")

    left, right = st.columns(2)

    # ---------------------------------------------------
    # Left Column
    # ---------------------------------------------------

    with left:

        # Failed Login
        latest_failed = _latest_event(events, 4625)

        if latest_failed:

            severity = get_severity(4625)

            st.error(
                f"""
{severity}

**Failed Login Detected**

**Count:** {stats['failed_logins']}

**User:** {latest_failed['username']}

**Computer:** {latest_failed['computer']}

**Time:** {latest_failed['timestamp']}
"""
            )

        else:

            st.success("🟢 No Failed Login Attempts")

        # -----------------------------------------------

        latest_account = _latest_event(events, 4720)

        if latest_account:

            severity = get_severity(4720)

            st.warning(
                f"""
{severity}

**New Account Created**

**Count:** {stats['account_creations']}

**User:** {latest_account['username']}

**Computer:** {latest_account['computer']}

**Time:** {latest_account['timestamp']}
"""
            )

        else:

            st.success("🟢 No New User Accounts")

    # ---------------------------------------------------
    # Right Column
    # ---------------------------------------------------

    with right:

        latest_privilege = _latest_event(events, 4672)

        if latest_privilege:

            severity = get_severity(4672)

            st.warning(
                f"""
{severity}

**Privilege Escalation Detected**

**Count:** {stats['privilege_escalations']}

**User:** {latest_privilege['username']}

**Computer:** {latest_privilege['computer']}

**Time:** {latest_privilege['timestamp']}
"""
            )

        else:

            st.success("🟢 No Privilege Escalations")

        # -----------------------------------------------

        latest_password = _latest_event(events, 4723)

        if latest_password:

            severity = get_severity(4723)

            st.info(
                f"""
{severity}

**Password Changed**

**Count:** {stats['password_changes']}

**User:** {latest_password['username']}

**Computer:** {latest_password['computer']}

**Time:** {latest_password['timestamp']}
"""
            )

        else:

            st.success("🟢 No Password Changes")