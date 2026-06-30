"""
Dashboard Statistics Module

Calculates statistics used by the Streamlit dashboard.

Author: Your Name
Project: Windows Security Log Analyzer
"""

from detection.failed_logins import detect_failed_logins
from detection.successful_logins import detect_successful_logins
from detection.account_creation import detect_account_creation
from detection.password_changes import detect_password_changes
from detection.privilege_escalation import detect_privilege_escalation


def get_statistics(events):
    """
    Calculate dashboard statistics.

    Parameters
    ----------
    events : list
        List of structured event dictionaries.

    Returns
    -------
    dict
        Dictionary containing dashboard statistics.
    """

    successful = detect_successful_logins(events)
    failed = detect_failed_logins(events)
    created = detect_account_creation(events)
    password = detect_password_changes(events)
    privilege = detect_privilege_escalation(events)

    return {

        "total_events": len(events),

        "successful_logins": len(successful),

        "failed_logins": len(failed),

        "account_creations": len(created),

        "password_changes": len(password),

        "privilege_escalations": len(privilege)

    }