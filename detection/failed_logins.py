"""
Failed Login Detection Module

Detects Windows Failed Login events
(Event ID 4625).

Author: Your Name
Project: Windows Security Log Analyzer
"""


def detect_failed_logins(events):
    """
    Detect failed login events.

    Parameters:
        events (list): List of structured event dictionaries.

    Returns:
        list: List containing only failed login events.
    """

    failed_logins = []

    for event in events:

        if event["event_id"] == 4625:

            failed_logins.append(event)

    return failed_logins